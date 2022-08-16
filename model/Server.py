from typing import List
from error import NumberOfUsersExceededException

from model.User import User
from model.ServerStatusEnum import ServerStatusEnum


class Server:
    
    name: str
    users : List[User]
    ticks: int
    umax: int
    status: str
    
    def __init__(self, _name: str, user: User, _umax: int) -> None:
        self.users = [ user ]
        self.ticks = 0
        self.umax = _umax
        self.name = _name
        self.status = ServerStatusEnum.ACTIVE

    def __add_tick(self) -> None:
        """
            Metodo de adição de ticks, no processamento dos servidor
        """
        self.ticks += 1

    def __process_users(self) -> None:
        """
            Metodo de processamento das tasks dos usuarios, onde decrementa as taks dos usuarios
            pos processamento, e remove o ususario apos completar as tasks.
        """
        users_finsh_task: List[User] = []
        for user in self.users:
            user.decrement_task()
            if user.is_finsh_tasks():
                users_finsh_task.append(user)
        self.__remove_users_finsh_task(users_finsh_task)

    def __remove_users_finsh_task(self, users_finsh_task: List[User]):
        """
            Metodo de remoção dos usuarios que teve as tasks completas.
        """
        for user_finsh in users_finsh_task:
            self.remove_user(user_finsh)

    def process(self) -> None:
        """
            Metodo principal de processamento do servidor.
        """
        self.__process_users()
        self.__add_tick()
        if self.is_finsh_tasks():
            self.close_server()
        
    def add_new_user(self, user: User) -> None:
        """
            Metodo de alocação de novo usuario para o servidor.
        """
        if self.is_full():
            raise NumberOfUsersExceededException("Quantiade de usuarios no servidor excedida.")
        self.users.append(user)
    
    def get_len_users(self) -> int:
        """
            Metodo de controle que retorna quantidade de usuarios no servidor.
        """
        return len(self.users)

    def remove_user(self, user: User) -> None:
        """
            Metodo de remoção do usuario do servidor.
        """
        self.users.remove(user)

    def close_server(self) -> None:
        """
            Metodo de Inativação do Servidor.
        """
        self.status = ServerStatusEnum.INACTIVE

    def is_finsh_tasks(self) -> bool:
        """
            Metodo de controle para verificar se todas as tasks foram finalizadas, justamente
            por não haver mais usuario conectados.
        """
        return self.get_len_users() == 0
    
    def is_active(self):
        """
            Metodo de verificação se o servidor esta ativo
        """
        return self.status == ServerStatusEnum.ACTIVE

    def is_full(self) -> bool:
        """
            Metodo de verificação se o servidor esta com a capacidade maxima de usuarios.
        """
        return self.get_len_users() >= self.umax

    def __str__(self) -> str:
        users_qtd = self.get_len_users()
        return f"Server( name={self.name}, users={ users_qtd }, ticks={ self.ticks }, status={ self.status } )"
        