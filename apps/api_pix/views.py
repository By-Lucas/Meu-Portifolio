from multiprocessing import context
from django.shortcuts import redirect, render
import requests
import json
import os
import base64
import hmac
import hashlib
from math import floor
from datetime import datetime, timedelta

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.contrib import messages

from .models import Charge
from plataforma.models import MeusPedidos
from .serializers import ChargeSerializer
from .consts import (
    API_PIX_PRODUCTION_MODE,
    API_PIX_URL_BASE, 
    API_PIX_CLIENT_ID, 
    API_PIX_CLIENT_SECRET, 
    API_PIX_PRIVATE_TOKEN, 
    API_PIX_KEY,
    API_PIX_WEBHOOK_SECRET)

class BaseAPI(APIView):
    _url_base = f'{API_PIX_URL_BASE}{"/api-integration" if not API_PIX_PRODUCTION_MODE else ""}'

    def _get_token(self):
        if 'PIX_TOKEN_EXPIRES' in os.environ and datetime.now() < datetime.fromtimestamp(int(os.environ['PIX_TOKEN_EXPIRES'])):
            return os.environ['PIX_TOKEN_VALUE']
        else:
            token_info = self._get_token_from_server()
            if token_info:
                expires = datetime.timestamp(datetime.now() + timedelta(seconds=(token_info['expires_in']) - 60))
                os.environ['PIX_TOKEN_EXPIRES'] = str(floor(expires))
                os.environ['PIX_TOKEN_VALUE']  = token_info['access_token']
                return token_info['access_token']

        return ''
    
    def _get_token_from_server(self):
        auth = base64.b64encode(f'{API_PIX_CLIENT_ID}:{API_PIX_CLIENT_SECRET}'.encode()).decode()
        headers = {
            'Authorization': f'Basic {auth}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(f'{API_PIX_URL_BASE}/authorization-server/oauth/token', headers=headers, data='grant_type=client_credentials')

        if response.status_code == requests.codes.ok:
            return json.loads(response.content)
        return {}


class ChargeList(BaseAPI):
    
    def get(self, request):
        user_id = request.user.id
        charges = Charge.objects.all().order_by('-status')
        serializer = ChargeSerializer(charges, many=True)
        itens = MeusPedidos.objects.filter(usuario=request.user).all()
        for i in itens:
            numeros_comprados= i.numeros_comprados
        print('TESTE',itens.all(),dir(itens))

        
        context= {
            'serialazer': serializer.data,
            'charges':charges,
            'user_id':user_id,
            'itens':itens
        }
        return render(request,'cobrancas.html', context)
        
    
    def post(self, request):
        if request.user.is_authenticated:
            serializer = ChargeSerializer(data = request.data, context = {'request': request})

            if serializer.is_valid():
                txid = self.__create_charge(serializer.validated_data["value"])
                if txid:
                    serializer.validated_data['txid'] = txid
                    serializer.save()
                    response = {
                        'qrcode': self.__get_qrcode(txid),
                        'txid': txid
                    }
                    return Response(response, status=status.HTTP_201_CREATED)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def __create_charge(self,value):
        headers = {
            'X-API-Version': '2',
            'X-Resource-Token': f'{API_PIX_PRIVATE_TOKEN}',
            'Authorization': f'Bearer {self._get_token()}',
            'Content-Type': 'application/json'
        }
        payload = {
            'calendario': {
                'expiracao': 3600
            },
            'valor': {
                'original': f'{value}'
            },
            'chave': f'{API_PIX_KEY}',
            'solicitacaoPagador': 'Anotação'
        }

        response = requests.post(f'{self._url_base}/pix-api/v2/cob', headers=headers, data=json.dumps(payload))
        
        if response.status_code == requests.codes.created:
            return json.loads(response.content)['txid']
        return ''

    def __get_qrcode(self, txid):
        headers = {
            'X-API-Version': '2',
            'X-Resource-Token': f'{API_PIX_PRIVATE_TOKEN}',
            'Authorization': f'Bearer {self._get_token()}',
            'Content-Type': 'application/json'
        }

        response = requests.get(f'{self._url_base}/pix-api/qrcode/v2/{txid}/imagem', headers=headers)
        
        if response.status_code == requests.codes.ok:
            content = json.loads(response.content)
            return {
                'image': content['imagemBase64'],
                #'key': content['qrcodeBase64']
                'key': base64.b64decode(content['qrcodeBase64'].encode('utf-8')).decode('utf-8')
            }
        return {}


class ChargeDetail(BaseAPI):
     
    def __get_object(self, txid):
        try:
            return Charge.objects.get(txid=txid)
        except Charge.DoesNotExist:
            raise Http404
    
    def get(self, request, txid):
        if request.user.is_authenticated:
            charge = self.__get_object(txid)
            context = {
                'status': charge,
            }
            return Response({'status': charge.status})
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class Notification(APIView):

    def post(self, request):
        if 'X-Signature' in request.headers:
            event_msg = request.data
            signature = hmac.new(API_PIX_WEBHOOK_SECRET.encode(), json.dumps(event_msg).replace(" ", "").encode(), hashlib.sha256).hexdigest()
            
            if signature == request.headers['X-Signature']:
                try:
                    attributes = event_msg.get('data')[0].get('attributes')
                    status_paid = attributes.get('status')
                    if status_paid:
                        txid = attributes.get('pix').get('txid')
                        charge = Charge.objects.get(txid=txid)
                        serializer = ChargeSerializer(charge, data={'status': status_paid}, partial=True)
                        if serializer.is_valid():
                            serializer.save()
                            messages.success(request, 'Pagamento aprovado')
                            return Response(status=status.HTTP_200_OK)
                except AttributeError:
                    pass
                except Charge.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class WebhookList(BaseAPI):

    def get(self, request):
        headers = {
            'X-API-Version': '2',
            'X-Resource-Token': f'{API_PIX_PRIVATE_TOKEN}',
            'Authorization': f'Bearer {self._get_token()}',
            'Content-Type': 'application/json'
        }
        response = requests.get(f'{self._url_base}/notifications/webhooks', headers=headers)
        
        return Response(response)

    def post(self, request):
        if 'url' in request.data:
            headers = {
                'X-API-Version': '2',
                'Authorization': f'Bearer {self._get_token()}',
                'X-Resource-Token': f'{API_PIX_PRIVATE_TOKEN}',
                'Content-Type': 'application/json'
            }
            
            payload = {
                'url': request.data['url'],
                'eventTypes': [
                    'CHARGE_STATUS_CHANGED'
                    ]
            }
            
            response = requests.post(f'{self._url_base}/notifications/webhooks', headers=headers, data=json.dumps(payload))

            return Response(json.loads(response.content))
        return Response(status=status.HTTP_400_BAD_REQUEST)

class WebhookDetail(BaseAPI):

    def delete(self, request, webhook):
        headers = {
            'X-API-Version': '2',
            'X-Resource-Token': f'{API_PIX_PRIVATE_TOKEN}',
            'Authorization': f'Bearer {self._get_token()}',
            'Content-Type': 'application/json'
        }
        response = requests.delete(f'{self._url_base}/notifications/webhooks/{webhook}', headers=headers)
        
        return Response(response.content)
