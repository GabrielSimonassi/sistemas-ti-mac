from flask import render_template, request, Blueprint, session
import requests
from app.config import *

app = Blueprint('busca_mac', __name__)

# RENDERIZA O DASHBOARD
@app.route('/busca_mac')
def mac_busca():
    # CHECA SE O USUÁRIO ESTA LOGADO, CASO CONTRARIO, RETORNA A PAGINA DE LOGIN
    if not session.get('logged_in'):
        return render_template('login.html')
    # PEGA O NOME DO USUÁRIO LOGADO NA SESSÃO
    username = session.get('username')
    # CASO LOGADO, RENDERIZA A PAGINA DASHBOARD
    return render_template('busca_mac.html')

@app.route('/resolve_mac', methods=['GET', 'POST'])
def resolve_mac():
    # VERIFICA SE O USUARIO ESTA LOGADO PARA ACESSAR A ROTA
    if not session.get('logged_in'):
        return render_template('login.html')
    
    # PEGA O NOME DO USUARIO LOGADO NA SESSÃO PARA LOG APENAS
    usernameLST = session.get('usernameLST')

    if request.method == 'POST':
       
        # RECEBE O MAC DIGITADO NO INPUT DO FRONT
        mac_addr = request.form.get('mac_addr')

        # CONSULTA O FABRICANTE DO MAC FORNECIDO E FORMATA MENSAGEM
        vendorsURL = f'https://api.macvendors.com/{mac_addr}'
        response = requests.get(vendorsURL)
        manufacturer = "Fabricante: " + response.text

        # VERIFICA SE O RESULTADO DA CONSULTA FOI 404
        if("errors" in manufacturer):
            manufacturer = "Fabricante não encontrado. Certifique-se de buscar um MAC válido."

        # IMPRIME OS TESTE NA PAGINA RENDERIZADA
        return render_template('busca_mac.html', manufacturer=manufacturer)
    


##################################################################
# ADICIONAR NO __init__.py                                      #
#                                                                #
##CONSULTA DE FABRICANTE DE MAC ADDRESS                          #
#from app.busca_mac import app as busca_mac_app                 #
#app.register_blueprint(busca_mac_app)                          #
##################################################################