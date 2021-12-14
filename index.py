
import os
from bottle import Bottle, request, template, debug,route, error, run
import requests
import random

@route('/')
def index():
    return '''
<h1>RandomCat</h1>
<h2>Menu</h2>
    <a href="foto?tipo=aleatoria">Random Image </a> <br>
    <a href="foto?tipo=gif">Random Gif </a> <br>
    <a>Cat Saying... </a> <br>
    
    <form action="foto?tipo=text" method="POST">
    <textarea name="text" rows ="3" cols="20">
    </textarea>
    <input value="Enviar" type="submit" />
    </form>
'''
    

@route('/foto', method='POST')
@route('/foto', method='GET')
def exibe_foto():    
    tipo = str(request.params.get('tipo'))
    text = str(request.params.get('text'))
    if "aleatoria" in tipo:
        response = requests.get('https://cataas.com/cat?json=true')
        img = response.json().get("id");
        return f" <img src='https://cataas.com/cat/{img}' alt=''><br><br><a href=\"/\">Voltar </a> <br>" 
    
    if "gif" in tipo:
        response = requests.get('https://cataas.com/api/cats?tags=gif&limit=100')
        r = random.randint(0, 100) 
        json = response.json()
        img =  json[r]['id']   
        return f" <img src='https://cataas.com/cat/{img}' alt=''><br><br><a href=\"/\">Voltar </a> <br>" 
    
    if "text" in tipo:
        response = requests.get('https://cataas.com/cat?json=true')
        img = response.json().get("id");
        return f" <img src='https://cataas.com/cat/{img}/says/{text}' alt=''><br><br><a href=\"/\">Voltar </a> <br>" 
        

    
        
@error(404)
def error_404(error):
    return 'Página não encontrada.'

#debug(True)  
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

