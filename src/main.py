from show import *
from jogo import *


def start():
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
            quit()

    mostrar_jogo()
    mensagem('\nJogo finalizado! Deu velha', 'Amarelo')


start()
