import csv
from itertools import combinations

vertices = [['Id','Label',]] #Header columns for vertices. Add additional attributes as needed
edges = [['Source','Target','Type','Weight']] #Header columns for edges, remove 'weight' if not using

edgeDicts = {}
vertexPairsList = []

with open('DISCS-desert-island-discs-OnlyNeededFields_OpenRefined-RandomizedSelections_PerYear.csv','r',encoding='utf-8-sig') as networkFile: #Whatever your file is called
	networkData = csv.reader(networkFile)

	# Loop 1
	for row in networkData:
		vertex = row[9] #Row of vertex ID  (std_artist_id)
		vertexLabel = row[8] #Row of vertex Name (std_artist)
		# vertexAttribute1 = row[8] #Row of additional vertex data
		vertexAttribute1 = row[3] #Add additional attributes as needed 
		vertexAttribute2 = row[4] #(decade)
		vertexAttribute3 = row[10] #(std_name)
		# vertexAttribute3 = row[6]
		# vertexAttribute4 = row[19]
		# [...]
		edge = row[3] #Row of edge  (date)

		#Add each vertex (+additional info) to vertex list
		v = [vertex, vertexLabel, vertexAttribute1, vertexAttribute2, vertexAttribute3] #[...] Add additional attributes as needed
		if v not in vertices:
			vertices.append(v) 

		#Make a dict of form "e1:[v1,v2,[...]][...]"
		if edge not in edgeDicts:
			edgeDicts[edge] = [vertex]
		else: 
			edgeDicts[edge].append(vertex)

	# Loop 2
	for vertexList in edgeDicts.values(): #For each edge dict, list all combinations of vertex pairs
		vertexPairs = (list(combinations(vertexList,2)))
		vertexPairsList += vertexPairs

	# Loop 3
	for vertexPair in set(vertexPairsList): #For each vertex pair, count occurances and add to final list
		edgeWeight = vertexPairsList.count(vertexPair)
		# print(vertexPair)
		weightedVertexPair = [vertexPair[0],vertexPair[1],"Undirected",edgeWeight]
		edges.append(weightedVertexPair)

	# If you're not using weighted pairs, change this for Loop 3
	# for vertexPair in set(vertexPairsList): #"set" removes duplicates, remove if you want to keep them
	# 	print(vertexPair)
	# 	unweightedVertexPair = [vertexPair[0],vertexPair[1],"Undirected"]
	# 	edges.append(unweightedVertexPair) 

#Export to CSV
with open("vertices_random-art-date.csv",'w') as csvfile1:
	csvwriter = csv.writer(csvfile1)
	csvwriter.writerows(vertices)

with open("edges_random-art-date.csv",'w') as csvfile2:
	csvwriter = csv.writer(csvfile2)
	csvwriter.writerows(edges)