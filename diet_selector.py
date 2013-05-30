 
 
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
       
criteria = \
[ 
	[ 1.0, _15, _14 ],
	[ 5.0, 1.0, 3.0 ],
	[ 4.0, _13, 1.0 ],
]
 
price = \
[
	[ 1.0, 6.0, _13, 2.0, _17, _16, _17, _17, 2.0, _18 ],	# gyros 
	[ _16, 1.0, _18, _14, _19, _19, _18, _19, _12, _19 ],	# sushi
	[ 3.0, 8.0, 1.0, 7.0, _15, _14, _13, _12, 4.0, _12 ],	# salatka owocowa
	[ _12, 4.0, _17, 1.0, _18, _17, _16, _17, _12, _18 ],	# pizza
	[ 7.0, 9.0, 5.0, 8.0, 1.0, _12, 4.0, 3.0, 8.0, 2.0 ],	# jajecznica
	[ 6.0, 9.0, 4.0, 7.0, 2.0, 1.0, 3.0, 2.0, 9.0, 2.0 ],	# tosty
	[ 7.0, 8.0, 3.0, 6.0, _14, _13, 1.0, 2.0, 7.0, 5.0 ],	# zupa pomidorowa
	[ 7.0, 9.0, 2.0, 7.0, _13, _12, _12, 1.0, 8.0, 2.0 ],	# rosol
	[ _12, 2.0, _14, 2.0, _18, _19, _17, _18, 1.0, _18 ],	# losos z piekarnika
	[ 8.0, 9.0, 2.0, 8.0, _12, _12, _15, _12, 8.0, 1.0 ]	# salatka warzywna
]

nour = \
[
	[ 1.0, _16, 5.0, 4.0, _14, _12, 2.0, 3.0, _15, _13 ],	# gyros 
	[ 6.0, 1.0, 9.0, 9.0, 3.0, 5.0, 7.0, 8.0, 2.0, 4.0 ],	# sushi
	[ _15, _19, 1.0, _12, _18, _16, _14, _13, _19, _17 ],	# salatka owocowa
	[ _14, _19, 2.0, 1.0, _17, _15, _13, _12, _18, _16 ],	# pizza
	[ 4.0, _13, 8.0, 7.0, 1.0, 3.0, 5.0, 6.0, _12, 2.0 ],	# jajecznica
	[ 2.0, _15, 6.0, 5.0, _13, 1.0, 3.0, 4.0, _14, _12 ],	# tosty
	[ _12, _17, 4.0, 3.0, _15, _13, 1.0, 2.0, _16, _14 ],	# zupa pomidorowa
	[ _13, _18, 3.0, 2.0, _16, _14, _12, 1.0, _17, _15 ],	# rosol
	[ 5.0, _12, 9.0, 8.0, 2.0, 4.0, 6.0, 7.0, 1.0, 3.0 ],	# losos z piekarnika
	[ 3.0, _14, 7.0, 6.0, _12, 2.0, 4.0, 5.0, _13, 1.0 ]	# salatka warzywna
]
 
