import random

desenho_forca = ['''

>>>>>>>>>>FORCA<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


class Forca:

    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_corretas = []

    # Método para adivinhar a letra
    def guess(self, letra):
        if letra in self.palavra and letra not in self.letras_corretas:
            self.letras_corretas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def fim_de_jogo(self):
        return self.vencedor() or (len(self.letras_erradas) == 6)

    # Método para verificar se o jogador venceu
    def vencedor(self):
        if '_ ' not in self.esconde_palavra():
            return True
        return False

    # Método para não mostrar a letra no board
    def esconde_palavra(self):
        rtn = ''
        for letra in self.palavra:
            if letra not in self.letras_corretas:
                rtn += '_ '
            else:
                rtn += letra
        return rtn

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(desenho_forca[len(self.letras_erradas)])
        print('\nPalavra: ' + self.esconde_palavra())
        print('\nLetras erradas: ', )
        for letra in self.letras_erradas:
            print(letra, )
        print()
        print('Letras corretas: ', )
        for letra in self.letras_corretas:
            print(letra, )
        print()


# Método para ler uma palavra de forma aleatória do banco de palavras
def palavra_aleatoria():
    with open('palavras.txt', 'r', encoding='utf-8') as f:
        banco = f.readlines()
    return banco[random.randint(0, len(banco))].strip()

# Método Main - Execução do Programa


def main():
    # Objeto
    game = Forca(palavra_aleatoria().lower())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.fim_de_jogo():
        game.print_game_status()
        user_input = input('\nDigite uma letra: ')
        game.guess(user_input)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.vencedor():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.palavra)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
