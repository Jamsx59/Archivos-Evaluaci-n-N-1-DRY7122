import yaml

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

datos = {
    "nombre": nombre,
    "apellido": apellido
}

yaml_datos = yaml.dump(datos)

print(yaml_datos)
