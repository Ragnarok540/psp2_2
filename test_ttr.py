import unittest
import ttr
from lista import lista as ls

class TTRTestCase(unittest.TestCase):

    def setUp(self):
        self.l_t_1_a = ls(18, 18, 25, 31, 37, 82, 82, 87, 89, 230, 85, 87, 558)
        self.l_t_1_b = ls(3, 3, 3, 3, 3, 5, 4, 4, 4, 10, 3, 3, 10)
        self.l_t_2_a = ls(7, 12, 10, 12, 10, 12, 12, 12, 12, 8, 8, 8, 20, 14, 18, 12)
        self.l_t_2_b = ls(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

    def test_very_small(self):
        esperado = 4.395269124478685
        observado = ttr.very_small(self.l_t_1_a, self.l_t_1_b)
        self.assertEqual(esperado, observado)

        esperado = 6.33751796121173
        observado = ttr.very_small(self.l_t_2_a, self.l_t_2_b)
        self.assertEqual(esperado, observado)

    def test_small(self):
        esperado = 8.508138249389226
        observado = ttr.small(self.l_t_1_a, self.l_t_1_b)
        self.assertEqual(esperado, observado)

        esperado = 8.439281112126057
        observado = ttr.small(self.l_t_2_a, self.l_t_2_b)
        self.assertEqual(esperado, observado)

    def test_medium(self):
        esperado = 16.469620953940066
        observado = ttr.medium(self.l_t_1_a, self.l_t_1_b)
        self.assertEqual(esperado, observado)

        esperado = 11.238069244993529
        observado = ttr.medium(self.l_t_2_a, self.l_t_2_b)
        self.assertEqual(esperado, observado)

    def test_large(self):
        esperado = 31.88105392926987
        observado = ttr.large(self.l_t_1_a, self.l_t_1_b)
        self.assertEqual(esperado, observado)

        esperado = 14.965042481379422
        observado = ttr.large(self.l_t_2_a, self.l_t_2_b)
        self.assertEqual(esperado, observado)

    def test_very_large(self):
        esperado = 61.71372143193483
        observado = ttr.very_large(self.l_t_1_a, self.l_t_1_b)
        self.assertEqual(esperado, observado)

        esperado = 19.928022473189497
        observado = ttr.very_large(self.l_t_2_a, self.l_t_2_b)
        self.assertEqual(esperado, observado)
