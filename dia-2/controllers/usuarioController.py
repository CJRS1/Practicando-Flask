from flask_restful import Resource, request
from config import conexion
from models.usuarios import UsuarioModel

class UsuariosController(Resource):
    def get(self):
        #Devuelve una lista con todas las instancias de la clase Usuario model per olas tengo que formatear para devolverlas al frontend
        usuarios = conexion.session.query(UsuarioModel).all()
        print(usuarios)

        usuariosFinales = []
        for usuario in usuarios :
            usuarioDiccionario = {
                'id':usuario.id,
                'nombre':usuario.nombre,
                'correo':usuario.correo,
                'telefono':usuario.telefono,
            }
            usuariosFinales.append(usuarioDiccionario)
        return{
            'message':'Los usuarios son',
            'content': usuariosFinales
        }
    
    
    def post(self):
        body=request.get_json()
        try:
            #creo una nueva instancia de mi clase model
            nuevoUsuario = UsuarioModel()
            # asigno los valores a los atributos provenientes del body
            nuevoUsuario.correo = body.get('correo')
            nuevoUsuario.nombre = body.get('nombre')
            nuevoUsuario.telefono = body.get('telefono')
            # ahora agregamos a la base de datos ese nuevo registro creado en base a la instancia
            conexion.session.add(nuevoUsuario)

            conexion.session.commit()        
            print(body)
            conexion.session.query()
            return{
                'message':'Yo soy el post del usuario'
            }
        except Exception as error:
            print(error)
            return{
                'message':'Error al crear el usuario'
            }