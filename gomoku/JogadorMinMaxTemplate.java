/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package gomoku;
/*
 * Jogador.java
 *
 * Created on 25 de maio de 2010
 */
import java.util.Date;
import java.util.logging.Level;
import java.util.logging.Logger;
import jogo.Jogador;
import tabuleiro.Jogada;
import tabuleiro.Tabuleiro;

/**
 * Esta Classe implementa o esqueleto de um jogador que usa o algoritmo MimMax com corte alfa-beta.
 *<br>
 * @author  Alcione
 * @version 1.0
 */
public class JogadorMinMaxTemplate extends Jogador implements JogadorMinMax{

    public final static int MAXTEMPO = 10000;
    public Jogada jogada = null;



    public synchronized void setJogada(Jogada jogada) {
        this.jogada = jogada;
    }
    final static int MAXNIVEL = 6;

    /**
     * @param args host maquina onde esta o servidor
     */
    public JogadorMinMaxTemplate(String args[]) {
        super(args);
    }

    /**
     * Calcula uma nova jogada para o tabuleiro e jogador corrente.
     * @param tab Tabuleiro corrente
     * @param jogador Jogador corrente
     * @return retorna a jogada calculada.
     */
    @Override
    public Jogada calculaJogada(Tabuleiro tab, byte jogador) {
        Date tempo1 = new Date();
        Date tempo2 = null;
        long usado =0;
        for (int prof = 1; prof <= MAXNIVEL; prof++) {
            MinMaxTempl minMax = new MinMaxTempl(tab, jogador,  prof);
            minMax.setPai(this);
            minMax.start();

            try {
                minMax.join(MAXTEMPO-usado);
            } catch (InterruptedException ex) {
                Logger.getLogger(JogadorMinMaxTemplate.class.getName()).log(Level.SEVERE, null, ex);
            }
            tempo2 = new Date();
            usado = tempo2.getTime() - tempo1.getTime();
            if (usado >= MAXTEMPO){
                break;
            }
        }
        return jogada;
        
    }

    /**
     * @param args argumentos da linha de comando: host do servidor othelo
     */
    public static void main(String args[]) {
        if (args.length < 2) {
            String a[] = new String[2];
            a[0] = "MinMax" + new Double((Math.random() * 100)).shortValue();
            a[1] = "localhost";
            (new JogadorMinMaxImp(a)).joga();
            //System.out.println("Usar:java Jogador <nome> <host>!");
        } else {
            (new JogadorMinMaxImp(args)).joga();
        }
    }

    public Jogada getJogada() {
        throw new UnsupportedOperationException("Not supported yet.");
    }
}

class MinMaxTempl extends Thread {

   
    private int profundidade = 1;
    Tabuleiro tabIni;
    byte jogador;
    private JogadorMinMax pai = null;

    public void setPai(JogadorMinMax pai) {
        this.pai = pai;
    }

    public MinMaxTempl(Tabuleiro tab, byte jogador,  int profundidade) {
        tabIni = tab;
        this.jogador = jogador;
        this.profundidade = profundidade;

    }

    public void setProfundidade(int profundidade) {
        this.profundidade = profundidade;
    }

    @Override
    public void run() {
        Jogada j = null;
        // Descobre a jogada por MinMax e alfaBeta
        pai.setJogada(j);
    }

    
}

