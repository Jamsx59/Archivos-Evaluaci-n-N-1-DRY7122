import xml.etree.ElementTree as ET

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

datos = ET.Element("datos")
nombre_elem = ET.SubElement(datos, "nombre")
apellido_elem = ET.SubElement(datos, "apellido")

nombre_elem.text = nombre
apellido_elem.text = apellido

xml_datos = ET.tostring(datos)

print(xml_datos.decode())
