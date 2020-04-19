import unittest
import estadistica
from lista import lista as ls

class EstadisticaTestCase(unittest.TestCase):

    def setUp(self):
        self.l_pro_des_1 = ls(186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601)
        self.l_pro_des_2 = ls(160, 591, 114, 229, 230, 270, 128, 1657, 624, 1503)
        self.l_pro_des_3 = ls(15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2)        
        self.eps = ls(130, 650, 99,  150, 128, 302, 95,  945,  368, 961)
        self.paams = ls(163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130)
        self.aaams = ls(186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601)
        self.adh = ls(15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2)

    def test_promedio(self):
        l = ls()
        esperado = 0
        observado = estadistica.promedio(l)
        self.assertEqual(esperado, observado)

        l = ls(5)
        esperado = 5
        observado = estadistica.promedio(l)
        self.assertEqual(esperado, observado)

        l = ls(1, 1.5)
        esperado = 1.25
        observado = estadistica.promedio(l)
        self.assertEqual(esperado, observado)

        esperado = 638.9
        observado = estadistica.promedio(self.l_pro_des_1)
        self.assertEqual(esperado, observado)

        esperado = 550.6
        observado = estadistica.promedio(self.l_pro_des_2)
        self.assertEqual(esperado, observado)

        esperado = 60.31999999999999
        observado = estadistica.promedio(self.l_pro_des_3)
        self.assertEqual(esperado, observado)

    def test_desviacion(self):
        l = ls()
        esperado = 0
        observado = estadistica.desviacion(l)
        self.assertEqual(esperado, observado)

        l = ls(5)
        esperado = 0
        observado = estadistica.desviacion(l)
        self.assertEqual(esperado, observado)

        esperado = 625.6339806770231
        observado = estadistica.desviacion(self.l_pro_des_1)
        self.assertEqual(esperado, observado)

        esperado = 572.0268447469149
        observado = estadistica.desviacion(self.l_pro_des_2)
        self.assertEqual(esperado, observado)

        esperado = 62.25583060601187
        observado = estadistica.desviacion(self.l_pro_des_3)
        self.assertEqual(esperado, observado)

    def test_beta_1(self):
        # Test 1 estimated proxy size vs actual added and modified size
        esperado = 1.7279324262069864
        observado = estadistica.beta_1(self.eps, self.aaams)
        self.assertEqual(esperado, observado)
        
        # Test 2 estimated proxy size vs actual development hours
        esperado = 0.16812664988162906
        observado = estadistica.beta_1(self.eps, self.adh)
        self.assertEqual(esperado, observado)

        # Test 3 plan added and modified size vs actual added and modified size
        esperado = 1.430966943551199
        observado = estadistica.beta_1(self.paams, self.aaams)
        self.assertEqual(esperado, observado)

        # Test 4 plan added and modified size vs actual development hours
        esperado = 0.14016352638883633
        observado = estadistica.beta_1(self.paams, self.adh)
        self.assertEqual(esperado, observado)

    def test_beta_0(self):
        # Test 1 estimated proxy size vs actual added and modified size
        esperado = -22.55253275203438
        observado = estadistica.beta_0(self.eps, self.aaams)
        self.assertEqual(esperado, observado)

        # Test 2 estimated proxy size vs actual development hours
        esperado = -4.038881574687608
        observado = estadistica.beta_0(self.eps, self.adh)
        self.assertEqual(esperado, observado)

        # Test 3 plan added and modified size vs actual added and modified size
        esperado = -23.92388825291539
        observado = estadistica.beta_0(self.paams, self.aaams)
        self.assertEqual(esperado, observado)

        # Test 4 plan added and modified size vs actual development hours
        esperado = -4.603745423308993
        observado = estadistica.beta_0(self.paams, self.adh)
        self.assertEqual(esperado, observado)

    def test_r_xy(self):
        # Test 1 estimated proxy size vs actual added and modified size
        esperado = 0.9544965741046826
        observado = estadistica.r_xy(self.eps, self.aaams)
        self.assertEqual(esperado, observado)

        # Test 2 estimated proxy size vs actual development hours
        esperado = 0.9333068981405513
        observado = estadistica.r_xy(self.eps, self.adh)
        self.assertEqual(esperado, observado)

        # Test 3 plan added and modified size vs actual added and modified size
        esperado = 0.9631140931490527
        observado = estadistica.r_xy(self.paams, self.aaams)
        self.assertEqual(esperado, observado)

        # Test 4 plan added and modified size vs actual development hours
        esperado = 0.9480329874300509
        observado = estadistica.r_xy(self.paams, self.adh)
        self.assertEqual(esperado, observado)

    def test_r2(self):
        # Test 1 estimated proxy size vs actual added and modified size
        esperado = 0.9110637099775758
        observado = estadistica.r2(self.eps, self.aaams)
        self.assertEqual(esperado, observado)

        # Test 2 estimated proxy size vs actual development hours
        esperado = 0.8710617661167375
        observado = estadistica.r2(self.eps, self.adh)
        self.assertEqual(esperado, observado)

        # Test 3 plan added and modified size vs actual added and modified size
        esperado = 0.9275887564223222
        observado = estadistica.r2(self.paams, self.aaams)
        self.assertEqual(esperado, observado)

        # Test 4 plan added and modified size vs actual development hours
        esperado = 0.8987665452555471
        observado = estadistica.r2(self.paams, self.adh)
        self.assertEqual(esperado, observado)

    def test_y_k(self):
        # Test 1 estimated proxy size vs actual added and modified size
        esperado = 644.4293837638623
        observado = estadistica.y_k(self.eps, self.aaams, 386)
        self.assertEqual(esperado, observado)

        # Test 2 estimated proxy size vs actual development hours
        esperado = 60.85800527962121
        observado = estadistica.y_k(self.eps, self.adh, 386)
        self.assertEqual(esperado, observado)

        # Test 3 plan added and modified size vs actual added and modified size
        esperado = 528.4293519578474
        observado = estadistica.y_k(self.paams, self.aaams, 386)
        self.assertEqual(esperado, observado)

        # Test 4 plan added and modified size vs actual development hours
        esperado = 49.49937576278183
        observado = estadistica.y_k(self.paams, self.adh, 386)
        self.assertEqual(esperado, observado)
