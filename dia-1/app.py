from flask import Flask, render_template
from flask_mysqldb import MySQLdb


app = Flask(__name__)
#almacena todas las variables de configuracion de la aplicacion de flask
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] =  'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'colegio'
app.config['MYSQL_PORT'] = 3306
#Sirve para conectarse a la base de datos en MySQL
mysql = MySQLdb(app)



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

@app.route('/alumnos/',methods=['GET'])
def devolver_alumnos():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT*FROM alumnos")
    resultado = cursor.fetchall() #obtuiene todos los datos que estan en el execute
    print(resultado)
    return {
        'message':'Los alumnos son:'
    }
app.run(debug=True)