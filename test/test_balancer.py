import os
import unittest

from model.Balancer import Balancer
from error import LimitTasksException, LimitUmaxException


class TestBalancer(unittest.TestCase):
    """
        Classe de Teste do Objeto Balanceador.
    """

    def mock_acept_balancer(self):
        """
            Metodo de mock de informações corretas para o teste.
        """
        input_text = """4
2
1
3
0
1
0
1"""
        with open("input.txt", "w", encoding="utf-8") as stream:
            stream.write(input_text)

    def mock_exception_limits_ttasks(self):
        """
            Metodo de mock de informações incorretas de ttasks para o teste.
        """
        input_text = """11
2
1
3
0
1
0
1"""
        with open("input.txt", "w", encoding="utf-8") as stream:
            stream.write(input_text)

    def mock_exception_limts_umax(self):
        """
            Metodo de mock de informações incorretas de umax para o teste.
        """
        input_text = """4
11
1
3
0
1
0
1"""
        with open("input.txt", "w", encoding="utf-8") as stream:
            stream.write(input_text)


    def test_balancer_start(self):
        """
            Teste de Unidade do Metodo Start do Balancer com Implementação correta.
        """
        self.mock_acept_balancer()
        Balancer().start()

        output_text = """1
2,2
2,2
2,2,1
1,2,1
2
2
1
1
0
15"""

        with open("output.txt", "r", encoding="utf-8") as stream:
            texto = stream.read()

        self.assertEqual(texto, output_text)

    def test_exception_limits_tasks(self):
        """
            Teste de Unidade do Metodo Start do Balancer com Implementação incoreta
            gerendo exception LimitTasksException.
        """
        self.mock_exception_limits_ttasks()
        with self.assertRaises(LimitTasksException):
            Balancer().start()

    def test_exception_limits_umax(self):
        """
            Teste de Unidade do Metodo Start do Balancer com Implementação incoreta
            gerendo exception LimitUmaxException.
        """
        self.mock_exception_limts_umax()
        with self.assertRaises(LimitUmaxException):
            Balancer().start()


    def tearDown(self) -> None:
        try:
            os.remove("input.txt")
            os.remove("output.txt")
        except:
            pass

if __name__ == "__main__":
    unittest.main()
