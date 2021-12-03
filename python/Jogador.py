
# Jogador
#
# Created on 19 de Marco de 2001, 08:28

from abc import ABC, abstractmethod
from Jogada import Jogada
from Configuracao import Configuracao
from TabuleiroGoMoku import TabuleiroGoMoku
import traceback
import random
import socket


# Esta Classe implementa o esqueleto de um jogador para jogar um jogo de tabuleiro distribu&iacute;do.
# Trata-se de uma classe abstrata e, portanto, e preciso criar uma subclasse e implementar o metodo
# <b>calculaJogada</b> para que possa ser instanciada.
# Ele se conecta no servidor do jogo  no host passado pela linha de argumentos e
# na porta fornecida pela pelo singleton <b>Configuracao</b>.
# Passa entao a receber as jogadas do oponente e enviar jogadas por meio do servidor
# segundo um protocolo pre-definido. <br><br>
# <b>Execucao</b><br>
# <center><i>java Jogador <nome> <host></i></center> <br><br>
# <b>Exemplo:</b> <br>
# <center><i>java Jogador equipe1 localhost</i></center> <br><br>
# <b>Protocolo</b><br>
# A cada rodada o jogador recebe uma jogada e envia uma jogada. <br>
# A jogada recebida possui o seguinte formato:<br>
# <center><i><jogador>\n<linha>\n<coluna>\n<linhaInicial>\n<colunaInicial>\n</i></center> <br>
# Onde:
# <ul>
# <li><jogador>= indica qual e a cor do jogador (Tabuleiro.AZUL ou Tabuleiro.VERM) ou
# '#' indicando fim do jogo.
# <li> <linha><coluna> = sao as coordenadas da posicao recem ocupada.
# <li> <linhaInicial><colunaInicial> = sao as coordenadas da peca respons&aacute;vel pela jogada .
# </ul> <br><p>
# A jogada enviada possui o seguinte formato:<br>
# <center><i><linha>\n<coluna>\n<linhaInicial>\n<colunaInicial>\n</i></center> <br>
# Se o jogador precisar passar a jogada deve atribuir valor -1 as coordenadas.
# <br>
# Caso o jogador tenha algum problema ou desista deve enviar o caracter #
# <br>
# <br>
#
#
# author Alcione
# version 1.0

class Jogador(ABC):
    # param args - args[0] nome do jogador; args[1] endereco ip ou nome da maquina onde esta o servidor
    def __init__(self, nome):
        self.conf = Configuracao()
        self.host = self.conf.getHost()
        self.nome = nome
        self.tabuleiro = TabuleiroGoMoku()
        self.tempoEspera = 1000
        self.jogador = 0

        self.tabuleiro.iniciaLimpo()

        if nome == "":
            self.nome = "jogador" + random.randint(0, 1000)

    # Metodo que inicia o jogo.

    def joga(self):
        clisoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Iniciando...." + self.nome)
        try:
            clisoc.connect((self.host, self.conf.getPorta()))

            print("enviando...." + self.nome)
            # cinput.readLine()
            clisoc.sendall(bytes(self.nome + "\n", 'ascii'))
            linhaLida = clisoc.recv(1024).decode('utf-8').split('\n')
            print("Linha lida:" + " - ".join(linhaLida))

            jogadorLido = int(linhaLida[0])
            linha = int(linhaLida[1])
            coluna = int(linhaLida[2])

            oponente = self.tabuleiro.VERM if jogadorLido == self.tabuleiro.AZUL else self.tabuleiro.AZUL
            nJogador = self.tabuleiro.cor[jogadorLido]
            nOponente = self.tabuleiro.cor[(jogadorLido + 1) % 2]
            while True:
                if linha != -1:
                    sb = "Oponente: {} jogada({},{})".format(
                        oponente, linha, coluna)
                    print(sb)
                    jtemp = Jogada(-1, -1, linha, coluna)
                    if not self.tabuleiro.move(oponente, jtemp):
                        print("Jogada Invalida!!")

                print("Vou calcular jogada!")
                jog = self.calculaJogada(self.tabuleiro, jogadorLido)
                self.tabuleiro.imprimeTab(self.tabuleiro.getTab())

                if jog == None:
                    print("Jogada Nula!")
                else:
                    print("Jogada Boa!")
                if jog != None:
                    sb = "Eu: {} jogada({},{})".format(
                        nJogador, jog.getLinha(), jog.getColuna())
                    print(sb)
                    self.tabuleiro.move(jogadorLido, jog)
                    self.tabuleiro.imprimeTab(self.tabuleiro.getTab())

                    sb = "{}\n{}\n".format(jog.getLinha(), jog.getColuna())
                    clisoc.sendall(bytes(sb, 'ascii'))
                    print("enviando:" + sb)
                else:
                    clisoc.sendall(bytes("-1\n-1\n", 'ascii'))
                linhaLida = clisoc.recv(1024).decode('utf-8').split('\n')
                if linhaLida[0] == '#':
                    print("recebido #")
                    return
                linha = int(linhaLida[1])
                coluna = int(linhaLida[2])
        except Exception as e:
            print(e)
            traceback.print_exc()

            try:
                clisoc.sendall(b'#\n')
            except:
                print("Ocorreu um erro ")

        finally:
            print("Fim")
            clisoc.close()

    def getTempoEspera(self):
        return self.tempoEspera

    @abstractmethod
    def calculaJogada(tab, jogadorCor):
        pass

    def setTempoEspera(self, tempoEspera):
        self.tempoEspera = tempoEspera

    # Retorna o oponente.
    # retorna o oponente.
    def oponente(self):
        if self.jogador == tabuleiro.AZUL:
            return Tabuleiro.VERM
        return Tabuleiro.AZUL
