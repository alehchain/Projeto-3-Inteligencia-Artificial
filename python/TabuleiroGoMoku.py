from Configuracao import Configuracao
from Jogada import Jogada
from Tabuleiro import Tabuleiro
import sys
import numpy as np

# Gomoku &eacute um jogo japon&ecircs antigo, conhecido tamb&eacutem como
# RanJu . O objetivo do jogo &eacute conseguir colocar 5 bolinhas na diagonal,
# na horizontal ou&nbsp na vertical. Vence quem atingir este objetivo
# primeiro. <p><img SRC="file:gomoku.gif" height=179 width=178> <br>&nbsp
# <br>&nbsp Esta Classe implementa o servidor GoMokuServer. <br> Nao
# ALTERE ESSA CLASSE.<br> Ela se registra na porta porta 1962. Passa
# entao a receber as jogadas dos jogadores e envi&aacute-las para o
# oponente segundo um protocolo pr&eacute-definido. <br><br>
# <b>Execucao</b><br> <center><i>java GoMokuServer</i></center>
# <br><br> <b>Protocolo</b><br> A cada rodada o servidor recebe uma jogada e
# envia para o oponente. <br> A jogada recebida possui o seguinte formato:<br>
# <center><i>&ltx>\n&lty>\n</i></center> <br> <br> Caso o servidor receba o
# caracter# de um jogador significa que ocorreu algum problema e o jogador
# estï¿½ desistindo <br> A jogada enviada possui o seguinte format:<br>
# <center><i>&ltjogador>\n&ltx>\n&lty>\n</i></center> <br> Onde: <ul>
# <li>&ltjogador>= indica qual &eacute a cor do jogador (Tabuleiro.self.AZUL ou
# Tabuleiro.self.VERM) ou '#' indicando fim do jogo. <li> &ltx>&lty> = sao
# as coordenadas da jogada (0 a 7). </ul> <br><p> <br>
# author Alcione
# version 2.0


