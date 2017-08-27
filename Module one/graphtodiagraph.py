from __future__ import division
import collections
import numpy as np

# The name-key is the node name. The list contains all connected nodes. But the keys can be iterated over only in a random order.
# Due to python's language characteristics. Hence use OrderedDict

		
def no_of_nodes(unordered_graph):
	ordered_graph = collections.OrderedDict(sorted(unordered_graph.items(), key=lambda t: t[0]))
	count = 0
	for node,links in ordered_graph.items():
		count += 1
	return count	

# Creating edges of the graph
def create_edges(unordered_graph):
	ordered_graph = collections.OrderedDict(sorted(unordered_graph.items(), key=lambda t: t[0]))
	edges = []
	for node in ordered_graph:
		for link in ordered_graph[node]:	
			edges.append( (node,link) )

	return edges

# Checking for isolated_nodes
def find_isolated_nodes(unordered_graph):
	ordered_graph = collections.OrderedDict(sorted(unordered_graph.items(), key=lambda t: t[0]))
	isolated_nodes = []
	for node in ordered_graph:
		if not ordered_graph[node]:
			# If the node has no value attached to it then, it will have the default value of false	
			isolated_nodes.append(node)
	return isolated_nodes

# Creating the corresponding diagraph
def create_diagraph(unordered_graph):
	ordered_graph = collections.OrderedDict(sorted(unordered_graph.items(), key=lambda t: t[0]))
	headerarray = []
	for node,links in ordered_graph.items():
		headerarray.append(node)
	
	count = 0
	for nodes in ordered_graph:
		count += 1

	#creating an empty list with 0
	temp_array = np.zeros( [count,count] )
	row = 0;
	column = 0;

	for node,links in ordered_graph.items() :
		for link in links :
			outdegrees = len(links)
			column = 0
			for header in headerarray:
				if(header == link):
					temp_array[column][row] = 1/outdegrees
				else:
					temp_array[column][row] 
					column += 1
		row += 1
	# returning a matrice by typecasting
	return np.mat(temp_array)

