# Standard library imports.
import json
from pathlib import Path
from typing import Any
from uuid import uuid4

VALID_STATUSES = {
    "not_reviewed",
    "open",
    "not_a_finding",
    "not_applicable",
}

# Maps each output field to the set of input keys that may supply it,
# checked in order. This lets rules coming straight from read_xccdf_file
# (which uses rule_id/version/title/description/check/fix/cci) or from
# hand-built dicts (which may use the writer's own field names) both work
# without the caller having to remap keys first.
FIELD_ALIASES: dict[str, tuple[str, ...]] = {
    "rule_version": ("rule_version", "version"),
    "rule_title": ("rule_title", "title"),
    "discussion": ("discussion", "description"),
    "check_content": ("check_content", "check"),
    "fix_text": ("fix_text", "fix"),
    "ccis": ("ccis", "cci"),
}


def _get(rule: dict[str, Any], *keys: str, default: Any = "") -> Any:
    for key in keys:
        if key in rule and rule[key] not in (None, ""):
            return rule[key]
    return default


def write_cklb_file(
    path: str,
    title: str,
    stig_name: str,
    rules: list[dict[str, Any]],
    release_info: str = "",
    target_data: dict[str, str] | None = None,
) -> str:
    """Write assessment results to a CKLB checklist file.

    Args:
        path: Path where the CKLB file will be written.
        title: Title of the checklist.
        stig_name: Name of the SRG or STIG.
        rules: Assessed SRG or STIG rules. Each rule may use either this
            function's own field names (rule_version, rule_title,
            discussion, check_content, fix_text, ccis) or the field names
            returned by read_xccdf_file (version, title, description,
            check, fix, cci) — both are accepted interchangeably.
        release_info: Release information for the SRG or STIG.
        target_data: Information about the assessment target.

    Returns:
        Path to the generated CKLB file.

    Raises:
        ValueError: If a rule contains an invalid status.
    """
    output_path = Path(path)

    if output_path.suffix != ".cklb":
        output_path = output_path.with_suffix(".cklb")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    checklist_rules = []
    defaulted_count = 0

    for rule in rules:
        status = rule.get("status", "not_reviewed")

        if status not in VALID_STATUSES:
            raise ValueError(
                f"Invalid status '{status}'. Expected one of: {sorted(VALID_STATUSES)}"
            )

        if "status" not in rule:
            defaulted_count += 1

        checklist_rules.append(
            {
                "rule_id": rule.get("rule_id", ""),
                "group_id": rule.get("group_id", ""),
                "rule_version": _get(rule, *FIELD_ALIASES["rule_version"]),
                "severity": rule.get("severity", ""),
                "status": status,
                "rule_title": _get(rule, *FIELD_ALIASES["rule_title"]),
                "discussion": _get(rule, *FIELD_ALIASES["discussion"]),
                "check_content": _get(rule, *FIELD_ALIASES["check_content"]),
                "fix_text": _get(rule, *FIELD_ALIASES["fix_text"]),
                "finding_details": rule.get("finding_details", ""),
                "comments": rule.get("comments", ""),
                "ccis": _get(rule, *FIELD_ALIASES["ccis"], default=[]),
            }
        )

    checklist = {
        "title": title,
        "id": str(uuid4()),
        "cklb_version": "1",
        "target_data": target_data
        or {
            "host_name": "",
            "ip_address": "",
            "fqdn": "",
            "mac_address": "",
        },
        "stigs": [
            {
                "stig_name": stig_name,
                "release_info": release_info,
                "rules": checklist_rules,
            }
        ],
    }

    output_path.write_text(
        json.dumps(checklist, indent=2),
        encoding="utf-8",
    )

    if defaulted_count:
        print(
            f"Warning: {defaulted_count} of {len(checklist_rules)} rule(s) had "
            f"no explicit status and defaulted to 'not_reviewed'."
        )

    return str(output_path)
