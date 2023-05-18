from flask import Flask
from flask_migrate import Migrate 
from os import environ
from dotenv import load_dotenv
from flask_restful import Api

from config import conexion
from models.usuarios import UsuarioModel
from models.tareas import TareaModel
from controllers.usuarioController import UsuariosController, UsuarioController
from controllers.pruebaController import PruebaController

load_dotenv()

app = Flask(__name__)

#inicializa la clase Api que nos servira para poder utilizar todos los controladores dentro de al aaplicacion de Flask
api = Api(app)

#Conexion a la base de datos
app.config['SQLALCHEMY_DATABASE_URI']=environ.get('DATABASE_URI')
# Mostrara todas las consultas en el lenguaje SQL que se realiza a la base de datos
app.config['SQLALCHEMY_ECHO']=environ.get('MOSTRAR_SQL')

# Inicializamos la instancia de Flask-SQLAlchemy con las propiedades seteadas en la aplicacion de Flask
conexion.init_app(app)
#Inicializamos la clase Migrate con la configuracion de nuestra base de datos y aplicacion de Flask
migrate = Migrate(app,conexion)

# @app.route('/',methods=['GET'])
# def conexion():
#     return {
#         'message':'conectado'
#     }

#Declararar todas las rutas que vamos a utilizar mediante los controladores
api.add_resource(UsuariosController,'/usuarios')
api.add_resource(PruebaController,'/prueba')
api.add_resource(UsuarioController,'/usuario/<int:id>') #para que se pueda filtrar por id


if __name__ == '__main__':
    app.run(debug=True)