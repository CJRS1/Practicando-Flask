from flask_restful import Resource, request
from config import conexion
from models.usuarios import UsuarioModel
from dtos.usuarioDto import UsuarioRequestDto

class UsuariosController(Resource):
    def get(self):
        #Devuelve una lista con todas las instancias de la clase Usuario model per olas tengo que formatear para devolverlas al frontend
        usuarios = conexion.session.query(UsuarioModel).all()
        print(usuarios)
        serializador = UsuarioRequestDto(many=True) #Para traer a t odos los usuarios debe de haber un many=True
        data = serializador.dump(usuarios)

        # usuariosFinales = []
        # for usuario in usuarios :
        #     usuarioDiccionario = {
        #         'id':usuario.id,
        #         'nombre':usuario.nombre,
        #         'correo':usuario.correo,
        #         'telefono':usuario.telefono,
        #     }
        #     usuariosFinales.append(usuarioDiccionario)
        return{
            'message':'Los usuarios son',
            'content': data
        }
    

    def post(self):
        body=request.get_json()
        try:
            serializador = UsuarioRequestDto()
            dataSerializada = serializador.load(body)
            print(dataSerializada)


            #creo una nueva instancia de mi clase model
            #y se coloca la dataserializada
            nuevoUsuario = UsuarioModel(**dataSerializada)
            # asigno los valores a los atributos provenientes del body

            # nuevoUsuario.correo = body.get('correo')
            # nuevoUsuario.nombre = body.get('nombre')
            # nuevoUsuario.telefono = body.get('telefono')

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
                'message':'Error al crear el usuario',
                'content':error.args
            }

class UsuarioController(Resource):
    def get(self,id):
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
        serializador = UsuarioRequestDto()
        data = serializador.dump(usuarioEncontrado)
        return{
            'content':data

        }
    def put(self,id):
        try:
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter(id=id).first()
            if usuarioEncontrado is None:
                raise Exception('Usuario no existe')
            body = request.get_json()
            serializador = UsuarioRequestDto()
            data = serializador.load(body)

            usuarioEncontrado.correo = body.get('correo')
            usuarioEncontrado.nombre = body.get('nombre')
            usuarioEncontrado.telefono = body.get('telefono')

            conexion.session.commit()
            return{
                'message':'usuario actualizado exitosamente'
            }

        except Exception as error:
            return{
                'message': 'Error al actualizar usuario',
                'content':error.args
            }