class TabuleiroGoMoku(Tabuleiro):

    def __init__(self):
        self.DIM = Configuracao().getDim()
        self.tab = np.ones((self.DIM, self.DIM), dtype='i2') * self.LIVRE
        self.win_r1 = self.win_c1 = self.win_r2 = self.win_c2 = 0

    # Inicia o tabuleiro com a configuracao padrao

    def iniciaLimpo(self):
        self.tab = np.ones((self.DIM, self.DIM), dtype='i2') * self.LIVRE

    # Inicia o tabuleiro com a configuracao passada na forma de array
    # param aTab tabela com a configuracao

    def inicia(self, aTab):
        self.tab = np.zeros((self.DIM, self.DIM), dtype='i2')
        np.copyto(self.tab, aTab)

    # Copia as posicoes de um array
    # param aTab Array contendo os valores para a copia.

    def copiaTab(self, aTab):
        np.copyto(self.tab, aTab)

    # Copia as posicoes para um array
    # param aTab Array contendo os valores para a copia.

    def copiaToTab(self, aTab):
        np.copyto(aTab, self.tab)
        return atab

    # Retorna uma copia do tabuleiro na forma de array.
    # retorna array com os valores

    def getTab(self):
        labTab = np.zeros((self.DIM, self.DIM), dtype='i2')
        np.copyto(labTab, self.tab)
        return labTab

    # Retorna o n&uacutemero de pecas de um jogador.
    # param jogador byte numero do jogador
    # retorna n&uacutemero de pecas
    def numPecas(self, jogador):
        liTot = 0
        for i in range(0, self.DIM):
            for j in range(0, self.DIM):
                if self.tab[i][j] == jogador:
                    liTot = liTot+1
        return liTot

    # Executa um movimento. Retonar True se o movimento foi bem sucedido
    # param aiJogador jogador
    # param jog jogada
    # retorna True se o movimento eh valido.
    def move(self, aiJogador, jog):
        lbTot = self.verifica(aiJogador, jog)
        if lbTot > 0:
            self.tab[jog.getLinha()][jog.getColuna()] = aiJogador
            return True
        return False

    # Verifica se o jogo terminou
    # retorna False = nao terminou True = terminou

    def fimJogo(self):
        for linha in range(0, self.DIM):
            for coluna in range(0, self.DIM):
                if self.tab[linha][coluna] != self.LIVRE:
                    if temosVencedor(linha, coluna):
                        return True
        if self.obtemJogadasPossiveis(self.AZUL) != null or self.obtemJogadasPossiveis(self.VERM) != null:
            return False
        return True

    def vencedorCor(self):
        return self.cor[self.vencedorNum()]

    # Verifica quem e o vencedor
    # retorna 0 = nao terminou AZUL = venceu o jogador self.AZUL self.VERM = venceu o
    # jogador self.VERMelho -1 empate

    def vencedorNum(self):
        return self.tab[self.win_r1][self.win_c1]

    # Verifica se um movimento eh valido.
    # param jogador jogador
    # param j Jogada
    # retorna 0 se o movimento é inválido e >0 movimento eh valido.

    def verifica(self, jogador,  j):

        if j.getLinha() < 0 or j.getColuna() < 0 or j.getLinha() > self.DIM - 1 or j.getColuna() > self.DIM - 1:
            return 0
        if (self.tab[j.getLinha()][j.getColuna()] != self.LIVRE):
            return 0
        return 1

    # Verifica se uma posicao esta fora do tabuleiro.
    # param linha linha
    # param coluna coluna
    # retorna True se saiu.
    def saiuTabuleiro(self, linha, coluna):
        if linha < 0 or coluna < 0 or linha > self.DIM - 1 or coluna > self.DIM - 1:
            return True
        return False

    # Conta o numero de pecas de um jogador a partir da posicao passada e na
    # direcao especificada. O s valores da direcao definida por dirX e dirY
    # devem ser 0, 1, or -1, sendo que um deles deve ser diferente de zero.
    def count(self, jogador,  linha,  coluna,  dirX,  dirY):
        ct = 0  # Numero de pecas em linha de um jogador.

        lin = linha + dirX  # define a direcao .
        col = coluna + dirY
        while (not self.saiuTabuleiro(lin, col) and self.tab[lin][col] == jogador):
            # Quadrado esta no tabuleiro e contem uma peca do jogador.
            lin += dirX  # Va para o proximo.
            col += dirY

        # Quadrado anterior.
        # Quadrado nao esta no tabuleiro ou contem uma peca do jogador.
        self.win_r1 = lin - dirX
        self.win_c1 = col - dirY

        lin = self.win_r1  # Olhe na direcao oposta.
        col = self.win_c1
        while (not self.saiuTabuleiro(lin, col) and self.tab[lin][col] == jogador):
            # Quadrado esta no tabuleiro e contem uma peca do jogador.
            ct += 1
            lin -= dirX   # Va para o proximo.
            col -= dirY

        self.win_r2 = lin + dirX
        self.win_c2 = col + dirY

        # Neste ponto, (win_r1,win_c1) e (win_r2,win_c2) marcam as extremidades
        # da linha que pertence ao jogador.

        return ct

    # Retorna um vetor contendo as jogadas possiveis de um jogador
    # param jogador jogador
    # retorna jogadas possiveis
    def obtemJogadasPossiveis(self, jogador):
        lista = []

        for linha in range(0, self.DIM):
            for coluna in range(0, self.DIM):
                aux = Jogada(-1, -1, linha, coluna)
                if self.verifica(jogador, aux) > 0:
                    lista.append(aux)
        return lista

    # Retorna a melhor jogada
    # param jogador numero do jogador
    # retorna melhor jogada
    def obtemJogadaBoa(self, jogador):
        maxj = Jogada(-1, -1, -1, -1)
        for k in range(5, -1, -1):
            for linha in range(0, self.DIM):
                for coluna in range(0, self.DIM):
                    maxj = Jogada(-1, -1, linha, coluna)
                    if verifica(jogador, maxj) > 0:
                        if self.count(jogador, linha, coluna, 1, 0) >= k:
                            return maxj
                        if self.count(jogador, linha, coluna, 0, 1) >= k:
                            return maxj
                        if self.count(jogador, linha, coluna, 1, -1) >= k:
                            return maxj
                        if self.count(jogador, linha, coluna, 1, 1) >= k:
                            return maxj
        pass

    # Retorna a melhor jogada
    # param jogador numero do jogador
    # retorna melhor jogada
    def obtemJogadaHeuristica(self, jogador):
        maxj = Jogada(-1, -1, -1, -1)
        auxj = Jogada(-1, -1, -1, -1)
        valorMax = -10000
        tabAux = np.zeros((self.DIM, self.DIM), dtype='i2')
        for linha in range(0, self.DIM):
            for coluna in range(0, self.DIM):
                auxj.setJogada(-1, -1, linha, coluna)
                if self.verifica(jogador, auxj) > 0:
                    np.copyto(tabAux, self.tab)
                    tabAux[linha][coluna] = jogador
                    valor = self.heuristicaBasica(jogador, tabAux)
                    if valor > valorMax:
                        valorMax = valor
                        maxj.setJogada(-1, -1, linha, coluna)
                        if valor == 10000:
                            return maxj
        return maxj

    # Retorna um valor heuristico para o tabuleiro dado um jogador
    # param jogador numero do jogador
    # param tab tabuleiro
    # retorna valor do tabuleiro
    def heuristicaBasica(self, jogador, tab):
        valor = 0
        for linha in range(0, self.DIM):
            for coluna in range(0, self.DIM):
                if tab[linha][coluna] == jogador:
                    temp = self.contaHeuristica(
                        jogador, linha, coluna, 1, 0, tab)
                    if temp == 100:
                        return 10000
                    valor += temp
                    temp = self.contaHeuristica(
                        jogador, linha, coluna, 0, 1, tab)
                    if temp == 100:
                        return 10000
                    valor += temp
                    temp = self.contaHeuristica(
                        jogador, linha, coluna, 1, -1, tab)
                    if temp == 100:
                        return 10000
                    valor += temp
                    temp = self.contaHeuristica(
                        jogador, linha, coluna, 1, 1, tab)
                    if temp == 100:
                        return 10000
                    valor += temp
                elif tab[linha][coluna] != self.LIVRE:
                    valor -= 2 * self.contaHeuristica(self.oponente(
                        jogador), linha, coluna, 1, 0, tab)
                    valor -= 2 * self.contaHeuristica(self.oponente(
                        jogador), linha, coluna, 0, 1, tab)
                    valor -= 2 * self.contaHeuristica(self.oponente(
                        jogador), linha, coluna, 1, -1, tab)
                    valor -= 2 * self.contaHeuristica(self.oponente(
                        jogador), linha, coluna, 1, 1, tab)
      #  imprimeTab(tab)
        #print("valor do tabuleiro: {} -- para jogador:{}".format(valor, jogador))
        return valor

    # Conta o numero de pecas de um jogador a partir da posicao passada e na
    # direcao especificada levando em consideracao a vantagem. Os valores da
    # direcao definida por dirX e dirY devem ser 0, 1, or -1, sendo que um
    # deles deve ser diferente de zero.
    def contaHeuristica(self, jogador, linha, coluna, dirX, dirY, tab):
        boqueadoPonta1 = boqueadoPonta2 = False
        lin = linha + dirX  # define a direcao .
        col = coluna + dirY
        while (not self.saiuTabuleiro(lin, col) and tab[lin][col] == jogador):
            # Quadrado esta no tabuleiro e contem uma peca do jogador.
            lin += dirX  # Va para o proximo.
            col += dirY

        # verifica se fechou a ponta
        if (self.saiuTabuleiro(lin, col) or tab[lin][col] != self.LIVRE):
            boqueadoPonta1 = True

        self.win_r1 = lin - dirX  # Quadrado anterior.
        # Quadrado nao esta no tabuleiro ou contem uma peca do jogador.
        self.win_c1 = col - dirY

        lin = lin - dirX  # Olhe na direcao oposta.
        col = col - dirY

        ct = 0  # Numero de pecas em linha de um jogador.
        while (not self.saiuTabuleiro(lin, col) and tab[lin][col] == jogador):
            # Quadrado esta no tabuleiro e contem uma peca do jogador.
            ct += 1
            lin -= dirX   # Va para o proximo.
            col -= dirY

         # verifica se fechou a ponta
        if (self.saiuTabuleiro(lin, col) or tab[lin][col] != self.LIVRE):
            boqueadoPonta2 = True

        self.win_r2 = lin + dirX
        self.win_c2 = col + dirY

        # Neste ponto, (win_r1,win_c1) e (win_r2,win_c2) marcam as extremidades
        # da linha que pertence ao jogador.

        # Verifica se esta bloqueado e nao pode fechar essa linha
        if (ct < 5 and boqueadoPonta1 and boqueadoPonta2):
            ct = 0
        elif ct == 5:
            ct = 100
        elif ct == 4:
            ct = 50
        return ct

    # Chamado apos uma jogada para verificar se resultou em um ganhador
    # param linha linha da jogada
    # param coluna coluna da jogada
    # retorna True se existe um vencedor.

    def temosVencedor(self,  linha,  coluna):
        if self.count(self.tab[linha][coluna], linha, coluna, 1, 0) >= 5:
            return True
        if self.count(self.tab[linha][coluna], linha, coluna, 0, 1) >= 5:
            return True
        if self.count(self.tab[linha][coluna], linha, coluna, 1, -1) >= 5:
            return True
        if self.count(self.tab[linha][coluna], linha, coluna, 1, 1) >= 5:
            return True

        # ainda nao existe vencedor
        self.win_r1 = -1
        return False

    # Retorna o tabuleiro na forma de String
    def toString(self):

        loBuff = "   "
        for i in range(0, self.DIM):
            loBuff += string(i)+' '

        loBuff += "\n"
        for linha in range(0, self.DIM):
            loBuff += " "+linha
            for coluna in range(0, self.DIM):
                if self.tab[linha][coluna] == self.VERM:
                    loBuff += " V"
                elif self.tab[linha][coluna] == self.self.AZUL:
                    loBuff += " A"
                else:
                    loBuff += " -"
            loBuff += '\n'
        return loBuff

    def imprimeTab(self, tab):
        for linha in range(0, self.DIM):
            for coluna in range(0, self.DIM):
                if tab[linha][coluna] == self.VERM:
                    print(" V", end='')
                elif tab[linha][coluna] == self.AZUL:
                    print(" A", end='')
                elif tab[linha][coluna] == self.LIVRE:
                    print(" L", end='')
                else:
                    print(" -", end='')
            print(" ")

    def oponente(self, jogador):
        if jogador == self.AZUL:
            return self.VERM
        else:
            return self.AZUL
