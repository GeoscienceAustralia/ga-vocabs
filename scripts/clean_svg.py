from pathlib import Path

for f in Path("/Users/nick/Desktop/MorphologyFigures").glob('*.svg'):
    txt = Path(f).read_text()
    txt = "<svg " + txt.split("<svg", 1)[1].split("<script", 1)[0] + "</svg>"
    txt = txt.replace("\n", " ")
    txt = txt.replace("  ", " ")
    txt = txt.replace("  ", " ")
    txt = txt.replace("  ", " ")
    txt = txt.replace("\t", " ")
    n = f.with_suffix(".s.svg")
    print(n)
    n.write_text(txt)

