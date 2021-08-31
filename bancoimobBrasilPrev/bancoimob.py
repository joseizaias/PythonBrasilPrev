import random
import utils


def ordenaPorSaldo(e):
    return e['saldo']


def retornaVencedor(vencedores, ordemQueJogam):
    relacaoVencedores = vencedores
    ordem = ordemQueJogam
    maiorValor = 0
    idVencedor = 0

    for index in range(len(ordem) -1, 0, -1):
        
        if vencedores[ordem[index]]['saldo'] >= maiorValor:
            maiorValor = vencedores[ordem[index]]['saldo']
            idVencedor = ordem[index]
        
    return idVencedor


# comportamentos:
COMPORTAMENTOS = ('impulsivo', 'exigente', 'cauteloso', 'aleatorio')

#  Numero maximo de partidas por simulação - que pode finalizar por timeout
NUM_MAX_PARTIDAS = 1000

# Numero de Simulacoes 
SIMULACOES = 300

# Numero de Jogadores na Partida
NUM_JOGADORES = 4
# Quantidade de partidas que terminam por timeout
qtdePartidasAcabamPorTimeout = 0

# total de turnos de todas as partidas (para calcular a media de turnos por partida
totalTurnosTodasAsPartidas = 0

# vitorias por comportamento dos jogadores
# indice 0 => 'impulsivo', 1 =>'exigente', 2 => 'cauteloso e 3 => 'aleatorio
totalVitoriaPorComportamento = [0, 0, 0, 0]  

