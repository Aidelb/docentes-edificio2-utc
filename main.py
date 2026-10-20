import os
from docentes import Docente, RegistroDocentes

registro = RegistroDocentes()
registro.agregar(Docente("1001", "Ana López Ramírez", "Desarrollo de Software"))
registro.agregar(Docente("1002", "Carlos Pérez Díaz", "Redes"))
registro.agregar(Docente("1003", "María Torres Gómez", "Base de Datos"))

os.makedirs("datos", exist_ok=True)
print(registro.como_tabla())
registro.exportar_csv("datos/docentes.csv")
registro.exportar_yaml("datos/docentes.yaml")
registro.exportar_json("datos/docentes.json")
print("\nArchivos generados en la carpeta datos/")
