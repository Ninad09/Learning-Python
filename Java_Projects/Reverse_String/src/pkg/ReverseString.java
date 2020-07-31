package pkg;

import java.util.Scanner;

public class ReverseString {
    public static void main(String[] args) {
        System.out.println("Enter String to reverse:: ");
        Scanner scan=new Scanner(System.in);
        String userWord=scan.nextLine();

        System.out.println("\nReversed String:: ");
        System.out.println(reverse(userWord));
    }

    //Reversing Function
    public static String reverse(String st){

        char[] letter=new char[st.length()];
        for(int i=st.length()-1,m=0;i>=0;i--,m++) {
            letter[m]=st.charAt(i);
        }

        String revst="";
        for(char ch: letter){
            revst=revst + ch;
        }
        return revst;
    }
}
