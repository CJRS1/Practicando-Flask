from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from os import environ #libreria propia de python
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
#almacena todas las variables de configuracion de la aplicacion de flask
app.config['MYSQL_HOST'] = environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] =  environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = environ.get('MYSQL_DB')
app.config['MYSQL_PORT'] = int(environ.get('MYSQL_PORT'))
#Sirve para conectarse a la base de datos en MySQL
mysql = MySQL(app)



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

@app.route('/mostrar-alumnos/',methods=['GET'])
def devolver_alumnos():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT*FROM alumnos")
    resultado = cursor.fetchall() #obtuiene todos los datos que estan en el execute
    print(resultado)
    resultado_final = []
    for alumno in resultado:
        alumno_diccionario={
            'id':alumno[0],
            'nombre':alumno[1],
            'ape_paterno':alumno[2],
            'ape_materno':alumno[3],
            'correo':alumno[4],
            'num_emergencia':alumno[5],
            'curso_id':alumno[6],
        }
        resultado_final.append(alumno_diccionario)
    # return {
    #     'message':'Los alumnos son:',
    #     'content': resultado_final
    # }
    return render_template('mostrar_alumnos.html',alumnos=resultado_final,mensaje='Hola desde Flask')

@app.route('/agregar-alumno/',methods=['GET','POST'])
def agregar_alumnos():
    print(request.method)
    if request.method == 'GET':
        return render_template('agregar_alumno.html')
    elif request.method == 'POST':
        print(request.data)
        body = request.get_json()
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO alumnos (id, nombre, ape_paterno, ape_materno, correo, num_emergencia) VALUES (DEFAULT, '%s','%s','%s','%s','%s') "% (body.get('nombre'),body.get('ape_paterno'),body.get('ape_materno'),body.get('correo'),body.get('num_emergencia')))
        mysql.connection.commit()
        cursor.close()
        print(body)
        return{
            'message':'Alumno agregado exitosamente'
        }

app.run(debug=True)