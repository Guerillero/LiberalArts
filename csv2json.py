import csv

fn = ["page_title", "gt_lat", "gt_lon", "rank"]

fin = open("LA.csv", 'rb')
csvIN = csv.DictReader(fin, fieldnames= fn)
fout = open("LA.json", 'wb')

fout.write("{ \"type\": \"FeatureCollection\"," + "\n")
fout.write("\t\"features\": [" + "\n")

foo = 0

for line in csvIN:
  if line['rank'] != 'rank':
    if foo > 1:
      fout.write(",\n")
      
    if line['gt_lon'] <> 'gt_lon':
      fout.write("\t\t{ \"type\": \"Feature\"," + "\n")
      fout.write("\t\t\"geometry\": {\"type\": \"Point\", \"coordinates\": [" + line['gt_lon'] + ", " + line['gt_lat'] + "]}," + "\n")
      fout.write("\t\t\"properties\": {" + "\n")
      fout.write("\t\t\t\"title\": \"" + line['page_title'] + "\",\n")
      fout.write("\t\t\t\"type\": \"" + str(line['rank']) + "\"\n")
      fout.write("\t\t\t}\n")
      fout.write("\t\t}")
    
    foo += 1

fout.write("\n\t]\n")
fout.write("}")
