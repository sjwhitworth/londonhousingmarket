import csv, json, os

boroughmetrics = {}

geojson = json.load(open('clean.json'))
csvdata = csv.reader(open('london-borough-profiles.csv', 'U'))

csvdata.next() #Skip headers.

for line in csvdata:
	tempdict = {}
	csvname = line[0]
	tempdict = {'population': int(line[1]), 
				'avghouseprice': int(line[2]), 
				'numnewhomes': int(line[3]), 
				'percentrent': float(line[4]),
				'peoplepernewhome': float(line[1]) / int(line[3])}

	for borough in geojson['objects']['thenewestdict1']['geometries']:
		boroughname = borough['properties']['Name']
		if csvname == boroughname:
			borough['properties'].update(tempdict)

with open('statgeo.json', 'w') as outfile:
	json.dump(geojson, outfile)

os.system("topojson -o stattopo.json statgeo.json -p")




