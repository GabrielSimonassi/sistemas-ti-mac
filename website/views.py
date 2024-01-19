from flask import Blueprint, render_template, request
import requests

views = Blueprint('views', __name__)

@views.route('/consulta-mac', methods=["GET"])
def macCheck():
    #pega o MAC que se deseja consultar
    data = request.args.get('macAddr')
    vendorsURL = f'https://api.macvendors.com/{data}'
    response = requests.get(vendorsURL)
    api_data = response.text
    print(api_data)

    return render_template("consultaMac.html")

@views.route('/')
def home():
    return render_template("index.html")