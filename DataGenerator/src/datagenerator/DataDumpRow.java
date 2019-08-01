package datagenerator;

import java.util.Random;

/**
 *
 * @author bilorge
 */
public class DataDumpRow {

    //CSV row 0 headers
    private final String CI_NAME = "CI_NAME";                            // ( A 0  )  CI_NAME                 Sever name?
    private final String CI_ID = "CI_ID";                                // ( B 1  )  CI_ID                   
    private final String STATUS = "STATUS";                              // ( C 2  )  STATUS                  
    private final String STATUSREASON = "STATUSREASON";                  // ( D 3  )  STATUSREASON            
    private final String SYSTEMROLE = "SYSTEMROLE";                      // ( E 4  )  SYSTEMROLE              Possibly identifies to which environment server belongs to?
    private final String SERVER_FUNCTION = "SERVER_FUNCTION";            // ( F 5  )  SERVER_FUNCTION         
    private final String OWNED_BY = "OWNED_BY";                          // ( G 6  )  OWNED_BY                
    private final String APP_SUPPORT = "APP_SUPPORT";                    // ( H 7  )  APP_SUPPORT             
    private final String OS_SUPPORT = "OS_SUPPORT";                      // ( I 8  )  OS_SUPPORT              determines the OS host uses?
    private final String SA_DVC_ID = "SA_DVC_ID";                        // ( J 9  )  SA_DVC_ID               
    private final String SA_SERVERNAME = "SA_SERVERNAME";                // ( K 10 )  SA_SERVERNAME          Provides the FQN server name.
    private final String SA_LOCALHOSTNAME = "SA_LOCALHOSTNAME";          // ( L 11 )  SA_LOCALHOSTNAME        Provide the server name
    private final String SA_PRIMARY_IP = "SA_PRIMARY_IP";                // ( M 12 )  SA_PRIMARY_IP           
    private final String SA_MANAGEMENT_IP = "SA_MANAGEMENT_IP";          // ( N 13 )  SA_MANAGEMENT_IP        
    private final String SA_OS_VERSION = "SA_OS_VERSION";                // ( O 14 )  SA_OS_VERSION           Provise the sever's OS version
    private final String SA_AGENT_VERSION = "SA_AGENT_VERSION";          // ( P 15 )  SA_AGENT_VERSION       
    private final String SA_AGENT_INTIAL_REG = "SA_AGENT_INTIAL_REG";    // ( Q 16 )  SA_AGENT_INTIAL_REG    
    private final String SA_UNREACHABLEDAYS = "SA_UNREACHABLEDAYS";      // ( R 17 )  SA_UNREACHABLEDAYS      
    private final String STATE = "STATE";                                // ( S 18 )  STATE                   
    private final String SA_CUSTOMER = "SA_CUSTOMER";                    // ( T 19 )  SA_CUSTOMER             
    private final String SA_FACILITY = "SA_FACILITY";                    // ( U 20 )  SA_FACILITY             This represents the data center?
    private final String PRIMARYCORE = "PRIMARYCORE";                    // ( V 21 )  PRIMARYCORE            
    private final String SA_MESH = "SA_MESH";                            // ( W 22 )  SA_MESH                 
    private final String CERTOWNER = "CERTOWNER";                        // ( X 23 )  CERTOWNER               
    private final String CERTVALIDDATE = "CERTVALIDDATE";                // ( Y 24 )  CERTVALIDDATE

    //CSV Data row
    public String ci_name;
    public String ci_id;
    public String status;
    public String statusreason;
    public String systemrole;
    public String server_function;
    public String owned_by;
    public String app_support;
    public String os_support;
    public String sa_dvc_id;
    public String sa_servername;
    public String sa_localhostname;
    public String sa_primary_ip;
    public String sa_management_IP;
    public String sa_os_version;
    public String sa_agent_version;
    public String sa_agent_intial_reg;
    public String sa_unreachabledays;
    public String state;
    public String sa_customer;
    public String sa_facility;
    public String primarycore;
    public String sa_mesh;
    public String certowner;
    public String certvaliddate;
    
    private Random r = new Random(System.currentTimeMillis());
    private final String[] NAMES = {"Rick", "Morty", "Chewbaca", "Luke Skywalker", "Anakin Skywalker", "Clint Barton", "Sam Wilson", "Groot", "Bruce Baner", "Thor", "Tony Stark", "Pepper Pots","Nick Fury", "Rocket", "Nebula", "Gomoraah"};
    private final String[] DATACENTERS = {"OXMORE", "SILAS", "TEMPE"};
    private final String[] MESH = {"PURPLE", "GREEN", "GREY", "ORANGE", "YELLOW", "B-72"};

    public DataDumpRow() {
    }

    public DataDumpRow(String ci_name, String ci_id, String status, String statusreason, String systemrole, String server_function, String owned_by, String app_support, String os_support, String sa_dvc_id, String sa_server_name, String sa_localhostname, String sa_primary_ip, String sa_management_IP, String sa_os_version, String sa_agent_versions, String sa_agent_initial_reg, String sa_unreachabledays, String state, String sa_customer, String sa_facility, String primarycore, String sa_mesh, String certowner, String certvalidate) {
        this.ci_name = ci_name;
        this.ci_id = ci_id;
        this.status = status;
        this.statusreason = statusreason;
        this.systemrole = systemrole;
        this.server_function = server_function;
        this.owned_by = owned_by;
        this.app_support = app_support;
        this.os_support = os_support;
        this.sa_dvc_id = sa_dvc_id;
        this.sa_servername = sa_server_name;
        this.sa_localhostname = sa_localhostname;
        this.sa_primary_ip = sa_primary_ip;
        this.sa_management_IP = sa_management_IP;
        this.sa_os_version = sa_os_version;
        this.sa_agent_version = sa_agent_versions;
        this.sa_agent_intial_reg = sa_agent_initial_reg; //misspelled
        this.sa_unreachabledays = sa_unreachabledays;
        this.state = state;
        this.sa_customer = sa_customer;
        this.sa_facility = sa_facility;
        this.primarycore = primarycore;
        this.sa_mesh = sa_mesh;
        this.certowner = certowner;
        this.certvaliddate = certvalidate;
    }

