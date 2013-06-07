 
 
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

# cena 
# pozywnosc
# szybkosc przygotowania
# lekkostrawnosc
# kalorycznosc
# latwosc przygotowania
	   
CRITERIA = ( 'PRICE', 'NOUR', 'TIME', 'DIGESTIBILITY', 'CALORIFIC', 'SIMPLICITY' )
COURSES = ( 'GYROS', 'SUSHI', 'FRUIT SALAD', 'PIZZA', 'SCRAMBLED EGGS', 'TOSTS', 'TOMATO SOUP', 'CHICKEN SOUP', 'ROASTED SALMON', 'VEGETABLE SALAD' )

price = \
[
	[ 1.0, 3.0, _15, _17, _13 ],	# gyros 4
	[ _13, 1.0, _17, _19, _15 ],	# sushi 5
	[ 5.0, 7.0, 1.0, _13, 3.0 ],	# salatka owocowa 2
	[ 7.0, 9.0, 3.0, 1.0, 5.0 ],	# zupa pomidorowa 1
	[ 3.0, 5.0, _13, _15, 1.0 ],	# losos z piekarnika 3
]

nour = \
[
	[ 1.0, _19, _15, _13, _17 ],	# gyros 5
	[ 9.0, 1.0, 5.0, 7.0, 3.0 ],	# sushi 1
	[ 5.0, _15, 1.0, 3.0, _13 ],	# salatka owocowa 3
	[ 3.0, _17, _13, 1.0, _15 ],	# zupa pomidorowa 4
	[ 7.0, _13, 3.0, 5.0, 1.0 ],	# losos z piekarnika 2
]
 
time = \
[ 
	[ 1.0, 3.0, _15, _13, _17 ],	# gyros 4
	[ _13, 1.0, _17, _15, _19 ],	# sushi 5
	[ 5.0, 7.0, 1.0, 3.0, _13 ],	# salatka owocowa 2
	[ 3.0, 5.0, _13, 1.0, _15 ],	# zupa pomidorowa 3
	[ 7.0, 9.0, 3.0, 5.0, 1.0 ],	# losos z piekarnika 1
]

	
digestibility = \
[ 
	[ 1.0, _13, _19, _17, _15 ],	# gyros 5
	[ 3.0, 1.0, _17, _15, _13 ],	# sushi 4
	[ 9.0, 7.0, 1.0, 3.0, 5.0 ],	# salatka owocowa 1
	[ 7.0, 5.0, _13, 1.0, 3.0 ],	# zupa pomidorowa 2
	[ 5.0, 3.0, _15, _13, 1.0 ],	# losos z piekarnika 3
]
	

calorific = \
[
	[ 1.0, _13, 7.0, 5.0, 3.0 ],	# gyros 2
	[ 3.0, 1.0, 9.0, 7.0, 5.0 ],	# sushi 1
	[ _17, _19, 1.0, _13, _15 ],	# salatka owocowa 5
	[ _15, _17, 3.0, 1.0, _13 ],	# zupa pomidorowa 4
	[ _13, _15, 5.0, 3.0, 1.0 ],	# losos z piekarnika 3
]


simplicity = \
[
	[ 1.0, 3.0, _17, _13, _15 ],	# gyros 4
	[ _13, 1.0, _19, _15, _17 ],	# sushi 5
	[ 7.0, 9.0, 1.0, 5.0, 3.0 ],	# salatka owocowa 1
	[ 3.0, 5.0, _15, 1.0, _13 ],	# zupa pomidorowa 3
	[ 5.0, 7.0, _13, 3.0, 1.0 ],	# losos z piekarnika 2
]
		   
	
def main( ): 
	lamPrice = lambdaMax( price ); 
	print "Lambda Price\t ", lamPrice
	print "Consists Price\t ", \
		countMatrixConsistency( price, RI ), \
		isMatrixConsistence( price, RI ) 
		
	lamNour = lambdaMax( nour );
	print "Lambda Nourishment\t ", lamNour
	print "Consists Nourishment\t ", \
		countMatrixConsistency( nour, RI ), \
		isMatrixConsistence( nour, RI ) 
		
		
	lamTime = lambdaMax( time );
	print "Lambda Time\t ", lamTime
	print "Consists Time\t ", \
		countMatrixConsistency( time, RI ), \
		isMatrixConsistence( time, RI )
		
	lamDige = lambdaMax( digestibility );
	print "Lambda Digestibility\t ", lamDige
	print "Consists Digestibility\t ", \
		countMatrixConsistency( digestibility, RI ), \
		isMatrixConsistence( digestibility, RI ) 

	lamCalo = lambdaMax( calorific );
	print "Lambda Calorific\t ", lamCalo
	print "Consists Calorific\t ", \
		countMatrixConsistency( calorific, RI ), \
		isMatrixConsistence( calorific, RI ) 
		
	lamSimp = lambdaMax( simplicity );
	print "Lambda Simplicity\t ", lamSimp
	print "Consists Simplicity\t ", \
		countMatrixConsistency( simplicity, RI ), \
		isMatrixConsistence( simplicity, RI ) 
	
def normalizeVertically( matrix ):
	"""Normalizes the given matrix vertically"""

	newMatrix = [row[:] for row in matrix]
	# sum all of the columns
	colSums = [sum(x) for x in zip(*newMatrix)]
		
	# use the colSums to divide values in the given matrix	
	colCount = len( newMatrix[0] )
	rowCount = len( newMatrix )
	for col in range( colCount ):
		for row in range( rowCount ):
			newMatrix[row][col] /= colSums[col]
            
	return newMatrix

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

def debugMatrix( matrix ):
	s = [[str(e) for e in row] for row in matrix]
	lens = [len(max(col, key=len)) for col in zip(*s)]
	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	print '\n'.join(table)

if __name__ == '__main__':
	main()
	