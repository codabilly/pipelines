package datagenerator;

/**
 *
 * @author bilorge
 */
public class WFServer {
//  #this class is a representation of basic server implementation in a Wells Fargo data center model
    private String fqn; //   # ( K ) - Defines the server's fully qualified name
    private String name; //  # ( L ) - Defines the server's name
    private String ip; //    # ( M ) - Defines the server's IP
    private String os; //    # is it provided by column I or should be derived from column O?
    private String osv; //   # ( O ) - Defines the server's OS Version
    private String env; //   # ( E ) - Defines the server's environment
    private String dtc; //   # ( U ) - Defines the data center where the server resides

    public WFServer() {
    }

    public WFServer(String fqn, String name, String ip, String os, String osv, String env, String dtc) {
        this.fqn = fqn;
        this.name = name;
        this.ip = ip;
        this.os = os;
        this.osv = osv;
        this.env = env;
        this.dtc = dtc;
    }

    @Override
    public String toString() {
        return "WFServer{" + "fqn=" + fqn + ", name=" + name + ", ip=" + ip + ", os=" + os + ", osv=" + osv + ", env=" + env + ", dtc=" + dtc + '}';
    }
    
    /**
     * @return the fqn
     */
    public String getFqn() {
        return fqn;
    }

    /**
     * @param fqn the fqn to set
     */
    public void setFqn(String fqn) {
        this.fqn = fqn;
    }

    /**
     * @return the name
     */
    public String getName() {
        return name;
    }

    /**
     * @param name the name to set
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * @return the ip
     */
    public String getIp() {
        return ip;
    }

    /**
     * @param ip the ip to set
     */
    public void setIp(String ip) {
        this.ip = ip;
    }

    /**
     * @return the os
     */
    public String getOs() {
        return os;
    }

    /**
     * @param os the os to set
     */
    public void setOs(String os) {
        this.os = os;
    }

    /**
     * @return the osv
     */
    public String getOsv() {
        return osv;
    }

    /**
     * @param osv the osv to set
     */
    public void setOsv(String osv) {
        this.osv = osv;
    }

    /**
     * @return the env
     */
    public String getEnv() {
        return env;
    }

    /**
     * @param env the env to set
     */
    public void setEnv(String env) {
        this.env = env;
    }

    /**
     * @return the dtc
     */
    public String getDtc() {
        return dtc;
    }

    /**
     * @param dtc the dtc to set
     */
    public void setDtc(String dtc) {
        this.dtc = dtc;
    }
    
}
