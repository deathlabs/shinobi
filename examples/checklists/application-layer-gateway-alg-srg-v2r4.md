# ALG SRG V2R4 — Terraform assessment

Evaluated with `compliance_analyst` on 2026-09-19. Scope: `examples/modules/application-layer-gateway/`; the requested `.examples/` path is `examples/` in this repository.

[Download CKLB checklist](application-layer-gateway-alg-srg-v2r4.cklb)

## Results

| Status | Rules |
|---|---:|
| open | 5 |
| not_a_finding | 0 |
| not_applicable | 70 |
| not_reviewed | 85 |

All 160 requirements have explicit statuses, evidence, and stakeholder responsibility blocks. No control is marked compliant from the available evidence.

## Scope and limitations

This is a Terraform source assessment, not a deployed-system compliance determination. The backend pool is empty. No plan/apply, live configuration, effective Azure policies, audit logs, or operational tests were inspected. Open findings describe gaps in the declared module. Controls dependent on inherited, provider-managed, operational, or organizational evidence remain not reviewed.

Service-specific not-applicable decisions apply only to the declared HTTP forwarding configuration; reassess when the operational role or enabled services change. Cross-domain and remote-access mission context requires separate confirmation. Stakeholder flags assign evidence/remediation follow-up, not contractual responsibility.

## Method and provenance

The compliance analyst reviewed the supplied benchmark and Terraform source, using the repository `srg-stig-compliance` skill. Terraform MCP `search_providers` and `get_provider_details` supplied hashicorp/azurerm 5.4.0 application_gateway documentation (document 13497420). The Shinobi MCP parser was attempted but could not access the benchmark at its container path; the repository implementations of `read_xccdf_file` and `write_cklb_file` were used locally. Existing assessed entries were retained where confirmed by the analyst and revised where evidence or applicability needed correction.

Validation checks exact one-to-one coverage of all 160 source rules, preservation of benchmark fields, valid explicit statuses, evidence, stakeholder blocks, and Markdown/CKLB agreement. This does not establish compatibility with a particular STIG Viewer release.

Input SHA-256 hashes:

- `examples/benchmarks/U_Application_Layer_Gateway_SRG_V2R4_Manual-xccdf.xml`: `ce1276c85c0f88d06c4b027cad1015b03703acff865ec4ae71c9a14d8ea3b9e3`
- `examples/modules/application-layer-gateway/main.tf`: `3f532b60ba549ae25aaf0fc3b3c239f58cd712ebc1721e66d7a16a617521b4d8`
- `examples/modules/application-layer-gateway/provider.tf`: `c0289377204e647e307e036b52da1588ab4876536eb31af2565dd8bf57ebd6d0`
- `examples/modules/application-layer-gateway/variables.tf`: `6a551b943be52f84079af989ec096d648ace1c0b7901bb7c4290502d63d48c01`

## Open findings

| Rule | Requirement | Evidence and remediation |
|---|---|---|
| V-204910 / SRG-NET-000018-ALG-000017 | The ALG must enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. | Requirement: The ALG must enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.  examples/modules/application-layer-gateway/main.tf:34-38 explicitly selects Standard_v2 for azurerm_application_gateway.example and main.tf:45-81 configures Basic routing from public HTTP listener to backend-pool. No content inspection/filtering policy or WAF configuration implements required authorized attribute/content flow enforcement or harmful-traffic blocking. Implement and validate the required inspection/enforcement mechanism; HTTP routing does not satisfy this control. |
| V-204911 / SRG-NET-000019-ALG-000018 | The ALG must restrict or block harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. | Requirement: The ALG must restrict or block harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.  examples/modules/application-layer-gateway/main.tf:34-38 explicitly selects Standard_v2 for azurerm_application_gateway.example and main.tf:45-81 configures Basic routing from public HTTP listener to backend-pool. No content inspection/filtering policy or WAF configuration implements required authorized attribute/content flow enforcement or harmful-traffic blocking. Implement and validate the required inspection/enforcement mechanism; HTTP routing does not satisfy this control. |
| V-204956 / SRG-NET-000228-ALG-000108 | The ALG must detect, at a minimum, mobile code that is unsigned or exhibiting unusual behavior, has not undergone a risk assessment, or is prohibited for use based on a risk assessment. | Requirement: The ALG must detect, at a minimum, mobile code that is unsigned or exhibiting unusual behavior, has not undergone a risk assessment, or is prohibited for use based on a risk assessment.  examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 and main.tf:59-81 implements Basic HTTP forwarding with no mobile-code inspection, signature/nonsignature malware scanner or detection/eradication path. These unconditional controls apply even though separately conditional content-filtering controls are N/A. Add appropriate malware inspection and validate detection/eradication against approved policy. |
| V-204957 / SRG-NET-000230-ALG-000113 | The ALG must protect the authenticity of communications sessions. | Requirement: The ALG must protect the authenticity of communications sessions.  examples/modules/application-layer-gateway/main.tf:50-52 exposes port 80; backend_http_settings uses port=80/protocol=Http (main.tf:59-64); http_listener uses protocol=Http (main.tf:67-71). Both declared legs lack cryptographic peer/session authentication and transport integrity; Basic forwarding (main.tf:74-81) adds none. Configure authenticated protected sessions on both legs and validate session authenticity. |
| V-263547 / SRG-NET-000765-ALG-000170 | The ALG must implement signature based and/or nonsignature based malicious code protection mechanisms at system entry and exit points to detect and eradicate malicious code. | Requirement: The ALG must implement signature based and/or nonsignature based malicious code protection mechanisms at system entry and exit points to detect and eradicate malicious code.  examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 and main.tf:59-81 implements Basic HTTP forwarding with no mobile-code inspection, signature/nonsignature malware scanner or detection/eradication path. These unconditional controls apply even though separately conditional content-filtering controls are N/A. Add appropriate malware inspection and validate detection/eradication against approved policy. |

## Full checklist

Paths are relative to the repository root. The CKLB preserves full benchmark discussion, checks, fixes, severity, identifiers and CCI references.

### V-204909 — SRG-NET-000015-ALG-000016

**The ALG must enforce approved authorizations for logical access to information and system resources by employing identity-based, role-based, and/or attribute-based security policies.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must enforce approved authorizations for logical access to information and system resources by employing identity-based, role-based, and/or attribute-based security policies.

examples/modules/application-layer-gateway/main.tf:1-82 declares gateway/network resources; provider.tf:12-15 selects Azure subscription but supplies no effective Azure RBAC, inherited policy, management locks, privileged-access conditions or approved authorization matrix. Review effective management-plane assignments, conditional access/change restrictions and approvals; omission does not prove absence in deployment.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204910 — SRG-NET-000018-ALG-000017

**The ALG must enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.**

Status: `open` · Severity: medium

Requirement: The ALG must enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.

examples/modules/application-layer-gateway/main.tf:34-38 explicitly selects Standard_v2 for azurerm_application_gateway.example and main.tf:45-81 configures Basic routing from public HTTP listener to backend-pool. No content inspection/filtering policy or WAF configuration implements required authorized attribute/content flow enforcement or harmful-traffic blocking. Implement and validate the required inspection/enforcement mechanism; HTTP routing does not satisfy this control.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204911 — SRG-NET-000019-ALG-000018

**The ALG must restrict or block harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.**

Status: `open` · Severity: medium

Requirement: The ALG must restrict or block harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.

examples/modules/application-layer-gateway/main.tf:34-38 explicitly selects Standard_v2 for azurerm_application_gateway.example and main.tf:45-81 configures Basic routing from public HTTP listener to backend-pool. No content inspection/filtering policy or WAF configuration implements required authorized attribute/content flow enforcement or harmful-traffic blocking. Implement and validate the required inspection/enforcement mechanism; HTTP routing does not satisfy this control.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204912 — SRG-NET-000019-ALG-000019

**The ALG must immediately use updates made to policy enforcement mechanisms such as policy filters, rules, signatures, and analysis algorithms for gateway and/or intermediary functions.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must immediately use updates made to policy enforcement mechanisms such as policy filters, rules, signatures, and analysis algorithms for gateway and/or intermediary functions.

examples/modules/application-layer-gateway/main.tf:34-38,74-81 declares Standard_v2/Basic routing, not policy propagation timing. Obtain service-enforcement documentation and runtime change tests proving immediate relevant policy/rule updates, including established sessions where applicable.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204913 — SRG-NET-000019-ALG-000021