for simulacao in range(SIMULACOES):
    # quantidade de partidas que terminam por timeout
    quantidadePartidasTimeOut = 0

    # qtde de jogadores na partida. Se somente um, temos o vencedor!
    vencedor = 4

    #cria tabuleiro
    tabuleiro = utils.criaTabuleiro()

    # cria jogadores
    jogadores = utils.criaJogadores()

    # definindo sequencia de quem joga primeiro // lembrando que: 0 => 'impulsivo', 1 =>'exigente', 2 => 'cauteloso e 3 => 'aleatorio
    ordemQueJogam = utils.ordemQueJogadoresJogam( [ 0, 1, 2, 3 ] )

    # Dita de quem eh a vez de jogar // inicia com um numero superior ao de jogadores para zerar no inicio da partida
    jogadorDaVez = 777  

    while (vencedor != 1 and quantidadePartidasTimeOut < NUM_MAX_PARTIDAS):
        jogadorDaVez += 1
        quantidadePartidasTimeOut += 1

        if (jogadorDaVez > NUM_JOGADORES -1):
            jogadorDaVez = 0

        # se jogador da vez estah inativo
        if not(jogadores[ordemQueJogam[jogadorDaVez]]['aindaNoJogo']):
            continue
        
        # joga-se o dado
        resultadoDado = utils.dado()

        if ( jogadores[ordemQueJogam[jogadorDaVez]]['posicaoTabuleiro'] + resultadoDado ) > 20:
            jogadores[ordemQueJogam[jogadorDaVez]]['saldo'] += 100
            jogadores[ordemQueJogam[jogadorDaVez]]['posicaoTabuleiro'] += resultadoDado - 20
        else:
            jogadores[ordemQueJogam[jogadorDaVez]]['posicaoTabuleiro'] += resultadoDado
        
        localTabuleiro = jogadores[ordemQueJogam[jogadorDaVez]]['posicaoTabuleiro']

        if tabuleiro[localTabuleiro]['proprietario'] == -1:

            if jogadores[ordemQueJogam[jogadorDaVez]]['player'] =='impulsivo': 
                if (jogadores[ordemQueJogam[jogadorDaVez]]['saldo']) > tabuleiro[localTabuleiro]['venda']:
                    jogadores[ordemQueJogam[jogadorDaVez]]['saldo'] -= tabuleiro[localTabuleiro]['venda']
                    tabuleiro[localTabuleiro]['proprietario'] = ordemQueJogam[jogadorDaVez]
            elif jogadores[ordemQueJogam[jogadorDaVez]]['player'] =='exigente':
                if tabuleiro[localTabuleiro]['aluguel'] > 50:
                    if (jogadores[ordemQueJogam[jogadorDaVez]]['saldo']) > tabuleiro[localTabuleiro]['venda']:
                        jogadores[ordemQueJogam[jogadorDaVez]]['saldo'] -= tabuleiro[localTabuleiro]['venda']
                        tabuleiro[localTabuleiro]['proprietario'] = ordemQueJogam[jogadorDaVez]
            elif jogadores[ordemQueJogam[jogadorDaVez]]['player'] =='cauteloso':
                if tabuleiro[localTabuleiro]['venda'] + 80 < jogadores[ordemQueJogam[jogadorDaVez]]['saldo']:
                    jogadores[ordemQueJogam[jogadorDaVez]]['saldo'] -= tabuleiro[localTabuleiro]['venda']
                    tabuleiro[localTabuleiro]['proprietario'] = ordemQueJogam[jogadorDaVez]
            elif jogadores[ordemQueJogam[jogadorDaVez]]['player'] =='aleatorio':
                if (jogadores[ordemQueJogam[jogadorDaVez]]['saldo']) > tabuleiro[localTabuleiro]['venda']:
                    if random.randrange(0,2) == 1:
                        jogadores[ordemQueJogam[jogadorDaVez]]['saldo'] -= tabuleiro[localTabuleiro]['venda']
                        tabuleiro[localTabuleiro]['proprietario'] = ordemQueJogam[jogadorDaVez]
        else:
            jogadores[tabuleiro[localTabuleiro]['proprietario']]['saldo'] = jogadores[tabuleiro[localTabuleiro]['proprietario']]['saldo'] + tabuleiro[localTabuleiro]['aluguel']
            jogadores[ordemQueJogam[jogadorDaVez]]['saldo'] = jogadores[ordemQueJogam[jogadorDaVez]]['saldo'] - tabuleiro[localTabuleiro]['aluguel']
            
            if jogadores[ordemQueJogam[jogadorDaVez]]['saldo'] < 0:
                vencedor -= 1
                jogadores[ordemQueJogam[jogadorDaVez]]['aindaNoJogo'] = False
    
    totalTurnosTodasAsPartidas += quantidadePartidasTimeOut

    if vencedor == 1:
        if jogadores[0]['aindaNoJogo']:
            totalVitoriaPorComportamento[0] += 1
        elif jogadores[1]['aindaNoJogo']:
            totalVitoriaPorComportamento[1] += 1
        elif jogadores[2]['aindaNoJogo']:
            totalVitoriaPorComportamento[2] += 1
        elif jogadores[3]['aindaNoJogo']:
            totalVitoriaPorComportamento[3] += 1
    else:
        qtdePartidasAcabamPorTimeout += 1
        vencedor = retornaVencedor(jogadores, ordemQueJogam)
        totalVitoriaPorComportamento[vencedor] += 1

### Exibe Relatorio Final
print('\n\nRelatorio...\n\n')
print('Total de Partidas que Terminam por TimeOut: {0:4}'.format(qtdePartidasAcabamPorTimeout))
print ('\nQuantidade de Turnos (em media) demora uma partida: {0:4.2f}'.format(totalTurnosTodasAsPartidas / SIMULACOES) )

oQueMaisVence = 0
maiorQuantidade = -1

print('\n==== Percentual de Vitorias Por Comportamento ====\n')

for i in range(len(totalVitoriaPorComportamento)):
    if totalVitoriaPorComportamento[i] > maiorQuantidade:
        maiorQuantidade = totalVitoriaPorComportamento[i]
        oQueMaisVence = i
    
    print ('=> {:15}: {:.2%}'.format(COMPORTAMENTOS[i],totalVitoriaPorComportamento[i] / SIMULACOES))

print ('\n\n===> O Comportamento que mais venceu foi: << {} >>'.format(COMPORTAMENTOS[oQueMaisVence]))
    