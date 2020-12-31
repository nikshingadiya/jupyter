package javaio;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class FileOut {
    public static void main(String[] args) throws IOException {
        File f1=new File("txt_file\\fout.txt");
        f1.createNewFile();
        FileOutputStream fout;
        fout=new FileOutputStream(f1,true);
        String s="hello java nikhil";
        char[] ch =s.toCharArray();
        byte[] b= s.getBytes(StandardCharsets.UTF_8) ;
        fout.write(b);
        System.out.println(b);
//        for (int i=0; i<s.length(); i++)
//        {
//            fout.write(ch[i]);
//            System.out.println(ch[i]);
//        }
        fout.close();
    }
}