**The ALG that is part of a CDS must apply information flow control to data transferred between security domains by means of a policy filter which consists of a set of hardware and/or software.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204914 — SRG-NET-000021-ALG-000068

**The ALG that is part of a CDS must allow privileged administrators to enable/disable all security policy filters used to enforce information flow control.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204915 — SRG-NET-000022-ALG-000069

**The ALG that is part of a CDS must allow privileged administrators to configure and make changes to all security policy filters that are used to enforce information flow control.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204916 — SRG-NET-000029-ALG-000079

**The ALG that is part of a CDS must enforce dynamic traffic flow control based on organization-defined policies.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204917 — SRG-NET-000032-ALG-000082

**The ALG that is part of a CDS must enforce organization-defined one-way information flows using hardware mechanisms.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204918 — SRG-NET-000033-ALG-000083

**The ALG that is part of a CDS must enforce information flow control using organization-defined security policy filters as a basis for flow control decisions for organization-defined information flows.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204919 — SRG-NET-000041-ALG-000022

**The ALG providing user access control intermediary services must display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to the network.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to the network.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204920 — SRG-NET-000042-ALG-000023

**The ALG providing user access control intermediary services must retain the Standard Mandatory DoD-approved Notice and Consent Banner on the screen until users acknowledge the usage conditions and take explicit actions to log on for further access.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must retain the Standard Mandatory DoD-approved Notice and Consent Banner on the screen until users acknowledge the usage conditions and take explicit actions to log on for further access.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204921 — SRG-NET-000043-ALG-000024

**The ALG providing user access control intermediary services for publicly accessible applications must display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to the system.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services for publicly accessible applications must display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to the system.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204922 — SRG-NET-000053-ALG-000001

**The ALG providing user access control intermediary services must limit the number of concurrent sessions to an organization-defined number for all accounts and/or account types.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must limit the number of concurrent sessions to an organization-defined number for all accounts and/or account types.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204923 — SRG-NET-000061-ALG-000009

**The ALG providing intermediary services for remote access communications traffic must ensure inbound and outbound traffic is monitored for compliance with remote access security policies.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG providing intermediary services for remote access communications traffic must ensure inbound and outbound traffic is monitored for compliance with remote access security policies.

examples/modules/application-layer-gateway/main.tf:45-81 configures a public HTTP reverse proxy with empty backend pool; eventual workload/remote-access role is unknown. Obtain remote-access architecture/service inventory, approved methods, monitoring/disconnection tests and applicable cryptographic evidence. If this listener carries remote-access sessions, explicit Http (main.tf:63,71) cannot supply required confidentiality/integrity; applicability is unresolved.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: Y
```

### V-204924 — SRG-NET-000062-ALG-000011

**The ALG providing intermediary services for remote access communications traffic must use encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG providing intermediary services for remote access communications traffic must use encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions.

examples/modules/application-layer-gateway/main.tf:45-81 configures a public HTTP reverse proxy with empty backend pool; eventual workload/remote-access role is unknown. Obtain remote-access architecture/service inventory, approved methods, monitoring/disconnection tests and applicable cryptographic evidence. If this listener carries remote-access sessions, explicit Http (main.tf:63,71) cannot supply required confidentiality/integrity; applicability is unresolved.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: Y
```

### V-204925 — SRG-NET-000062-ALG-000092

**The ALG that stores secret or private keys must use FIPS-approved key management technology and processes in the production and control of private/secret cryptographic keys.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG that stores secret or private keys must use FIPS-approved key management technology and processes in the production and control of private/secret cryptographic keys.

examples/modules/application-layer-gateway/main.tf:50-72 explicitly configures port 80/Http on frontend and backend; main.tf:29-82 contains no TLS listener, certificate, private-key reference, or encryption intermediary. The check's TLS/encryption/key-generation-or-storage precondition does not apply to the declared data-plane configuration; this is not approval of plaintext communications.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204926 — SRG-NET-000062-ALG-000150

**The ALG that provides intermediary services for TLS must be configured to comply with the required TLS settings in NIST SP 800-52.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG that provides intermediary services for TLS must be configured to comply with the required TLS settings in NIST SP 800-52.

examples/modules/application-layer-gateway/main.tf:50-72 explicitly configures port 80/Http on frontend and backend; main.tf:29-82 contains no TLS listener, certificate, private-key reference, or encryption intermediary. The check's TLS/encryption/key-generation-or-storage precondition does not apply to the declared data-plane configuration; this is not approval of plaintext communications.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204927 — SRG-NET-000063-ALG-000012

**The ALG providing intermediary services for remote access communications traffic must use NIST FIPS-validated cryptography to protect the integrity of remote access sessions.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG providing intermediary services for remote access communications traffic must use NIST FIPS-validated cryptography to protect the integrity of remote access sessions.

