package revisao_final;

public class q2{
    public String area(int arg1, int arg2, String forma){
        if (forma.equals("retangulo")){
            return "O retangulo tem " + arg1 * arg2 + " de area";
        } else if (forma.equals("losango")){ 
            return "O losango tem " + (arg1 * arg2)/2 + " de area";
        } else if (forma.equals("triangulo")){
            return "O triangulo tem " + (arg1 * arg2)/2 + " de area";
        } else {
            return "Invalido";
        }
    }
}