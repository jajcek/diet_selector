import diet_selector
import unittest

class TestDietSelector( unittest.TestCase ):
	def setUp( self ):
		self.k1 = [[1.0,         3.0,     7.0, 9.0],
				   [1.0/3.0,     1.0,     3.0, 7.0],
				   [1.0/7.0, 1.0/3.0,     1.0, 3.0],
				   [1.0/9.0, 1.0/7.0, 1.0/3.0, 1.0]]
				   
	def test_normalizeVertically( self ):
		diet_selector.normalizeVertically( self.k1 )
		self.assertEqual( self.k1, 
			[[0.63,   0.6702127659574468,  0.6176470588235293, 0.45],
			 [0.21,  0.22340425531914893,  0.2647058823529412, 0.35],
			 [0.09,  0.07446808510638298, 0.08823529411764705, 0.15],
			 [0.07, 0.031914893617021274, 0.02941176470588235, 0.05]] )		
		 
	def test_makeMatrixWithAvgRows( self ):
		diet_selector.normalizeVertically( self.k1 )
		s = diet_selector.makeMatrixWithAvgRows( self.k1 );
		self.assertEqual( s,
			[[0.5919649561952441, 0.2620275344180225, 0.1006758448060075, 0.045331664580725906]] )
			
if __name__ == '__main__':			
	suite = unittest.TestLoader().loadTestsFromTestCase( TestDietSelector )
	unittest.TextTestRunner( verbosity = 2 ).run( suite )