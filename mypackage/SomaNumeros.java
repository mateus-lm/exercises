package mypackage;
import java.util.Scanner;

public class SomaNumeros {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        System.out.println("Oi, Esse programa lê 2 números e retorna a soma deles");
        int valorA = entrada.nextInt();
        int valorB = entrada.nextInt();

        int soma = valorA + valorB;

        System.out.println("A soma é : " + soma);

        entrada.close();
    }
}