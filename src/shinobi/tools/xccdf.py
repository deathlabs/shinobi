from pathlib import Path
from typing import TypedDict

from defusedxml import ElementTree


class Requirement(TypedDict):
    group_id: str | None
    rule_id: str | None
    version: str
    severity: str | None
    title: str
    description: str
    check: str
    fix: str
    cci: list[str]


_SUPPORTED_NAMESPACES = [
    "http://checklists.nist.gov/xccdf/1.2",
    "http://checklists.nist.gov/xccdf/1.1",
]


class XccdfParseError(Exception):
    """Raised when an XCCDF file cannot be parsed or contains no requirements."""


def _detect_namespace(root: ElementTree.Element) -> str:
    """Determine the XCCDF namespace URI from the root element's tag."""
    if root.tag.startswith("{"):
        uri = root.tag[1:].split("}", 1)[0]
        if uri in _SUPPORTED_NAMESPACES:
            return uri

    raise XccdfParseError(
        f"Unrecognized or missing XCCDF namespace on root element '{root.tag}'. "
        f"Supported namespaces: {_SUPPORTED_NAMESPACES}"
    )


def _extract_vuln_discussion(description: str) -> str:
    """Extract the vulnerability discussion from a DISA XCCDF description."""
    start_tag = "<VulnDiscussion>"
    end_tag = "</VulnDiscussion>"

    if start_tag not in description:
        return description.strip()

    _, _, remainder = description.partition(start_tag)
    discussion, separator, _ = remainder.partition(end_tag)

    if not separator:
        return description.strip()

    return discussion.strip()


def _extract_rule(
    rule: ElementTree.Element,
    group_id: str | None,
    ns: dict,
) -> Requirement:
    title = rule.findtext("xccdf:title", default="", namespaces=ns)
    description = rule.findtext("xccdf:description", default="", namespaces=ns)
    fixtext = rule.findtext("xccdf:fixtext", default="", namespaces=ns)
    version = rule.findtext("xccdf:version", default="", namespaces=ns)
    check_content = rule.findtext(
        "xccdf:check/xccdf:check-content",
        default="",
        namespaces=ns,
    )

    cci_refs = [
        ident.text
        for ident in rule.findall("xccdf:ident", ns)
        if ident.get("system", "").endswith("cci") and ident.text
    ]

    return {
        "group_id": group_id,
        "rule_id": rule.get("id"),
        "version": version.strip(),
        "severity": rule.get("severity"),
        "title": title.strip(),
        "description": _extract_vuln_discussion(description),
        "check": check_content.strip(),
        "fix": fixtext.strip(),
        "cci": cci_refs,
    }


def read_xccdf_file(path: str) -> list[Requirement]:
    """Read security requirements from an XCCDF file.

    Args:
        path: Path to the XCCDF XML file.

    Returns:
        Security requirements extracted from the XCCDF document. Each
        requirement includes rule_id, version (e.g. SRG-APP-000001),
        severity, title, description, check text, fix text, and any
        associated CCI references.

    Raises:
        XccdfParseError: If the file is missing, malformed, uses an
            unsupported XCCDF namespace, or contains no rules.
    """
    xccdf_path = Path(path)

    if not xccdf_path.is_file():
        raise XccdfParseError(f"No such file: {path}")

    try:
        tree = ElementTree.parse(xccdf_path)
    except ElementTree.ParseError as exc:
        raise XccdfParseError(f"Malformed XML in {path}: {exc}") from exc

    root = tree.getroot()
    namespace_uri = _detect_namespace(root)
    ns = {"xccdf": namespace_uri}

    requirements: list[Requirement] = []

    # Rules nested inside Groups.
    for group in root.findall(".//xccdf:Group", ns):
        group_id = group.get("id")

        for rule in group.findall("xccdf:Rule", ns):
            requirements.append(_extract_rule(rule, group_id, ns))

    # Rules that live directly under the Benchmark, outside any Group.
    for rule in root.findall("xccdf:Rule", ns):
        requirements.append(_extract_rule(rule, group_id=None, ns=ns))

    if not requirements:
        raise XccdfParseError(
            f"No Rule elements found in {path}. The file may not be a valid "
            f"XCCDF benchmark."
        )

    return requirements
