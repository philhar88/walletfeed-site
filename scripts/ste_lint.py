#!/home/pph/.venv/bin/python
"""Mechanical ASD-STE100 and house-style checks for the guide sources in src/.

  ~/.venv/bin/python scripts/ste_lint.py src/guides/apple-card-to-pocketsmith.md [more.md …]
  ~/.venv/bin/python scripts/ste_lint.py --all

Errors must be fixed. Warnings need a person (or agent) to look: some are allowed, such as an -ing
word that is part of a UI label or product name. The checks don't replace reading the STE rules:
they catch what a reader would count.

Word counts follow STE rule 8.6 as this site applies it: a bold UI label, a code span, a link's
text, a product name and a number with its unit each count as one word.
"""
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORDS = tomllib.loads((ROOT / "scripts/data/ste-words.toml").read_text())

PROCEDURE_MAX = 20
DESCRIPTIVE_MAX = 25
PARAGRAPH_MAX = 6
# -ing words that aren't verb forms, or that STE approves.
ING_OK = set(WORDS.get("ing_allowed", []))
WH = re.compile(r"^(what|why|how|where|when|who|which)\b", re.I)
IRREGULAR = "sent|shown|done|made|taken|given|written|seen|known|kept|set|found|paid|built|chosen|hidden|broken|held|left|lost|read|run|said|sold|told|put|cut|got|gotten|met|brought|bought|caught|taught|thought|meant"
PASSIVE = re.compile(rf"\b(is|are|was|were|be|been|being|gets|got)\s+(\w+ly\s+)?(\w+ed|{IRREGULAR})\b", re.I)


def forms(word: str) -> list[str]:
    """The word and the stems it could come from: ensures, ensured, ensuring all point to ensure."""
    out = [word]
    for suffix, add in (("ies", "y"), ("es", ""), ("s", ""), ("ed", ""), ("ed", "e"), ("ing", ""), ("ing", "e"), ("ly", "")):
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            out.append(word[: -len(suffix)] + add)
    return out


# Product and service names, which count as one word and keep their spelling.
NAMES = sorted(WORDS.get("names", []), key=len, reverse=True)


def strip_front_matter(text: str) -> tuple[str, int]:
    match = re.match(r"\+\+\+\n.*?\n\+\+\+\n", text, re.S)
    return (text[match.end():], text[:match.end()].count("\n")) if match else (text, 0)


def collapse(text: str) -> str:
    """Replaces the spans that count as one word with a single token."""
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)  # images
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", lambda m: "Zlink", text)  # links
    text = re.sub(r"\*\*[^*]+\*\*", "Zlabel", text)  # UI labels
    text = re.sub(r"“[^”]+”|\"[^\"]+\"", "Zquote", text)  # quoted messages and searches
    text = re.sub(r"`[^`]+`", "Zcode", text)
    for name in NAMES:
        text = re.sub(rf"(?<![\w-]){re.escape(name)}(?![\w-])", "Zname", text)
    text = re.sub(r"\$?\d[\d,.]*\s?(%|percent|seconds?|minutes?|hours?|days?|weeks?|months?|years?|characters?|MB|GB)?", "Znum", text)
    return text


def sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text.strip())
    parts = re.split(r"(?<=[.!?:])\s+(?=[A-Z\"“(])", text)
    return [p for p in parts if p.strip()]


def count_words(sentence: str) -> int:
    return len(re.findall(r"[A-Za-z0-9’'-]+", collapse(sentence)))