    public DataDumpRow(String ci_name, String systemrole, String os_support, String sa_server_name, String sa_localhostname, String sa_os_version) {
        this.ci_name = ci_name;
        this.ci_id = "OI-AAA0001";
        this.status = "Deployed";
        this.statusreason = "LOB Ready";
        this.systemrole = systemrole;
        this.server_function = "SUPPORT SERVER";
        this.owned_by = randNameGenerator();
        this.app_support = "Database Apps";
        this.os_support = os_support;
        this.sa_dvc_id = "1000001";
        this.sa_servername = sa_server_name;
        this.sa_localhostname = sa_localhostname;
        this.sa_primary_ip = randIPGenerator();
        this.sa_management_IP = randIPGenerator();
        this.sa_os_version = sa_os_version;
        this.sa_agent_version = "1.0.30.7";
        this.sa_agent_intial_reg = "YES";  //misspelled
        this.sa_unreachabledays = "0";
        this.state = "OK";
        this.sa_customer = "MIDDLEWARE";
        this.sa_facility = randDataCenterGenerator();
        this.primarycore = "sasvprc02";
        this.sa_mesh = randMeshGenerator();
        this.certowner = "SECURITY";
        this.certvaliddate = "01/01/2020";
    }
    
    public String DataDynDumpRow(String ci_name, String systemrole, String os_support, String sa_server_name, String sa_localhostname, String sa_os_version) {
        r.setSeed(r.nextLong());
        this.ci_name = ci_name;
        this.ci_id = "OI-AAA0001";
        this.status = "Deployed";
        this.statusreason = "LOB Ready";
        this.systemrole = systemrole;
        this.server_function = "SUPPORT SERVER";
        this.owned_by = randNameGenerator();
        this.app_support = "Database Apps";
        this.os_support = os_support;
        this.sa_dvc_id = "1000001";
        this.sa_servername = sa_server_name;
        this.sa_localhostname = sa_localhostname;
        this.sa_primary_ip = randIPGenerator();
        this.sa_management_IP = randIPGenerator();
        this.sa_os_version = sa_os_version;
        this.sa_agent_version = "1.0.30.7";
        this.sa_agent_intial_reg = "YES";  //misspelled
        this.sa_unreachabledays = "0";
        this.state = "OK";
        this.sa_customer = "MIDDLEWARE";
        this.sa_facility = randDataCenterGenerator();
        this.primarycore = "sasvprc02";
        this.sa_mesh = randMeshGenerator();
        this.certowner = "SECURITY";
        this.certvaliddate = "01/01/2020";
        return printRow();
    }

    public String printHeaders() {
        return this.CI_NAME + ","
                + this.CI_ID + ","
                + this.STATUS + ","
                + this.STATUSREASON + ","
                + this.SYSTEMROLE + ","
                + this.SERVER_FUNCTION + ","
                + this.OWNED_BY + ","
                + this.APP_SUPPORT + ","
                + this.OS_SUPPORT + ","
                + this.SA_DVC_ID + ","
                + this.SA_SERVERNAME + ","
                + this.SA_LOCALHOSTNAME + ","
                + this.SA_PRIMARY_IP + ","
                + this.SA_MANAGEMENT_IP + ","
                + this.SA_OS_VERSION + ","
                + this.SA_AGENT_VERSION + ","
                + this.SA_AGENT_INTIAL_REG + "," //misspelled
                + this.SA_UNREACHABLEDAYS + ","
                + this.STATE + ","
                + this.SA_CUSTOMER + ","
                + this.SA_FACILITY + ","
                + this.PRIMARYCORE + ","
                + this.SA_MESH + ","
                + this.CERTOWNER + ","
                + this.CERTVALIDDATE;
    }

    public String printRow() {
        return this.ci_name + ","
                + this.ci_id + ","
                + this.status + ","
                + this.statusreason + ","
                + this.systemrole + ","
                + this.server_function + ","
                + this.owned_by + ","
                + this.app_support + ","
                + this.os_support + ","
                + this.sa_dvc_id + ","
                + this.sa_servername + ","
                + this.sa_localhostname + ","
                + this.sa_primary_ip + ","
                + this.sa_management_IP + ","
                + this.sa_os_version + ","
                + this.sa_agent_version + ","
                + this.sa_agent_intial_reg + ","
                + this.sa_unreachabledays + ","
                + this.state + ","
                + this.sa_customer + ","
                + this.sa_facility + ","
                + this.primarycore + ","
                + this.sa_mesh + ","
                + this.certowner + ","
                + this.certvaliddate;
    }

    private String randIPGenerator() {
        return r.nextInt(256) + "." + r.nextInt(256) + "." +r.nextInt(256) + "." +r.nextInt(256);
    }
    
    private String randNameGenerator() {
        return NAMES[r.nextInt(NAMES.length)];
    }
    
    private String randDataCenterGenerator() {
        return DATACENTERS[r.nextInt(DATACENTERS.length)];
    }
    
    private String randMeshGenerator() {
        return MESH[r.nextInt(MESH.length)];
    }
}
