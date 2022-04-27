'''aluna: larissa de souza schottz
curso: análise e desenvolvimento de sistemas
'''
# importações necessárias para rodar o programa:
import emoji
import random
from time import sleep


def point():
    print('=-' * 30)
def min_pont():
    print('-'*30)


# início do programa, boas vindas, instruções de jogo e recebendo o número de jogadores e o nome deles e colocando dentro de uma lista
# contador para número de jogadores, iniciando em 0
print(emoji.emojize('\033[1;97;42mBem-vindos ao Zombie Dice!\033[m :zombie:'))
print('*Instruções de jogo* \n'
      'Objetivo principal: Comer mais cérebros (13 no total) que seus amigos e tentar não levar um tiro de espingarda!\n'
      'O jogo possui 13 dados com 6 faces cada.\n'
      'A cada rodada o jogador pode jogar 3 dados, escolhendo se vai ou não continuar jogando. Caso leve 3 tiros, '
      'perde todos os cérebros que ganhou até o momento, caso consiga 13 cérebros, jogador vence.\n'
      '\033[1;32mDados verdes:\033[m Possuem 6 dados com 3 cérebros, 2 passos, 1 tiro.\n'
      '\033[1;33mDados amarelos:\033[m Possuem 4 dados com 2 cérebros, 2 passos e 2 tiros.\n'
      '\033[1;31mDados vermelhos:\033[m Possuem 3 dados com 1 cérebro, 2 passos e 3 tiros.')
point()
print('Insira as informações ')
sleep(0.5)

import random

# Solicitando o número de jogadores
num_players = 0  # total de jogadores
while True:
    num_players = int(input('Qual o total de jogadores? (Mínimo 2, máximo 8): '))
    if num_players <= 1:
        print(f'Não é possivel jogar apaenas com {num_players} pessoa, insira um número de jogadores válido. ')
    elif num_players >= 8:
        print(f'Não é possivel jogar apenas com {num_players} pessoa, insira um número de jogadores válido. ')
    else:
        print('Legal!')
        break

list_jog = []
for i in range(num_players):
    nomes = str(input(f'Nome do jogador de número {i + 1} é: '))
    list_jog.append(nomes)
point()



# numero total de jogadas em um único jogo
max_rodadas = num_players * 500

# pontos necessários para vencer o jogo
ponto_max = 13

# número total de dados
num_dados = 13

# número de faces do dado
num_faces = 6

# Inicializando a pontuação
pontos = [0] * num_players

# número de dados para cada turno
dados_jogada = 3

# definindo cada elemento e quantidade para cada cor, verde possui maior quantidade de cérebros, enquanto o vermelho tem menos
dadoverde = ["cerebro", "passos", "tiros", "cerebro", "cerebro", "passos", "verde"]
dadoamarelo = ["passos", "cerebro", "tiros", "passos", "tiros", "cerebro", "amarelo"]
dadovermelho = ["tiros", "passos", "cerebro", "tiros", "tiros", "passos", "vermelho"]

# Definindo os dados que o jogo usará com base no número máximo de lados do dado
verde_lados = []
amarelo_lados = []
vermelho_lados = []
for i in range(0, num_faces):
    verde_lados.append(dadoverde[i % (len(dadoverde) - 1)])
    amarelo_lados.append(dadoamarelo[i % (len(dadoamarelo) - 1)])
    vermelho_lados.append(dadovermelho[i % (len(dadovermelho) - 1)])
verde_lados.append("verde")
amarelo_lados.append("amarelo")
vermelho_lados.append("vermelho")

# Definindo os dados do jogo

list_dados = [
    dadoverde, dadoverde, dadoverde, dadoverde, dadoverde, dadoverde,
    dadoamarelo, dadoamarelo, dadoamarelo, dadoamarelo,
    dadovermelho, dadovermelho, dadovermelho
]

# certificando os valores selecionados para as variáveis
if dados_jogada > num_dados:
    print("O número de dados selecionados por rodada excede o número total de dados no jogo.(", dados_jogada, ">",
          num_dados, ")")
    raise SystemExit

for j in range(0, max_rodadas):
    print("PONTUAÇÃO")
    for i in range(0, num_players):
        print("Jogador", i + 1, ":", pontos[i])
    print("Jogador ", (j % num_players) + 1, "é sua vez...")
    input("Pressione enter para continuar...")
    print(emoji.emojize('SORTEANDO OS DADOS.... :game_die:'))
    sleep(0.5)
    point()

    cerebro = 0
    tiros = 0

    dados_selec = random.sample(range(0, num_dados), num_dados)

    # Jogando os dados
    # Selecionando os 3 primeiros dados sorteados
    jogar_dado = []
    for dado_sort in range(0, dados_jogada):
        jogar_dado.append(dados_selec[dado_sort])

    opcao = "s"
    # loop enquanto o jogador quiser continuar jogando os dados ou não
    while opcao == "s":
        # Jogando os 3 dados
        print("Os dados sorteados foram:  ")
        point()
        for i in range(0, dados_jogada):
            jogo = list_dados[jogar_dado[i]][(random.randint(0, num_faces - 1))]
            print(list_dados[jogar_dado[i]][num_faces], " - ", jogo)

            # Se o jogador conseguiu um cérebro, é incrementado mais um cérebro, adicionando ao total
            # Se o jogador conseguiu um tiro, é incrementado mais um tiro, adicionando ao total
            # Se o jogador conseguir um passo, nem perde e nem ganha pontos
            if jogo == "cerebro":
                cerebro += 1
                jogar_dado[i] = dados_selec[dado_sort]
                dado_sort += 1
            elif jogo == "tiros":
                tiros += 1
                jogar_dado[i] = dados_selec[dado_sort]
                dado_sort += 1

        min_pont()
        print(emoji.emojize(f'Quantidade de :brain::'))
        print(cerebro)
        print(emoji.emojize(f'Quantidade de :water_pistol::'))
        print(tiros)
        min_pont()

        # se o jogador não tiver sorteado 3 tiros, poderá optar por continuar ou não a rodada
        if tiros < 3:
            opcao = input("Jogar novamente? s/n ").strip().lower()
        else:
            break

    # Se o jogador não tiver sorteado ainda 3 tiros, o programa irá adicionar o número de cérebros aos pontos totais
    if tiros < 3:
        pontos[j % num_players] += cerebro
        # Verificando se o jogador tem cérebros suficientes para vencer
        if pontos[j % num_players] >= ponto_max:
            print("Jogador", j % num_players + 1, "ganhou!")
            raise SystemExit
        else:
            print("Você tem", pontos[j % num_players], "pontos")
    else:
        print(emoji.emojize(f'Você levou 3 tiros :collision:'))
        print(emoji.emojize('Você perdeu os :brain: que havia conseguido nessa rodada...'))

    print("")