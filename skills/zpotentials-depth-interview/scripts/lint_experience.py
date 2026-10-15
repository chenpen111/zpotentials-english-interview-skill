"""Check experience references and compactness; character budgets are not token counts."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main():
    rules = json.loads((ROOT / "references/rules.json").read_text(encoding="utf-8"))
    entry = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    errors, warnings, seen, counts = [], [], set(), {}
    for stage in rules["experience_stages"]:
        relative = f"references/experience/{stage}.md"
        path = ROOT / relative
        if relative not in entry or not path.is_file():
            errors.append(f"Missing stage route or reference: {stage}")
            continue
        text = path.read_text(encoding="utf-8")
        ids = re.findall(r"^### ([A-Z]+\d+)\b", text, re.MULTILINE)
        for lesson_id in ids:
            if lesson_id in seen:
                errors.append(f"Duplicate experience ID: {lesson_id}")
            seen.add(lesson_id)
        counts[stage] = {"lessons": len(ids), "characters": len(text)}
        if len(ids) > 6 or len(text) > 1500:
            warnings.append(f"Consider merging/shortening {stage}; preserve necessary safeguards.")
    print(json.dumps({"passed": not errors, "stages": counts,
                      "errors": errors, "warnings": warnings}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
