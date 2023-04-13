import json

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

datos = {
    "nombre": nombre,
    "apellido": apellido
}

json_datos = json.dumps(datos)

print(json_datos)
