package javaio;

import java.io.File;
import java.io.IOException;

public class FileInfo {
    public static void main(String[] args) throws IOException {
        System.out.println("nikhil");
        File f1=new File("txt_file\\nik.txt");
        f1.createNewFile();
        System.out.println(f1.exists());
        System.out.println(f1.canWrite());
        System.out.println(f1.canExecute());
        System.out.println(f1.getName());
        System.out.println(f1.canRead());
        System.out.println(f1.hashCode());
        System.out.println(f1.setWritable(true));
        System.out.println(f1.getPath());

        System.out.println(f1.getAbsolutePath());
        System.out.println(f1.getCanonicalPath());
        System.out.println(f1.toURI());

//        System.out.println(f1.delete());







    }
}
