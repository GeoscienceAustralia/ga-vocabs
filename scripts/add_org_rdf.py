import glob
from rdflib import Graph
from rdflib.namespace import SDO

for f in glob.glob("/Users/nick/Work/ga/ga-vocabs/vocabularies/*.ttl"):
    g = Graph().parse(f)
    addition = """
        PREFIX sdo: <https://schema.org/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        
        
        <https://linked.data.gov.au/org/ga>
            a sdo:Organization ;
            sdo:description "Geoscience Australia is Australia's pre-eminent public sector geoscience organisation. It is the nation's trusted advisor on the geology and geography of Australia. It applies science and technology to describe and understand the Earth for the benefit of Australia."@en ;
            sdo:name "Geoscience Australia" ;
            sdo:url "https://www.ga.gov.au"^^xsd:anyURI ;
        .    
        """
    g += Graph().parse(data=addition, format="turtle")
    g.bind("sdo", SDO)
    g.serialize(destination=f, format="longturtle")

    print(f"Done {f}")
