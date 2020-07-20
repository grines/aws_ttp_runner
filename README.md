# AWS TTP runner options  
  
# TTPs  
ec2_enum_userdata()  
enum_network()  
enum_secrets()  
iam_enum()  
iam_enum2()  
lambda_enum()  

# TTPs  
iam_persist()  

# Scenarios  
# 1
Initial Access: Valid Account  
Execution: lambda_invoke()  
Persistence: iam_persist()  
Privesc: iam_privesc()  
Credential Access: ec2_userdata  
Discovery: iam_enum()  
Collrction: s3_collect()  

Tactic	Technique	Attack Details
Initial Access	Exploit Public-Facing Application	Identify a server-side request forgery
Credential Access	Cloud Instance Metadata API	Gain access to instance meta-data credentials
Discovery	IAM Discovery	Enumerate IAM permissions
Privesc	IAM User Manipulation	Privilege escalation to user