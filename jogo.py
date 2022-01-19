class JogoDaVelha:
    def __init__(self):
        self._tabuleiro = []

    def cria_tabuleiro(self):
        for i in range(3):
            self._linha = []
            for j in range(3):
                self._linha.append('-')
            self._tabuleiro.append(self._linha)

    def print_tab(self):
        for linha in self._tabuleiro:
            for espaco in linha:
                print(espaco, end='')
            print()

    def escolhe_jogador(self):
        return 0

    def escolhe_espaco(self, linha, coluna, jogador):
        self._tabuleiro[linha][coluna] = jogador

    # def jogador_ganha(self, jogador):
    #     win = None
    #
    #     tab = len(self._tabuleiro)
    #
    #     for i in range(tab):
    #         for j in range(tab):
    #             if self._tabuleiro[i][j] != jogador:
    #                 win = False
    #                 break

    def verifica_espaco(self):
        for linha in self._tabuleiro:
            for espaco in linha:
                if espaco == '-':
                    return False  # espaco vazio
        return True  # espaco com marca

    def iniciar_jogo(self):
        self.cria_tabuleiro()  # cria o tabuleiro