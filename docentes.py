import csv
import json


class Docente:
    def __init__(self, numero_empleado, nombre, especialidad):
        if not str(numero_empleado).strip():
            raise ValueError("El número de empleado es obligatorio")
        if not nombre.strip():
            raise ValueError("El nombre es obligatorio")
        if not especialidad.strip():
            raise ValueError("La especialidad es obligatoria")
        self.numero_empleado = str(numero_empleado)
        self.nombre = nombre
        self.especialidad = especialidad

    def a_diccionario(self):
        return {
            "numero_empleado": self.numero_empleado,
            "nombre": self.nombre,
            "especialidad": self.especialidad,
        }


class RegistroDocentes:
    def __init__(self):
        self.docentes = []

    def agregar(self, docente):
        if self.buscar(docente.numero_empleado):
            raise ValueError("Ya existe un docente con ese número de empleado")
        self.docentes.append(docente)

    def buscar(self, numero_empleado):
        for d in self.docentes:
            if d.numero_empleado == str(numero_empleado):
                return d
        return None

    def eliminar(self, numero_empleado):
        d = self.buscar(numero_empleado)
        if d is None:
            raise ValueError("Docente no encontrado")
        self.docentes.remove(d)

    def actualizar(self, numero_empleado, nombre=None, especialidad=None):
        d = self.buscar(numero_empleado)
        if d is None:
            raise ValueError("Docente no encontrado")
        if nombre:
            d.nombre = nombre
        if especialidad:
            d.especialidad = especialidad

    def exportar_csv(self, ruta):
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["numero_empleado", "nombre", "especialidad"])
            w.writeheader()
            for d in self.docentes:
                w.writerow(d.a_diccionario())

    def exportar_json(self, ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump([d.a_diccionario() for d in self.docentes], f,
                      ensure_ascii=False, indent=4)
    def exportar_yaml(self, ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("docentes:\n")
            for d in self.docentes:
                f.write(f"  - numero_empleado: {json.dumps(d.numero_empleado, ensure_ascii=False)}\n")
                f.write(f"    nombre: {json.dumps(d.nombre, ensure_ascii=False)}\n")
                f.write(f"    especialidad: {json.dumps(d.especialidad, ensure_ascii=False)}\n")
                
    def como_tabla(self):
        lineas = [f"{'No. Empleado':<15}{'Nombre':<30}{'Especialidad':<25}", "-" * 70]
        for d in self.docentes:
            lineas.append(f"{d.numero_empleado:<15}{d.nombre:<30}{d.especialidad:<25}")
        return "\n".join(lineas)
