from flask import Flask, render_template

app = Flask(__name__)

#Decorador es la forma en la cual nosotros podemos modificar el comportamiento de un metodo de una clase sin la necesidad de modificarlo directamente, es como utilizar la herencia para poder modificar su comportamiento m en este caso , dependiendo de su ruta y su metodo
@app.route('/',methods=['GET'])
def inicio():
    return {
        'message':'Bienvenido a mi API de colegios'
    }
#Decorador para devolver una plantilla y hacer la parte de frontend, y debe estar dentro de una carpeta llamanda templates
@app.route('/inicio/',methods=['GET'])
def pagina_inicial():
    return render_template('index.html')

app.run(debug=True)