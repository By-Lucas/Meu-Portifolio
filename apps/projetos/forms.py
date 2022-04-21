from django import forms
from site_portifolio.models_2.projetos import projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = projeto
        fields = [
            'nome',
            'descricao',
            'img_projeto',
            'tecnologias',
            'link_github'
        ]

    
    error_messagens = {
            "codigo_produto": {
                "required": "O Código do produto é obrigatório."
            },
            "nome_produto": {
                "required": "O Código do produto é obrigatório."
            },
            "descricao_produto": {
                "required": "Por favor, informe a descrição do produto."
            },
        }

            # SE FOR USAR DATAS, AQUI ESTÁ O MODELO PARA ERROS
            #"data_cadastro": {
                #"required": "A data de nascimento completo do visitante e obrigatorio para o resgistro.",
                #"invalid": "Por favor, informa um formato valido para a data de nascimento (DD/MM/AAA)"
                