#
# Configuracao.java
#
# Criada em 6 de Abril de 2007, 06:45
#
# Esta classe mantem a configura&ccedil;&atilde;o do jogo
#
# @author Alcione de Paiva
# @version 1.0
#/


class Configuracao:
   
    def __init__(self):
       self.DIM = 13
       self.nome = "GoMoKu"
       self.pecas = ["gomoku/blue.png","gomoku/red.png"]
       self.porta = 1962
       self.timeout = 11000
       self.espera = 10
       self.host = "localhost"
   

    def  getNome(self):
        return self.nome

    def getDim(self):
        return self.DIM

    def getPecas(self):
        return self.pecas
 
    def getPorta(self):
        return self.porta
 
    def getTimeout(self):
        return self.timeout
 
    def getHost(self):
        return self.host
 
    def getEspera(self):
        return self.espera

    def  setEspera(self, espera):
        self.espera = espera
 
