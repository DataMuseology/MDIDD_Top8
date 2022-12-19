import csv
from itertools import combinations

vertices = [['Id','Label',]] #Header columns for vertices. Add additional attributes as needed
edges = [['Source','Target','Type','Weight']] #Header columns for edges, remove 'weight' if not using

edgeDicts = {}
vertexPairsList = []

with open('DISCS-desert-island-discs-OnlyNeededFields_OpenRefined-1960s_vs_2000s.csv','r',encoding='utf-8-sig') as networkFile: #Whatever your file is called
	networkData = csv.reader(networkFile)

	# Loop 1
	for row in networkData:
		vertex = row[5] #Row of vertex ID (decade_episode)
		vertexLabel = row[6] #Row of vertex Name (decade_episode_castaway_name)
		# vertexAttribute1 = row[3] #Row of additional vertex data
		# vertexAttribute2 = row[?] #Add additional attributes as needed
		# vertexAttribute1 = row[4]
		# vertexAttribute2 = row[5]
		# vertexAttribute3 = row[6]
		# vertexAttribute4 = row[19]
		# [...]
		edge = row[8] #Row of edge (std_artist)

		#Add each vertex (+additional info) to vertex list
		v = [vertex, vertexLabel] #[...] Add additional attributes as needed
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
with open("vertices_artist60vs00.csv",'w') as csvfile1:
	csvwriter = csv.writer(csvfile1)
	csvwriter.writerows(vertices)

with open("edges_artist60vs00.csv",'w') as csvfile2:
	csvwriter = csv.writer(csvfile2)
	csvwriter.writerows(edges)