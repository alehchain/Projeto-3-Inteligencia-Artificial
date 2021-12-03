# Esta Classe implementa as coordenadas de uma jogada.
# Alcione de Paiva

class Jogada:
     # Cria uma objeto jogada com as coordenadas. Se a origem for negativa entao
     # a jogada é considerada como a colocação de uma peça nova.
     # linhaInicial linha original da peça
     # colunaInicial coluna original da peça 
     # linha linha da jogada
     # coluna coluna da jogada

    def __init__(self, linhaInicial, colunaInicial, l, c):
        self.linhaInicial = linhaInicial
        self.linha = l
        self.colunaInicial = colunaInicial
        self.coluna = c

     # Cria uma objeto jogada com as coordenadas.
     # linha linha da jogada
     # coluna coluna da jogada
     
    def JogadaNova(self, linha,  coluna):
        self.linha = linha
        self.coluna = coluna
        self.linhaInicial = -1
        self.colunaInicial = -1

     # Define as coordenadas do objeto.
     # linhaInicial linha original da peça
     # colunaInicial coluna original da peça
     # linha linha da jogada
     # coluna coluna da jogada
     
    def setJogada(self, linhaInicial,  colunaInicial,  linha,  coluna):
        self.linhaInicial = linhaInicial
        self.linha = linha
        self.colunaInicial = colunaInicial
        self.coluna = coluna
    
    #Retorna a coordenada X de destino.
    def  getLinha(self):
        return self.linha
 
    #Retorna a coordenada Y de destino.
    def  getColuna(self) :
        return self.coluna

    #Retorna a coordenada X de origem.
    def  getLinhaInicial(self) :
        return self.linhaInicial

     #Retorna a coordenada Y de origem.
    def  getColunaInicial(self) :
        return self.colunaInicial
 