examples/modules/application-layer-gateway/main.tf:45-81 configures a public HTTP reverse proxy with empty backend pool; eventual workload/remote-access role is unknown. Obtain remote-access architecture/service inventory, approved methods, monitoring/disconnection tests and applicable cryptographic evidence. If this listener carries remote-access sessions, explicit Http (main.tf:63,71) cannot supply required confidentiality/integrity; applicability is unresolved.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: Y
```

### V-204928 — SRG-NET-000074-ALG-000043

**The ALG must produce audit records containing information to establish what type of events occurred.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must produce audit records containing information to establish what type of events occurred.

examples/modules/application-layer-gateway/main.tf:1-82 has no diagnostic/audit configuration or sample records. Azure control-plane records and external diagnostic settings are unshown. Review effective logging and successful/unsuccessful samples to verify the particular event/field required by this rule; missing IaC alone does not prove audit failure.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204929 — SRG-NET-000075-ALG-000044

**The ALG must produce audit records containing information to establish when (date and time) the events occurred.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must produce audit records containing information to establish when (date and time) the events occurred.

examples/modules/application-layer-gateway/main.tf:1-82 has no diagnostic/audit configuration or sample records. Azure control-plane records and external diagnostic settings are unshown. Review effective logging and successful/unsuccessful samples to verify the particular event/field required by this rule; missing IaC alone does not prove audit failure.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204930 — SRG-NET-000076-ALG-000045

**The ALG must produce audit records containing information to establish where the events occurred.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must produce audit records containing information to establish where the events occurred.

examples/modules/application-layer-gateway/main.tf:1-82 has no diagnostic/audit configuration or sample records. Azure control-plane records and external diagnostic settings are unshown. Review effective logging and successful/unsuccessful samples to verify the particular event/field required by this rule; missing IaC alone does not prove audit failure.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204931 — SRG-NET-000077-ALG-000046

**The ALG must produce audit records containing information to establish the source of the events.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must produce audit records containing information to establish the source of the events.

examples/modules/application-layer-gateway/main.tf:1-82 has no diagnostic/audit configuration or sample records. Azure control-plane records and external diagnostic settings are unshown. Review effective logging and successful/unsuccessful samples to verify the particular event/field required by this rule; missing IaC alone does not prove audit failure.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204932 — SRG-NET-000078-ALG-000047

**The ALG must produce audit records containing information to establish the outcome of the events.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must produce audit records containing information to establish the outcome of the events.

examples/modules/application-layer-gateway/main.tf:1-82 has no diagnostic/audit configuration or sample records. Azure control-plane records and external diagnostic settings are unshown. Review effective logging and successful/unsuccessful samples to verify the particular event/field required by this rule; missing IaC alone does not prove audit failure.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204933 — SRG-NET-000079-ALG-000048

**The ALG must generate audit records containing information to establish the identity of any individual or process associated with the event.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must generate audit records containing information to establish the identity of any individual or process associated with the event.

examples/modules/application-layer-gateway/main.tf:1-82 has no diagnostic/audit configuration or sample records. Azure control-plane records and external diagnostic settings are unshown. Review effective logging and successful/unsuccessful samples to verify the particular event/field required by this rule; missing IaC alone does not prove audit failure.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204934 — SRG-NET-000088-ALG-000054

**The ALG must send an alert to, at a minimum, the information system security officer (ISSO) and system administrator (SA) when an audit processing failure occurs.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must send an alert to, at a minimum, the information system security officer (ISSO) and system administrator (SA) when an audit processing failure occurs.

examples/modules/application-layer-gateway/main.tf:1-82 declares no audit-failure alert, action group, recipient mapping or latency. Obtain effective external monitoring, named security-role recipients and simulated audit-processing/storage failure tests satisfying this rule's recipients/timing.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204936 — SRG-NET-000098-ALG-000056

**The ALG must protect audit information from unauthorized read access.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must protect audit information from unauthorized read access.

examples/modules/application-layer-gateway/main.tf:1-82 defines no audit repository/tool or effective access/retention policies. Obtain actual log/tool locations, inherited RBAC and read/write/delete restrictions plus access tests appropriate to this rule. Provider/external logging controls are unassessed.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204937 — SRG-NET-000099-ALG-000057

**The ALG must protect audit information from unauthorized modification.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must protect audit information from unauthorized modification.

examples/modules/application-layer-gateway/main.tf:1-82 defines no audit repository/tool or effective access/retention policies. Obtain actual log/tool locations, inherited RBAC and read/write/delete restrictions plus access tests appropriate to this rule. Provider/external logging controls are unassessed.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204938 — SRG-NET-000100-ALG-000058

**The ALG must protect audit information from unauthorized deletion.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must protect audit information from unauthorized deletion.

examples/modules/application-layer-gateway/main.tf:1-82 defines no audit repository/tool or effective access/retention policies. Obtain actual log/tool locations, inherited RBAC and read/write/delete restrictions plus access tests appropriate to this rule. Provider/external logging controls are unassessed.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204939 — SRG-NET-000101-ALG-000059

**The ALG must protect audit tools from unauthorized access.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must protect audit tools from unauthorized access.

examples/modules/application-layer-gateway/main.tf:1-82 defines no audit repository/tool or effective access/retention policies. Obtain actual log/tool locations, inherited RBAC and read/write/delete restrictions plus access tests appropriate to this rule. Provider/external logging controls are unassessed.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204940 — SRG-NET-000102-ALG-000060

**The ALG must protect audit tools from unauthorized modification.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must protect audit tools from unauthorized modification.

examples/modules/application-layer-gateway/main.tf:1-82 defines no audit repository/tool or effective access/retention policies. Obtain actual log/tool locations, inherited RBAC and read/write/delete restrictions plus access tests appropriate to this rule. Provider/external logging controls are unassessed.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204941 — SRG-NET-000103-ALG-000061

**The ALG must protect audit tools from unauthorized deletion.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must protect audit tools from unauthorized deletion.

examples/modules/application-layer-gateway/main.tf:1-82 defines no audit repository/tool or effective access/retention policies. Obtain actual log/tool locations, inherited RBAC and read/write/delete restrictions plus access tests appropriate to this rule. Provider/external logging controls are unassessed.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204942 — SRG-NET-000131-ALG-000085

**The ALG must not have unnecessary services and functions enabled.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must not have unnecessary services and functions enabled.

examples/modules/application-layer-gateway/main.tf:50-81 enables HTTP/80 forwarding only, but approved service inventory, PPSM CAL authorization and vulnerability assessment are absent. Compare effective service/proxy inventory including managed functions against mission needs and PPSM/IAVM.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204943 — SRG-NET-000131-ALG-000086

**The ALG must be configured to remove or disable unrelated or unneeded application proxy services.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must be configured to remove or disable unrelated or unneeded application proxy services.

examples/modules/application-layer-gateway/main.tf:50-81 enables HTTP/80 forwarding only, but approved service inventory, PPSM CAL authorization and vulnerability assessment are absent. Compare effective service/proxy inventory including managed functions against mission needs and PPSM/IAVM.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204944 — SRG-NET-000132-ALG-000087

**The ALG must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

examples/modules/application-layer-gateway/main.tf:50-81 enables HTTP/80 forwarding only, but approved service inventory, PPSM CAL authorization and vulnerability assessment are absent. Compare effective service/proxy inventory including managed functions against mission needs and PPSM/IAVM.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204945 — SRG-NET-000138-ALG-000063

**The ALG providing user authentication intermediary services must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user authentication intermediary services must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204946 — SRG-NET-000138-ALG-000088

**The ALG providing user access control intermediary services must be configured with a pre-established trust relationship and mechanisms with appropriate authorities (e.g., Active Directory or AAA server) which validate user account access authorizations and privileges.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must be configured with a pre-established trust relationship and mechanisms with appropriate authorities (e.g., Active Directory or AAA server) which validate user account access authorizations and privileges.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204947 — SRG-NET-000138-ALG-000089

**The ALG providing user authentication intermediary services must restrict user authentication traffic to specific authentication server(s).**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user authentication intermediary services must restrict user authentication traffic to specific authentication server(s).

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204948 — SRG-NET-000140-ALG-000094

**The ALG providing user authentication intermediary services must use multifactor authentication for network access to non-privileged accounts.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user authentication intermediary services must use multifactor authentication for network access to non-privileged accounts.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204949 — SRG-NET-000147-ALG-000095

**The ALG providing user authentication intermediary services must implement replay-resistant authentication mechanisms for network access to nonprivileged accounts.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user authentication intermediary services must implement replay-resistant authentication mechanisms for network access to nonprivileged accounts.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204950 — SRG-NET-000164-ALG-000100

**The ALG that provides intermediary services for TLS must validate certificates used for TLS functions by performing RFC 5280-compliant certification path validation.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG that provides intermediary services for TLS must validate certificates used for TLS functions by performing RFC 5280-compliant certification path validation.

examples/modules/application-layer-gateway/main.tf:50-72 explicitly configures port 80/Http on frontend and backend; main.tf:29-82 contains no TLS listener, certificate, private-key reference, or encryption intermediary. The check's TLS/encryption/key-generation-or-storage precondition does not apply to the declared data-plane configuration; this is not approval of plaintext communications.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204951 — SRG-NET-000166-ALG-000101

**The ALG providing PKI-based user authentication intermediary services must map authenticated identities to the user account.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing PKI-based user authentication intermediary services must map authenticated identities to the user account.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204952 — SRG-NET-000169-ALG-000102

**The ALG providing user authentication intermediary services must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user authentication intermediary services must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204953 — SRG-NET-000192-ALG-000121

**The ALG providing content filtering must block outbound traffic containing known and unknown DoS attacks to protect against the use of internal information systems to launch any Denial of Service (DoS) attacks against other networks or endpoints.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must block outbound traffic containing known and unknown DoS attacks to protect against the use of internal information systems to launch any Denial of Service (DoS) attacks against other networks or endpoints.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204954 — SRG-NET-000202-ALG-000124

**The ALG must deny network communications traffic by default and allow network communications traffic by exception (i.e., deny all, permit by exception).**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must deny network communications traffic by default and allow network communications traffic by exception (i.e., deny all, permit by exception).

examples/modules/application-layer-gateway/main.tf:45-81 defines public listener/Basic routing/empty pool; main.tf:13-18 has no NSG association. Approved source/destination exceptions and effective inherited network policy are unknown. Review authorized flows, effective network/WAF rules and allow/deny tests; HTTP listener alone neither proves deny-by-default on both interfaces nor a known unauthorized flow.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204955 — SRG-NET-000213-ALG-000107

**The ALG must terminate all network connections associated with a communications session at the end of the session, or as follows: for in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity; and for user sessions (non-privileged session), the session must be terminated after 15 minutes of inactivity.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must terminate all network connections associated with a communications session at the end of the session, or as follows: for in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity; and for user sessions (non-privileged session), the session must be terminated after 15 minutes of inactivity.

examples/modules/application-layer-gateway/main.tf:64 request_timeout=20 is backend HTTP request timeout, not evidence of session-idle termination. Obtain actual session lifetime settings and tests for teardown and 10-/15-minute management/user inactivity.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204956 — SRG-NET-000228-ALG-000108

**The ALG must detect, at a minimum, mobile code that is unsigned or exhibiting unusual behavior, has not undergone a risk assessment, or is prohibited for use based on a risk assessment.**

Status: `open` · Severity: medium

Requirement: The ALG must detect, at a minimum, mobile code that is unsigned or exhibiting unusual behavior, has not undergone a risk assessment, or is prohibited for use based on a risk assessment.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 and main.tf:59-81 implements Basic HTTP forwarding with no mobile-code inspection, signature/nonsignature malware scanner or detection/eradication path. These unconditional controls apply even though separately conditional content-filtering controls are N/A. Add appropriate malware inspection and validate detection/eradication against approved policy.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204957 — SRG-NET-000230-ALG-000113

**The ALG must protect the authenticity of communications sessions.**

Status: `open` · Severity: medium

Requirement: The ALG must protect the authenticity of communications sessions.

examples/modules/application-layer-gateway/main.tf:50-52 exposes port 80; backend_http_settings uses port=80/protocol=Http (main.tf:59-64); http_listener uses protocol=Http (main.tf:67-71). Both declared legs lack cryptographic peer/session authentication and transport integrity; Basic forwarding (main.tf:74-81) adds none. Configure authenticated protected sessions on both legs and validate session authenticity.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204958 — SRG-NET-000231-ALG-000114

**The ALG must invalidate session identifiers upon user logout or other session termination.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must invalidate session identifiers upon user logout or other session termination.

examples/modules/application-layer-gateway/main.tf:61 disables cookie affinity; main.tf:67-81 forwards HTTP without defining user-session identifier generation/invalidation or authenticator caching. Obtain deployed session/auth architecture, application/management settings, logout/cache-expiry tests and relevant RNG validation. Disabled affinity does not prove compliance.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: Y
```

