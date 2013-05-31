import Tkinter
import math
import diet_selector

class DietSelectorGUI:
    gradHeight = 50
    windowWidth = 800
    groups = ( -255, -226, -198, -170, -141, -113, -85, -56, -28, 0, 28, 56, 85, 113, 141, 170, 198, 226, 255 )
    criteriaPairs = []
    beltPosOffset = 130
    finished = False
    userChoicesMatrix = [ [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], ]
	
    def __init__( self, root ):
        self.preparePairs()
    
        C = Tkinter.Canvas( root, bg = 'white', height = 330, width = self.windowWidth, cursor = 'hand2' )
        C.pack()
        C.bind( '<Motion>', lambda event: self.OnMouseMove( event, C ) )
        C.bind( '<Button-1>', lambda event: self.OnMouseClick( event, C ) )

        buttonsOffsetX = 100
        buttonOffsetY = 90
        
        orderLabel = Tkinter.Label( root, text = 'You can choose which criterion should be displayed as first:', bg = 'white' )
        orderLabel.place( x = self.windowWidth / 2 - 155, y = buttonOffsetY - 30, height = 30, width = 320 )
        
        priceButton = Tkinter.Button( root, relief = 'groove', text = diet_selector.CRITERIA[0] )
        priceButton.place( x = buttonsOffsetX, y = buttonOffsetY, height = 30, width = 100 )
        priceButton.bind( '<Button-1>', lambda event: self.OnOrderButtonClick( event, diet_selector.CRITERIA[0], C ) )
        
        nourButton = Tkinter.Button( root, relief = 'groove', text = diet_selector.CRITERIA[1] )
        nourButton.place( x = buttonsOffsetX + 100, y = buttonOffsetY, height = 30, width = 100 )
        nourButton.bind( '<Button-1>', lambda event: self.OnOrderButtonClick( event, diet_selector.CRITERIA[1], C ) )
        
        timeButton = Tkinter.Button( root, relief = 'groove', text = diet_selector.CRITERIA[2] )
        timeButton.place( x = buttonsOffsetX + 200, y = buttonOffsetY, height = 30, width = 100 )
        timeButton.bind( '<Button-1>', lambda event: self.OnOrderButtonClick( event, diet_selector.CRITERIA[2], C ) )
        
        digestibilityButton = Tkinter.Button( root, relief = 'groove', text = diet_selector.CRITERIA[3] )
        digestibilityButton.place( x = buttonsOffsetX + 300, y = buttonOffsetY, height = 30, width = 100 )
        digestibilityButton.bind( '<Button-1>', lambda event: self.OnOrderButtonClick( event, diet_selector.CRITERIA[3], C ) )
        
        calorificButton = Tkinter.Button( root, relief = 'groove', text = diet_selector.CRITERIA[4] )
        calorificButton.place( x = buttonsOffsetX + 400, y = buttonOffsetY, height = 30, width = 100 )
        calorificButton.bind( '<Button-1>', lambda event: self.OnOrderButtonClick( event, diet_selector.CRITERIA[4], C ) )
        
        simplicityButton = Tkinter.Button( root, relief = 'groove', text = diet_selector.CRITERIA[5] )
        simplicityButton.place( x = buttonsOffsetX + 500, y = buttonOffsetY, height = 30, width = 100 )
        simplicityButton.bind( '<Button-1>', lambda event: self.OnOrderButtonClick( event, diet_selector.CRITERIA[5], C ) )
        
        self.drawHeader( C )
        self.drawGroups( C )
        self.drawCurrentCritPair( C )
        
    def OnOrderButtonClick( self, event, criterion, canvas ):
        orderedCriteria = []
        removedCriteria = []
        for crit in self.criteriaPairs:
            if( crit[0] == criterion ):
                orderedCriteria.append( [crit[0], crit[1]] )
            elif( crit[1] == criterion ):
                orderedCriteria.append( [crit[1], crit[0]] )
            else:
                removedCriteria.append( crit )
                
        orderedCriteria += removedCriteria
        
        self.criteriaPairs = []
        for crit in orderedCriteria:
            self.criteriaPairs.append( crit )
        print self.criteriaPairs
        print '-------------------------------------------------------------------------'
        self.OnMouseMove( event, canvas )

    def drawHeader( self, canvas ):
        canvas.create_rectangle( 2, 2, self.windowWidth, 50, fill = 'snow' )
        canvas.create_text( self.windowWidth / 2, self.beltPosOffset + 10,
                       text = 'What is more important?', font = ( 'Calibri', 13 ), fill = 'black' )
        canvas.create_text( self.windowWidth / 2, self.beltPosOffset - 115,
                       text = 'Choose between:', font = ( 'Calibri', 9 ), fill = 'black' )
        canvas.create_text( self.windowWidth / 2, self.beltPosOffset - 95,
                       text = ', '.join( diet_selector.COURSES ), font = ( 'Calibri', 9 ), fill = 'black' )
                       
    def drawCurrentCritPair( self, canvas ):
        canvas.create_text( self.windowWidth / 2 - 150, self.beltPosOffset + 20,
                            text = self.criteriaPairs[0][0], font = ( "Calibri", 16 ),  fill = 'black' )
        canvas.create_text( self.windowWidth / 2 + 150, self.beltPosOffset + 20,
                            text = self.criteriaPairs[0][1], font = ( "Calibri", 16 ),  fill = 'black' )
        
    def setNextCritPair( self ):
        del self.criteriaPairs[0]
        
    def preparePairs( self ):
        criteriaCount = len( diet_selector.CRITERIA )
        for i in range( 0, criteriaCount ):
            for j in range( i + 1, criteriaCount ):
                self.criteriaPairs.append( [diet_selector.CRITERIA[i], diet_selector.CRITERIA[j]] )
        
    def OnMouseClick( self, event, canvas ):
        if( self.finished ):
            return
            
        x = self.findIndex( event.x - self.windowWidth / 2 ) - 9
        if( x == 1 or x == -1 ):
            None
        elif( x < 0 ):
            None
        else:
            None
        
        self.updateUserChoice( x )
        
        if( len( self.criteriaPairs ) != 0 ):
            self.setNextCritPair()
        
        self.OnMouseMove( event, canvas )
        
    def updateUserChoice( self, x ):
        if( len( self.criteriaPairs ) == 0 ):
            return
        leftFromPair  = self.criteriaPairs[0][0]
        rightFromPair = self.criteriaPairs[0][1]
        
        leftIndex  = diet_selector.CRITERIA.index( leftFromPair )
        rightIndex = diet_selector.CRITERIA.index( rightFromPair )
        
        if( x < -1 ):
            self.userChoicesMatrix[leftIndex][rightIndex] = abs( x ) * 1.0
            self.userChoicesMatrix[rightIndex][leftIndex] = 1.0 / abs( x )
        elif( x > -1 ):
            self.userChoicesMatrix[rightIndex][leftIndex] = x * 1.0
            self.userChoicesMatrix[leftIndex][rightIndex] = 1.0 / x
        
        """s = [[str(e) for e in row] for row in self.userChoicesMatrix]
        lens = [len(max(col, key=len)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print '--------------------------------------------------'
        print '\n'.join(table)"""
        
    def drawSummary( self, canvas ):
        if( self.finished ):
            return
        self.finished = True
        
        print '------------------ user matrix ------------------------------'
        s = [[str(e) for e in row] for row in self.userChoicesMatrix]
        lens = [len(max(col, key=len)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print '\n'.join(table)
        user          = diet_selector.normalizeVertically( self.userChoicesMatrix )
        price         = diet_selector.normalizeVertically( diet_selector.price )
        nour          = diet_selector.normalizeVertically( diet_selector.nour )
        time          = diet_selector.normalizeVertically( diet_selector.time )
        digestibility = diet_selector.normalizeVertically( diet_selector.digestibility )
        calorific     = diet_selector.normalizeVertically( diet_selector.calorific )
        simplicity    = diet_selector.normalizeVertically( diet_selector.simplicity )
        s0 = diet_selector.calcMatrixWithAvgRows( user )
        s  = diet_selector.calcMatrixWithAvgRows( price, nour, time, digestibility, calorific, simplicity )
        r  = diet_selector.calcDecisionValues( s0, s )
        u  = diet_selector.prepareDecisionVector( r )
        
        result = ['', '', '', '', '', '', '', '', '', '']
        index = 0
        for i in u:
            result[i-1] = diet_selector.COURSES[index]
            index += 1

        print '------------------ user matrix afgre normalization ------------------------------'
        s = [[str(e) for e in row] for row in user]
        lens = [len(max(col, key=len)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print '\n'.join(table)
        print '------------------------------------------------'
        print diet_selector.RI
        if( diet_selector.isMatrixConsistence( user, diet_selector.RI ) ):
            canvas.create_text( self.windowWidth / 2, 110 + self.beltPosOffset,
                                text = 'Top 3 choices:', font = ( 'Calibri', 13 ), fill = 'black' )
            canvas.create_text( self.windowWidth / 2, 130 + self.beltPosOffset,
                                text = '1. ' + result[0], font = ( 'Calibri', 15 ), fill = 'black' )
            canvas.create_text( self.windowWidth / 2, 150 + self.beltPosOffset,
                                text = '2. ' + result[1], font = ( 'Calibri', 13 ), fill = 'black' )
            canvas.create_text( self.windowWidth / 2, 170 + self.beltPosOffset,
                                text = '3. ' + result[2], font = ( 'Calibri', 11 ), fill = 'black' )
        else:
            canvas.create_text( self.windowWidth / 2, 110 + self.beltPosOffset,
                                text = 'The choice is inconsitence!', font = ( 'Calibri', 15 ), fill = 'r' )
    
    def OnMouseMove( self, event, canvas ):
        canvas.delete( "all" )
    
        if( self.finished ):
            self.drawHeader( canvas )
            self.drawGroups( canvas )
            self.drawSummary( canvas )
            return
    
        x = self.findIndex( event.x - self.windowWidth / 2 )
        if( x is not 8 and x is not 10 ):
            self.drawGradient( canvas, self.windowWidth / 2, 0, self.groups[x] + self.windowWidth / 2, self.gradHeight )
        else:
            canvas.create_rectangle( self.groups[8] + self.windowWidth / 2,
                                    0 + self.beltPosOffset, self.groups[10] + self.windowWidth / 2, 50 + self.beltPosOffset, fill = 'grey' )
            canvas.create_text( self.windowWidth / 2, 70 + self.beltPosOffset, text = 'EQUAL', fill = 'red' )
        self.drawGroups( canvas )
        
        self.drawHeader( canvas )
        
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
root.title( 'Diet selector' )
app = DietSelectorGUI( root )
root.mainloop()