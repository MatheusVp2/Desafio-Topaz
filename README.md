# Desafio Topaz

### Instruções
- Resolva o problema proposto no documento em anexo e disponibilize o código via github, nos envie o link do seu repositório quando finalizar a tarefa. Caso não possua afinidade com Python o teste pode ser desenvolvido em outra linguagem, mas damos preferência para resoluções em Python 3, caso a resolução seja em outra linguagem descreva no README a forma de executar o seu projeto.

### Rodar Programa
```shel
    python main.py
```

### Problema
- Balanceamento de carga é muito importante em ambientes Cloud. 
Estamos sempre tentando minimizar os custos para que possamos manter o número de servidores o menor possível. 
Em contrapartida a capacidade e performance aumenta quando adicionamos mais servidores. 
Em nosso ambiente de simulação, em cada tick, os usuários conectam aos servidores disponíveis e executam uma tarefa. 
Cada tarefa leva um número de ticks para ser ﬁnalizada, e após isso o usuário se desconecta automaticamente.

- Os servidores são máquinas virtuais que se auto criam para acomodar novos usuários. 
Cada servidor custa R$ 1,00 por tick e suporta no máximo umax usuários simultaneamente. 
Você deve ﬁnalizar servidores que não estão sendo mais usados.
O desaﬁo é fazer um programa em Python que recebe usuários e os aloca nos servidores tentando manter o menor custo possível.

### Dicionário
- tick = 'unidade básica de tempo da simulação'
- ttask = 'o número de ticks de uma tarefa'
- umax = 'capacidade de usuarios no servidor simultaneamente'

### Input
- Primeira Linha possui o valor de ttask.
- Segunda linha possui o valor de umax.
- Linhas seguintes contém os números de novos ususários para cada tick.

### Output
- Um arquivo onde cada linha contém uma lista de servidores disponíveis no ﬁnal de cada tick, representado pelo número de usuários em cada servidor separados por vírgula e, ao ﬁnal, o custo total por utilização dos servidores.

### Limites
- 1 ≤ ttask ≤ 10
- 1 ≤ umax ≤ 10

### Exemplo 

- input.txt
```txt
4
2
1
3
0
1
0
1
```
- output.txt
```txt
1
2,2
2,2
2,2,1
1,2,1
2
2
1
1
0
15
```

| Tick | Input | Output | Explicação                                                         |
|------|-------|--------|--------------------------------------------------------------------|
| 1    | 1     | 1      | 1 servidor para 1 usuário. (1 servidor criado)                     |
| 2    | 3     | 2,2    | 2 servidores para 4 usuários. (1 servidor criado)                  |
| 3    | 0     | 2,2    | 2 servidores para 4 usuários. (nenhum servidor criado ou removido) |
| 4    | 1     | 2,2,1  | 3 servidores para 5 usuários. (1 servidor criado)                  |
| 5    | 0     | 1,2,1  | 3 servidores para 4 usuários. (nenhum servidor criado ou removido) |
| 6    | 1     | 2      | 1 servidor para 2 usuários. (2 servidores removidos)               |
| 7    |       | 2      | 1 servidor para 2 usuários. (nenhum servidor criado ou removido)   |
| 8    |       | 1      | 1 servidor para 1 usuário. (nenhum servidor criado ou removido)    |
| 9    |       | 1      | 1 servidor para 1 usuário. (nenhum servidor criado ou removido)    |
|      |       | 0      | nenhum servidor e nenhum usuário. (1 servidor removido)            |
|      |       | 15     | Custo Total: R$1 x 5 ticks ( primeira vm ) + R$1 x 4 ticks ( segunda vm ) + R$1 x 6 ticks ( terceira vm ) = R$15     |


### Teste
```shel
    python -m unittest discover test
    
    pip install coverage
    python -m coverage run -m unittest discover test
    python -m coverage report
    python -m coverage html
```

### Path Tree
```
.
├── error
│   └── __init__.py
├── model
│   ├── Balancer.py
│   ├── Server.py
│   ├── ServerStatusEnum.py
│   ├── User.py
│   └── __init__.py
├── test
│   ├── test_server.py
│   └── test_user.py
├── input.txt
├── main.py
├── output.txt
└── readme.md
```