### V-204959 — SRG-NET-000233-ALG-000115

**The ALG must recognize only system-generated session identifiers.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must recognize only system-generated session identifiers.

examples/modules/application-layer-gateway/main.tf:61 disables cookie affinity; main.tf:67-81 forwards HTTP without defining user-session identifier generation/invalidation or authenticator caching. Obtain deployed session/auth architecture, application/management settings, logout/cache-expiry tests and relevant RNG validation. Disabled affinity does not prove compliance.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: Y
```

### V-204960 — SRG-NET-000234-ALG-000116

**The ALG must generate unique session identifiers using a FIPS 140-2 approved random number generator.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must generate unique session identifiers using a FIPS 140-2 approved random number generator.

examples/modules/application-layer-gateway/main.tf:61 disables cookie affinity; main.tf:67-81 forwards HTTP without defining user-session identifier generation/invalidation or authenticator caching. Obtain deployed session/auth architecture, application/management settings, logout/cache-expiry tests and relevant RNG validation. Disabled affinity does not prove compliance.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: Y
```

### V-204961 — SRG-NET-000235-ALG-000118

**The ALG must fail to a secure state upon failure of initialization, shutdown, or abort actions.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must fail to a secure state upon failure of initialization, shutdown, or abort actions.

examples/modules/application-layer-gateway/main.tf:34-38 capacity=2 does not specify failure transitions, restart policy restoration or diagnostic persistence. Obtain managed-service fail-secure/recovery documentation and failure/restart tests.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204962 — SRG-NET-000236-ALG-000119

**In the event of a system failure of the ALG function, the ALG must save diagnostic information, log system messages, and load the most current security policies, rules, and signatures when restarted.**

Status: `not_reviewed` · Severity: medium

Requirement: In the event of a system failure of the ALG function, the ALG must save diagnostic information, log system messages, and load the most current security policies, rules, and signatures when restarted.

examples/modules/application-layer-gateway/main.tf:34-38 capacity=2 does not specify failure transitions, restart policy restoration or diagnostic persistence. Obtain managed-service fail-secure/recovery documentation and failure/restart tests.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204963 — SRG-NET-000246-ALG-000132

**The ALG providing content filtering must update malicious code protection mechanisms and signature definitions whenever new releases are available in accordance with organizational configuration management policy.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must update malicious code protection mechanisms and signature definitions whenever new releases are available in accordance with organizational configuration management policy.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204964 — SRG-NET-000248-ALG-000133

**The ALG providing content filtering must be configured to perform real-time scans of files from external sources at network entry/exit points as they are downloaded and prior to being opened or executed.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must be configured to perform real-time scans of files from external sources at network entry/exit points as they are downloaded and prior to being opened or executed.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204965 — SRG-NET-000249-ALG-000134

**The ALG providing content filtering must block malicious code upon detection.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must block malicious code upon detection.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204966 — SRG-NET-000249-ALG-000145

**The ALG providing content filtering must delete or quarantine malicious code in response to malicious code detection.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must delete or quarantine malicious code in response to malicious code detection.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204967 — SRG-NET-000249-ALG-000146

**The ALG providing content filtering must send an immediate (within seconds) alert to the system administrator, at a minimum, in response to malicious code detection.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must send an immediate (within seconds) alert to the system administrator, at a minimum, in response to malicious code detection.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204968 — SRG-NET-000251-ALG-000131

**The ALG providing content filtering must update malicious code protection mechanisms and signature definitions whenever new releases are available in accordance with organizational configuration management procedures.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must update malicious code protection mechanisms and signature definitions whenever new releases are available in accordance with organizational configuration management procedures.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204969 — SRG-NET-000273-ALG-000129

**The ALG must generate error messages that provide the information necessary for corrective actions without revealing information that could be exploited by adversaries.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must generate error messages that provide the information necessary for corrective actions without revealing information that could be exploited by adversaries.

examples/modules/application-layer-gateway/main.tf:59-81 configures HTTP forwarding without custom error handling/validation policy. Standard_v2 does not prove absence of built-in parsing/validation. Review provider protocol-validation/error behavior, effective settings, malformed-input/response tests, approved exceptions and disclosure recipients as relevant to each rule.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-204970 — SRG-NET-000280-ALG-000080

**The ALG that is part of a CDS must enforce information flow control based on organization-defined metadata.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204971 — SRG-NET-000280-ALG-000081

**The ALG that is part of a CDS must block the transfer of data with malformed security attribute metadata structures.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204972 — SRG-NET-000282-ALG-000071

**The ALG that is part of a CDS must decompose information into organization-defined, policy-relevant subcomponents for submission to policy enforcement mechanisms before transferring information between different security domains.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204973 — SRG-NET-000283-ALG-000072

**The ALG that is part of a CDS, when transferring information between different security domains, must implement organization-defined security policy filters requiring fully enumerated formats that restrict data structure and content.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204974 — SRG-NET-000284-ALG-000073

**The ALG that is part of a CDS, when transferring information between different security domains, must examine the information for the presence of organization-defined unsanctioned information.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204975 — SRG-NET-000285-ALG-000074

**The ALG that is part of a CDS must prohibit the transfer of unsanctioned information in accordance with the security policy when transferring information between different security domains.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204976 — SRG-NET-000288-ALG-000109

**The ALG providing content filtering must block or restrict detected prohibited mobile code.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must block or restrict detected prohibited mobile code.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204977 — SRG-NET-000289-ALG-000110

**The ALG providing content filtering must prevent the download of prohibited mobile code.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must prevent the download of prohibited mobile code.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204978 — SRG-NET-000313-ALG-000010

**The ALG providing intermediary services for remote access communications traffic must control remote access methods.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG providing intermediary services for remote access communications traffic must control remote access methods.

examples/modules/application-layer-gateway/main.tf:45-81 configures a public HTTP reverse proxy with empty backend pool; eventual workload/remote-access role is unknown. Obtain remote-access architecture/service inventory, approved methods, monitoring/disconnection tests and applicable cryptographic evidence. If this listener carries remote-access sessions, explicit Http (main.tf:63,71) cannot supply required confidentiality/integrity; applicability is unresolved.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: Y
```

### V-204979 — SRG-NET-000314-ALG-000013

**The ALG providing intermediary services for remote access communications traffic must provide the capability to immediately disconnect or disable remote access to the information system.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG providing intermediary services for remote access communications traffic must provide the capability to immediately disconnect or disable remote access to the information system.

examples/modules/application-layer-gateway/main.tf:45-81 configures a public HTTP reverse proxy with empty backend pool; eventual workload/remote-access role is unknown. Obtain remote-access architecture/service inventory, approved methods, monitoring/disconnection tests and applicable cryptographic evidence. If this listener carries remote-access sessions, explicit Http (main.tf:63,71) cannot supply required confidentiality/integrity; applicability is unresolved.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: Y
```

### V-204980 — SRG-NET-000318-ALG-000014

**To protect against data mining, the ALG providing content filtering must prevent code injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.**

Status: `not_applicable` · Severity: medium

Requirement: To protect against data mining, the ALG providing content filtering must prevent code injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204981 — SRG-NET-000318-ALG-000151

**To protect against data mining, the ALG providing content filtering must prevent code injection attacks launched against application objects including, at a minimum, application URLs and application code.**

Status: `not_applicable` · Severity: medium

Requirement: To protect against data mining, the ALG providing content filtering must prevent code injection attacks launched against application objects including, at a minimum, application URLs and application code.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204982 — SRG-NET-000318-ALG-000152

**To protect against data mining, the ALG providing content filtering must prevent SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields.**

Status: `not_applicable` · Severity: medium

Requirement: To protect against data mining, the ALG providing content filtering must prevent SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204983 — SRG-NET-000319-ALG-000015

**To protect against data mining, the ALG providing content filtering must detect code injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.**

Status: `not_applicable` · Severity: medium

