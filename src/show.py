import os
import jogo


cores = {
    'Preto': '\033[1;30m',
    'Vermelho': '\033[1;31m',
    'Verde': '\033[1;32m',
    'Amarelo': '\033[1;33m',
    'Azul': '\033[1;34m',
    'Magenta': '\033[1;35m',
    'Cyan': '\033[1;36m',
    'Cinza': '\033[1;90m',
    'Vermelho Claro': '\033[1;91m',
    'Verde Claro': '\033[1;92m',
    'Amarelo Claro': '\033[1;93m',
    'Azul Claro': '\033[1;94m',
    'Magenta Claro': '\033[1;95m',
    'Cyan Claro': '\033[1;96m',
    'Branco': '\033[1;97m',
    'Negrito': '\033[; 1m',
    'Inverte':	'\033[;7m'
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
    'Vermelho Claro': '\033[1;101m',
    'Verde Claro': '\033[1;102m',
    'Amarelo Claro': '\033[1;103m',
    'Azul Claro': '\033[1;104m',
    'Magenta Claro': '\033[1;105m',
    'Cyan Claro': '\033[1;106m',
    'Branco': '\033[1;107m'
}


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


def cor_jogador(jogador):
    if jogador == 'X':
        return 'Vermelho'
    elif jogador == 'O':
        return 'Azul'
    else:
        return 'Cinza'


def mostrar_jogo(vencedor=None):
    posicoes = jogo.posicoes.copy()
    if vencedor is not None:
        for chave, valor in posicoes.items():
            if chave in vencedor[1]:
                posicoes[chave] = colorir_fundo(
                    valor, cor_jogador(vencedor[2]))

    for chave, valor in posicoes.items():
        posicoes[chave] = colorir(valor, cor_jogador(valor))

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f' {posicoes[1]} | {posicoes[2]} | {posicoes[3]}')
    print('---+---+---')
    print(f' {posicoes[4]} | {posicoes[5]} | {posicoes[6]}')
    print('---+---+---')
    print(f' {posicoes[7]} | {posicoes[8]} | {posicoes[9]}')
