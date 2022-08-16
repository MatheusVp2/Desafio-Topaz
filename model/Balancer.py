from typing import List
from functools import reduce

from model.Server import Server
from model.User import User
from error import LimitTasksException, LimitUmaxException


class Balancer:
    
    ttask: int
    umax: int
    users: List[int]
    servers: List[Server]
    loggers_output_file: List[str]

    def __init__(self) -> None:
        data = self.__read_file()
        self.servers = []
        self.loggers_output_file = []
        self.ttask = int( data.pop(0) )
        self.umax = int( data.pop(0) )
        self.users = list( map( lambda num : int(num), data ) )
        self.__validate_limits()

    def __validate_limits(self) -> None:
        """
            Função de validação dos limits de tasks e umax permitidos, gerando uma exceção caso venha
            passar dos limits permitidos.
        """
        if self.ttask < 1 or self.ttask > 10:
            raise LimitTasksException("Quantidade de ttask validas são entre 1 e 10.")
        
        if self.umax < 1 or self.umax > 10:
            raise LimitUmaxException("Quantidade de umax validas são entre 1 e 10.")

    def __read_file(self) -> List[str]:
        """
            Função de leitura de arquivo input.txt, retornando uma lista de informações das
            linhas do arquivo.
        """
        with open("input.txt", "r") as fs:
            return fs.read().splitlines()

    def __get_next_amount_user(self) -> int | None:
        """
            Metodo para pegar a proxima quantidade de usuarios a ser alocados nos servidores, caso
            não exista mais na lista retorna None.
        """
        return self.users.pop(0) if len( self.users ) != 0 else None

    def __get_last_server(self) -> Server | None:
        """
            Metodo onde pega sempre o ultimo servidor alocado, sendo assim o servidor com a
            quantidade necessaria ou não de usuarios a serem alocados, caso não exista na lista
            retorna None.
        """
        return self.servers[-1] if len( self.servers ) else None

    def __process_servers(self) -> None:
        """
            Metodo que executa, metodo interno da classe deo servidor de processamento do tick
            onde somente sera processado se o servidor estiver ativo.
        """
        for server in self.servers:
            if server.is_active():
                server.process()

    def __is_server_process_completed(self) -> bool:
        """
            Metodo de verificação de processamento completo, onde todos os servidores estao inativos
            sem usuarios em processamento.
        """
        active_servers = list( filter( lambda server : server.is_active(), self.servers ) )
        return len(active_servers) == 0

    def __create_new_server(self) -> None:
        """
            Metodo de reaproveitamento de codigo, para criar um novo servidor com usuario
            ja alocado.
        """
        amount_servers = len(self.servers)
        new_server = Server(f"Server{amount_servers + 1}", User(self.ttask), self.umax)
        self.servers.append(new_server)

    def __get_ticks_cost_count(self, value_tick: int) -> str:
        """
            Metodo de calculo dos ticks, utilizando map reduce, para o somatorio.
        """
        map_count = map( lambda server : (server.ticks * value_tick), self.servers )
        reduce_count = reduce( lambda a, b : a + b, map_count )
        return str(reduce_count)

    def __get_logger_output(self) -> str:
        """
            Metodo de logger de retorno para o output, da quantidade de usuarios por servidor.
        """
        active_servers = filter( lambda server : server.is_active(), self.servers )
        users = map( lambda server : str( server.get_len_users() ) , active_servers )
        return ",".join(users)

    def __write_logger_file(self) -> None:
        """
            Metodo de escrita no arquivo de output.
        """
        text = "\n".join( self.loggers_output_file )
        with open("output.txt", "w") as fs:
            fs.write(text)

    def start(self) -> None:
        """
            Metodo principal do balancemento de carga.
        """
        process_completed = False
        while process_completed == False:
            next_amount_user = self.__get_next_amount_user()
            if next_amount_user != None:
                for _ in range(next_amount_user):
                    last_server = self.__get_last_server()
                    if last_server == None:
                        self.__create_new_server()
                    elif last_server.is_full():
                        self.__create_new_server()
                    elif not last_server.is_full():
                        self.servers[-1].add_new_user( User( self.ttask ) )
            
            self.loggers_output_file.append( self.__get_logger_output() )
            self.__process_servers()

            process_completed = self.__is_server_process_completed()
            if process_completed:
                self.loggers_output_file.append('0')
                self.loggers_output_file.append( self.__get_ticks_cost_count( 1 ) )

        self.__write_logger_file()            
    
    def __str__(self) -> str:
        return f"Balancer( ttask={self.ttask}, umax={self.umax}, users={self.users}, servers={self.servers} )"