Requirement: To protect against data mining, the ALG providing content filtering must detect code injection attacks from being launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204984 — SRG-NET-000319-ALG-000020

**To protect against data mining, the ALG providing content filtering must detect SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields.**

Status: `not_applicable` · Severity: medium

Requirement: To protect against data mining, the ALG providing content filtering must detect SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204985 — SRG-NET-000319-ALG-000153

**To protect against data mining, the ALG providing content filtering as part of its intermediary services must detect code injection attacks launched against application objects including, at a minimum, application URLs and application code.**

Status: `not_applicable` · Severity: medium

Requirement: To protect against data mining, the ALG providing content filtering as part of its intermediary services must detect code injection attacks launched against application objects including, at a minimum, application URLs and application code.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204986 — SRG-NET-000323-ALG-000067

**The ALG that is part of a CDS must use source and destination security attributes associated with organization-defined information, source, and/or destination objects to enforce organization-defined information flow control policies as a basis for flow control decisions.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204987 — SRG-NET-000324-ALG-000070

**The ALG that is part of a CDS, when transferring information between different security domains, must use organization-defined data type identifiers to validate data essential for information flow decisions.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204988 — SRG-NET-000325-ALG-000075

**The ALG that is part of a CDS must uniquely identify and authenticate source by organization, system, application, and/or individual for information transfer.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204989 — SRG-NET-000326-ALG-000076

**The ALG that is part of a CDS must uniquely identify and authenticate destination by organization, system, application, and/or individual for information transfer.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204991 — SRG-NET-000328-ALG-000078

**The ALG that is part of a CDS, when transferring information between different security domains, must apply the same security policy filtering to metadata as it applies to data payloads.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204992 — SRG-NET-000329-ALG-000084

**The ALG that is part of a CDS must enforce the use of human reviews for organization-defined information flows under organization-defined conditions.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204993 — SRG-NET-000331-ALG-000041

**The ALG providing user access control intermediary services must provide the capability for authorized users to select a user session to capture or view.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must provide the capability for authorized users to select a user session to capture or view.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204995 — SRG-NET-000334-ALG-000050

**The ALG must off-load audit records onto a centralized log server.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must off-load audit records onto a centralized log server.

examples/modules/application-layer-gateway/main.tf:1-82 has no azurerm_monitor_diagnostic_setting or central destination. External policy-assigned settings/delivery are unknown. Obtain effective diagnostics, centralized receipt samples and latency evidence (real time for V-205045); source omission alone does not prove operational noncompliance.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204996 — SRG-NET-000335-ALG-000053

**The ALG must provide an immediate real-time alert to, at a minimum, the SCA and ISSO, of all audit failure events where the detection and/or prevention function is unable to write events to either local storage or the centralized server.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must provide an immediate real-time alert to, at a minimum, the SCA and ISSO, of all audit failure events where the detection and/or prevention function is unable to write events to either local storage or the centralized server.

examples/modules/application-layer-gateway/main.tf:1-82 declares no audit-failure alert, action group, recipient mapping or latency. Obtain effective external monitoring, named security-role recipients and simulated audit-processing/storage failure tests satisfying this rule's recipients/timing.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-204997 — SRG-NET-000337-ALG-000096

**The ALG providing user authentication intermediary services must require users to reauthenticate when organization-defined circumstances or situations require reauthentication.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user authentication intermediary services must require users to reauthenticate when organization-defined circumstances or situations require reauthentication.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204998 — SRG-NET-000339-ALG-000090

**The ALG providing user authentication intermediary services must implement multifactor authentication for remote access to nonprivileged accounts such that one of the factors is provided by a device separate from the system gaining access.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user authentication intermediary services must implement multifactor authentication for remote access to nonprivileged accounts such that one of the factors is provided by a device separate from the system gaining access.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-204999 — SRG-NET-000340-ALG-000091

**The ALG providing user authentication intermediary services must implement multifactor authentication for remote access to privileged accounts such that one of the factors is provided by a device separate from the system gaining access.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user authentication intermediary services must implement multifactor authentication for remote access to privileged accounts such that one of the factors is provided by a device separate from the system gaining access.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205000 — SRG-NET-000344-ALG-000098

**The ALG must prohibit the use of cached authenticators after an organization-defined time period.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must prohibit the use of cached authenticators after an organization-defined time period.

examples/modules/application-layer-gateway/main.tf:61 disables cookie affinity; main.tf:67-81 forwards HTTP without defining user-session identifier generation/invalidation or authenticator caching. Obtain deployed session/auth architecture, application/management settings, logout/cache-expiry tests and relevant RNG validation. Disabled affinity does not prove compliance.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: Y
```

### V-205001 — SRG-NET-000345-ALG-000099

**The ALG providing user authentication intermediary services using PKI-based user authentication must implement a local cache of revocation data to support path discovery and validation in case of the inability to access revocation information via the network.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user authentication intermediary services using PKI-based user authentication must implement a local cache of revocation data to support path discovery and validation in case of the inability to access revocation information via the network.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205002 — SRG-NET-000349-ALG-000106

**The ALG providing user authentication intermediary services must conform to Federal Identity, Credential, and Access Management (FICAM)-issued profiles.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user authentication intermediary services must conform to Federal Identity, Credential, and Access Management (FICAM)-issued profiles.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205003 — SRG-NET-000355-ALG-000117

**The ALG providing user authentication intermediary services using PKI-based user authentication must only accept end entity certificates issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs) for the establishment of protected sessions.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user authentication intermediary services using PKI-based user authentication must only accept end entity certificates issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs) for the establishment of protected sessions.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205004 — SRG-NET-000362-ALG-000112

**The ALG providing content filtering must protect against known and unknown types of Denial of Service (DoS) attacks by employing rate-based attack prevention behavior analysis.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must protect against known and unknown types of Denial of Service (DoS) attacks by employing rate-based attack prevention behavior analysis.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205005 — SRG-NET-000362-ALG-000120

**The ALG must implement load balancing to limit the effects of known and unknown types of Denial of Service (DoS) attacks.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must implement load balancing to limit the effects of known and unknown types of Denial of Service (DoS) attacks.

examples/modules/application-layer-gateway/main.tf:34-38 capacity=2, but backend_address_pool (main.tf:55-57) is empty. Basic routing (main.tf:74-81) demonstrates no load distribution/DoS effect. Obtain populated topology and load/DoS tests; capacity alone is insufficient.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-205006 — SRG-NET-000362-ALG-000126

**The ALG providing content filtering must protect against known types of Denial of Service (DoS) attacks by employing signatures.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must protect against known types of Denial of Service (DoS) attacks by employing signatures.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205007 — SRG-NET-000362-ALG-000155

**The ALG providing content filtering must protect against or limit the effects of known and unknown types of Denial of Service (DoS) attacks by employing pattern recognition pre-processors.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must protect against or limit the effects of known and unknown types of Denial of Service (DoS) attacks by employing pattern recognition pre-processors.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205008 — SRG-NET-000364-ALG-000122

**The ALG must only allow incoming communications from organization-defined authorized sources routed to organization-defined authorized destinations.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must only allow incoming communications from organization-defined authorized sources routed to organization-defined authorized destinations.

examples/modules/application-layer-gateway/main.tf:45-81 defines public listener/Basic routing/empty pool; main.tf:13-18 has no NSG association. Approved source/destination exceptions and effective inherited network policy are unknown. Review authorized flows, effective network/WAF rules and allow/deny tests; HTTP listener alone neither proves deny-by-default on both interfaces nor a known unauthorized flow.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-205009 — SRG-NET-000365-ALG-000123

**The ALG must fail securely in the event of an operational failure.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must fail securely in the event of an operational failure.

examples/modules/application-layer-gateway/main.tf:34-38 capacity=2 does not specify failure transitions, restart policy restoration or diagnostic persistence. Obtain managed-service fail-secure/recovery documentation and failure/restart tests.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-205010 — SRG-NET-000370-ALG-000125

**The ALG must identify and log internal users associated with denied outgoing communications traffic posing a threat to external information systems.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must identify and log internal users associated with denied outgoing communications traffic posing a threat to external information systems.

examples/modules/application-layer-gateway/main.tf:45-81 defines inbound reverse-proxy routing only, with no documented egress inspection, internal-user attribution or denied-flow samples. Obtain deployment egress topology, identification mechanism and denied outbound threat records to determine applicability/compliance.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: Y
```

### V-205011 — SRG-NET-000380-ALG-000128

