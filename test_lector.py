import unittest
import lector

class LectorTestCase(unittest.TestCase):

    def test_leer_archivo(self):
        esperado = ((18.0, (18.0, (25.0, (31.0, (37.0, (82.0, (82.0, (87.0, (89.0, (230.0, (85.0, (87.0, (558.0, None))))))))))))), (3.0, (3.0, (3.0, (3.0, (3.0, (5.0, (4.0, (4.0, (4.0, (10.0, (3.0, (3.0, (10.0, None))))))))))))))
        observado = lector.leer_archivo("test1.csv")
        self.assertEqual(esperado, observado)

        esperado = ((7.0, (12.0, (10.0, (12.0, (10.0, (12.0, (12.0, (12.0, (12.0, (8.0, (8.0, (8.0, (20.0, (14.0, (18.0, (12.0, None)))))))))))))))), (1.0, (1.0, (1.0, (1.0, (1.0, (1.0, (1.0, (1.0, (1.0, (1.0, (1.0, (1.0, (1.0, (1.0, (1.0, (1.0, None)))))))))))))))))
        observado = lector.leer_archivo("test2.csv")
        self.assertEqual(esperado, observado)

        self.assertRaises(FileNotFoundError, lector.leer_archivo, "xyz.csv")
