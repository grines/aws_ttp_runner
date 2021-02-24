<p><img src="https://attack.mitre.org/theme/images/MITRE_ATTACK_logo_Lockup-black.jpg" width="150px" /></p>

# AWS TTP Runner

AWS TTP Runner allows every security team to test their AWS controls by executing simple
"tests" that exercise the same techniques used by adversaries (all mapped to
[Mitre's ATT&CK](https://attack.mitre.org/wiki/Main_Page)).

## Philosophy

AWS TTP Runner is a library of simple tests that every security team can execute to test their controls. Tests are
focused, have few dependencies, and are defined in a structured format that be used by automation frameworks.

## Next Steps
- Add terraform resources
- Finalize TTPs
- Raw API output examples
- Build out scenarios
- Improve runner code
- Improve module comments
- Add weaponize option


## Techniques
### Initial Access
* Metadata compromise (initial_Meta)
### Persistence
- [x] Access Key Creation (modules/persist_AccessKey)
- [x] User Creation w/ inline policy (modules/persist_CreateUser)
- [x] EC2 w/ SSM run command payload (modules/persist_EC2_SSM)
- [x] EC2 with Userdata payload (modules/persist_EC2_userdata)
- [x] Lambda Function with external post of ec2 creds (modules/persist_Lambda)
### Privilege escalalations
- [x] Add user to a group (modules/privesc_Group)
- [ ] Update user policy (modules/privesc_Policy)
- [ ] Create login profile (modules/privesc_Profile)
### Discovery
- [x] User/Group/Roles/Polices Enumeration v1 (modules/enum_Iamv1)
- [x] User/Group/Roles/Polices Enumeration v2 (modules/enum_Iamv2)
- [x] EC2 Userdata Enumeration (modules/enum_Userdata)
- [x] Lambda Functions Enumeration (modules/enum_Lambda)
- [x] Secrets Storage Enumeration (modules/enum_Secrets)
- [x] VPC Enumeration (modules/enum_Network)
### Exfiltration
- [ ] S3 Bucket (modules/exfil_S3)
- [ ] Snapshots (modules/exfil_Snapshots)
- [ ] Network (modules/exfil_Network)
### Collection
- [ ] VPC Mirror (modules/collect_Mirror)
- [ ] Share snapshots with external account (modules/collect_Snapshots)
- [ ] S3 Bucket (modules/collect_S3)
### Defense Evasion
- [ ] Change user agent (modules/evasion_Useragent)
- [ ] Dynamically change regions (modules/evasion_Region)
- [ ] IAM Hopping Keys, Roles (modules/evasion_IAM)
### Lateral Movement
- [ ] Assume Role (modules/lateral_Assume)

## Scenarios
### Scenario 1
### Scenario 2
### Scenario 3
### Scenario 4
### Scenario 5
