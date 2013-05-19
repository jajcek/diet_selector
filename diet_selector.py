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

# cena 
# pozywnosc
# czas przygotowania
# lekkostrawnosc
# kalorycznosc
# trudnosc
	  
RI = [    0,    0, 0.58, 0.90, 1.12,
	   1.24, 1.32, 1.41, 1.45, 1.49 ];

	   
_12 = 1.0/2.0
_13 = 1.0/3.0
_14 = 1.0/4.0
_15 = 1.0/5.0
_16 = 1.0/6.0
_17 = 1.0/7.0
_18 = 1.0/8.0
_19 = 1.0/9.0
	   
criteria = \
[ 
	[ 1.0, _15, _14 ],
	[ 5.0, 1.0, 3.0 ],
	[ 4.0, _13, 1.0 ],
]

# gyros  
# sushi
# fruit salat

price = \
[
	[ 1.0, 7.0, _13 ],
	[ _17, 1.0, _19 ],
	[ 3.0, 9.0, 1.0 ]
]

nour = \
[
	[ 1.0, _15, 3.0 ],
	[ 5.0, 1.0, 7.0 ],
	[ _13, _17, 1.0 ]
]

time = \
[
	[ 1.0, 5.0, _14 ],
	[ _15, 1.0, _19 ],
	[ 4.0, 9.0, 1.0 ]
]
	
	
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
	
	lamCrit = lambdaMax( criteria ); 
	lamPrice = lambdaMax( price ); 
	lamNour = lambdaMax( nour );
	lamTime = lambdaMax( time );
	 
	print "Lambda Criteria\t ", lamCrit
	print "Lambda Price\t ", lamPrice
	print "Lambda Nour\t ", lamNour
	print "Lambda Time\t ", lamTime, "\n"
	
	print "Consists Criteria", \
		countMatrixConsistency( criteria, RI ), \
		isMatrixConsistence( criteria, RI ) 
	print "Consists Price\t ", \
		countMatrixConsistency( price, RI ), \
		isMatrixConsistence( price, RI ) 
	print "Consists Nour\t ", \
		countMatrixConsistency( nour, RI ), \
		isMatrixConsistence( nour, RI ) 
	print "Consists Time\t ", \
		countMatrixConsistency( time, RI ), \
		isMatrixConsistence( time, RI ), "\n"
	
	normalizeVertically( criteria )
	normalizeVertically( price )
	normalizeVertically( nour )
	normalizeVertically( time )
	
	print "Norm Criteria\n", criteria[0]
	print criteria[1]
	print criteria[2]
	print "\nNorm Price\n", price[0]
	print price[1]
	print price[2]
	print "\nNorm Nour\n", nour[0]
	print nour[1]
	print nour[2]
	print "\nNorm Time\n", time[0]
	print time[1]
	print time[2], "\n"
	
	s0 = calcMatrixWithAvgRows( criteria )
	print "S0:\n", s0, "\n"
	
	s  = calcMatrixWithAvgRows( price, nour, time )
	print "S:\n", s, "\n"
	
	r  = calcDecisionValues( s0, s )
	print "R:\n", r, "\n"
	
	u  = prepareDecisionVector( r )
	print "U:\n", u, "\n"
	
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
	