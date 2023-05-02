from flask import Flask

app = Flask(__name__)

#Decorador
@app.route('/',methods=['GET'])
def inicio():
    return {
        'message':'Bienvenido a mi API de colegios'
    }



app.run(debug=True)