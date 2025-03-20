
# /Users/nick/Library/Caches/pypoetry/virtualenvs/vocexcel-XgwzAsEM-py3.11/bin/python /Users/nick/Work/rdflib/VocExcel/vocexcel/__main__.py Borehole_Construction_Type_Boreholes.xlsx > Borehole_Construction_Type_Boreholes.ttl
# echo "Borehole_Construction_Type_Boreholes"


FILES=/Users/nick/Work/ga/ga-vocabs/excel/0.4.3/*.xlsx

for f in $FILES
do
  echo "Processing $f"
  fttl=${f%.*}.ttl

  /Users/nick/Library/Caches/pypoetry/virtualenvs/vocexcel-XgwzAsEM-py3.11/bin/python /Users/nick/Work/rdflib/VocExcel/vocexcel/__main__.py $f > $fttl
  echo "Completed $fttl"
done