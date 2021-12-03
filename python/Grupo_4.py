
# Jogador
# Created on 11 de Junho de 2021

from TabuleiroGoMoku import TabuleiroGoMoku
from Jogador import Jogador
from Jogada import Jogada
from Tabuleiro import Tabuleiro
import time
import threading
import numpy as np

# Esta Classe implementa o esqueleto de um jogador guloso.
#
# Ele se conecta no servidor do jogo  no host passado pela linha de argumentos e
# na porta fornecida pela classe Servidor.
# Passa ent&atilde;o a receber as jogadas do oponente e enviar jogadas por meio do servidor
# segundo um protocolo pr&eacute;-definido.
#
# Execucao
# java Jogador <nome> <host>
# Exemplo:
# java Jogador equipe1 localhost
# <b>Protocolo</b>
# A cada rodada o jogador recebe uma jogada e envia uma jogada.
# A jogada recebida possui o seguinte formato:
# <jogador>\n<x>\n<y>\n<xp>\n<yp>\n
# Onde:
#
# <jogador>= indica qual &eacute; a cor do jogador (Tabuleiro.AZUL ou Tabuleiro.VERM) ou
# '#' indicando fim do jogo.
# <x><y> = sao as coordenadas da posicao recem ocupada (0 a 7).
# <xp><yp> = sao as coordenadas da pe&ccedil;a responsavel pela jogada (0 a 7).
#
# A jogada enviada possui o seguinte formato:
# <x>\n<y>\n<xp>\n<yp>\n
# Se o jogador precisar passar a jogada deve atribuir valor -1 as coordenadas.
#
# Caso o jogador tenha algum problema ou desista deve enviar o caracter #
#
# @author Alcione
# @version 1.0


class Grupo_4(Jogador):

    def __init__(self, nome):
        Jogador.__init__(self, nome)
        self.MAXNIVEL = 10
        self.TEMPOMAXIMO = 1.0
        self.jogada = Jogada(-1, -1, -1, -1)

     # Calcula uma nova jogada para o tabuleiro e jogador corrente.
     # Aqui deve ser colocado o algoritmo com as t&eacute;cnicas de inteligencia
     # artificial. No momento as jogadas s&atilde;o calculadas apenas por crit&eacute;rio de
     # validade. Coloque aqui seu algoritmo minmax.
     # @param tab Tabuleiro corrente
     # @param jogadorCor Jogador corrente
     # @return retorna a jogada calculada.

    def calculaJogada(self, tab, jogadorCor):
        tempo1 = time.time()
        usado = 0.0
        op = 1 if jogadorCor == 0 else 0

        j = np.random.randint(0,14, (2))
        # se for jogador 1 e o tabuleiro está vazio
        if tab.numPecas(jogadorCor) + tab.numPecas(op) == 0:
            jogada = Jogada(-1,-1,j[0],j[1])
            return jogada

        aux_tab = TabuleiroGoMoku()
        aux_tab.inicia(tab.getTab())

        possiveis = self.possiveisJogadas(tab, jogadorCor)
        # jogada = self.checarVencedor(possiveis, tab, jogadorCor)

        # if jogada != None:
        #     return jogada

        for prof in range(1, self.MAXNIVEL):
            tempo2 = time.time()
            
            t1 = threading.Thread(target=self.melhorJogada, args=(tab, prof, possiveis, jogadorCor))
            t1.start()
            t1.join(self.TEMPOMAXIMO - usado)
            usado = tempo2 - tempo1
            if usado >= self.TEMPOMAXIMO:
                break

        return self.jogada
    
    def checarVencedor(self, possiveis, tab, jogador):
        for j in possiveis:
            aux = TabuleiroGoMoku()
            aux.inicia(tab.getTab())
            aux.move(jogador, Jogada(-1, -1, j[0], j[1]))
            if aux.temosVencedor(j[0], j[1]):
                return Jogada(-1, -1, j[0], j[1])

        op = 1 if jogador == 0 else 0
        for j in possiveis:
            aux = TabuleiroGoMoku()
            aux.inicia(tab.getTab())
            aux.move(op, Jogada(-1, -1, j[0], j[1]))
            if aux.temosVencedor(j[0], j[1]):
                return Jogada(-1, -1, j[0], j[1])

        return None

    def naLista(self, lista, a, b):
        for i in lista:
            if i[0] == a and i[1] == b:
                return True

        return False

    
    def possiveisJogadas(self, tab, jogador):
        a_tab = tab.getTab()

        possiveis = list()

        for i in range(13):
            for j in range(13):
                if a_tab[i][j] != -1:
                    vizinhos = [(i-1,j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
                    for p in vizinhos:
                        if p[0] >= 0 and p[0] < 13 and p[1] >= 0 and p[1] < 13:
                            if a_tab[p[0]][p[1]] == -1:
                                if not self.naLista(possiveis, p[0], p[1]):
                                    possiveis.append((p[0], p[1]))

        return possiveis

    
    def melhorJogada(self, tab, prof, acoes, jogador):
        maxj = [-1,-1,-99999]

        for p in acoes:

            a_tab = TabuleiroGoMoku()
            a_tab.inicia(tab.getTab())
            joga = Jogada(-1,-1, p[0], p[1])
            a_tab.move(jogador, joga)
            val = self.mim(a_tab, jogador, prof-1, acoes)

            if val > maxj[2]:
                maxj[0] = p[0]
                maxj[1] = p[1]
                maxj[2] = val
        
        self.jogada = Jogada(-1,-1, maxj[0], maxj[1])


    def max(self, tab, jogador, prof, acoes, alpha=-99999, beta=99999, jogada=None):
        if prof == 0 or (jogada != None and tab.temosVencedor(jogada.getLinha(), jogada.getColuna())):
            val = tab.heuristicaBasica(jogador, tab.getTab())
            return val

        a_tab = TabuleiroGoMoku()
        a_tab.inicia(tab.getTab())

        maxVal = -99999

        for p in acoes:
            joga = Jogada(-1,-1, p[0], p[1])
            if a_tab.verifica(jogador, joga) == 1:
                if jogada != None:
                    a_tab.move(jogador, joga)

                val = self.mim(a_tab, jogador, prof-1, acoes, alpha, beta, joga)
                    
                if maxVal < val:
                    maxVal = val
                
                if alpha < val:
                    alpha = val
                
                if beta <= alpha:
                    break

        return maxVal

    
    def mim(self, tab, jogador, prof, acoes, alpha=-99999, beta=99999, jogada=None):
        if prof == 0 or (jogada != None and tab.temosVencedor(jogada.getLinha(), jogada.getColuna())):
            val = tab.heuristicaBasica(jogador, tab.getTab())

            return val

        a_tab = TabuleiroGoMoku()
        a_tab.inicia(tab.getTab())

        mimVal = 99999
        for p in acoes:
            joga = Jogada(-1,-1, p[0], p[1])
            if a_tab.verifica(jogador, joga) == 1:
                
                if jogada != None:
                    a_tab.move(jogador, joga)

                val = self.max(a_tab, jogador, prof-1, acoes, alpha, beta, joga)
                
                if mimVal > val:
                    mimVal = val
                
                if beta > val:
                    beta = val
                
                if beta <= alpha:
                    break

        return mimVal

if __name__ == "__main__":
    import sys
    Grupo_4(sys.argv[1]).joga()
    print("Fim")