**The ALG must behave in a predictable and documented manner that reflects organizational and system objectives when invalid inputs are received.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must behave in a predictable and documented manner that reflects organizational and system objectives when invalid inputs are received.

examples/modules/application-layer-gateway/main.tf:59-81 configures HTTP forwarding without custom error handling/validation policy. Standard_v2 does not prove absence of built-in parsing/validation. Review provider protocol-validation/error behavior, effective settings, malformed-input/response tests, approved exceptions and disclosure recipients as relevant to each rule.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-205012 — SRG-NET-000383-ALG-000135

**The ALG providing content filtering must be configured to integrate with a system-wide intrusion detection system.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must be configured to integrate with a system-wide intrusion detection system.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205013 — SRG-NET-000384-ALG-000136

**The ALG providing content filtering must detect use of network services that have not been authorized or approved by the ISSM and ISSO, at a minimum.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must detect use of network services that have not been authorized or approved by the ISSM and ISSO, at a minimum.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205014 — SRG-NET-000385-ALG-000137

**The ALG providing content filtering must generate a log record when unauthorized network services are detected.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must generate a log record when unauthorized network services are detected.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205015 — SRG-NET-000385-ALG-000138

**The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when unauthorized network services are detected.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when unauthorized network services are detected.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205016 — SRG-NET-000390-ALG-000139

**The ALG providing content filtering must continuously monitor inbound communications traffic crossing internal security boundaries for unusual or unauthorized activities or conditions.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must continuously monitor inbound communications traffic crossing internal security boundaries for unusual or unauthorized activities or conditions.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205017 — SRG-NET-000391-ALG-000140

**The ALG providing content filtering must continuously monitor outbound communications traffic crossing internal security boundaries for unusual/unauthorized activities or conditions.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must continuously monitor outbound communications traffic crossing internal security boundaries for unusual/unauthorized activities or conditions.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205018 — SRG-NET-000392-ALG-000141

**The ALG providing content filtering must send an alert to, at a minimum, the ISSO and ISSM when detection events occur.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must send an alert to, at a minimum, the ISSO and ISSM when detection events occur.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205019 — SRG-NET-000392-ALG-000142

**The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when threats identified by authoritative sources (e.g., IAVMs or CTOs) are detected.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when threats identified by authoritative sources (e.g., IAVMs or CTOs) are detected.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205020 — SRG-NET-000392-ALG-000143

**The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when root level intrusion events which provide unauthorized privileged access are detected.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when root level intrusion events which provide unauthorized privileged access are detected.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205021 — SRG-NET-000392-ALG-000147

**The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when user level intrusions which provide non-privileged access are detected.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when user level intrusions which provide non-privileged access are detected.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205022 — SRG-NET-000392-ALG-000148

**The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when denial of service incidents are detected.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when denial of service incidents are detected.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205023 — SRG-NET-000392-ALG-000149

**The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when new active propagation of malware infecting
DoD systems or malicious code adversely affecting the operations and/or security
of DoD systems is detected.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing content filtering must generate an alert to, at a minimum, the ISSO and ISSM when new active propagation of malware infecting
DoD systems or malicious code adversely affecting the operations and/or security
of DoD systems is detected.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 for azurerm_application_gateway.example, with Basic HTTP forwarding (main.tf:59-81) and no WAF/content-filter configuration. The supplied check expressly excludes gateways that do not perform content filtering. This module-scoped N/A does not waive unconditional ALG inspection and malware requirements, assessed separately.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205024 — SRG-NET-000393-ALG-000144

**The ALG that implements spam protection mechanisms must be updated automatically.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG that implements spam protection mechanisms must be updated automatically.

examples/modules/application-layer-gateway/main.tf:50-81 defines only an HTTP port-80 listener, HTTP backend settings and Basic routing. No SMTP/spam protection or FTP intermediary is configured, so the service-specific precondition in this rule's check is absent.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205026 — SRG-NET-000400-ALG-000097

**The ALG providing user authentication intermediary services must transmit only encrypted representations of passwords.**

Status: `not_applicable` · Severity: high

Requirement: The ALG providing user authentication intermediary services must transmit only encrypted representations of passwords.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205027 — SRG-NET-000401-ALG-000127

**The ALG must check the validity of all data inputs except those specifically identified by the organization.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must check the validity of all data inputs except those specifically identified by the organization.

examples/modules/application-layer-gateway/main.tf:59-81 configures HTTP forwarding without custom error handling/validation policy. Standard_v2 does not prove absence of built-in parsing/validation. Review provider protocol-validation/error behavior, effective settings, malformed-input/response tests, approved exceptions and disclosure recipients as relevant to each rule.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-205028 — SRG-NET-000402-ALG-000130

**The ALG must reveal error messages only to the ISSO, ISSM, and SCA.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must reveal error messages only to the ISSO, ISSM, and SCA.

examples/modules/application-layer-gateway/main.tf:59-81 configures HTTP forwarding without custom error handling/validation policy. Standard_v2 does not prove absence of built-in parsing/validation. Review provider protocol-validation/error behavior, effective settings, malformed-input/response tests, approved exceptions and disclosure recipients as relevant to each rule.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-205029 — SRG-NET-000492-ALG-000027

**The ALG must generate audit records when successful/unsuccessful attempts to access security objects occur.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must generate audit records when successful/unsuccessful attempts to access security objects occur.

examples/modules/application-layer-gateway/main.tf:1-82 has no diagnostic/audit configuration or sample records. Azure control-plane records and external diagnostic settings are unshown. Review effective logging and successful/unsuccessful samples to verify the particular event/field required by this rule; missing IaC alone does not prove audit failure.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-205030 — SRG-NET-000493-ALG-000028

**The ALG that is part of a CDS must generate audit records when successful/unsuccessful attempts to access security levels occur.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-205031 — SRG-NET-000494-ALG-000029

**The ALG must generate audit records when successful/unsuccessful attempts to access categories of information (e.g., classification levels) occur.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must generate audit records when successful/unsuccessful attempts to access categories of information (e.g., classification levels) occur.

examples/modules/application-layer-gateway/main.tf:1-82 has no diagnostic/audit configuration or sample records. Azure control-plane records and external diagnostic settings are unshown. Review effective logging and successful/unsuccessful samples to verify the particular event/field required by this rule; missing IaC alone does not prove audit failure.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-205032 — SRG-NET-000495-ALG-000030

**The ALG providing user access control intermediary services must generate audit records when successful/unsuccessful attempts to modify privileges occur.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must generate audit records when successful/unsuccessful attempts to modify privileges occur.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205033 — SRG-NET-000496-ALG-000031

**The ALG must generate audit records when successful/unsuccessful attempts to modify security objects occur.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must generate audit records when successful/unsuccessful attempts to modify security objects occur.

examples/modules/application-layer-gateway/main.tf:1-82 has no diagnostic/audit configuration or sample records. Azure control-plane records and external diagnostic settings are unshown. Review effective logging and successful/unsuccessful samples to verify the particular event/field required by this rule; missing IaC alone does not prove audit failure.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-205034 — SRG-NET-000497-ALG-000032

**The ALG must generate audit records when successful/unsuccessful attempts to modify security levels occur.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must generate audit records when successful/unsuccessful attempts to modify security levels occur.

examples/modules/application-layer-gateway/main.tf:1-82 has no diagnostic/audit configuration or sample records. Azure control-plane records and external diagnostic settings are unshown. Review effective logging and successful/unsuccessful samples to verify the particular event/field required by this rule; missing IaC alone does not prove audit failure.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-205035 — SRG-NET-000498-ALG-000033

**The ALG must generate audit records when successful/unsuccessful attempts to modify categories of information (e.g., classification levels) occur.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must generate audit records when successful/unsuccessful attempts to modify categories of information (e.g., classification levels) occur.

examples/modules/application-layer-gateway/main.tf:1-82 has no diagnostic/audit configuration or sample records. Azure control-plane records and external diagnostic settings are unshown. Review effective logging and successful/unsuccessful samples to verify the particular event/field required by this rule; missing IaC alone does not prove audit failure.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-205036 — SRG-NET-000499-ALG-000034

**The ALG providing user access control intermediary services must generate audit records when successful/unsuccessful attempts to delete privileges occur.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must generate audit records when successful/unsuccessful attempts to delete privileges occur.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205037 — SRG-NET-000500-ALG-000035

**The ALG must generate audit records when successful/unsuccessful attempts to delete security levels occur.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must generate audit records when successful/unsuccessful attempts to delete security levels occur.

