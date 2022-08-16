import os
import unittest

from model.Balancer import Balancer
from error import LimitTasksException, LimitUmaxException


class TestBalancer(unittest.TestCase):

    def mock_acept_balancer(self):
        input_text = """4
2
1
3
0
1
0
1"""
        with open("input.txt", "w") as fs:
            fs.write(input_text)

    def mock_exception_limits_ttasks(self):
        input_text = """11
2
1
3
0
1
0
1"""
        with open("input.txt", "w") as fs:
            fs.write(input_text)

    def mock_exception_limts_umax(self):
        input_text = """4
11
1
3
0
1
0
1"""
        with open("input.txt", "w") as fs:
            fs.write(input_text)


    def test_balancer_start(self):
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

        with open("output.txt") as fs:
            texto = fs.read()

        self.assertEqual(texto, output_text)

    def test_exception_limits_tasks(self):
        self.mock_exception_limits_ttasks()
        with self.assertRaises(LimitTasksException):
            Balancer().start()

    def test_exception_limits_umax(self):
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