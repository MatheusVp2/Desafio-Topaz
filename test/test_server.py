import unittest
from error import NumberOfUsersExceededException

from model.Server import Server
from model.ServerStatusEnum import ServerStatusEnum
from model.User import User

class TestServer(unittest.TestCase):
    """
        Classe de Teste do Objeto Servidor.
    """

    def setUp(self):
        self.user = User(4)
        self.server = Server("Server1", self.user, 2)

    def test_add_new_user(self):
        """
            Teste de adição de novo usuário no servidor.
        """
        self.server.add_new_user( User( 4 ) )
        self.assertEqual( self.server.get_len_users(), 2 )

    def test_add_new_user_number_of_user_exceeded_exception(self):
        """
            Teste de adição de novo usuário, excendendo o limite
            de usuários do servidor.
        """
        with self.assertRaises( NumberOfUsersExceededException ):
            self.server.add_new_user( User( 4 ) )
            self.server.add_new_user( User( 4 ) )
        
    def test_remove_user(self):
        """
            Teste do metodo de remoção do usuário do servidor.
        """
        self.server.remove_user( self.user )
        self.assertEqual( self.server.get_len_users(), 0 )

    def test_is_active_server(self):
        """
            Teste de verificação do status do servidor esta Ativo.
        """
        self.assertTrue(self.server.is_active())

    def test_close_server_method(self):
        """
            Teste de verificação do status do servidor esta Inativo.
        """
        self.server.close_server()
        self.assertEqual( self.server.status, ServerStatusEnum.INACTIVE )

    def test_process_tasks_user(self):
        """
            Teste de processamento da task dos usuarios no servidor.
        """
        for _ in range(4):
            self.server.process()
        self.assertFalse( self.server.is_active() )



if __name__ == "__main__":
    unittest.main()
