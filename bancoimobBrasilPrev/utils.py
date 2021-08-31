import random

def dado ():
    return random.randrange(1, 7)


def criaTabuleiro ():
    tabuleiro = [
        { 'venda':  -1, 'aluguel': -1, 'proprietario': -1},  ## nao usado
        { 'venda': 111, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 222, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 133, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 234, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 225, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 256, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 257, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 258, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 129, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 370, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 291, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 282, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 213, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 314, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 115, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 316, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 417, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 218, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 119, 'aluguel': 55, 'proprietario': -1},
        { 'venda': 320, 'aluguel': 75, 'proprietario': -1},
        ]
    return tabuleiro


def criaJogadores():
    jogagores = [
        {'player': 'impulsivo', 'saldo': 300, 'aindaNoJogo': True, 'posicaoTabuleiro': -1 },
        {'player': 'exigente',  'saldo': 300, 'aindaNoJogo': True, 'posicaoTabuleiro': -1 },
        {'player': 'cauteloso', 'saldo': 300, 'aindaNoJogo': True, 'posicaoTabuleiro': -1 },
        {'player': 'aleatorio', 'saldo': 300, 'aindaNoJogo': True, 'posicaoTabuleiro': -1 }
    ]

    return jogagores


def ordemQueJogadoresJogam (lista_jogadores):
    lista = lista_jogadores
    random.shuffle(lista)
    return lista

    