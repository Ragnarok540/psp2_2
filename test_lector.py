import unittest
import lector

class LectorTestCase(unittest.TestCase):

    def test_leer_archivo(self):
        esperado = ((130.0, (650.0, (99.0, (150.0, (128.0, (302.0, (95.0, (945.0, (368.0, (961.0, None)))))))))),
                    (186.0, (699.0, (132.0, (272.0, (291.0, (331.0, (199.0, (1890.0, (788.0, (1601.0, None)))))))))))
        observado = lector.leer_archivo("test.csv")
        self.assertEqual(esperado, observado)

        self.assertRaises(FileNotFoundError, lector.leer_archivo, "xyz.csv")