examples/modules/application-layer-gateway/main.tf:1-82 has no diagnostic/audit configuration or sample records. Azure control-plane records and external diagnostic settings are unshown. Review effective logging and successful/unsuccessful samples to verify the particular event/field required by this rule; missing IaC alone does not prove audit failure.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-205038 — SRG-NET-000501-ALG-000036

**The ALG must generate audit records when successful/unsuccessful attempts to delete security objects occur.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must generate audit records when successful/unsuccessful attempts to delete security objects occur.

examples/modules/application-layer-gateway/main.tf:1-82 has no diagnostic/audit configuration or sample records. Azure control-plane records and external diagnostic settings are unshown. Review effective logging and successful/unsuccessful samples to verify the particular event/field required by this rule; missing IaC alone does not prove audit failure.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-205039 — SRG-NET-000502-ALG-000037

**The ALG must generate audit records when successful/unsuccessful attempts to delete categories of information (e.g., classification levels) occur.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must generate audit records when successful/unsuccessful attempts to delete categories of information (e.g., classification levels) occur.

examples/modules/application-layer-gateway/main.tf:1-82 has no diagnostic/audit configuration or sample records. Azure control-plane records and external diagnostic settings are unshown. Review effective logging and successful/unsuccessful samples to verify the particular event/field required by this rule; missing IaC alone does not prove audit failure.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-205040 — SRG-NET-000503-ALG-000038

**The ALG providing user access control intermediary services must generate audit records when successful/unsuccessful logon attempts occur.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must generate audit records when successful/unsuccessful logon attempts occur.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205041 — SRG-NET-000505-ALG-000039

**The ALG providing user access control intermediary services must generate audit records showing starting and ending time for user access to the system.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must generate audit records showing starting and ending time for user access to the system.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205042 — SRG-NET-000510-ALG-000025

**The ALG providing encryption intermediary services must implement NIST FIPS-validated cryptography to generate cryptographic hashes.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing encryption intermediary services must implement NIST FIPS-validated cryptography to generate cryptographic hashes.

examples/modules/application-layer-gateway/main.tf:50-72 explicitly configures port 80/Http on frontend and backend; main.tf:29-82 contains no TLS listener, certificate, private-key reference, or encryption intermediary. The check's TLS/encryption/key-generation-or-storage precondition does not apply to the declared data-plane configuration; this is not approval of plaintext communications.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205043 — SRG-NET-000510-ALG-000040

**The ALG providing encryption intermediary services must implement NIST FIPS-validated cryptography for digital signatures.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing encryption intermediary services must implement NIST FIPS-validated cryptography for digital signatures.

examples/modules/application-layer-gateway/main.tf:50-72 explicitly configures port 80/Http on frontend and backend; main.tf:29-82 contains no TLS listener, certificate, private-key reference, or encryption intermediary. The check's TLS/encryption/key-generation-or-storage precondition does not apply to the declared data-plane configuration; this is not approval of plaintext communications.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205044 — SRG-NET-000510-ALG-000111

**The ALG providing encryption intermediary services must use NIST FIPS-validated cryptography to implement encryption services.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing encryption intermediary services must use NIST FIPS-validated cryptography to implement encryption services.

examples/modules/application-layer-gateway/main.tf:50-72 explicitly configures port 80/Http on frontend and backend; main.tf:29-82 contains no TLS listener, certificate, private-key reference, or encryption intermediary. The check's TLS/encryption/key-generation-or-storage precondition does not apply to the declared data-plane configuration; this is not approval of plaintext communications.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205045 — SRG-NET-000511-ALG-000051

**The ALG must off-load audit records onto a centralized log server in real time.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must off-load audit records onto a centralized log server in real time.

examples/modules/application-layer-gateway/main.tf:1-82 has no azurerm_monitor_diagnostic_setting or central destination. External policy-assigned settings/delivery are unknown. Obtain effective diagnostics, centralized receipt samples and latency evidence (real time for V-205045); source omission alone does not prove operational noncompliance.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-205046 — SRG-NET-000511-ALG-000052

**The ALG that is part of a CDS must have the capability to implement journaling.**

Status: `not_reviewed` · Severity: medium

examples/modules/application-layer-gateway/main.tf:6-18 and main.tf:29-82 declare one VNet, one gateway subnet, and a public HTTP gateway. No mission or authorization-boundary evidence establishes whether the gateway is part of a cross-domain solution (CDS). Obtain the approved architecture and CDS designation, then apply this rule’s specific check. If not part of a CDS, the explicit check exclusion applies; absent CDS configuration alone is insufficient to establish mission applicability.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-205047 — SRG-NET-000512-ALG-000062

**The ALG must be configured in accordance with the security configuration settings based on DoD security policy and technology-specific security best practices.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must be configured in accordance with the security configuration settings based on DoD security policy and technology-specific security best practices.

examples/modules/application-layer-gateway/main.tf:29-82 config and provider.tf:1-10 version constraints are supplied, but no approved DoD/technology baseline, tailoring or deployed config. Compare effective settings to approved baseline and resolve separate plaintext/inspection findings.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-205048 — SRG-NET-000512-ALG-000064

**The ALG that provides intermediary services for SMTP must inspect inbound and outbound SMTP and Extended SMTP communications traffic for protocol compliance and protocol anomalies.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG that provides intermediary services for SMTP must inspect inbound and outbound SMTP and Extended SMTP communications traffic for protocol compliance and protocol anomalies.

examples/modules/application-layer-gateway/main.tf:50-81 defines only an HTTP port-80 listener, HTTP backend settings and Basic routing. No SMTP/spam protection or FTP intermediary is configured, so the service-specific precondition in this rule's check is absent.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205049 — SRG-NET-000512-ALG-000065

**The ALG that provides intermediary services for FTP must inspect inbound and outbound FTP communications traffic for protocol compliance and protocol anomalies.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG that provides intermediary services for FTP must inspect inbound and outbound FTP communications traffic for protocol compliance and protocol anomalies.

examples/modules/application-layer-gateway/main.tf:50-81 defines only an HTTP port-80 listener, HTTP backend settings and Basic routing. No SMTP/spam protection or FTP intermediary is configured, so the service-specific precondition in this rule's check is absent.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205050 — SRG-NET-000512-ALG-000066

**The ALG that provides intermediary services for HTTP must inspect inbound and outbound HTTP traffic for protocol compliance and protocol anomalies.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG that provides intermediary services for HTTP must inspect inbound and outbound HTTP traffic for protocol compliance and protocol anomalies.

examples/modules/application-layer-gateway/main.tf:59-81 configures HTTP forwarding without custom error handling/validation policy. Standard_v2 does not prove absence of built-in parsing/validation. Review provider protocol-validation/error behavior, effective settings, malformed-input/response tests, approved exceptions and disclosure recipients as relevant to each rule.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-205051 — SRG-NET-000513-ALG-000026

**The ALG providing user access control intermediary services must generate audit records when successful/unsuccessful attempts to access privileges occur.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must generate audit records when successful/unsuccessful attempts to access privileges occur.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205052 — SRG-NET-000514-ALG-000514

**The ALG providing user access control intermediary services must initiate a session lock after a 15-minute period of inactivity.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must initiate a session lock after a 15-minute period of inactivity.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205053 — SRG-NET-000515-ALG-000515

**The ALG providing user access control intermediary services must provide the capability for users to directly initiate a session lock.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must provide the capability for users to directly initiate a session lock.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205054 — SRG-NET-000516-ALG-000516

**The ALG providing user access control intermediary services must retain the session lock until the user reestablishes access using established identification and authentication procedures.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must retain the session lock until the user reestablishes access using established identification and authentication procedures.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205055 — SRG-NET-000517-ALG-000006

**The ALG providing user access control intermediary services must automatically terminate a user session when organization-defined conditions or trigger events that require a session disconnect occur.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must automatically terminate a user session when organization-defined conditions or trigger events that require a session disconnect occur.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205056 — SRG-NET-000518-ALG-000007

**The ALG providing user access control intermediary services must provide a logoff capability for user-initiated communications sessions.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must provide a logoff capability for user-initiated communications sessions.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205057 — SRG-NET-000519-ALG-000008

**The ALG providing user access control intermediary services must display an explicit logoff message to users indicating the reliable termination of authenticated communications sessions.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must display an explicit logoff message to users indicating the reliable termination of authenticated communications sessions.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-205058 — SRG-NET-000521-ALG-000002

**The ALG providing user access control intermediary services must conceal, via the session lock, information previously visible on the display with a publicly viewable image.**

