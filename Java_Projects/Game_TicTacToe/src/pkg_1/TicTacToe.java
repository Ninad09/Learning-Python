package pkg_1;

import java.util.*;

public class TicTacToe {
    //Player Positions
    static ArrayList<Integer> userPos=new ArrayList<Integer>();
    static ArrayList<Integer> cpuPos=new ArrayList<Integer>();
    static char [][] gameBoard={{' ','|',' ','|',' '},{'-','+','-','+','-'},
            {' ','|',' ','|',' '},{'-','+','-','+','-'},{' ','|',' ','|',' '}};

    //Driver Function
    public static void main(String[] args) {
        printBoard();
        plays();
    }
    //End of Main

    //User CPU Plays
    public static void plays(){
        while(true){
            //User Plays
            System.out.println("Enter Position (1-9):: ");
            Scanner sc=new Scanner(System.in);
            int userpos=sc.nextInt();
            //Check valid
            while(userPos.contains(userpos)||cpuPos.contains(userpos)||userpos>9){
                System.out.println("Invalid Position...Enter Again");
                userpos=sc.nextInt();
            }
            placemark(userpos,"player");
            if(loopbreak()){
                break;
            }

            //CPU Plays
            Random rnd=new Random();
            int cpupos= rnd.nextInt(9)+1;
            //Check valid
            while(userPos.contains(cpupos)||cpuPos.contains(cpupos)){
                cpupos=rnd.nextInt(9)+1;
            }
            placemark(cpupos,"cpu");
            printBoard();
            if(loopbreak()){
                break;
            }
        }
    }

    //Check for Winning Conditions
    public static boolean loopbreak(){
        String res=checkWin();
        if(res!=""){
            printBoard();
            System.out.println(res);
            return true;
        }
        return false;
    }

    //Display Board
    public static void printBoard(){
        for(char[] row:gameBoard){
            for(char ch:row){
                System.out.print(ch);
            }
            System.out.println();
        }
    }

    //Enter X or O in gameBoard
    public static void placemark(int pos,String user){
        char ch=' ';
        if(user.equals("player")) {
            ch = 'X';
            userPos.add(pos);
        }else if(user.equals("cpu")){
            ch='O';
            cpuPos.add(pos);
        }
        switch(pos) {
            case 1:
                gameBoard[0][0] = ch;
                break;
            case 2:
                gameBoard[0][2] = ch;
                break;
            case 3:
                gameBoard[0][4] = ch;
                break;
            case 4:
                gameBoard[2][0] = ch;
                break;
            case 5:
                gameBoard[2][2] = ch;
                break;
            case 6:
                gameBoard[2][4] = ch;
                break;
            case 7:
                gameBoard[4][0] = ch;
                break;
            case 8:
                gameBoard[4][2] = ch;
                break;
            case 9:
                gameBoard[4][4] = ch;
                break;
            default:
                break;
        }
    }

    //Winning Conditions
    public static String checkWin(){
        //Winning Conditions
        List tRow= Arrays.asList(1,2,3);    List mRow= Arrays.asList(4,5,6);
        List bRow= Arrays.asList(7,8,9);    List lCol= Arrays.asList(1,4,7);
        List mCol= Arrays.asList(2,5,8);    List rCol= Arrays.asList(3,6,9);
        List Diag_1= Arrays.asList(1,5,9);  List Diag_2= Arrays.asList(7,5,3);

        List<List> winCondition=new ArrayList<List>();
        winCondition.add(tRow); winCondition.add(mRow);
        winCondition.add(bRow); winCondition.add(lCol);
        winCondition.add(mCol); winCondition.add(rCol);
        winCondition.add(Diag_1); winCondition.add(Diag_2);

        //Check for Winner
        for(List lst:winCondition) {
            if (userPos.containsAll(lst)){
                return "You Win!!";
            }else if (cpuPos.containsAll(lst)){
                return "CPU Wins";
            }else if(userPos.size()+cpuPos.size()==9){
                return "DRAW";
            }
        }
        return "";
    }
}
