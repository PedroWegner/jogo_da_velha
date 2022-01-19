from random import randint

class JogoDaVelha:
    def __init__(self):
        self._tabuleiro = []

    def cria_tabuleiro(self):
        for i in range(3):
            self._linha = []
            for j in range(3):
                self._linha.append('-')
            self._tabuleiro.append(self._linha)

    def exibe_tabuleiro(self):
        for linha in self._tabuleiro:
            for espaco in linha:
                print(espaco, end='')
            print()

    def escolhe_jogador(self):
        return randint(0, 1)

    def troca_jogador(self, jogador):
        return 'X' if jogador == 'O' else 'O'

    def escolhe_espaco(self, linha, coluna, jogador):
        self._tabuleiro[linha][coluna] = jogador

    def jogador_ganha(self, jogador):
        ganhou = None

        tab = len(self._tabuleiro)
        print(tab)

        # checa linhas
        for linha in range(tab):
            win = True
            for coluna in range(tab):
                if self._tabuleiro[linha][coluna] != jogador:
                    win = False
                    break
            if win:
                return win

        # checa coluna
        for linha in range(tab):
            win = True
            for coluna in range(tab):
                if self._tabuleiro[coluna][linha] != jogador:
                    win = False
                    break
            if win:
                return win



    def verifica_espaco(self):
        for linha in self._tabuleiro:
            for espaco in linha:
                if espaco == '-':
                    return False  # espaco vazio
        return True  # espaco com marca

    def iniciar_jogo(self):
        self.cria_tabuleiro()  # cria o tabuleiro
        jogador = 'O' if self.escolhe_jogador() == 1 else 'X'
        while True:
            self.exibe_tabuleiro()

            linha, coluna = list(map(int, input('escolha uma linha e uma coluna: ')))
            while linha > 3 or coluna > 3 or linha < 1 or coluna < 1:
                print('numero de linha ou coluna inválido, digite novamente')
                linha, coluna = list(map(int, input('escolha uma linha e uma coluna: ')))

            self.escolhe_espaco(linha - 1, coluna - 1, jogador)

            if self.jogador_ganha(jogador):
                print(f'{jogador} ganhou')
            jogador = self.troca_jogador(jogador)

            self.jogador_ganha(jogador)
