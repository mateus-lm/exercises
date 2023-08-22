package mypackage;

import java.util.List;
import java.util.ArrayList;

public class TestLista {
    public void retornaString(String[] args){
        List <String> myList = new ArrayList<>();
        myList.add("Olá, ");
        myList.add("Meu nome ");
        myList.add("Mateus");
        myList.add("Moreira");
        myList.get(0);

        System.out.println(myList.get(0));
    }
    
}
