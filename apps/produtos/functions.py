from django.db import models, connection
from .models import MeusPedidos

def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

def getNrPedidos(request, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT max(nr_pedido) nr_pedido FROM plataforma_meuspedidos WHERE usuario_id = %s", [user_id])
        row = dictfetchall(cursor)
        #print(row)        
    class Meta:
        model = MeusPedidos
    return row

def get_meuspedidos(request, user_id, user_username):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM plataforma_meuspedidos WHERE usuario_id = %s", [user_id])
        pedido = dictfetchall(cursor)
        #print(pedido)        
    class Meta:
        model = MeusPedidos
    return pedido