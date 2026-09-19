# ALG SRG assessment

Assessed 2026-09-18 using Shinobi MCP `read_xccdf_file` and `write_cklb_file`, following `tools/shinobi/skills/srg-stig-compliance/SKILL.md`.

Target: `modules/application-layer-gateway/` (`main.tf`, `provider.tf`, `variables.tf`). Benchmark: Application Layer Gateway SRG, Version 2, Release 4, benchmark date 01 Jul 2026. All 160 rules are included without profile filtering.

**Compliance is not established:** 3 Open, 68 Not Applicable, 89 Not Reviewed, 0 Not a Finding.

[Download the CKLB checklist](application-layer-gateway-alg-srg-v2r4.cklb)

This is a static source assessment. No Terraform plan/apply, Azure inspection, runtime tests, provider-version validation or STIG Viewer import was performed. Not Reviewed means the evidence or applicability is unresolved; it is not a confirmed failure. No inherited controls were credited without evidence.

The Open findings concern the configured gateway path: inspection-based authorization (V-204910), harmful/suspicious traffic inspection and blocking (V-204911), and session authenticity (V-204957). The gateway selects Standard_v2 and Basic routing without inspection policies, and explicitly uses HTTP on both communication legs. Implement appropriate inspection/enforcement and authenticated transport, then verify effectiveness against approved traffic flows.

Logging, alerts, authorization, malware protection and operational behavior require effective configuration and test evidence. Their absence from this module alone does not establish that externally implemented controls are disabled. Obtain diagnostic settings, log samples, permissions, alert delivery tests and inherited-control evidence. Capacity=2 and an empty backend pool do not establish working load balancing; request_timeout=20 does not establish session inactivity enforcement.

Not Applicable decisions use explicit benchmark exclusions for absent user authentication/access-control, content filtering, TLS/encryption, SMTP, FTP or spam-protection roles in the supplied configuration. These exclusions do not waive unconditional inspection or session-authenticity requirements. Reassess them when the configured role changes. CDS, remote-access use, traffic classification, non-organizational users and provider-managed key storage remain unresolved.

Responsibility blocks identify Platform as the owner of applicable gateway configuration or evidence collection. CSP and Tenant remain N where their responsibility is not established by the supplied evidence; N does not certify exemption from wider organizational responsibilities.

Validation: all 160 unique rule IDs, group IDs, versions, severities, titles, descriptions, checks, fixes and CCI references match the original XCCDF. Every rule has an explicit status, evidence and the required responsibility block. The original benchmark was read directly by MCP without namespace conversion. This assessment replaces the earlier checklist and summary, which referenced an obsolete module path and treated several missing external controls as confirmed failures.

## Input hashes

- `benchmarks/U_Application_Layer_Gateway_SRG_V2R4_Manual-xccdf.xml`: `ce1276c85c0f88d06c4b027cad1015b03703acff865ec4ae71c9a14d8ea3b9e3`
- `modules/application-layer-gateway/main.tf`: `3f532b60ba549ae25aaf0fc3b3c239f58cd712ebc1721e66d7a16a617521b4d8`
- `modules/application-layer-gateway/provider.tf`: `c0289377204e647e307e036b52da1588ab4876536eb31af2565dd8bf57ebd6d0`
- `modules/application-layer-gateway/variables.tf`: `6a551b943be52f84079af989ec096d648ace1c0b7901bb7c4290502d63d48c01`

## Rules

