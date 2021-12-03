from Jogada import Jogada
from Configuracao import Configuracao
from TabuleiroGoMoku import TabuleiroGoMoku
from JogadorGuloso import JogadorGuloso

j = Jogada(1,1,2,2)
c = Configuracao()
tg= TabuleiroGoMoku()
jogador = JogadorGuloso("Guloso")

t = tg.getTab()

print(t)

tg.copiaTab(t)
print("\n===================\n")
t = tg.getTab()
print(t)


print("",j.getColuna())