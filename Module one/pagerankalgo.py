from __future__ import division
import graphtodiagraph
import numpy as np
import collections


def create_initialvector(unordered_graph):
	ordered_graph = collections.OrderedDict(sorted(unordered_graph.items(), key=lambda t: t[0]))
	noofnodes = 0;
	for node,links in ordered_graph.items():
		noofnodes += 1

	temp_array = np.ones([noofnodes,1])
	temp_array = (temp_array)/noofnodes

	return np.mat(temp_array)

def difference_math_matrices(matrix1,matrix2):
	matrix3 = matrix1 - matrix2
	
	sum = 0.0
	(rows,columns) = np.array(matrix3.shape)
	# the row in matrix is NOT AN INTEGER. MIND YOU !!
	# the row is a sub array of the 2d matrice

	for i in range(0,rows):
		for j in range(0,columns):
			sum += abs(matrix3[i,j])
	return sum

def one_multiplication_round(noofnodes,diagraph,previous_matrix,beta):

	# When defining the size of the array, keep in mind the dimensions are columns*rows!!
	# Very important to specify the data type !!
	temp_array = np.zeros([noofnodes,noofnodes],dtype = 'f')
	current = np.mat(temp_array)

	temp_array_2 = 	np.ones([noofnodes,1], dtype = 'f')
	temp_array_2 = temp_array_2*( (1-beta)/noofnodes )
	temp_matrix_2 = np.mat(temp_array_2)

	#final_diagraph = beta*diagraph

	#current = final_diagraph*previous_matrix + temp_matrix_2
	current = diagraph*previous_matrix 


	return current


def return_final_matrix(mathlimit,noofnodes,diagraph,previous_matrix,beta):
	
	temp_array = np.zeros([noofnodes,noofnodes],dtype = 'f')
	current_matrix = np.mat(temp_array)
	current_matrix = previous_matrix
	difference = mathlimit + 1

	while( difference > mathlimit ):
			# Keeping track of the previous and the current matrix
			previous_matrix = current_matrix
			print(previous_matrix)
			current_matrix = one_multiplication_round(noofnodes,diagraph,previous_matrix,beta)
			print(current_matrix)
			difference = difference_math_matrices(previous_matrix,current_matrix)
			print(difference)
			print(" This is a new round! ")
		

	return current_matrix


unordered_graph = {
	"A" : ["B","C",],
	"B" : ["C",],
	"C" : ["A",]
}

''' The start of the main diagram '''

initial_vector = create_initialvector(unordered_graph)
diagraph =  graphtodiagraph.create_diagraph(unordered_graph)
noofnodes = graphtodiagraph.no_of_nodes(unordered_graph)
beta = 0.08

print(" The method for the final matrix is --> ")
final_matrix = return_final_matrix(0.001,noofnodes,diagraph,initial_vector,beta)
print(final_matrix)