Status: `not_applicable` · Severity: medium

Requirement: The ALG providing user access control intermediary services must conceal, via the session lock, information previously visible on the display with a publicly viewable image.

examples/modules/application-layer-gateway/main.tf:59-81 configures plain HTTP forwarding with cookie_based_affinity=Disabled, one HTTP listener and Basic routing. It implements no user authentication/access-control intermediary, login UI, user accounts, or identity-provider integration; this rule's explicit intermediary-service precondition is absent. Application and Azure administrative identity controls are outside this component scope.

```text
Responsible?
- CSP: N
- Platform: N
- Tenant: N
```

### V-263540 — SRG-NET-000700-ALG-000100

**The ALG must prevent or restrict changes to the configuration of the system under organization-defined circumstances.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must prevent or restrict changes to the configuration of the system under organization-defined circumstances.

examples/modules/application-layer-gateway/main.tf:1-82 declares gateway/network resources; provider.tf:12-15 selects Azure subscription but supplies no effective Azure RBAC, inherited policy, management locks, privileged-access conditions or approved authorization matrix. Review effective management-plane assignments, conditional access/change restrictions and approvals; omission does not prove absence in deployment.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-263541 — SRG-NET-000705-ALG-000110

**The ALG must employ organization-defined controls by type of denial of service (DoS) to achieve the DoS objective.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must employ organization-defined controls by type of denial of service (DoS) to achieve the DoS objective.

examples/modules/application-layer-gateway/main.tf:34-38 Standard_v2 capacity=2; main.tf:6-27 networking without DDoS plan. Organization-defined DoS types/objectives and inherited protection are absent. Obtain threat/objective matrix, effective Azure protection and tests; absent plan alone does not prove no protection.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-263542 — SRG-NET-000715-ALG-000120

**The ALG must implement physically or logically separate subnetworks to isolate organization-defined critical system components and functions.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must implement physically or logically separate subnetworks to isolate organization-defined critical system components and functions.

examples/modules/application-layer-gateway/main.tf:6-18 VNet 10.0.0.0/16/subnet 10.0.1.0/24; gateway attached (main.tf:40-42). Critical-component definitions, other subnetworks and isolation rules unknown. Review full topology and segmentation tests; dedicated subnet name does not prove isolation of all critical functions.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-263543 — SRG-NET-000735-ALG-000130

**The ALG must implement antispoofing mechanisms to prevent adversaries from falsifying the security attributes indicating the successful application of the security process.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must implement antispoofing mechanisms to prevent adversaries from falsifying the security attributes indicating the successful application of the security process.

examples/modules/application-layer-gateway/main.tf:59-81 HTTP forwarding has no explicit security-attribute validation; attribute types/security processes unspecified. Obtain attribute/identity/header trust design, provider/application antispoofing controls and tamper tests; plaintext separately assessed in V-204957.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: Y
```

### V-263544 — SRG-NET-000750-ALG-000140

**The ALG must include only approved trust anchors in trust stores or certificate stores managed by the organization.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must include only approved trust anchors in trust stores or certificate stores managed by the organization.

examples/modules/application-layer-gateway/main.tf:29-82 declares no TLS certificates, trust stores, keys or signature service; protocols Http (main.tf:63,71). These unconditional checks also require provider-managed/deployment crypto scope. Obtain applicable trust/key/signing inventory, ownership/safeguards and validation evidence before compliance or broader N/A.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-263545 — SRG-NET-000755-ALG-000150

**The ALG must provide protected storage for cryptographic keys with organization-defined safeguards and/or hardware protected key store.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must provide protected storage for cryptographic keys with organization-defined safeguards and/or hardware protected key store.

examples/modules/application-layer-gateway/main.tf:29-82 declares no TLS certificates, trust stores, keys or signature service; protocols Http (main.tf:63,71). These unconditional checks also require provider-managed/deployment crypto scope. Obtain applicable trust/key/signing inventory, ownership/safeguards and validation evidence before compliance or broader N/A.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-263546 — SRG-NET-000760-ALG-000160

**The ALG must establish organization-defined alternate communications paths for system operations organizational command and control.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must establish organization-defined alternate communications paths for system operations organizational command and control.

examples/modules/application-layer-gateway/main.tf:45-48 single public frontend; capacity=2 (main.tf:34-38) is not alternate communications path. Organization-defined command/control paths and external management design unknown. Obtain alternate-path requirements/design and failover evidence.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-263547 — SRG-NET-000765-ALG-000170

**The ALG must implement signature based and/or nonsignature based malicious code protection mechanisms at system entry and exit points to detect and eradicate malicious code.**

Status: `open` · Severity: medium

Requirement: The ALG must implement signature based and/or nonsignature based malicious code protection mechanisms at system entry and exit points to detect and eradicate malicious code.

examples/modules/application-layer-gateway/main.tf:34-38 selects Standard_v2 and main.tf:59-81 implements Basic HTTP forwarding with no mobile-code inspection, signature/nonsignature malware scanner or detection/eradication path. These unconditional controls apply even though separately conditional content-filtering controls are N/A. Add appropriate malware inspection and validate detection/eradication against approved policy.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-263548 — SRG-NET-000770-ALG-000180

**The ALG must configure malicious code protection mechanisms to send alerts to organization-defined personnel in response to malicious code detection.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must configure malicious code protection mechanisms to send alerts to organization-defined personnel in response to malicious code detection.

examples/modules/application-layer-gateway/main.tf:1-82 has no malware-alert routing/designated recipients. Obtain external malware/monitoring integrations, personnel mapping and detection-to-alert tests. Missing module malware mechanism is V-263547; external alert delivery remains unverified.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: N
```

### V-278954 — SRG-NET-000226-ALG-000108

**The ALG must validate the integrity of transmitted security attributes.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must validate the integrity of transmitted security attributes.

examples/modules/application-layer-gateway/main.tf:59-81 HTTP forwarding has no explicit security-attribute validation; attribute types/security processes unspecified. Obtain attribute/identity/header trust design, provider/application antispoofing controls and tamper tests; plaintext separately assessed in V-204957.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: Y
```

### V-278955 — SRG-NET-000352-ALG-000110

**The ALG must use cryptographic algorithms approved by NSA to protect NSS when transporting classified traffic across an unclassified network.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must use cryptographic algorithms approved by NSA to protect NSS when transporting classified traffic across an unclassified network.

examples/modules/application-layer-gateway/main.tf:45-81 public HTTP proxy but no classification, NSS boundary or classified remote-access mission. Obtain classification/authorization boundary; if applicable review approved NSA crypto architecture and operational evidence. Do not infer classified or unclassified mission from names.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: Y
```

### V-278956 — SRG-NET-000565-ALG-000010

**The ALG must be configured to use cryptographic algorithms approved by NSA to protect NSS for remote access to a classified network.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must be configured to use cryptographic algorithms approved by NSA to protect NSS for remote access to a classified network.

examples/modules/application-layer-gateway/main.tf:45-81 public HTTP proxy but no classification, NSS boundary or classified remote-access mission. Obtain classification/authorization boundary; if applicable review approved NSA crypto architecture and operational evidence. Do not infer classified or unclassified mission from names.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: Y
```

### V-278957 — SRG-NET-000570-ALG-000015

**The ALG must use a FIPS-validated cryptographic module to provision digital signatures.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must use a FIPS-validated cryptographic module to provision digital signatures.

examples/modules/application-layer-gateway/main.tf:29-82 declares no TLS certificates, trust stores, keys or signature service; protocols Http (main.tf:63,71). These unconditional checks also require provider-managed/deployment crypto scope. Obtain applicable trust/key/signing inventory, ownership/safeguards and validation evidence before compliance or broader N/A.

```text
Responsible?
- CSP: Y
- Platform: Y
- Tenant: N
```

### V-278958 — SRG-NET-000575-ALG-000020

**The ALG must use a FIPS-validated cryptographic module to implement encryption services for unclassified information requiring confidentiality.**

Status: `not_reviewed` · Severity: medium

Requirement: The ALG must use a FIPS-validated cryptographic module to implement encryption services for unclassified information requiring confidentiality.

examples/modules/application-layer-gateway/main.tf:63,71 Http both legs; benchmark check specifically concerns transmitted passwords; empty backend pool (main.tf:55-57) identifies no workload/password flow. Obtain data/password-flow inventory and approved confidentiality requirements, then capture/configuration evidence. Passwords or confidentiality-required data on these plaintext legs would fail.

```text
Responsible?
- CSP: N
- Platform: Y
- Tenant: Y
```
