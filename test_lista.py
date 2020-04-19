import unittest
import lista

class ListaTestCase(unittest.TestCase):

    def test_construir(self):
        esperado = (1, None)
        observado = lista.construir(1)
        self.assertEqual(esperado, observado)

        esperado = (1.5, None)
        observado = lista.construir(1.5)
        self.assertEqual(esperado, observado)

        esperado = (1, (2, None))
        observado = lista.construir(1, lista.construir(2))
        self.assertEqual(esperado, observado)

        self.assertRaises(ValueError, lista.construir, "a")

    def test_lista(self):
        esperado = None
        observado = lista.lista()
        self.assertEqual(esperado, observado)

        esperado = (1, None)
        observado = lista.lista(1)
        self.assertEqual(esperado, observado)
        
        esperado = (1, (2, None))
        observado = lista.lista(1, 2)
        self.assertEqual(esperado, observado)
        
    def test_primero(self):
        l = lista.lista(1, 2, 3)
        esperado = 1
        observado = lista.primero(l)
        self.assertEqual(esperado, observado)

    def test_resto(self):
        l = lista.lista(1, 2, 3)
        esperado = lista.lista(2, 3)
        observado = lista.resto(l)
        self.assertEqual(esperado, observado)

    def test_vacia(self):
        l = lista.lista()
        esperado = True
        observado = lista.vacia(l)
        self.assertEqual(esperado, observado)

        l = lista.lista(1)
        esperado = False
        observado = lista.vacia(l)
        self.assertEqual(esperado, observado)

    def test_largo(self):
        l = lista.lista()
        esperado = 0
        observado = lista.largo(l)
        self.assertEqual(esperado, observado)

        l = lista.lista(1, 2, 3)
        esperado = 3
        observado = lista.largo(l)
        self.assertEqual(esperado, observado)

    def test_sumar(self):
        l = lista.lista()
        esperado = 0
        observado = lista.sumar(l)
        self.assertEqual(esperado, observado)

        l = lista.lista(1, 2, 3)
        esperado = 6
        observado = lista.sumar(l)
        self.assertEqual(esperado, observado)

    def test_mapear(self):
        l = lista.lista(1, 2, 3)
        esperado = lista.lista(1, 4, 9)
        observado = lista.mapear(lambda x: x * x, l)
        self.assertEqual(esperado, observado)

        esperado = lista.lista(0, 1, 2)
        observado = lista.mapear(lambda x: x - 1, l)
        self.assertEqual(esperado, observado)

    def test_zipear(self):
        l1 = lista.lista(1, 2, 3)
        l2 = lista.lista(3, 2, 1)

        esperado = lista.lista(4, 4, 4)
        observado = lista.zipear(lambda x, y: x + y, l1, l2)
        self.assertEqual(esperado, observado)

        esperado = lista.lista(3, 4, 3)
        observado = lista.zipear(lambda x, y: x * y, l1, l2)
        self.assertEqual(esperado, observado)
