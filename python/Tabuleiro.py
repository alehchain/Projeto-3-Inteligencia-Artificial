import abc


  # Tabuleiro.java
  # Esta &eacute; a interface do tabuleiro
  # N&Atilde;O ALTERE ESSA CLASSE.
  # <p>Se precisar alter&aacute;-la fa&ccedil;a outra classe.
  # Criado em  23 de maio de 2021
  # author  Alcione
  # version 1.0

class Tabuleiro(metaclass=abc.ABCMeta):

    AZUL = 0
    LIVRE = -1
    VERM = 1
    EMPATE = -2
    cor=["Azul","Vermelho"]

    # Copia as posicoes de um array
    #  param aTab Array contendo os valores para a c&oacute;pia.
    @abc.abstractmethod
    def copiaTab(self,aTab):
       return

    
    # Verifica se o jogo terminou
    # returna false = nao terminou; true = terminou
    @abc.abstractmethod
    def fimJogo(self):
       return
    
      # Verifica quem  &eacute; o vencedor
      # returna 0 = nao terminou; AZUL = venceu o jogador 1; VERM = venceu o jogador 2
    @abc.abstractmethod
    def vencedorCor(self):
       return
    
      # Verifica quem &eacute; o vencedor
      #   returna 0 = nao terminou; 1 = venceu o jogador 1; 2 = venceu o jogador 2
    @abc.abstractmethod
    def vencedorNum(self):
       return
    
      # Executa um movimento. Retonar true se o movimento foi bem sucedido
      # 
      #  param jogador jogador que irá jogar
      #  param j jogada que será realizada
      #  returna true se o movimento &ecute; v&acute;lido.
    @abc.abstractmethod
    def move(self, jogador,  j):
       return
       
      # Retorna o n&uacute;mero de pe&ccedil;as de um jogador.
      #  param aiJogador jogador
      #   returna n&uacute;mero de pe&ccedil;as
    @abc.abstractmethod
    def numPecas(self, aiJogador):
       return
       
      # Retorna a melhor jogada
      #  param aiJogador jogador
      #   returna melhor jogada
    @abc.abstractmethod
    def obtemJogadaBoa(self, aiJogador):
       return
       
      # Retorna a melhor jogada
      #  param jogador numero do jogador
      #   returna melhor jogada
    @abc.abstractmethod
    def obtemJogadaHeuristica(self, jogador):
       return
       
      # Retorna um vetor contendo as jogadas poss&icute;veis de um jogador
      #  param aiJogador jogador
      #   returna jogadas poss&icute;veis
    @abc.abstractmethod
    def obtemJogadasPossiveis(self, aiJogador):
       return
           
      # Retorna uma c&oacute;pia do tabuleiro na forma de array.
      # returna array com os valores
    @abc.abstractmethod
    def getTab(self):
       return
           
      # Retorna o tabuleiro na forma de String
    @abc.abstractmethod
    def toString(self):
       return
           
      #   Verifica se um movimento &ecute; v&acute;lido.
      #  param aiJogador jogador
      #  param j Jogada
      #   returna 0 se o movimento é inválido e >0 movimento &ecute; v&acute;lido.
    @abc.abstractmethod
    def verifica(self, aiJogador, j):
       return
           
      # Inicia o tabuleiro com a configura&ccedil;&atilde;o padr;&atilde;o
    @abc.abstractmethod
    def inicia(self):
       return
    
      # Inicia o tabuleiro com a configura&ccedil;&atilde;o passada na forma de array
      #  param tab tabela com a configura&ccedil;&atilde;o
    @abc.abstractmethod
    def inicia(self, tab):
       return
       
      #  param jogador
      #   returna oponente 
    @abc.abstractmethod
    def oponente(self, jogador):
       return
       
