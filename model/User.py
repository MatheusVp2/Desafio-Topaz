class User:
    """
        Classe do Usuário.
    """
    ttask: int
    def __init__(self, _ttask: int) -> None:
        self.ttask = _ttask

    def is_finsh_tasks(self) -> None:
        """
            Metodo de verificação das tasks concluidas do usuario.
        """
        return self.ttask == 0

    def decrement_task(self) -> None:
        """
            Metodo de decremento de tasks, do usuario.
        """
        self.ttask -= 1

    def __str__(self) -> str:
        return f"User( ttask={self.ttask} )"
