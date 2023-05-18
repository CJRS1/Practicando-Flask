def prueba(**argumentos):
    print(argumentos)

prueba(nombre='eduardo', apellido='de rivero')

persona = {
    'nombre':'eduardo',
    'apellido':'de rivero'
}

prueba(persona=persona)

#cuando en una funcion pasamos un DICCIONARIO pero con doble asterisco antes (**) significa que sacara las llaves(keys) y lo colocara como parámetro de la función y sus valores como los valores de esos parámetrps
prueba(**persona)

prueba(nombre=persona['nombre'],apellido=persona['apellido'])

def saludar (nombre):
    print(nombre)

usuario = {
    'nombre':'eduardo',
    'apellido':'derivero'
}
usuario2 = {
    'nombrecito':'christian'
}

saludar(**usuario)
saludar(**usuario2)
saludar(nombrecito='pedrito')