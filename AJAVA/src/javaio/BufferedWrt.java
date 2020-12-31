package javaio;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class BufferedWrt {
    public static void main(String[] args) throws IOException {
        BufferedWriter b= new BufferedWriter(new FileWriter("txt_file\\Bufout.txt",true));
        b.write(" pacific rim");
        b.write(" good movie ");
        b.flush();
        b.close();
    }
}
