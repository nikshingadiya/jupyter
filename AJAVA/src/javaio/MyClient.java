package javaio;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class MyClient {
    public static void main(String[] args) {
        try{
            Socket s=new Socket("localhost",6666);
            DataOutputStream dout=new DataOutputStream(s.getOutputStream());
            DataInputStream din=new DataInputStream(s.getInputStream());
//            BufferedReader bf= new BufferedReader(new InputStreamReader(System.in));
            Scanner in=new Scanner(System.in);
            String clientmessage="";
            String servermessage="";
            while (!clientmessage.equals("bye"))
            {
                System.out.print("Please enter the message :");
                clientmessage=in.nextLine();
                dout.writeUTF(clientmessage);
                dout.flush();

                servermessage=din.readUTF();
                System.out.println("From server : "+servermessage);



            }
            din.close();
            dout.close();
            s.close();
        }catch(Exception e){System.out.println(e);}
    }
}  