import diet_selector
import unittest

class TestDietSelector( unittest.TestCase ):
	def setUp( self ):
		# matrices based on the L5Z2
		self.m0 = [[    1.0,     3.0,     7.0, 9.0],
				   [1.0/3.0,     1.0,     3.0, 7.0],
				   [1.0/7.0, 1.0/3.0,     1.0, 3.0],
				   [1.0/9.0, 1.0/7.0, 1.0/3.0, 1.0]]
			  
		self.m1 = [[    1.0,     1.0, 7.0],
				   [    1.0,     1.0, 3.0],
				   [1.0/7.0, 1.0/3.0, 1.0]]
			  
		self.m2 = [[1.0, 1.0/5.0, 1.0],
				   [5.0,     1.0, 3.0],
				   [1.0, 1.0/3.0, 1.0]]
				   
		self.m3 = [[    1.0,     1.0, 7.0],
				   [    1.0,     1.0, 3.0],
				   [1.0/7.0, 1.0/3.0, 1.0]]
			  
		self.m4 = [[    1.0, 7.0, 9.0],
				   [1.0/7.0, 1.0, 1.0],
				   [1.0/9.0, 1.0, 1.0]]
				   
	def test_normalizeVertically( self ):
		diet_selector.normalizeVertically( self.m0 )
		self.assertEqual( self.m0, 
			[[0.63,   0.6702127659574468,  0.6176470588235293, 0.45],
			 [0.21,  0.22340425531914893,  0.2647058823529412, 0.35],
			 [0.09,  0.07446808510638298, 0.08823529411764705, 0.15],
			 [0.07, 0.031914893617021274, 0.02941176470588235, 0.05]] )		
		 
	def test_makeMatrixWithAvgRows_singleMatrix( self ):
		diet_selector.normalizeVertically( self.m0 )
		s = diet_selector.calcMatrixWithAvgRows( self.m0 );
		self.assertEqual( s,
			[[0.5919649561952441, 0.2620275344180225, 0.1006758448060075, 0.045331664580725906]] )
			
	def test_makeMatrixWithAvgRows_multipleMatrices( self ):
		diet_selector.normalizeVertically( self.m1 )
		diet_selector.normalizeVertically( self.m2 )
		diet_selector.normalizeVertically( self.m3 )
		diet_selector.normalizeVertically( self.m4 )
		s = diet_selector.calcMatrixWithAvgRows( self.m1, self.m2, self.m3, self.m4 );
		self.assertEqual( s,
			[[0.5105339105339105, 0.3893217893217893, 0.10014430014430013],
			 [0.1577639751552795, 0.6554865424430641, 0.1867494824016563],
			 [0.5105339105339105, 0.3893217893217893, 0.10014430014430013],
			 [0.7978093167966587, 0.10531475088437114, 0.09687593231897029]] )

	def test_calcDecisionValues( self ):
		diet_selector.normalizeVertically( self.m0 )
		diet_selector.normalizeVertically( self.m1 )
		diet_selector.normalizeVertically( self.m2 )
		diet_selector.normalizeVertically( self.m3 )
		diet_selector.normalizeVertically( self.m4 )
		s0 = diet_selector.calcMatrixWithAvgRows( self.m0 );
		s  = diet_selector.calcMatrixWithAvgRows( self.m1, self.m2, self.m3, self.m4 );
		r  = diet_selector.calcDecisionValues( s0, s )
		self.assertEqual( r,
			[0.43112114650883737, 0.4461897715261283, 0.12268908196503436] )
			
	def test_prepareDecisionVector( self ):
		diet_selector.normalizeVertically( self.m0 )
		diet_selector.normalizeVertically( self.m1 )
		diet_selector.normalizeVertically( self.m2 )
		diet_selector.normalizeVertically( self.m3 )
		diet_selector.normalizeVertically( self.m4 )
		s0 = diet_selector.calcMatrixWithAvgRows( self.m0 );
		s  = diet_selector.calcMatrixWithAvgRows( self.m1, self.m2, self.m3, self.m4 );
		r  = diet_selector.calcDecisionValues( s0, s )
		u  = diet_selector.prepareDecisionVector( r )
		self.assertEqual( u, [2, 1, 3] )

			
if __name__ == '__main__':			
	suite = unittest.TestLoader().loadTestsFromTestCase( TestDietSelector )
	unittest.TextTestRunner( verbosity = 2 ).run( suite )
	