
import os
from bottle import Bottle, request, template, debug,route, error, run
import requests

@route('/')
def index():
    return '''
<h1>RandomCat</h1>
<h2>Menu</h2>
    <a href="foto?tipo=aleatoria">Random Image </a> <br>
    <a>Random Gif </a> <br>
    <a>Cat Saying... </a> <br>
    </form>
'''
    

@route('/foto', method='POST')
@route('/foto', method='GET')
def exibe_foto():
    raca = str(request.forms.get('raca'))
    tipo = str(request.params.get('tipo'))
    if "aleatoria" in tipo:
        response = requests.get('https://cataas.com/cat?json=true')
        img = response.json().get("id");
        return f" <img src='https://cataas.com/cat/{img}' alt=''><br><br><a href=\"/\">Voltar </a> <br>" 

    
        
@error(404)
def error_404(error):
    return 'Página não encontrada.'

#debug(True)  
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

