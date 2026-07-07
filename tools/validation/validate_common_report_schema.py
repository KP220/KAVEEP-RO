import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[2]

SCHEMA_PATH = ROOT / "schemas" / "common-report.schema.json"

EXAMPLE_FILES = [
    ROOT / "examples" / "common-report.success.example.json",
    ROOT / "examples" / "common-report.warning.example.json",
    ROOT / "examples" / "common-report.error.example.json",
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> int:
    schema = load_json(SCHEMA_PATH)

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker()
    )

    failed = False

    for example_path in EXAMPLE_FILES:
        report = load_json(example_path)
        errors = sorted(
            validator.iter_errors(report),
            key=lambda error: list(error.path)
        )

        if errors:
            failed = True
            print(f"[FAIL] {example_path.relative_to(ROOT)}")

            for error in errors:
                location = ".".join(str(part) for part in error.path) or "<root>"
                print(f"  - {location}: {error.message}")
        else:
            print(f"[PASS] {example_path.relative_to(ROOT)}")

    if failed:
        return 1

    print("All common report examples passed schema validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
