package pkg;

import java.util.Scanner;

public class JavaPattern {
    //Driver Code
    public static void main(String[] args) {
        //User Prompt
        System.out.println("Enter pattern length:: ");
        Scanner scn=new Scanner(System.in);
        int num=scn.nextInt();

        basic_pattern(num);
        centre_pattern(num);
        reverse_pattern(num);
    }
    //Left-Align Pattern draw method
    public static void basic_pattern(int len){
        for(int i=1;i<=len;i++){
            for(int cnt=1;cnt<=i;cnt++){
                System.out.print('*');
            }
            System.out.println();
        }
        for(int i=len-1;i>0;i--){
            for(int cnt=1;cnt<=i;cnt++){
                System.out.print('*');
            }
            System.out.println();
        }
    }
    //Centre-Align Pattern draw method
    public static void centre_pattern(int len){
        for(int i=1;i<=len;i++){
            for(int j=0;j<(len-i);j++){
                System.out.print(' ');
            }
            for(int cnt=1;cnt<=2*i;cnt++){
                System.out.print('*');
            }
            System.out.println();
        }
        for(int i=len-1;i>=1;i--){
            for(int j=0;j<(len-i);j++){
                System.out.print(' ');
            }
            for(int cnt=1;cnt<=2*i;cnt++){
                System.out.print('*');
            }
            System.out.println();
        }
    }
    //Reverse Centre-Align Pattern draw method
    public static void reverse_pattern(int len){
        for(int i=1;i<=len;i++){
            for(int cnt=1;cnt<=i;cnt++){
                System.out.print('*');
            }
            for(int j=0;j<2*(len-i);j++){
                System.out.print(' ');
            }
            for(int cnt=1;cnt<=i;cnt++){
                System.out.print('*');
            }
            System.out.println();
        }
        for(int i=len-1;i>=1;i--){
            for(int cnt=1;cnt<=i;cnt++){
                System.out.print('*');
            }
            for(int j=0;j<2*(len-i);j++){
                System.out.print(' ');
            }
            for(int cnt=1;cnt<=i;cnt++){
                System.out.print('*');
            }
            System.out.println();
        }
    }
}
