package javaio;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class MyServer {
    public static void main(String[] args){
        try{
            ServerSocket ss=new ServerSocket(6666);
            Socket s=ss.accept();//establishes connection
            DataInputStream din=new DataInputStream(s.getInputStream());
            DataOutputStream dout=new DataOutputStream(s.getOutputStream());
//            BufferedReader bf= new BufferedReader(new InputStreamReader(System.in));
            Scanner in = new Scanner(System.in);
            String clientmessage="";
            String servermessage="";
            while(!clientmessage.equals("bye"))
            {

                clientmessage=din.readUTF();
                System.out.println("From client :"+clientmessage);
                System.out.print("Please enter the meassage :");

                servermessage=in.nextLine();
                dout.writeUTF(servermessage);
                dout.flush();


            }
            din.close();
            dout.close();
            ss.close();
        }catch(Exception e){System.out.println(e);}
    }
}  