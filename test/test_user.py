import unittest

from model.User import User


class TestUser(unittest.TestCase):
    """
        Classe de Teste do Objeto User.
    """

    def setUp(self):
        amount_tasks = 4
        self.user = User(amount_tasks)

    def test_not_finhsh_tasks(self):
        """
            Teste de verificação da não finalização das tasks do usuário.
        """
        self.assertFalse( self.user.is_finsh_tasks() )

    def test_finhsh_tasks(self):
        """
            Teste de verificação da finalização das tasks do usuário.
        """
        for _ in range(4):
            self.user.decrement_task()
        self.assertTrue( self.user.is_finsh_tasks() )

    def test_decrement_task(self):
        """
            Teste de decremento da quantidade das tasks, apos processadas.
        """
        self.user.decrement_task()
        self.assertEqual(self.user.ttask, 3 )


if __name__ == "__main__":
    unittest.main()
