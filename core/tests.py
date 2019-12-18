from django.test import TestCase,unittest,models,views,forms

# Create your tests here.
class TestOperaciones(unittest.TestCase):
    def setUp(self):
        pass
   
    def test_ToString(self):
        clase = models.Flor
        clase.nombre = "amapola"
        clase.valor = 1
        clase.descripcion = "default"
        clase.estado = True
        clase.stock = 9
        self.assertEqual("amapola",models.Flor.__str__(clase))

    def test_agregarflor(self):

        ejemplo = models.Flor
        self.assertEqual()


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

