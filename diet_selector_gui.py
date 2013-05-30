import Tkinter
import math
import diet_selector

class DietSelectorGUI:
    gradHeight = 50
    windowWidth = 800
    groups = ( -255, -226, -198, -170, -141, -113, -85, -56, -28, 0, 28, 56, 85, 113, 141, 170, 198, 226, 255 )
    criteriaPairs = []
    beltPosOffset = 60
	
    def __init__( self, root ):
        self.preparePairs()
    
        C = Tkinter.Canvas( root, bg = "white", height = 200, width = self.windowWidth, cursor = 'hand2' )
        C.pack()
        C.bind( "<Motion>", lambda event: self.OnMouseMove( event, C ) )
        C.bind( "<Button-1>", lambda event: self.OnMouseClick( event, C ) )
        self.drawGroups( C )
        self.drawCurrentCritPair( C )

    def drawCurrentCritPair( self, canvas ):
        canvas.create_text( self.windowWidth / 2 - 150, self.beltPosOffset + 20, text = self.criteriaPairs[0][0], font = ( "Verdana", 16 ),  fill = 'black' )
        canvas.create_text( self.windowWidth / 2 + 150, self.beltPosOffset + 20, text = self.criteriaPairs[0][1], font = ( "Verdana", 16 ),  fill = 'black' )
        
    def setNextCritPair( self ):
        del self.criteriaPairs[0]
        
    def preparePairs( self ):
        criteriaCount = len( diet_selector.CRITERIA )
        for i in range( 0, criteriaCount ):
            for j in range( i + 1, criteriaCount ):
                self.criteriaPairs.append( ( diet_selector.CRITERIA[i], diet_selector.CRITERIA[j] ) )
        
    def OnMouseClick( self, event, canvas ):
        x = self.findIndex( event.x - self.windowWidth / 2 ) - 9
        if( x == 1 or x == -1 ):
            None
        elif( x < 0 ):
            None
        else:
            None
        
        if( len( self.criteriaPairs ) != 0 ):
            self.setNextCritPair()
        
        self.OnMouseMove( event, canvas )
        #print str( x )
        
    def drawSummary( self, canvas ):
        canvas.create_text( self.windowWidth / 2, 100 + self.beltPosOffset, text = 'SUMMARY', fill = 'black' )
    
    def OnMouseMove( self, event, canvas ):
        canvas.delete( "all" )
        x = self.findIndex( event.x - self.windowWidth / 2 )
        if( x is not 8 and x is not 10 ):
            self.drawGradient( canvas, self.windowWidth / 2, 0, self.groups[x] + self.windowWidth / 2, self.gradHeight )
        else:
            canvas.create_rectangle( self.groups[8] + self.windowWidth / 2,
                                    0 + self.beltPosOffset, self.groups[10] + self.windowWidth / 2, 50 + self.beltPosOffset, fill = 'grey' )
            canvas.create_text( self.windowWidth / 2, 70 + self.beltPosOffset, text = 'EQUAL', fill = 'red' )
        self.drawGroups( canvas )
        
        if( len( self.criteriaPairs ) == 0 ):
            self.drawSummary( canvas )
        else:
            self.drawCurrentCritPair( canvas )
        
    def findIndex( self, x ):
        index = int( math.ceil( x / 28 ) ) + 10
        if( index > 18 ):
            index = 18
        elif( index < 0 ):
            index = 0
        
        if( x < 0 ):
            index -= 1 if index > 0 else 0
        return index
	
    def drawGroups( self, canvas ):
        bottomOffset = 5
        criticalGroupsOffset = 8
        textOffset = 10
        lineColour = 'black'
    
        for i in range( 0, len( self.groups ) ):
            groupValue = self.groups[i]
            canvas.create_line( self.windowWidth / 2 + groupValue, 40 + self.beltPosOffset,
                                self.windowWidth / 2 + groupValue, self.gradHeight + bottomOffset + self.beltPosOffset,
                                fill = lineColour )
            if( i != len( self.groups ) / 2 ):
                canvas.create_text( self.windowWidth / 2 + groupValue, self.gradHeight + bottomOffset + textOffset + self.beltPosOffset,
                                    text = str( abs( i - 9 ) ) )

        # first group
        pos = self.groups[0]
        canvas.create_line( self.windowWidth / 2 + pos, 20 + self.beltPosOffset, self.windowWidth / 2 + pos,
                            self.gradHeight + criticalGroupsOffset + self.beltPosOffset, fill = lineColour )
        
        # middle group
        pos = self.groups[len( self.groups ) / 2]
        canvas.create_line( self.windowWidth / 2 + pos, 20 + self.beltPosOffset, self.windowWidth / 2 + pos,
                            self.gradHeight + criticalGroupsOffset + self.beltPosOffset, fill = lineColour )
        
        # last group
        pos = self.groups[len( self.groups ) - 1]
        canvas.create_line( self.windowWidth / 2 + pos, 20 + self.beltPosOffset, self.windowWidth / 2 + pos,
                            self.gradHeight + criticalGroupsOffset + self.beltPosOffset, fill = lineColour )
    
    def drawGradient( self, canvas, x1, y1, x2, h ):
        if( x1 <= x2 ):
            if( x2 - x1 > 255 ):
                x2 = x1 + 255
            for offset in range( x1, x2 ):
                color = 255 - ( offset - x1 )
                gradColor = '#%02x%02x%02x' % ( color, 255, color )
                canvas.create_line( offset, y1 + self.beltPosOffset, offset, y1 + h + self.beltPosOffset, fill = gradColor )
        else:
            if( x1 - x2 > 255 ):
                x2 = x1 - 255
            for offset in range( x2, x1 ):
                color = 255 - ( x1 - offset )
                gradColor = '#%02x%02x%02x' % ( color, 255, color )
                canvas.create_line( offset, y1 + self.beltPosOffset, offset, y1 + h + self.beltPosOffset, fill = gradColor )

root = Tkinter.Tk()
app = DietSelectorGUI( root )
root.mainloop()