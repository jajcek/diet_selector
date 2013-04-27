k1 = [[1.0,         3.0,     7.0, 9.0],
	  [1.0/3.0,     1.0,     3.0, 7.0],
	  [1.0/7.0, 1.0/3.0,     1.0, 3.0],
	  [1.0/9.0, 1.0/7.0, 1.0/3.0, 1.0]]

def main():
	normalizeVertically( k1 )
	print k1
	
def normalizeVertically( matrix ):
	'Normalize the given matrix vertically'

	# sum all of the columns
	colSums = [sum(x) for x in zip(*matrix)]
	print colSums
		
	# use the colSums to divide values in the given matrix	
	colCount = len( k1[0] )
	rowCount = len( k1 )
	for col in range( colCount ):
		for row in range( rowCount ):
			matrix[row][col] /= colSums[col]

if __name__ == '__main__':
	main()