| Rule | Severity | Status | Requirement |
|---|---|---|---|
| V-204909 | medium | not_reviewed | The ALG must enforce approved authorizations for logical access to information and system resources by employing identity-based, role-based, and/or attribute-based security policies. |
| V-204910 | medium | open | The ALG must enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. |
| V-204911 | medium | open | The ALG must restrict or block harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. |
| V-204912 | medium | not_reviewed | The ALG must immediately use updates made to policy enforcement mechanisms such as policy filters, rules, signatures, and analysis algorithms for gateway and/or intermediary functions. |
| V-204913 | medium | not_reviewed | The ALG that is part of a CDS must apply information flow control to data transferred between security domains by means of a policy filter which consists of a set of hardware and/or software. |
| V-204914 | medium | not_reviewed | The ALG that is part of a CDS must allow privileged administrators to enable/disable all security policy filters used to enforce information flow control. |
| V-204915 | medium | not_reviewed | The ALG that is part of a CDS must allow privileged administrators to configure and make changes to all security policy filters that are used to enforce information flow control. |
| V-204916 | medium | not_reviewed | The ALG that is part of a CDS must enforce dynamic traffic flow control based on organization-defined policies. |
| V-204917 | medium | not_reviewed | The ALG that is part of a CDS must enforce organization-defined one-way information flows using hardware mechanisms. |
| V-204918 | medium | not_reviewed | The ALG that is part of a CDS must enforce information flow control using organization-defined security policy filters as a basis for flow control decisions for organization-defined information flows. |
| V-204919 | medium | not_applicable | The ALG providing user access control intermediary services must display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to the network. |
| V-204920 | medium | not_applicable | The ALG providing user access control intermediary services must retain the Standard Mandatory DoD-approved Notice and Consent Banner on the screen until users acknowledge the usage conditions and take explicit actions to log on for further access. |
| V-204921 | medium | not_applicable | The ALG providing user access control intermediary services for publicly accessible applications must display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to the system. |
| V-204922 | medium | not_applicable | The ALG providing user access control intermediary services must limit the number of concurrent sessions to an organization-defined number for all accounts and/or account types. |
| V-204923 | medium | not_reviewed | The ALG providing intermediary services for remote access communications traffic must ensure inbound and outbound traffic is monitored for compliance with remote access security policies. |
| V-204924 | medium | not_reviewed | The ALG providing intermediary services for remote access communications traffic must use encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions. |
| V-204925 | medium | not_reviewed | The ALG that stores secret or private keys must use FIPS-approved key management technology and processes in the production and control of private/secret cryptographic keys. |
| V-204926 | medium | not_applicable | The ALG that provides intermediary services for TLS must be configured to comply with the required TLS settings in NIST SP 800-52. |
| V-204927 | medium | not_reviewed | The ALG providing intermediary services for remote access communications traffic must use NIST FIPS-validated cryptography to protect the integrity of remote access sessions. |
| V-204928 | medium | not_reviewed | The ALG must produce audit records containing information to establish what type of events occurred. |
| V-204929 | medium | not_reviewed | The ALG must produce audit records containing information to establish when (date and time) the events occurred. |
| V-204930 | medium | not_reviewed | The ALG must produce audit records containing information to establish where the events occurred. |
| V-204931 | medium | not_reviewed | The ALG must produce audit records containing information to establish the source of the events. |
| V-204932 | medium | not_reviewed | The ALG must produce audit records containing information to establish the outcome of the events. |
| V-204933 | medium | not_reviewed | The ALG must generate audit records containing information to establish the identity of any individual or process associated with the event. |
| V-204934 | medium | not_reviewed | The ALG must send an alert to, at a minimum, the information system security officer (ISSO) and system administrator (SA) when an audit processing failure occurs. |
| V-204936 | medium | not_reviewed | The ALG must protect audit information from unauthorized read access. |
| V-204937 | medium | not_reviewed | The ALG must protect audit information from unauthorized modification. |
| V-204938 | medium | not_reviewed | The ALG must protect audit information from unauthorized deletion. |
| V-204939 | medium | not_reviewed | The ALG must protect audit tools from unauthorized access. |
| V-204940 | medium | not_reviewed | The ALG must protect audit tools from unauthorized modification. |
| V-204941 | medium | not_reviewed | The ALG must protect audit tools from unauthorized deletion. |
| V-204942 | medium | not_reviewed | The ALG must not have unnecessary services and functions enabled. |
| V-204943 | medium | not_reviewed | The ALG must be configured to remove or disable unrelated or unneeded application proxy services. |
| V-204944 | medium | not_reviewed | The ALG must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments. |
| V-204945 | medium | not_applicable | The ALG providing user authentication intermediary services must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users). |
| V-204946 | medium | not_applicable | The ALG providing user access control intermediary services must be configured with a pre-established trust relationship and mechanisms with appropriate authorities (e.g., Active Directory or AAA server) which validate user account access authorizations and privileges. |
| V-204947 | medium | not_applicable | The ALG providing user authentication intermediary services must restrict user authentication traffic to specific authentication server(s). |
| V-204948 | medium | not_applicable | The ALG providing user authentication intermediary services must use multifactor authentication for network access to non-privileged accounts. |
| V-204949 | medium | not_applicable | The ALG providing user authentication intermediary services must implement replay-resistant authentication mechanisms for network access to nonprivileged accounts. |
| V-204950 | medium | not_applicable | The ALG that provides intermediary services for TLS must validate certificates used for TLS functions by performing RFC 5280-compliant certification path validation. |
| V-204951 | medium | not_applicable | The ALG providing PKI-based user authentication intermediary services must map authenticated identities to the user account. |
| V-204952 | medium | not_reviewed | The ALG providing user authentication intermediary services must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users). |
| V-204953 | medium | not_applicable | The ALG providing content filtering must block outbound traffic containing known and unknown DoS attacks to protect against the use of internal information systems to launch any Denial of Service (DoS) attacks against other networks or endpoints. |
| V-204954 | medium | not_reviewed | The ALG must deny network communications traffic by default and allow network communications traffic by exception (i.e., deny all, permit by exception). |
| V-204955 | medium | not_reviewed | The ALG must terminate all network connections associated with a communications session at the end of the session, or as follows: for in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity; and for user sessions (non-privileged session), the session must be terminated after 15 minutes of inactivity. |
| V-204956 | medium | not_reviewed | The ALG must detect, at a minimum, mobile code that is unsigned or exhibiting unusual behavior, has not undergone a risk assessment, or is prohibited for use based on a risk assessment. |
| V-204957 | medium | open | The ALG must protect the authenticity of communications sessions. |
| V-204958 | medium | not_reviewed | The ALG must invalidate session identifiers upon user logout or other session termination. |
| V-204959 | medium | not_reviewed | The ALG must recognize only system-generated session identifiers. |
| V-204960 | medium | not_reviewed | The ALG must generate unique session identifiers using a FIPS 140-2 approved random number generator. |
| V-204961 | medium | not_reviewed | The ALG must fail to a secure state upon failure of initialization, shutdown, or abort actions. |
| V-204962 | medium | not_reviewed | In the event of a system failure of the ALG function, the ALG must save diagnostic information, log system messages, and load the most current security policies, rules, and signatures when restarted. |
| V-204963 | medium | not_applicable | The ALG providing content filtering must update malicious code protection mechanisms and signature definitions whenever new releases are available in accordance with organizational configuration management policy. |
| V-204964 | medium | not_applicable | The ALG providing content filtering must be configured to perform real-time scans of files from external sources at network entry/exit points as they are downloaded and prior to being opened or executed. |
| V-204965 | medium | not_applicable | The ALG providing content filtering must block malicious code upon detection. |
| V-204966 | medium | not_applicable | The ALG providing content filtering must delete or quarantine malicious code in response to malicious code detection. |
| V-204967 | medium | not_applicable | The ALG providing content filtering must send an immediate (within seconds) alert to the system administrator, at a minimum, in response to malicious code detection. |
| V-204968 | medium | not_applicable | The ALG providing content filtering must update malicious code protection mechanisms and signature definitions whenever new releases are available in accordance with organizational configuration management procedures. |
| V-204969 | medium | not_reviewed | The ALG must generate error messages that provide the information necessary for corrective actions without revealing information that could be exploited by adversaries. |
| V-204970 | medium | not_reviewed | The ALG that is part of a CDS must enforce information flow control based on organization-defined metadata. |
| V-204971 | medium | not_reviewed | The ALG that is part of a CDS must block the transfer of data with malformed security attribute metadata structures. |
| V-204972 | medium | not_reviewed | The ALG that is part of a CDS must decompose information into organization-defined, policy-relevant subcomponents for submission to policy enforcement mechanisms before transferring information between different security domains. |
| V-204973 | medium | not_reviewed | The ALG that is part of a CDS, when transferring information between different security domains, must implement organization-defined security policy filters requiring fully enumerated formats that restrict data structure and content. |
| V-204974 | medium | not_reviewed | The ALG that is part of a CDS, when transferring information between different security domains, must examine the information for the presence of organization-defined unsanctioned information. |
| V-204975 | medium | not_reviewed | The ALG that is part of a CDS must prohibit the transfer of unsanctioned information in accordance with the security policy when transferring information between different security domains. |
| V-204976 | medium | not_applicable | The ALG providing content filtering must block or restrict detected prohibited mobile code. |
| V-204977 | medium | not_applicable | The ALG providing content filtering must prevent the download of prohibited mobile code. |
| V-204978 | medium | not_reviewed | The ALG providing intermediary services for remote access communications traffic must control remote access methods. |
| V-204979 | medium | not_reviewed | The ALG providing intermediary services for remote access communications traffic must provide the capability to immediately disconnect or disable remote access to the information system. |
| V-204980 | medium | not_applicable | To protect against data mining, the ALG providing content filtering must prevent code injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields. |
| V-204981 | medium | not_applicable | To protect against data mining, the ALG providing content filtering must prevent code injection attacks launched against application objects including, at a minimum, application URLs and application code. |
| V-204982 | medium | not_applicable | To protect against data mining, the ALG providing content filtering must prevent SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields. |
| V-204983 | medium | not_applicable | To protect against data mining, the ALG providing content filtering must detect code injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields. |
| V-204984 | medium | not_applicable | To protect against data mining, the ALG providing content filtering must detect SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields. |
| V-204985 | medium | not_applicable | To protect against data mining, the ALG providing content filtering as part of its intermediary services must detect code injection attacks launched against application objects including, at a minimum, application URLs and application code. |
| V-204986 | medium | not_reviewed | The ALG that is part of a CDS must use source and destination security attributes associated with organization-defined information, source, and/or destination objects to enforce organization-defined information flow control policies as a basis for flow control decisions. |
| V-204987 | medium | not_reviewed | The ALG that is part of a CDS, when transferring information between different security domains, must use organization-defined data type identifiers to validate data essential for information flow decisions. |
| V-204988 | medium | not_reviewed | The ALG that is part of a CDS must uniquely identify and authenticate source by organization, system, application, and/or individual for information transfer. |
| V-204989 | medium | not_reviewed | The ALG that is part of a CDS must uniquely identify and authenticate destination by organization, system, application, and/or individual for information transfer. |
| V-204991 | medium | not_reviewed | The ALG that is part of a CDS, when transferring information between different security domains, must apply the same security policy filtering to metadata as it applies to data payloads. |
| V-204992 | medium | not_reviewed | The ALG that is part of a CDS must enforce the use of human reviews for organization-defined information flows under organization-defined conditions. |
| V-204993 | medium | not_applicable | The ALG providing user access control intermediary services must provide the capability for authorized users to select a user session to capture or view. |
| V-204995 | medium | not_reviewed | The ALG must off-load audit records onto a centralized log server. |
| V-204996 | medium | not_reviewed | The ALG must provide an immediate real-time alert to, at a minimum, the SCA and ISSO, of all audit failure events where the detection and/or prevention function is unable to write events to either local storage or the centralized server. |
| V-204997 | medium | not_applicable | The ALG providing user authentication intermediary services must require users to reauthenticate when organization-defined circumstances or situations require reauthentication. |
| V-204998 | medium | not_applicable | The ALG providing user authentication intermediary services must implement multifactor authentication for remote access to nonprivileged accounts such that one of the factors is provided by a device separate from the system gaining access. |
| V-204999 | medium | not_applicable | The ALG providing user authentication intermediary services must implement multifactor authentication for remote access to privileged accounts such that one of the factors is provided by a device separate from the system gaining access. |
| V-205000 | medium | not_reviewed | The ALG must prohibit the use of cached authenticators after an organization-defined time period. |
| V-205001 | medium | not_applicable | The ALG providing user authentication intermediary services using PKI-based user authentication must implement a local cache of revocation data to support path discovery and validation in case of the inability to access revocation information via the network. |
| V-205002 | medium | not_applicable | The ALG providing user authentication intermediary services must conform to Federal Identity, Credential, and Access Management (FICAM)-issued profiles. |
| V-205003 | medium | not_applicable | The ALG providing user authentication intermediary services using PKI-based user authentication must only accept end entity certificates issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs) for the establishment of protected sessions. |
| V-205004 | medium | not_applicable | The ALG providing content filtering must protect against known and unknown types of Denial of Service (DoS) attacks by employing rate-based attack prevention behavior analysis. |
| V-205005 | medium | not_reviewed | The ALG must implement load balancing to limit the effects of known and unknown types of Denial of Service (DoS) attacks. |
| V-205006 | medium | not_applicable | The ALG providing content filtering must protect against known types of Denial of Service (DoS) attacks by employing signatures. |
| V-205007 | medium | not_applicable | The ALG providing content filtering must protect against or limit the effects of known and unknown types of Denial of Service (DoS) attacks by employing pattern recognition pre-processors. |
| V-205008 | medium | not_reviewed | The ALG must only allow incoming communications from organization-defined authorized sources routed to organization-defined authorized destinations. |
| V-205009 | medium | not_reviewed | The ALG must fail securely in the event of an operational failure. |
| V-205010 | medium | not_reviewed | The ALG must identify and log internal users associated with denied outgoing communications traffic posing a threat to external information systems. |
| V-205011 | medium | not_reviewed | The ALG must behave in a predictable and documented manner that reflects organizational and system objectives when invalid inputs are received. |
| V-205012 | medium | not_applicable | The ALG providing content filtering must be configured to integrate with a system-wide intrusion detection system. |
| V-205013 | medium | not_applicable | The ALG providing content filtering must detect use of network services that have not been authorized or approved by the ISSM and ISSO, at a minimum. |
| V-205014 | medium | not_applicable | The ALG providing content filtering must generate a log record when unauthorized network services are detected. |
| V-205015 | medium | not_applicable | The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when unauthorized network services are detected. |
| V-205016 | medium | not_applicable | The ALG providing content filtering must continuously monitor inbound communications traffic crossing internal security boundaries for unusual or unauthorized activities or conditions. |
| V-205017 | medium | not_applicable | The ALG providing content filtering must continuously monitor outbound communications traffic crossing internal security boundaries for unusual/unauthorized activities or conditions. |
| V-205018 | medium | not_applicable | The ALG providing content filtering must send an alert to, at a minimum, the ISSO and ISSM when detection events occur. |
| V-205019 | medium | not_applicable | The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when threats identified by authoritative sources (e.g., IAVMs or CTOs) are detected. |
| V-205020 | medium | not_applicable | The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when root level intrusion events which provide unauthorized privileged access are detected. |
| V-205021 | medium | not_applicable | The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when user level intrusions which provide non-privileged access are detected. |
| V-205022 | medium | not_applicable | The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when denial of service incidents are detected. |
| V-205023 | medium | not_applicable | The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when new active propagation of malware infecting DoD systems or malicious code adversely affecting the operations and/or security of DoD systems is detected. |
| V-205024 | medium | not_applicable | The ALG that implements spam protection mechanisms must be updated automatically. |
| V-205026 | high | not_applicable | The ALG providing user authentication intermediary services must transmit only encrypted representations of passwords. |
| V-205027 | medium | not_reviewed | The ALG must check the validity of all data inputs except those specifically identified by the organization. |
| V-205028 | medium | not_reviewed | The ALG must reveal error messages only to the ISSO, ISSM, and SCA. |
| V-205029 | medium | not_reviewed | The ALG must generate audit records when successful/unsuccessful attempts to access security objects occur. |
| V-205030 | medium | not_reviewed | The ALG that is part of a CDS must generate audit records when successful/unsuccessful attempts to access security levels occur. |
| V-205031 | medium | not_reviewed | The ALG must generate audit records when successful/unsuccessful attempts to access categories of information (e.g., classification levels) occur. |
| V-205032 | medium | not_applicable | The ALG providing user access control intermediary services must generate audit records when successful/unsuccessful attempts to modify privileges occur. |
| V-205033 | medium | not_reviewed | The ALG must generate audit records when successful/unsuccessful attempts to modify security objects occur. |
| V-205034 | medium | not_reviewed | The ALG must generate audit records when successful/unsuccessful attempts to modify security levels occur. |
| V-205035 | medium | not_reviewed | The ALG must generate audit records when successful/unsuccessful attempts to modify categories of information (e.g., classification levels) occur. |
| V-205036 | medium | not_applicable | The ALG providing user access control intermediary services must generate audit records when successful/unsuccessful attempts to delete privileges occur. |
| V-205037 | medium | not_reviewed | The ALG must generate audit records when successful/unsuccessful attempts to delete security levels occur. |
| V-205038 | medium | not_reviewed | The ALG must generate audit records when successful/unsuccessful attempts to delete security objects occur. |
| V-205039 | medium | not_reviewed | The ALG must generate audit records when successful/unsuccessful attempts to delete categories of information (e.g., classification levels) occur. |
| V-205040 | medium | not_applicable | The ALG providing user access control intermediary services must generate audit records when successful/unsuccessful logon attempts occur. |
| V-205041 | medium | not_applicable | The ALG providing user access control intermediary services must generate audit records showing starting and ending time for user access to the system. |
| V-205042 | medium | not_applicable | The ALG providing encryption intermediary services must implement NIST FIPS-validated cryptography to generate cryptographic hashes. |
| V-205043 | medium | not_applicable | The ALG providing encryption intermediary services must implement NIST FIPS-validated cryptography for digital signatures. |
| V-205044 | medium | not_applicable | The ALG providing encryption intermediary services must use NIST FIPS-validated cryptography to implement encryption services. |
| V-205045 | medium | not_reviewed | The ALG must off-load audit records onto a centralized log server in real time. |
| V-205046 | medium | not_reviewed | The ALG that is part of a CDS must have the capability to implement journaling. |
| V-205047 | medium | not_reviewed | The ALG must be configured in accordance with the security configuration settings based on DoD security policy and technology-specific security best practices. |
| V-205048 | medium | not_applicable | The ALG that provides intermediary services for SMTP must inspect inbound and outbound SMTP and Extended SMTP communications traffic for protocol compliance and protocol anomalies. |
| V-205049 | medium | not_applicable | The ALG that provides intermediary services for FTP must inspect inbound and outbound FTP communications traffic for protocol compliance and protocol anomalies. |
| V-205050 | medium | not_reviewed | The ALG that provides intermediary services for HTTP must inspect inbound and outbound HTTP traffic for protocol compliance and protocol anomalies. |
| V-205051 | medium | not_applicable | The ALG providing user access control intermediary services must generate audit records when successful/unsuccessful attempts to access privileges occur. |
| V-205052 | medium | not_applicable | The ALG providing user access control intermediary services must initiate a session lock after a 15-minute period of inactivity. |
| V-205053 | medium | not_applicable | The ALG providing user access control intermediary services must provide the capability for users to directly initiate a session lock. |
| V-205054 | medium | not_applicable | The ALG providing user access control intermediary services must retain the session lock until the user reestablishes access using established identification and authentication procedures. |
| V-205055 | medium | not_applicable | The ALG providing user access control intermediary services must automatically terminate a user session when organization-defined conditions or trigger events that require a session disconnect occur. |
| V-205056 | medium | not_applicable | The ALG providing user access control intermediary services must provide a logoff capability for user-initiated communications sessions. |
| V-205057 | medium | not_applicable | The ALG providing user access control intermediary services must display an explicit logoff message to users indicating the reliable termination of authenticated communications sessions. |
| V-205058 | medium | not_applicable | The ALG providing user access control intermediary services must conceal, via the session lock, information previously visible on the display with a publicly viewable image. |
| V-263540 | medium | not_reviewed | The ALG must prevent or restrict changes to the configuration of the system under organization-defined circumstances. |
| V-263541 | medium | not_reviewed | The ALG must employ organization-defined controls by type of denial of service (DoS) to achieve the DoS objective. |
| V-263542 | medium | not_reviewed | The ALG must implement physically or logically separate subnetworks to isolate organization-defined critical system components and functions. |
| V-263543 | medium | not_reviewed | The ALG must implement antispoofing mechanisms to prevent adversaries from falsifying the security attributes indicating the successful application of the security process. |
| V-263544 | medium | not_reviewed | The ALG must include only approved trust anchors in trust stores or certificate stores managed by the organization. |
| V-263545 | medium | not_reviewed | The ALG must provide protected storage for cryptographic keys with organization-defined safeguards and/or hardware protected key store. |
| V-263546 | medium | not_reviewed | The ALG must establish organization-defined alternate communications paths for system operations organizational command and control. |
| V-263547 | medium | not_reviewed | The ALG must implement signature based and/or nonsignature based malicious code protection mechanisms at system entry and exit points to detect and eradicate malicious code. |
| V-263548 | medium | not_reviewed | The ALG must configure malicious code protection mechanisms to send alerts to organization-defined personnel in response to malicious code detection. |
| V-278954 | medium | not_reviewed | The ALG must validate the integrity of transmitted security attributes. |
| V-278955 | medium | not_reviewed | The ALG must use cryptographic algorithms approved by NSA to protect NSS when transporting classified traffic across an unclassified network. |
| V-278956 | medium | not_reviewed | The ALG must be configured to use cryptographic algorithms approved by NSA to protect NSS for remote access to a classified network. |
| V-278957 | medium | not_reviewed | The ALG must use a FIPS-validated cryptographic module to provision digital signatures. |
| V-278958 | medium | not_reviewed | The ALG must use a FIPS-validated cryptographic module to implement encryption services for unclassified information requiring confidentiality. |
