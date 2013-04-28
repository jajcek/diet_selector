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
	  
m3 = [[    1.0,     1.0, 7.0],
	  [    1.0,     1.0, 3.0],
	  [1.0/7.0, 1.0/3.0, 1.0]]
	  
m4 = [[    1.0, 7.0, 9.0],
	  [1.0/7.0, 1.0, 1.0],
	  [1.0/9.0, 1.0, 1.0]]

mt = [[    1.0, 1.0/4.0, 3.0, 1.0/5.0, 1.0/5.0 ],
	  [    4.0, 	1.0, 5.0, 	  3.0, 1.0/3.0 ],
	  [1.0/3.0, 1.0/5.0, 1.0, 1.0/5.0, 1.0/3.0 ],
	  [    5.0, 1.0/3.0, 5.0, 	  1.0,     5.0 ],
	  [    5.0, 	3.0, 3.0, 1.0/5.0,     1.0 ]]

RI = [    0,    0, 0.58, 0.90, 1.12,
	   1.24, 1.32, 1.41, 1.45, 1.49 ];


def main():
	"""normalizeVertically( m0 )
	normalizeVertically( m1 )
	normalizeVertically( m2 )
	normalizeVertically( m3 )
	normalizeVertically( m4 )
	s0 = calcMatrixWithAvgRows( m0 )
	s  = calcMatrixWithAvgRows( m1, m2, m3, m4 )
	r  = calcDecisionValues( s0, s )
	u  = prepareDecisionVector( r )"""
	
	u = lambdaMax( mt );
	w = consistencyIndex( u, len( mt[0] ) );
	c = consistencyRatio( w, RI[len( mt[0] )-1] )
	i = isMatrixConsistence( mt, RI )
	ii = countMatrixConsistency( mt, RI )
	print u
	print w
	print c
	print ii
	print i
	
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
	
def calcDecisionValues( s0, s ):
	"""Calculates final decision values"""

	colCount = len( s[0] )
	rowCount = len( s )
	r = [0.0] * colCount
	for col in range( colCount ):
		for row in range( rowCount ):
			#print str( s0[0][row] ) + " * " + str( s[row][col] )
			r[col] += s0[0][row] * s[row][col]
			
	return r
	
def prepareDecisionVector( valVec ):
	"""Returns the vector of the final decisions"""
	
	u = [1] * len( valVec )
	index = 0
	for val in valVec:
		for val2 in valVec:
			if val < val2:
				u[index] += 1
		index += 1
	
	return u



def gMean( matrixRow ):
	product = 1.0;
	for i in matrixRow :
		product *= i; 
	return ( product ** ( 1.0 / len( matrixRow ) ) );

def consistencyIndex( lMax, matrixSize ): 
	return ( ( lMax - matrixSize ) / ( matrixSize - 1 ) );

def consistencyRatio( ci, ri ):
	return ( ci / ri );
 
def lambdaMax( matrix ):
	"""Check if matrix is consistence"""
	"""epsilon [0;1] - error margin"""
	gMeans = [ gMean( mat ) for mat in matrix ]; 
	gMeanSum = sum( gMeans );  
	
	priorityVector = [ ( gm / gMeanSum ) for gm in gMeans ];

	colSums = [ sum(x) for x in zip(*matrix) ];  

	priorityRow = [ ( colSums[x] * priorityVector[x] ) for x in range( len( colSums ) ) ];

	return sum( priorityRow );

def countMatrixConsistency( matrix, riTable ): 
	c = consistencyIndex( lambdaMax( matrix ), len( matrix[0] ) );
	r = riTable[ len( matrix[0] )-1 ];
	return consistencyRatio( c, r );

def isMatrixConsistence( matrix, riTable, epsilon = 0.1 ): 
	return ( countMatrixConsistency( matrix, riTable ) < epsilon );


if __name__ == '__main__':
	main()
	