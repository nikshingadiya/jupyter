package javaio;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Bufferred {
    public static void main(String[] args) throws IOException {
        BufferedReader bf=new BufferedReader(new FileReader("txt_file\\Bufout.txt"));
//        System.out.println(bf.readLine());
        char[] c=new char[10];

        bf.read(c,2,7);
        System.out.println(c);
    }
}
