import unittest
from bhaskara_test import bhaskara_test


class TestBhaskara(unittest.TestCase):
    def test_sol_real(self):
        a, b, c = 1, -3, 2  # x^2 - 3x + 2 = 0
        x1, x2 = bhaskara_test(a, b, c)
        self.assertAlmostEqual(x1, 2)
        self.assertAlmostEqual(x2, 1)

    def test_sem_sol_real(self):
        a, b, c = 2, 3, 10  # 2x^2 + 3x + 10 = 0 (sem soluções reais)
        solucao = bhaskara_test(a, b, c)
        self.assertIsNone(solucao)

    def test_sol_dupla(self):
        a, b, c = 1, -4, 4  # x^2 - 4x + 4 = 0 (solução dupla: x = 2)
        x1, x2 = bhaskara_test(a, b, c)
        self.assertAlmostEqual(x1, 2)
        self.assertAlmostEqual(x2, 2)


if __name__ == '__main__':
    unittest.main()
