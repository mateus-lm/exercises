package revisao_final;

public class Banner{
    public String banner(int n){
        if (is_Par(n) && n >= 0){
            return "| | | | | | | | |";
        }
        else if (!is_Par(n) && n >= 0){
            return "- - - - - - - -";
        }
        else if (is_Par(n) && n < 0){
            return ". . . . . . . .";
        }
        else if (!is_Par(n) && n < 0){
            return "= = = = = = = = =";
        }
        else return "Invalido";
    }
    public Boolean is_Par(int n){
        return (n % 2 == 0);
    }
}