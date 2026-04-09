from pathlib import Path
from kurra.file import reformat

voc_dir = Path(Path(__file__).parent.parent / "vocabularies")

for f in sorted(voc_dir.glob("*.ttl")):
    print(f)
    reformat(f, check=False, output_format="longturtle")
