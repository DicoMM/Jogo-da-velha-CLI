def reiniciar_posicoes():
    global posicoes
    posicoes = {
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9'
    }


def jogar(jogador: str, jogada: int) -> list:
    global posicoes

    try:
        posicao = posicoes[int(jogada)]
    except:
        return [False, 'Jogada inválida']

    if posicao not in ['X', 'O']:
        posicoes[int(jogada)] = jogador
        return [True, 'Sucesso']
    else:
        return [False, 'Posição ja ocupada']


def juiz(jogador: str) -> list:
    global posicoes
    '''Verifica se o X ou o O ganhou e retorna em quais posições'''
    if posicoes[1] == posicoes[2] == posicoes[3] == jogador:
        return [True, (1, 2, 3), jogador]
    elif posicoes[4] == posicoes[5] == posicoes[6] == jogador:
        return [True, (4, 5, 6), jogador]
    elif posicoes[7] == posicoes[8] == posicoes[9] == jogador:
        return [True, (7, 8, 9), jogador]
    elif posicoes[1] == posicoes[4] == posicoes[7] == jogador:
        return [True, (1, 4, 7), jogador]
    elif posicoes[2] == posicoes[5] == posicoes[8] == jogador:
        return [True, (2, 5, 8), jogador]
    elif posicoes[3] == posicoes[6] == posicoes[9] == jogador:
        return [True, (3, 6, 9), jogador]
    elif posicoes[1] == posicoes[5] == posicoes[9] == jogador:
        return [True, (1, 5, 9), jogador]
    elif posicoes[3] == posicoes[5] == posicoes[7] == jogador:
        return [True, (3, 5, 7), jogador]
    else:
        return [False, (None, None, None)]
