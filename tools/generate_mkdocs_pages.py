from pathlib import Path

import mkdocs_gen_files


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git", ".github", ".venv-docs", "docs", "site"}
PUBLISHABLE_ASSET_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


for source in sorted(ROOT.rglob("*.md")):
    relative = source.relative_to(ROOT)
    if any(part in EXCLUDED_PARTS for part in relative.parts):
        continue

    destination = Path("_source") / relative
    with mkdocs_gen_files.open(destination.as_posix(), "w", encoding="utf-8") as output:
        output.write(source.read_text(encoding="utf-8"))

for source in sorted(ROOT.rglob("*")):
    if not source.is_file() or source.suffix.lower() not in PUBLISHABLE_ASSET_SUFFIXES:
        continue

    relative = source.relative_to(ROOT)
    if any(part in EXCLUDED_PARTS for part in relative.parts):
        continue

    destination = Path("_source") / relative
    with mkdocs_gen_files.open(destination.as_posix(), "wb") as output:
        output.write(source.read_bytes())


with mkdocs_gen_files.open("_source/mkdocs.yml", "w", encoding="utf-8") as output:
    output.write((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
