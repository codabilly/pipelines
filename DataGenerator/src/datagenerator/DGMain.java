package datagenerator;

import java.io.FileWriter;
import java.io.IOException;

/**
 *
 * @author bilorge
 */
public class DGMain {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        DGMain me = new DGMain();
        DataDumpRow dr;
        
        long startTimeMills = System.currentTimeMillis();
        long completionTime = 0;
        
        FileWriter fw = new FileWriter("feed.csv");
        try {
            dr = new DataDumpRow();
            fw.write(dr.printHeaders() + "\n");
            
            for (int i = 0; i < 2500; i++) {
                fw.write(dr.DataDynDumpRow("TEST-SERVER-" + i, "TEST", "Linux", "TEST-SERVER-" + i + ".els.com", "TEST-SERVER-" + i, "OpenSuse Leap 15") + "\n");
            }
        } finally {
            fw.close();
            completionTime = System.currentTimeMillis() - startTimeMills;
            System.out.println("Total run time in milliseconds: " + completionTime);
        }

    }

}