def lint(path: Path) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    text, offset = strip_front_matter(path.read_text())
    lines = text.split("\n")
    in_code = False
    para: list[str] = []
    para_start = [0]

    def flush():
        if para:
            check_block(para_start[0], "para", " ".join(para))
        para.clear()

    def check_block(line_no: int, kind: str, raw: str):
        where = f"{path.name}:{line_no + offset}"
        body = re.sub(r"^(\d+\.|[-*]|>\s*)\s*", "", raw.strip())
        body = re.sub(r"^\*\*Note:\*\*\s*", "", body)
        limit = PROCEDURE_MAX if kind == "step" else DESCRIPTIVE_MAX
        sents = sentences(body)
        if kind == "para" and len(sents) > PARAGRAPH_MAX:
            errors.append(f"{where}: paragraph has {len(sents)} sentences (STE 6.2: at most {PARAGRAPH_MAX})")
        for s in sents:
            n = count_words(s)
            if n > limit:
                errors.append(f"{where}: {n} words, {kind} limit {limit} (STE 4.1/5.x): “{s[:90]}…”")
        if kind == "step":
            imperative_ok = re.match(r"^(\*\*|If |When |On |In |After |Before |To |For |At |From |Under |Below |Above |With |Without |Until )", body) or \
                re.match(r"^[A-Z][a-z]+\b", body)
            if not imperative_ok:
                warnings.append(f"{where}: step doesn't start with a verb or a condition: “{body[:60]}”")
            if len(re.findall(r"\b(then|and then)\b", collapse(body))) > 1:
                warnings.append(f"{where}: step may hold more than one instruction (STE 5.1): “{body[:80]}”")
        check_words(where, body)

    def check_words(where: str, body: str):
        plain = collapse(body)
        if ";" in plain:
            errors.append(f"{where}: semicolon (STE 8.x)")
        if "—" in plain or " – " in plain or " - " in plain:
            errors.append(f"{where}: dash used as punctuation")
        for word in re.findall(r"\b[A-Za-z]+ing\b", plain):
            if word.lower() not in ING_OK:
                warnings.append(f"{where}: -ing word “{word}” (STE 3.x: use only as a technical name or modifier)")
        for word in re.findall(r"\b[A-Za-z’']+\b", plain):
            lower = word.lower().replace("’", "'")
            banned = next((f for f in forms(lower) if f in WORDS["banned"]), None)
            check = next((f for f in forms(lower) if f in WORDS.get("check", {})), None)
            if banned:
                errors.append(f"{where}: “{word}” is not approved here: {WORDS['banned'][banned]}")
            elif check:
                warnings.append(f"{where}: “{word}”: {WORDS['check'][check]}")
        m = PASSIVE.search(plain)
        if m:
            warnings.append(f"{where}: possible passive voice “{m.group(0)}” (STE 3.6)")
        for phrase in WORDS.get("phrases", {}):
            if phrase in plain.lower():
                errors.append(f"{where}: “{phrase}”: {WORDS['phrases'][phrase]}")

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            flush()
            in_code = not in_code
            continue
        if in_code:
            continue
        if not stripped or stripped.startswith("|") or re.match(r"^\s*!\[", line):
            flush()
            if stripped.startswith("|") and not re.match(r"^\|[\s:|-]+\|$", stripped):
                cells = [c.strip() for c in stripped.strip("|").split("|")]
                for c in cells:
                    if count_words(c) > DESCRIPTIVE_MAX:
                        errors.append(f"{path.name}:{i + offset}: table cell over {DESCRIPTIVE_MAX} words")
                    check_words(f"{path.name}:{i + offset}", c)
            continue
        if stripped.startswith("#"):
            flush()
            heading = stripped.lstrip("#").strip()
            where = f"{path.name}:{i + offset}"
            if WH.match(heading):
                errors.append(f"{where}: heading starts with a Wh-word (owner rules): “{heading}”")
            words = re.findall(r"[A-Za-z][\w’'-]*", collapse(heading))
            capitals = [w for w in words[1:] if w[0].isupper() and w not in ("Zlabel", "Zcode", "Zname", "Zlink", "Znum", "Zquote", "I", "If", "Step")]
            if len(capitals) >= 2 and len(capitals) >= len(words[1:]) / 2:
                warnings.append(f"{where}: heading may be in title case: “{heading}”")
            if count_words(heading) > 12:
                warnings.append(f"{where}: long heading")
            check_words(where, heading)
            continue
        if re.match(r"^(\d+\.)\s", stripped) or (line.startswith("   ") and not stripped.startswith(("!", "|", "-", "*"))):
            # A step, or a paragraph that continues a step inside its list item.
            flush()
            check_block(i, "step", stripped)
            continue
        if re.match(r"^[-*]\s", stripped):
            flush()
            check_block(i, "item", stripped)
            continue
        if not para:
            para_start[0] = i
        para.append(stripped)
    flush()
    return errors, warnings


def main(argv: list[str]) -> int:
    paths = sorted((ROOT / "src").glob("*/*.md")) if argv == ["--all"] else [Path(a) for a in argv]
    if not paths:
        print(__doc__)
        return 2
    total = 0
    for path in paths:
        errors, warnings = lint(path)
        total += len(errors)
        for e in errors:
            print(f"error   {e}")
        for w in warnings:
            print(f"warning {w}")
        print(f"{path.name}: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
