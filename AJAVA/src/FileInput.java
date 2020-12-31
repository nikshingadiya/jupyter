import java.io.FileInputStream;
import java.io.IOException;

public class FileInput {
    public static void main(String[] args) throws IOException {
        FileInputStream fin;
        fin=new FileInputStream("txt_file\\fout.txt");
        int i;
        byte [] b=fin.readAllBytes();
        String s = new String(b);
        System.out.println(s);
        fin.close();
//        do
//        {
//            i=fin.read();
//            if(i!=-1)
//             System.out.print((char)i);
//
//        }while (i!=-1);
//        fin.close();

    }
}
