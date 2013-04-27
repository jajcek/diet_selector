# matrices based on the L5Z2

m0 = [[    1.0,     3.0,     7.0, 9.0],
	  [1.0/3.0,     1.0,     3.0, 7.0],
	  [1.0/7.0, 1.0/3.0,     1.0, 3.0],
	  [1.0/9.0, 1.0/7.0, 1.0/3.0, 1.0]]
	  
m1 = [[    1.0,     1.0, 7.0],
	  [    1.0,     1.0, 3.0],
	  [1.0/7.0, 1.0/3.0, 1.0]]
	  
m2 = [[1.0, 1.0/5.0, 1.0],
	  [5.0,     1.0, 3.0],
	  [1.0, 1.0/3.0, 1.0]]
	  
m3 = [[    1.0, 7.0, 9.0],
	  [1.0/7.0, 1.0, 1.0],
	  [1.0/9.0, 1.0, 1.0]]

def main():
	normalizeVertically( m1 )
	normalizeVertically( m2 )
	normalizeVertically( m3 )
	s = calcMatrixWithAvgRows( m1, m2, m3 )
	
	print s
	
def normalizeVertically( matrix ):
	"""Normalizes the given matrix vertically"""

	# sum all of the columns
	colSums = [sum(x) for x in zip(*matrix)]
		
	# use the colSums to divide values in the given matrix	
	colCount = len( matrix[0] )
	rowCount = len( matrix )
	for col in range( colCount ):
		for row in range( rowCount ):
			matrix[row][col] /= colSums[col]

def calcMatrixWithAvgRows( *matrices ):
	"""Creates the S matrix with averages of the other matrices
	if used only on one matrix it returns an S vector"""
	
	s = []
	for matrix in matrices:
		rowSums = [sum(x)/len(matrix[0]) for x in matrix]
		s.append( rowSums )

	return s

if __name__ == '__main__':
	main()
	