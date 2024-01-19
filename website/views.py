from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/consulta-mac', methods=["GET", "ṔOST"])
def macCheck():
    data = request.form
    print(data)
    # macaddress = "FC-A1-3E-2A-1C-33"
    # r = requests.get(url="http://api.macvendors.com/%s" %macaddress)
    # print(r.text)
    return render_template("consultaMac.html")

@views.route('/')
def home():
    return render_template("index.html")