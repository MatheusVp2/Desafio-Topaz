import unittest

from model.User import User


class TestUser(unittest.TestCase):

    def setUp(self):
        amount_tasks = 4
        self.user = User(amount_tasks)

    def test_not_finhsh_tasks(self):
        self.assertFalse( self.user.is_finsh_tasks() )

    def test_finhsh_tasks(self):
        for _ in range(4):
            self.user.decrement_task()
        self.assertTrue( self.user.is_finsh_tasks() )

    def test_decrement_task(self):
        self.user.decrement_task()
        self.assertEqual(self.user.ttask, 3 )

    def test_to_string_method(self):
        self.assertEqual(self.user.__str__(), "User( ttask=4 )")


if __name__ == "__main__": 
    unittest.main()