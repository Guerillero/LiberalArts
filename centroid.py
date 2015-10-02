import csv
from decimal import *

fn = ["page_title", "gt_lat", "gt_lon", "rank"]

fin = open("LA.csv", 'rb')
csvIN = csv.DictReader(fin, fieldnames= fn)

lat = Decimal(0)
lon = Decimal(0)
i = 0

for line in csvIN:
  # since csvIN has no length
  i += 1
  
  # makes life easier
  a = line['gt_lat']
  b = line['gt_lon']
  
  # rmv reader
  if line['gt_lat'] != 'gt_lat':
    lat += Decimal(a)
    lon += Decimal(b)

lat = lat/i
lon = lon/i

print str(lon) + ", " + str(lat)
