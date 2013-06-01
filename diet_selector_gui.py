import Tkinter
import math
import diet_selector

class DietSelectorGUI:
    gradHeight = 50
    windowWidth = 800
    windowHeight = 390
    groups = ( -255, -226, -198, -170, -141, -113, -85, -56, -28, 0, 28, 56, 85, 113, 141, 170, 198, 226, 255 )
    criteriaPairs = []
    beltPosOffset = 190
    finished = False
    resultInconsistence = False
    userChoicesMatrix = [ [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], ]
	
    def __init__( self, root ):
        self.preparePairs()
    
        canvas = Tkinter.Canvas( root, bg = 'white', height = self.windowHeight, width = self.windowWidth, cursor = 'hand2' )
        canvas.pack()
        canvas.bind( '<Motion>', lambda event: self.OnMouseMove( event, canvas ) )
        canvas.bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvas ) )

        self.createHeader( root )
        self.createButtons( root, canvas )
        self.createSelectionQuestion()
        self.drawGroups( canvas )
        self.drawCurrentCritPair( canvas )
        
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

        self.OnMouseMove( event, canvas )

    def createButtons( self, root, canvas ):
        buttonsOffsetX = 100
        buttonOffsetY = 90
        
        orderLabel = Tkinter.Label( root, text = 'You can choose which criterion should be displayed as first:', bg = 'white' )
        orderLabel.place( x = self.windowWidth / 2 - 155, y = buttonOffsetY - 30, height = 30, width = 320 )
        
        priceButton = Tkinter.Button( root, relief = 'groove', text = diet_selector.CRITERIA[0] )
        priceButton.place( x = buttonsOffsetX, y = buttonOffsetY, height = 30, width = 100 )
        priceButton.bind( '<Button-1>', lambda event: self.OnOrderButtonClick( event, diet_selector.CRITERIA[0], canvas ) )
        
        nourButton = Tkinter.Button( root, relief = 'groove', text = diet_selector.CRITERIA[1] )
        nourButton.place( x = buttonsOffsetX + 100, y = buttonOffsetY, height = 30, width = 100 )
        nourButton.bind( '<Button-1>', lambda event: self.OnOrderButtonClick( event, diet_selector.CRITERIA[1], canvas ) )
        
        timeButton = Tkinter.Button( root, relief = 'groove', text = diet_selector.CRITERIA[2] )
        timeButton.place( x = buttonsOffsetX + 200, y = buttonOffsetY, height = 30, width = 100 )
        timeButton.bind( '<Button-1>', lambda event: self.OnOrderButtonClick( event, diet_selector.CRITERIA[2], canvas ) )
        
        digestibilityButton = Tkinter.Button( root, relief = 'groove', text = diet_selector.CRITERIA[3] )
        digestibilityButton.place( x = buttonsOffsetX + 300, y = buttonOffsetY, height = 30, width = 100 )
        digestibilityButton.bind( '<Button-1>', lambda event: self.OnOrderButtonClick( event, diet_selector.CRITERIA[3], canvas ) )
        
        calorificButton = Tkinter.Button( root, relief = 'groove', text = diet_selector.CRITERIA[4] )
        calorificButton.place( x = buttonsOffsetX + 400, y = buttonOffsetY, height = 30, width = 100 )
        calorificButton.bind( '<Button-1>', lambda event: self.OnOrderButtonClick( event, diet_selector.CRITERIA[4], canvas ) )
        
        simplicityButton = Tkinter.Button( root, relief = 'groove', text = diet_selector.CRITERIA[5] )
        simplicityButton.place( x = buttonsOffsetX + 500, y = buttonOffsetY, height = 30, width = 100 )
        simplicityButton.bind( '<Button-1>', lambda event: self.OnOrderButtonClick( event, diet_selector.CRITERIA[5], canvas ) )
        
        finishButton = Tkinter.Button( root, relief = 'groove', text ='Finish now' )
        finishButton.place( x = buttonsOffsetX + 250, y = buttonOffsetY + 35, height = 30, width = 100 )
        finishButton.bind( '<Button-1>', lambda event: self.OnFinishButtonClick( event, canvas ) )
        
    def OnFinishButtonClick( self, event, canvas ):
        self.drawSummary( canvas )
        self.criteriaPairs = []
        
        self.OnMouseMove( event, canvas )
        
    def createHeader( self, root ):
        frame = Tkinter.Frame( root, bg = 'white', bd = 2, relief = 'groove' )
        frame.place( x = 0, y = 0, width = self.windowWidth + 5, height = 50 )
    
        label1 = Tkinter.Label( frame, text = 'Choose between:', font = ( 'Calibri', 9 ), bg = 'snow' )
        label1.place( x = self.windowWidth / 2 - 50, y = 5 )
        
        label2 = Tkinter.Label( frame, text = ', '.join( diet_selector.COURSES ), font = ( 'Calibri', 9 ), bg = 'snow' )
        label2.place( x = 55, y = 25 )
		
    def createSelectionQuestion( self ):
        selectionQuestion = Tkinter.Label( text = 'What is more important?', font = ( 'Calibri', 13 ), bg = 'snow' )
        selectionQuestion.place( x = self.windowWidth / 2 - 90, y = self.beltPosOffset - 30 )
                       
    def drawCurrentCritPair( self, canvas ):
        if( len( self.criteriaPairs ) != 0 ):
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
        
    def drawSummary( self, canvas ):
        self.finished = True

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
        
        if( diet_selector.isMatrixConsistence( self.userChoicesMatrix, diet_selector.RI ) ):
            canvas.create_rectangle( self.windowWidth / 2 - 100, 85 + self.beltPosOffset,
                                     self.windowWidth / 2 + 100, 185 + self.beltPosOffset, fill = 'light green' )
            canvas.create_text( self.windowWidth / 2, 100 + self.beltPosOffset,
                                text = 'Top 3 choices:', font = ( 'Calibri', 13 ), fill = 'black' )
            canvas.create_text( self.windowWidth / 2, 130 + self.beltPosOffset,
                                text = '1. ' + result[0], font = ( 'Calibri', 15 ), fill = 'black' )
            canvas.create_text( self.windowWidth / 2, 150 + self.beltPosOffset,
                                text = '2. ' + result[1], font = ( 'Calibri', 13 ), fill = 'black' )
            canvas.create_text( self.windowWidth / 2, 170 + self.beltPosOffset,
                                text = '3. ' + result[2], font = ( 'Calibri', 11 ), fill = 'black' )
        else:
            self.resultInconsistence = True
            canvas.create_text( self.windowWidth / 2, 110 + self.beltPosOffset,
                                text = 'The choice is inconsistence!', font = ( 'Calibri', 15 ), fill = 'red' )
    
    def OnMouseMove( self, event, canvas ):
        canvas.delete( "all" )
    
        if( self.finished ):
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