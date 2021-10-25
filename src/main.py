from show import *
from jogo import *


def escolher_cor():
    clear()
    mensagem('Bem vindo ao menu de escolha de cores!!!\nEscolha uma das opções abaixo para o jogador X', 'Ciano')
    contador = 0
    for nome, cor in cores.items():
        mensagem(f'     {contador} - {nome}', nome)
        contador += 1
    cor_jogador_x = input('\n-> ')
    mudar_cor_jogador('X', list(cores.keys())[int(cor_jogador_x)])

    clear()
    mensagem('Agora uma das opções abaixo para o jogador O', 'Ciano')
    contador = 0
    for nome, cor in cores.items():
        mensagem(f'     {contador} - {nome}', nome)
        contador += 1
    cor_jogador_o = input('\n-> ')
    mudar_cor_jogador('O', list(cores.keys())[int(cor_jogador_o)])


def start():
    pegar_cores()
    reiniciar_posicoes()
    for i in range(1, 10):
        mostrar_jogo()

        jogador = 'O' if i % 2 == 0 else 'X'

        tentar_jogar = [False, 'Não jogado']

        while not tentar_jogar[0]:
            jogada = input(
                f'\nJogador {jogador}, digite a posição para jogar: ')
            tentar_jogar = jogar(jogador, jogada)

            if tentar_jogar[0] == False:
                mostrar_jogo()
                mensagem(tentar_jogar[1], 'Vermelho')

        if(juiz(jogador)[0]):
            mostrar_jogo(juiz(jogador))
            mensagem(f'\nJogador {jogador} venceu!', cor_jogador(jogador))
            input('Aperte ENTER para continuar')
            return

    mostrar_jogo()
    mensagem('\nJogo finalizado! Deu velha', 'Amarelo')


def computador():
    mensagem('---Em desenvolvimento---')
    input('Aperte ENTER para voltar')

def menu_jogar():
    clear()
    mensagem('Escolha o modo de jogo:', 'Ciano')
    print('''
    [1] - Local
    [2] - VS Computador
    ''')
    modo_jogo = input('-> ')

    if modo_jogo not in ['1', '2']:
        mensagem('Opção inválida!', 'Vermelho')
        pass
    if modo_jogo == '1':
        start()
    elif modo_jogo == '2':
        computador()


while True:
    clear()
    mensagem('Bem vindo ao jogo da velha! Escolha uma das opções abaixo:', 'Ciano')
    print('''
    [1] - Jogar
    [2] - Escolher cor
    [3] - Sair
    ''')
    escolha_menu = input('-> ')

    if escolha_menu not in ['1', '2', '3']:
        mensagem('Opção inválida!', 'Vermelho')
        pass

    if escolha_menu == '1':
        menu_jogar()

    elif escolha_menu == '2':
        escolher_cor()
    
    elif escolha_menu == '3':
        break
