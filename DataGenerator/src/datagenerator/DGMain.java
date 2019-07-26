package datagenerator;

import java.util.Date;



/**
 *
 * @author bilorge
 */
public class DGMain {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        DGMain me = new DGMain();
        System.out.println("Hi!!!!!");
        me.SayDate();
    }
    
    public void SayDate() {
        System.out.println(new Date().toInstant().toString()); 
    }
    
}
