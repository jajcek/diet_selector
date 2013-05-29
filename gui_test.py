import Tkinter

class DietSelectorGUI:
    gradHeight = 50
    windowWidth = 800
	
    def __init__( self, root ):
        C = Tkinter.Canvas( root, bg = "blue", height = self.gradHeight, width = self.windowWidth )
        C.pack()
        C.bind( "<Motion>", lambda event: self.OnMouseMove(event, C ) )
        #self.drawGradient( C, self.windowWidth / 2, 0, 700, self.gradHeight )
        #self.drawGradient( C, self.windowWidth / 2, 0, 300, self.gradHeight )

    def OnMouseMove( self, event, canvas ):
        canvas.delete( "all" )
        offset = 10
        
        self.drawGradient( canvas, self.windowWidth / 2, 0, event.x, self.gradHeight )
        
		
    def drawGradient( self, canvas, x1, y1, x2, h ):
        if( x1 <= x2 ):
            if( x2 - x1 > 255 ):
                x2 = x1 + 255
            for offset in range( x1, x2 ):
                color = offset - x1
                gradColor = '#%02x%02x%02x' % ( color, color, color )
                canvas.create_line( offset, y1, offset, y1 + h, fill = gradColor )
        else:
            if( x1 - x2 > 255 ):
                x2 = x1 - 255
            for offset in range( x2, x1 ):
                color = x1 - offset
                gradColor = '#%02x%02x%02x' % ( color, color, color )
                canvas.create_line( offset, y1, offset, y1 + h, fill = gradColor )

root = Tkinter.Tk()
app = DietSelectorGUI( root )
root.mainloop()