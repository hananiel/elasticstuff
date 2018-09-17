file = open("../ml-100k/u.item",encoding = "ISO-8859-1")

labels = ["movie id", "movie title","release date","video release date",
"IMDb URL","unknown","Action","Adventure","Animation","Children's",
"Comedy","Crime","Documentary","Drama","Fantasy",
"Film-Noir","Horror","Musical","Mystery","Romance","Sci-Fi","Thriller","War","Western"]
for line in file:
	columns = line.strip().split("|")
	print("{ \"index\": {\"_type\" : \"_doc\"}}")
	
	jsonValues = []
	for i in range(0, len(columns)):
		jsonValues.append("\"{}\":\"{}\"".format(labels[i], columns[i]))
	print("{{ {} }}".format(','.join(jsonValues)))

