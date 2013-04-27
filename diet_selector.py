k1 = [[1.0,         3.0,     7.0, 9.0],
	  [1.0/3.0,     1.0,     3.0, 7.0],
	  [1.0/7.0, 1.0/3.0,     1.0, 3.0],
	  [1.0/9.0, 1.0/7.0, 1.0/3.0, 1.0]]

def main():
	normalizeVertically( k1 )
	s = makeMatrixWithAvgRows( k1 )
	
def normalizeVertically( matrix ):
	"""Normalizes the given matrix vertically"""

	# sum all of the columns
	colSums = [sum(x) for x in zip(*matrix)]
		
	# use the colSums to divide values in the given matrix	
	colCount = len( k1[0] )
	rowCount = len( k1 )
	for col in range( colCount ):
		for row in range( rowCount ):
			matrix[row][col] /= colSums[col]

def makeMatrixWithAvgRows( *matrices ):
	"""Creates the S matrix with averages of the other matrices
	if used only on one matrix it returns an S vector"""
	
	s = []
	for matrix in matrices:
		rowSums = [sum(x)/len(k1[0]) for x in matrix]
		s.append( rowSums )

	return s

if __name__ == '__main__':
	main()