---
name: srg-stig-compliance
description: Generate a checklist (.cklb) file for the Application Layer Gateway (ALG) Security Requirements Guide (SRG). Use this skill when evaluating Infrastructure-as-Code (IaC) modules for compliance with the ALG SRG.
---

**Step 1.** Use `read_xccdf_file` to extract the security requirements from the ALG SRG. Each requirement returned includes `rule_id`, `version`, `severity`, `title`, `description`, `check`, `fix`, and `cci`.

**Step 2.** For each requirement, review the provided IaC module(s) and determine a status:

- `not_a_finding` — the IaC clearly implements the control. Cite the specific resource, file, and setting that satisfies it.
- `open` — the IaC is in scope for the control but does not satisfy it. Cite what's missing or misconfigured.
- `not_applicable` — the control does not apply to this IaC's scope (e.g. it governs a component not present in the module). State why.
- `not_reviewed` — the control cannot be assessed from IaC alone (e.g. it's a runtime, operational, or procedural control). Note what would be needed to assess it (e.g. runtime config, log review, interview).

Only use `not_a_finding` or `open` when the IaC gives direct, citable evidence either way. Do not guess: if evidence is ambiguous or absent, use `not_reviewed` rather than assuming compliance or non-compliance.

For each requirement, build a rule dict carrying its assessment. Reuse the requirement's own fields (`rule_id`, `version`, `title`, `description`, `check`, `fix`, `cci`) and add:

- `status` — one of the four values above
- `finding_details` — the evidence supporting the status (resource/file/line, or the gap found)
- `comments` — a stakeholder responsibility block in the format below. Use `N` as the default value. Only use `Y` when the stakeholder is responsible for remediating or addressing the requirement. CSP is the cloud service provider. Platform represents the people operating and maintaining the platform. Tenant represents people using the platform (e.g., people who are paying the platform team to hosting their application).

```
Responsible?
- CSP: N
- Platform: N
- Tenant: N

```

**Step 3.** Use `write_cklb_file` to generate the checklist, passing the full list of assessed rule dicts from Step 2 as `rules`. It accepts the requirement field names directly (`version`, `title`, `description`, `check`, `fix`, `cci`) alongside `status`, `finding_details`, and `comments` — no remapping needed. Set `title` and `stig_name` to identify the ALG SRG, and pass `target_data` if the IaC module's target (host, environment) is known.

If any requirement was left without an explicit `status`, `write_cklb_file` will default it to `not_reviewed` and report how many rules were defaulted — treat that as a signal that Step 2 was incomplete, not as an acceptable final state.
