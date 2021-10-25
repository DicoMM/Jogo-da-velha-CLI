import os
import jogo


cores = {
    'Preto': '\033[1;30m',
    'Vermelho': '\033[1;31m',
    'Verde': '\033[1;32m',
    'Amarelo': '\033[1;33m',
    'Azul': '\033[1;34m',
    'Magenta': '\033[1;35m',
    'Ciano': '\033[1;36m',
    'Cinza': '\033[1;90m',
    'Branco': '\033[1;97m'
}

cores_fundo = {
    'Preto': '\033[1;40m',
    'Vermelho': '\033[1;41m',
    'Verde': '\033[1;42m',
    'Amarelo': '\033[1;43m',
    'Azul': '\033[1;44m',
    'Magenta': '\033[1;45m',
    'Cyan': '\033[1;46m',
    'Cinza': '\033[1;47m',
    'Branco': '\033[1;107m'
}

cor_x = 'Vermelho'
cor_o = 'Azul'


def pegar_cores():
    global cor_x, cor_o
    with open('.config', 'r') as arquivo:
        cores = arquivo.readlines()
        for cor in cores:
            cor = cor.split('=')
            if cor[0] == 'cor_x':
                cor_x = cor[1].strip().strip("'")
            elif cor[0] == 'cor_o':
                cor_o = cor[1].strip().strip("'")


def colorir(texto: str, cor: str) -> str:
    '''
    Retorna o texto colorido com a cor escolhida

    Parâmetros:
    cor -> cor escolhida
    texto -> texto a ser colorido

    Exemplo:
    >>> colorir(texto='exemplo', cor='Vermelho')
    # '\033[1;31mexemplo\033[0;0m'
    '''
    return cores[cor] + texto + '\033[0;0m'


def colorir_fundo(texto: str, cor: str) -> str:
    '''
    Retorna o texto com o fundo colorido com a cor escolhida

    Parâmetros:
    cor -> cor escolhida
    texto -> texto a ser colorido

    Exemplo:
    >>> colorir(texto='exemplo', cor='vermelho')
    # '\033[1;41mexemplo\033[0;0m'
    '''
    return cores_fundo[cor] + texto + '\033[0;0m'


def mensagem(texto: str, cor: str):
    '''
    Imprime uma mensagem colorida

    Parâmetros:
    texto -> texto a ser impresso
    cor -> cor escolhida
    '''
    print(colorir(texto, cor))


def mudar_cor_jogador(jogador, cor):
    global cor_x, cor_o
    if jogador == 'X':
        cor_x = cor
    elif jogador == 'O':
        cor_o = cor

    with open('.config', 'w') as arquivo:
        arquivo.write(f"cor_x='{cor_x}'\n")
        arquivo.write(f"cor_o='{cor_o}'")


def cor_jogador(jogador):
    global cor_x, cor_o
    if jogador == 'X':
        return cor_x
    elif jogador == 'O':
        return cor_o
    else:
        return 'Cinza'


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_jogo(vencedor=None):
    posicoes = jogo.posicoes.copy()
    if vencedor is not None:
        for chave, valor in posicoes.items():
            if chave in vencedor[1]:
                posicoes[chave] = colorir_fundo(
                    valor, cor_jogador(vencedor[2]))

    for chave, valor in posicoes.items():
        posicoes[chave] = colorir(valor, cor_jogador(valor))

    clear()
    print(f' {posicoes[1]} | {posicoes[2]} | {posicoes[3]}')
    print('---+---+---')
    print(f' {posicoes[4]} | {posicoes[5]} | {posicoes[6]}')
    print('---+---+---')
    print(f' {posicoes[7]} | {posicoes[8]} | {posicoes[9]}')
