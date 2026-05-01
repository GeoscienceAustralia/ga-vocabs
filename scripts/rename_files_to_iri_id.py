from pathlib import Path
from rdflib import Graph
from rdflib.namespace import RDF, SKOS

voc_dir = Path(Path(__file__).parent.parent / "vocabularies")

for f in sorted(voc_dir.glob("*.ttl")):
    # parse each vocab file into a graph
    g = Graph().parse(f)
    # get the Concept Scheme IRI
    cs = g.value(predicate=RDF.type, object=SKOS.ConceptScheme)
    # extract the ID
    cs_id = str(cs).replace("https://pid.geoscience.gov.au/def/voc/ga/", "")
    cs_id = str(cs).replace("http://qudt.org/community/ga/voc", "")
    # make the new file path
    new_f = f.parent / str(cs_id + ".ttl")
    # print for checking
    print(f"{f}:\t{new_f}\t{cs}")
    # move (rename) the old to new via interim for case insensitivity
    interim_f = f.parent / str(cs_id + ".ttx")
    Path(f).move(interim_f)
    Path(interim_f).move(new_f)
