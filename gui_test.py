import Tkinter
import math

class DietSelectorGUI:
    gradHeight = 50
    windowWidth = 800
    groups = ( -255, -226, -198, -170, -141, -113, -85, -56, -28, 0, 28, 56, 85, 113, 141, 170, 198, 226, 255 )
	
    def __init__( self, root ):
        C = Tkinter.Canvas( root, bg = "white", height = 100, width = self.windowWidth, cursor = 'hand2' )
        C.pack()
        C.bind( "<Motion>", lambda event: self.OnMouseMove( event, C ) )
        self.drawGroups( C )

    def OnMouseMove( self, event, canvas ):
        canvas.delete( "all" )
        x = self.findIndex( event.x - self.windowWidth / 2 )
        if( x is not 8 and x is not 10 ):
            self.drawGradient( canvas, self.windowWidth / 2, 0, self.groups[x] + self.windowWidth / 2, self.gradHeight )
        else:
            canvas.create_rectangle( self.groups[8] + self.windowWidth / 2, 0, self.groups[10] + self.windowWidth / 2, 50, fill = 'black' )
            canvas.create_text( self.windowWidth / 2, 70, text = 'EQUAL', fill = 'red' )
        self.drawGroups( canvas )
        
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
    
        for i in range( 0, len( self.groups ) ):
            groupValue = self.groups[i]
            canvas.create_line( self.windowWidth / 2 + groupValue, 40, self.windowWidth / 2 + groupValue, self.gradHeight + bottomOffset, fill = 'red' )
            if( i != len( self.groups ) / 2 ):
                canvas.create_text( self.windowWidth / 2 + groupValue, self.gradHeight + bottomOffset + textOffset, text = str( abs( i - 9 ) ) )

        # first group
        pos = self.groups[0]
        canvas.create_line( self.windowWidth / 2 + pos, 20, self.windowWidth / 2 + pos, self.gradHeight + criticalGroupsOffset, fill = 'red' )
        
        # middle group
        pos = self.groups[len( self.groups ) / 2]
        canvas.create_line( self.windowWidth / 2 + pos, 20, self.windowWidth / 2 + pos, self.gradHeight + criticalGroupsOffset, fill = 'red' )
        
        # last group
        pos = self.groups[len( self.groups ) - 1]
        canvas.create_line( self.windowWidth / 2 + pos, 20, self.windowWidth / 2 + pos, self.gradHeight + criticalGroupsOffset, fill = 'red' )
    
    def drawGradient( self, canvas, x1, y1, x2, h ):
        if( x1 <= x2 ):
            if( x2 - x1 > 255 ):
                x2 = x1 + 255
            for offset in range( x1, x2 ):
                color = 255 - ( offset - x1 )
                gradColor = '#%02x%02x%02x' % ( color, color, color )
                canvas.create_line( offset, y1, offset, y1 + h, fill = gradColor )
        else:
            if( x1 - x2 > 255 ):
                x2 = x1 - 255
            for offset in range( x2, x1 ):
                color = 255 - ( x1 - offset )
                gradColor = '#%02x%02x%02x' % ( color, color, color )
                canvas.create_line( offset, y1, offset, y1 + h, fill = gradColor )

root = Tkinter.Tk()
app = DietSelectorGUI( root )
root.mainloop()