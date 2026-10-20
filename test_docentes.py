import unittest
import os
from docentes import Docente, RegistroDocentes


class TestDocentes(unittest.TestCase):
    def setUp(self):
        self.reg = RegistroDocentes()
        self.reg.agregar(Docente("1", "Ana López", "Software"))

    def test_01_crear_docente_valido(self):
        d = Docente("2", "Luis", "Redes")
        self.assertEqual(d.nombre, "Luis")

    def test_02_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Docente("3", "", "Redes")

    def test_03_agregar_docente(self):
        self.reg.agregar(Docente("2", "Luis", "Redes"))
        self.assertEqual(len(self.reg.docentes), 2)

    def test_04_numero_duplicado(self):
        with self.assertRaises(ValueError):
            self.reg.agregar(Docente("1", "Otro", "Redes"))

    def test_05_buscar_existente(self):
        self.assertIsNotNone(self.reg.buscar("1"))

    def test_06_buscar_inexistente(self):
        self.assertIsNone(self.reg.buscar("99"))

    def test_07_actualizar(self):
        self.reg.actualizar("1", especialidad="IA")
        self.assertEqual(self.reg.buscar("1").especialidad, "IA")

    def test_08_eliminar(self):
        self.reg.eliminar("1")
        self.assertEqual(len(self.reg.docentes), 0)

    def test_09_exportar_csv(self):
        self.reg.exportar_csv("prueba.csv")
        self.assertTrue(os.path.exists("prueba.csv"))
        os.remove("prueba.csv")

    def test_10_exportar_json(self):
        self.reg.exportar_json("prueba.json")
        self.assertTrue(os.path.exists("prueba.json"))
        os.remove("prueba.json")

    def test_11_exportar_yaml(self):
        self.reg.exportar_yaml("prueba.yaml")
        self.assertTrue(os.path.exists("prueba.yaml"))
        os.remove("prueba.yaml")

