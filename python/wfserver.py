#using the following data dump to model the object
# COLUMN    VALUE                   COMMENT
# ( A 0  )  CI_NAME                 Sever name?
# ( B 1  )  CI_ID                   
# ( C 2  )  STATUS                  
# ( D 3  )  STATUSREASON            
# ( E 4  )  SYSTEMROLE              Possibly identifies to which environment server belongs to?
# ( F 5  )  SERVER_FUNCTION         
# ( G 6  )  OWNED_BY                
# ( H 7  )  APP_SUPPORT             
# ( I 8  )  OS_SUPPORT              determines the OS host uses?
# ( J 9  )  SA_DVC_ID               
# ( K 10 )  SA_SERVER NAME          Provides the FQN server name.
# ( L 11 )  SA_LOCALHOSTNAME        Provide the server name
# ( M 12 )  SA_PRIMARY_IP           
# ( N 13 )  SA_MANAGEMENT_IP        
# ( O 14 )  SA_OS_VERSION           Provise the sever's OS version
# ( P 15 )  SA_AGENT_VERSION        
# ( Q 16 )  SA_AGENT_INTIAL_REG     
# ( R 17 )  SA_UNREACHABLEDAYS      
# ( S 18 )  STATE                   
# ( T 19 )  SA_CUSTOMER             
# ( U 20 )  SA_FACILITY             This represents the data center?
# ( V 21 )  PRIMARYCORE             
# ( W 22 )  SA_MESH                 
# ( X 23 )  CERTOWNER               
# ( Y 24 )  CERTVALIDDATE           

#this class is a representation of basic server implementation in a Wells Fargo data center model
fqn = ''    # ( K ) - Defines the server's fully qualified name
name = ''   # ( L ) - Defines the server's name
ip = ''     # ( M ) - Defines the server's IP
os = ''     # is it provided by column I or should be derived from column O?
osv = ''    # ( O ) - Defines the server's OS Version
env = ''    # ( E ) - Defines the server's environment
dtc = ''    # ( U ) - Defines the data center where the server resides