time = \
[
	[ 1.0, 3.0, _17, 2.0, _15, _18, _12, _13, _14, _16 ],	# gyros 
	[ _13, 1.0, _19, _12, _17, _19, _14, _15, _16, _18 ],	# sushi
	[ 7.0, 9.0, 1.0, 8.0, 3.0, _12, 6.0, 5.0, 4.0, 2.0 ],	# salatka owocowa
	[ _12, 2.0, _18, 1.0, _16, _19, _13, _14, _15, _17 ],	# pizza
	[ 5.0, 7.0, _13, 6.0, 1.0, _14, 4.0, 3.0, 2.0, _12 ],	# jajecznica
	[ 8.0, 9.0, 2.0, 9.0, 4.0, 1.0, 7.0, 6.0, 5.0, 3.0 ],	# tosty
	[ 2.0, 4.0, _16, 3.0, _14, _17, 1.0, _12, _13, _15 ],	# zupa pomidorowa
	[ 3.0, 5.0, _15, 4.0, _13, _16, 2.0, 1.0, _12, _14 ],	# rosol
	[ 4.0, 6.0, _14, 5.0, _12, _15, 3.0, 2.0, 1.0, _13 ],	# losos z piekarnika
	[ 6.0, 8.0, _12, 7.0, 2.0, _13, 5.0, 4.0, 3.0, 1.0 ]	# salatka warzywna
]

	
digestibility = \
[
	[ 1.0, _14, _18, 2.0, _16, 2.0, _13, _12, _15, _17 ],	# gyros 
	[ 4.0, 1.0, _15, 5.0, _13, 5.0, 2.0, 3.0, _12, _14 ],	# sushi
	[ 8.0, 5.0, 1.0, 9.0, 3.0, 9.0, 6.0, 7.0, 4.0, 2.0 ],	# salatka owocowa
	[ _13, _16, _19, _12, _18, _12, _15, _14, _17, _19 ],	# pizza
	[ 6.0, 3.0, _13, 7.0, 1.0, 7.0, 4.0, 5.0, 2.0, _12 ],	# jajecznica
	[ _12, _15, _19, 1.0, _17, 1.0, _14, _13, _16, _18 ],	# tosty
	[ 3.0, _12, _16, 4.0, _14, 4.0, 1.0, 2.0, _13, _15 ],	# zupa pomidorowa
	[ 2.0, _13, _17, 3.0, _15, 3.0, _12, 1.0, _14, _16 ],	# rosol
	[ 5.0, 2.0, _14, 6.0, _12, 6.0, 3.0, 4.0, 1.0, _13 ],	# losos z piekarnika
	[ 7.0, 4.0, _12, 8.0, 2.0, 8.0, 5.0, 6.0, 3.0, 1.0 ]	# salatka warzywna
]
	

calorific = \
[
	[ 1.0, 2.0, 8.0, _12, 5.0, 4.0, 6.0, 3.0, 7.0, 9.0 ],	# gyros 
	[ _12, 1.0, 7.0, _13, 4.0, 3.0, 5.0, 2.0, 6.0, 8.0 ],	# sushi
	[ _18, _17, 1.0, _19, _14, _15, _13, _16, _12, 2.0 ],	# salatka owocowa
	[ 2.0, 3.0, 9.0, 1.0, 6.0, 5.0, 7.0, 4.0, 8.0, 9.0 ],	# pizza
	[ _15, _14, 4.0, _16, 1.0, _12, 2.0, _13, 3.0, 5.0 ],	# jajecznica
	[ _14, _13, 5.0, _15, 2.0, 1.0, 3.0, _12, 4.0, 6.0 ],	# tosty
	[ _16, _15, 3.0, _17, _12, _13, 1.0, _14, 2.0, 4.0 ],	# zupa pomidorowa
	[ _13, _12, 6.0, _14, 3.0, 2.0, 4.0, 1.0, 5.0, 7.0 ],	# rosol
	[ _17, _16, 2.0, _18, _13, _14, _12, _15, 1.0, 3.0 ],	# losos z piekarnika
	[ _19, _18, _12, _19, _15, _16, _14, _17, _13, 1.0 ]	# salatka warzywna
]


simplicity = \
[
	[ 1.0, 3.0, _17, 2.0, _15, _14, _12, _13, _16, _18 ],	# gyros 
	[ _13, 1.0, _19, _12, _17, _16, _14, _15, _18, _19 ],	# sushi
	[ 7.0, 9.0, 1.0, 8.0, 3.0, 4.0, 6.0, 5.0, 2.0, _12 ],	# salatka owocowa
	[ _12, 2.0, _18, 1.0, _16, _15, _13, _14, _17, _19 ],	# pizza
	[ 5.0, 7.0, _13, 6.0, 1.0, 2.0, 4.0, 3.0, _12, _14 ],	# jajecznica
	[ 4.0, 6.0, _14, 5.0, _12, 1.0, 3.0, 2.0, _13, _15 ],	# tosty
	[ 2.0, 4.0, _16, 3.0, _14, _13, 1.0, _12, _15, _17 ],	# zupa pomidorowa
	[ 3.0, 5.0, _15, 4.0, _13, _12, 2.0, 1.0, _14, _16 ],	# rosol
	[ 6.0, 8.0, _12, 7.0, 2.0, 3.0, 5.0, 4.0, 1.0, _13 ],	# losos z piekarnika
	[ 8.0, 9.0, 2.0, 9.0, 4.0, 5.0, 7.0, 6.0, 3.0, 1.0 ]	# salatka warzywna
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
	