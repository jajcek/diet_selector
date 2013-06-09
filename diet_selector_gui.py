import Tkinter
import ttk
import math
import diet_selector

class DietSelectorGUI:
    gradHeight = 10
    windowWidth = 800
    windowHeight = 390
    
    # pixel positions for the grouping lines
    groups = ( -255, -226, -198, -170, -141, -113, -85, -56, -28, 0, 28, 56, 85, 113, 141, 170, 198, 226, 255 )
    
    # list of all possible pairs
    criteriaPairs = []
    
    beltPosOffset = 0
    beltHeight = 30;
    userChoicesMatrix = [ [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], ]
	
    def __init__( self, root ):
        self.preparePairs()
    
        nothing = Tkinter.Canvas( root, bg = 'white', height = 27, width = self.windowWidth, cursor = 'hand2' )
        nothing.pack()
        self.createHeader( root )
        
        resultCanvas = Tkinter.Canvas( root, bg = 'white', height = 100, width = self.windowWidth )
        
        canvases = [Tkinter.Canvas()]*15
        
        canvases[0] = Tkinter.Canvas( root, bg = 'white', highlightthickness = 0, height = self.beltHeight, width = self.windowWidth, cursor = 'hand2' )
        canvases[0].pack()
        canvases[0].bind( '<Motion>', lambda event: self.OnMouseMove( event, canvases[0], 0 ) )
        canvases[0].bind( '<Leave>', lambda event: self.onMouseOut( event, canvases[0], 0 ) )
        canvases[0].bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvases[0], resultCanvas, 0 ) )
        
        canvases[1] = Tkinter.Canvas( root, bg = 'white', highlightthickness = 0, height = self.beltHeight, width = self.windowWidth, cursor = 'hand2' )
        canvases[1] .pack()
        canvases[1] .bind( '<Motion>', lambda event: self.OnMouseMove( event, canvases[1] , 1 ) )
        canvases[1] .bind( '<Leave>', lambda event: self.onMouseOut( event, canvases[1] , 1 ) )
        canvases[1] .bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvases[1], resultCanvas, 1 ) )
        
        canvases[2] = Tkinter.Canvas( root, bg = 'white', highlightthickness = 0, height = self.beltHeight, width = self.windowWidth, cursor = 'hand2' )
        canvases[2].pack()
        canvases[2].bind( '<Motion>', lambda event: self.OnMouseMove( event, canvases[2], 2 ) )
        canvases[2].bind( '<Leave>', lambda event: self.onMouseOut( event, canvases[2], 2 ) )
        canvases[2].bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvases[2], resultCanvas, 2 ) )
        
        canvases[3] = Tkinter.Canvas( root, bg = 'white', highlightthickness = 0, height = self.beltHeight, width = self.windowWidth, cursor = 'hand2' )
        canvases[3].pack()
        canvases[3].bind( '<Motion>', lambda event: self.OnMouseMove( event, canvases[3], 3 ) )
        canvases[3].bind( '<Leave>', lambda event: self.onMouseOut( event, canvases[3], 3 ) )
        canvases[3].bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvases[3], resultCanvas, 3 ) )
        
        canvases[4] = Tkinter.Canvas( root, bg = 'white', highlightthickness = 0, height = self.beltHeight, width = self.windowWidth, cursor = 'hand2' )
        canvases[4].pack()
        canvases[4].bind( '<Motion>', lambda event: self.OnMouseMove( event, canvases[4], 4 ) )
        canvases[4].bind( '<Leave>', lambda event: self.onMouseOut( event, canvases[4], 4 ) )
        canvases[4].bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvases[4], resultCanvas, 4 ) )
        
        canvases[5] = Tkinter.Canvas( root, bg = 'white', highlightthickness = 0, height = self.beltHeight, width = self.windowWidth, cursor = 'hand2' )
        canvases[5].pack()
        canvases[5].bind( '<Motion>', lambda event: self.OnMouseMove( event, canvases[5], 5 ) )
        canvases[5].bind( '<Leave>', lambda event: self.onMouseOut( event, canvases[5], 5 ) )
        canvases[5].bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvases[5], resultCanvas, 5 ) )
       
        canvases[6] = Tkinter.Canvas( root, bg = 'white', highlightthickness = 0, height = self.beltHeight, width = self.windowWidth, cursor = 'hand2' )
        canvases[6].pack()
        canvases[6].bind( '<Motion>', lambda event: self.OnMouseMove( event, canvases[6], 6 ) )
        canvases[6].bind( '<Leave>', lambda event: self.onMouseOut( event, canvases[6], 6 ) )
        canvases[6].bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvases[6], resultCanvas, 6 ) )
        
        canvases[7] = Tkinter.Canvas( root, bg = 'white', highlightthickness = 0, height = self.beltHeight, width = self.windowWidth, cursor = 'hand2' )
        canvases[7].pack()
        canvases[7].bind( '<Motion>', lambda event: self.OnMouseMove( event, canvases[7], 7 ) )
        canvases[7].bind( '<Leave>', lambda event: self.onMouseOut( event, canvases[7], 7 ) )
        canvases[7].bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvases[7], resultCanvas, 7 ) )
        
        canvases[8] = Tkinter.Canvas( root, bg = 'white', highlightthickness = 0, height = self.beltHeight, width = self.windowWidth, cursor = 'hand2' )
        canvases[8].pack()
        canvases[8].bind( '<Motion>', lambda event: self.OnMouseMove( event, canvases[8], 8 ) )
        canvases[8].bind( '<Leave>', lambda event: self.onMouseOut( event, canvases[8], 8 ) )
        canvases[8].bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvases[8], resultCanvas, 8 ) )
        
        canvases[9] = Tkinter.Canvas( root, bg = 'white', highlightthickness = 0, height = self.beltHeight, width = self.windowWidth, cursor = 'hand2' )
        canvases[9].pack()
        canvases[9].bind( '<Motion>', lambda event: self.OnMouseMove( event, canvases[9], 9 ) )
        canvases[9].bind( '<Leave>', lambda event: self.onMouseOut( event, canvases[9], 9 ) )
        canvases[9].bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvases[9], resultCanvas, 9 ) )
        
        canvases[10] = Tkinter.Canvas( root, bg = 'white', highlightthickness = 0, height = self.beltHeight, width = self.windowWidth, cursor = 'hand2' )
        canvases[10].pack()
        canvases[10].bind( '<Motion>', lambda event: self.OnMouseMove( event, canvases[10], 10 ) )
        canvases[10].bind( '<Leave>', lambda event: self.onMouseOut( event, canvases[10], 10 ) )
        canvases[10].bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvases[10], resultCanvas, 10 ) )
        
        canvases[11] = Tkinter.Canvas( root, bg = 'white', highlightthickness = 0, height = self.beltHeight, width = self.windowWidth, cursor = 'hand2' )
        canvases[11].pack()
        canvases[11].bind( '<Motion>', lambda event: self.OnMouseMove( event, canvases[11], 11 ) )
        canvases[11].bind( '<Leave>', lambda event: self.onMouseOut( event, canvases[11], 11 ) )
        canvases[11].bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvases[11], resultCanvas, 11 ) )
        
        canvases[12] = Tkinter.Canvas( root, bg = 'white', highlightthickness = 0, height = self.beltHeight, width = self.windowWidth, cursor = 'hand2' )
        canvases[12].pack()
        canvases[12].bind( '<Motion>', lambda event: self.OnMouseMove( event, canvases[12], 12 ) )
        canvases[12].bind( '<Leave>', lambda event: self.onMouseOut( event, canvases[12], 12 ) )
        canvases[12].bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvases[12], resultCanvas, 12 ) )
        
        canvases[13] = Tkinter.Canvas( root, bg = 'white', highlightthickness = 0, height = self.beltHeight, width = self.windowWidth, cursor = 'hand2' )
        canvases[13].pack()
        canvases[13].bind( '<Motion>', lambda event: self.OnMouseMove( event, canvases[13], 13 ) )
        canvases[13].bind( '<Leave>', lambda event: self.onMouseOut( event, canvases[13], 13 ) )
        canvases[13].bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvases[13], resultCanvas, 13 ) )
        
        canvases[14] = Tkinter.Canvas( root, bg = 'white', highlightthickness = 0, height = self.beltHeight, width = self.windowWidth, cursor = 'hand2' )
        canvases[14].pack()
        canvases[14].bind( '<Motion>', lambda event: self.OnMouseMove( event, canvases[14], 14 ) )
        canvases[14].bind( '<Leave>', lambda event: self.onMouseOut( event, canvases[14], 14 ) )
        canvases[14].bind( '<Button-1>', lambda event: self.OnMouseClick( event, canvases[14], resultCanvas, 14 ) )
        
        resultCanvas.pack()

        for canvas in canvases:
            self.drawGroups( canvas )
            self.drawCritPair( canvas, canvases.index( canvas ) )
            canvas.create_text( self.windowWidth / 2, 15 + self.beltPosOffset, text = 'EQUAL', fill = 'red' )
            
        self.updateResultBars( resultCanvas )

    def OnMouseClick( self, event, canvas, resultCanvas, pairNumber ):
        """ Event that is invoked during mouse click. It checks what a user clicked and sets new pair if exists. 
            It also invokes the OnMouseMove at the end, so see that function. """
        x = self.findIndex( event.x - self.windowWidth / 2 ) - 9
        self.updateUserChoice( x, pairNumber )
        self.updateResultBars( resultCanvas )
        self.OnMouseMove( event, canvas, pairNumber )
                                
    def OnMouseMove( self, event, canvas, pairNumber ):
        """ Event that is invoked during mouse move. It simpy redraws the belt with current pair (if exists).
            This also draws summary if no pair has been found. """
    
        canvas.delete( "all" )
    
        self.drawChosenBelt( event, canvas, pairNumber )
        self.drawBelt( event, canvas )
        self.drawGroups( canvas )
        self.drawCritPair( canvas, pairNumber ) 
        
    def onMouseOut( self, event, canvas, pairNumber ):
        canvas.delete( 'all' )
        self.drawChosenBelt( event, canvas, pairNumber )
        self.drawGroups( canvas )
        self.drawCritPair( canvas, pairNumber ) 
        
    def updateUserChoice( self, x, pairNumber ):
        """ Updates user choice by filling up the user matrix in the appropriate places
            (taken from criteriaPairs). """

        leftFromPair  = self.criteriaPairs[pairNumber][0]
        rightFromPair = self.criteriaPairs[pairNumber][1]
        
        leftIndex  = diet_selector.CRITERIA.index( leftFromPair )
        rightIndex = diet_selector.CRITERIA.index( rightFromPair )
        
        # note that we fill here the value that is needed
        # as well as the opposite value
        if( x < -1 ):
            self.userChoicesMatrix[leftIndex][rightIndex] = abs( x ) * 1.0
            self.userChoicesMatrix[rightIndex][leftIndex] = 1.0 / abs( x )
        else:
            self.userChoicesMatrix[rightIndex][leftIndex] = abs( x ) * 1.0
            self.userChoicesMatrix[leftIndex][rightIndex] = 1.0 / abs( x )    
        
    def updateResultBars( self, canvas ):
        """ Draws summary for the user. """
        canvas.delete( 'all' )
    
        # calculate all necessary values by using functions from diet_delector.py
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

        offsetY = -110
        offsetX = -100
        #canvas.create_rectangle( self.windowWidth / 2 - 100, 85 + self.beltPosOffset + offsetY,
        #                         self.windowWidth / 2 + 100, 185 + self.beltPosOffset + offsetY, fill = 'light green' )
        canvas.create_text( self.windowWidth / 2 + offsetX, 120 + offsetY, anchor = 'e',
                            text = diet_selector.COURSES[0], font = ( 'Calibri', 10 ), fill = 'black' )
        canvas.create_rectangle( self.windowWidth / 2 + offsetX + 10, 115 + offsetY,
                                 self.windowWidth / 2 + offsetX + r[0] * 1000, 125 + self.beltPosOffset + offsetY, fill = 'light green' )
                            
        canvas.create_text( self.windowWidth / 2 + offsetX, 135 + offsetY, anchor = 'e',
                            text = diet_selector.COURSES[1], font = ( 'Calibri', 10 ), fill = 'black' )
        canvas.create_rectangle( self.windowWidth / 2 + offsetX + 10, 130 + offsetY,
                                 self.windowWidth / 2 + offsetX + r[1] * 1000, 140 + self.beltPosOffset + offsetY, fill = 'light green' )
                            
        canvas.create_text( self.windowWidth / 2 + offsetX, 150 + offsetY, anchor = 'e',
                            text = diet_selector.COURSES[2], font = ( 'Calibri', 10 ), fill = 'black' )
        canvas.create_rectangle( self.windowWidth / 2 + offsetX + 10, 145 + offsetY,
                                 self.windowWidth / 2 + offsetX + r[2] * 1000, 155 + self.beltPosOffset + offsetY, fill = 'light green' )
                            
        canvas.create_text( self.windowWidth / 2 + offsetX, 165 + offsetY, anchor = 'e',
                            text = diet_selector.COURSES[3], font = ( 'Calibri', 10 ), fill = 'black' )
        canvas.create_rectangle( self.windowWidth / 2 + offsetX + 10, 160 + offsetY,
                                 self.windowWidth / 2 + offsetX + r[3] * 1000, 170 + self.beltPosOffset + offsetY, fill = 'light green' )
                            
        canvas.create_text( self.windowWidth / 2 + offsetX, 180 + offsetY, anchor = 'e',
                            text = diet_selector.COURSES[4], font = ( 'Calibri', 10 ), fill = 'black' )
        canvas.create_rectangle( self.windowWidth / 2 + offsetX + 10, 175 + offsetY,
                                 self.windowWidth / 2 + offsetX + r[4] * 1000, 185 + self.beltPosOffset + offsetY, fill = 'light green' )
                                 
        
        consistence = diet_selector.countMatrixConsistency( self.userChoicesMatrix, diet_selector.RI )

        consistencyPercent = 100 - ( consistence / 0.1 * 100.0 )
        if( not diet_selector.isMatrixConsistence( self.userChoicesMatrix, diet_selector.RI ) ):
            consistencyPercent = min( -( 100 - ( consistence / 0.1 * 100.0 ) ), 100 )
            canvas.create_text( self.windowWidth / 2, 200 + offsetY,
                                text = 'The choice is inconsistent! (' + str( int( consistencyPercent ) ) + '%)', font = ( 'Calibri', 13 ), fill = 'red' )
        else:
            canvas.create_text( self.windowWidth / 2, 200 + offsetY,
                                text = 'The choice is consistent. (' + str( int( consistencyPercent ) ) + '%)', font = ( 'Calibri', 13 ), fill = 'dark green' )
        
    def OnFinishButtonClick( self, event, canvas ):
        """ Function that is invoked by clicking on the 'Finish now' button. """
    
        if( self.finished ):
            return
    
        self.finished = True
    
        self.drawSummary( canvas )
        self.criteriaPairs = []
        
        self.OnMouseMove( event, canvas )
        
    def createHeader( self, root ):
        """ Displays buttons which will show window to modify decision values. """
    
        buttonsOffsetX = 0
        buttonOffsetY = 0
        
        priceButton = Tkinter.Button( root, relief = 'groove', text = 'Modify ' + diet_selector.CRITERIA[0] )
        priceButton.place( x = buttonsOffsetX, y = buttonOffsetY, height = 30, width = 130 )
        priceButton.bind( '<Button-1>', lambda event: self.onShowWindow( diet_selector.CRITERIA[0] ) )
        
        nourButton = Tkinter.Button( root, relief = 'groove', text = 'Modify ' + diet_selector.CRITERIA[1] )
        nourButton.place( x = buttonsOffsetX + 130, y = buttonOffsetY, height = 30, width = 130 )
        nourButton.bind( '<Button-1>', lambda event: self.onShowWindow( diet_selector.CRITERIA[1] ) )
        
        timeButton = Tkinter.Button( root, relief = 'groove', text = 'Modify ' + diet_selector.CRITERIA[2] )
        timeButton.place( x = buttonsOffsetX + 260, y = buttonOffsetY, height = 30, width = 130 )
        timeButton.bind( '<Button-1>', lambda event: self.onShowWindow( diet_selector.CRITERIA[2] ) )
        
        digestibilityButton = Tkinter.Button( root, relief = 'groove', text = 'Modify ' + diet_selector.CRITERIA[3] )
        digestibilityButton.place( x = buttonsOffsetX + 390, y = buttonOffsetY, height = 30, width = 130 )
        digestibilityButton.bind( '<Button-1>', lambda event: self.onShowWindow( diet_selector.CRITERIA[3] ) )
        
        calorificButton = Tkinter.Button( root, relief = 'groove', text = 'Modify ' + diet_selector.CRITERIA[4] )
        calorificButton.place( x = buttonsOffsetX + 520, y = buttonOffsetY, height = 30, width = 130 )
        calorificButton.bind( '<Button-1>', lambda event: self.onShowWindow( diet_selector.CRITERIA[4] ) )
        
        simplicityButton = Tkinter.Button( root, relief = 'groove', text = 'Modify ' + diet_selector.CRITERIA[5] )
        simplicityButton.place( x = buttonsOffsetX + 650, y = buttonOffsetY, height = 30, width = 160 )
        simplicityButton.bind( '<Button-1>', lambda event: self.onShowWindow( diet_selector.CRITERIA[5] ) )

    def onShowWindow( self, criterion ):
        self.wdw = wdw = Tkinter.Toplevel()
        wdw.geometry( '660x165' )
        
        frame = Tkinter.Frame( wdw, bd = 2, relief = 'groove' )
        frame.place( x = 0, y = 0, width = 661, height = 200 )
        
        for i in range( len( diet_selector.COURSES ) ):
            Tkinter.Label( frame, text = diet_selector.COURSES[i] ).grid( row = 0, column = i + 1 )
        for i in range( len( diet_selector.COURSES ) ):
            Tkinter.Label( frame, text = diet_selector.COURSES[i] ).grid( row = i + 1, column = 0 )
        for i in range( len( diet_selector.COURSES ) ):
            for j in range( len( diet_selector.COURSES ) ):
                if( i == j ):
                    Tkinter.Label( frame, text = '1.0' ).grid( row = i + 1, column = j + 1 )
        
        label1 = Tkinter.Label( frame, text = '1.0' )
        label1.grid( row = 1, column = 2 )
        if( criterion == diet_selector.CRITERIA[0] ): label1.config( text = str( diet_selector.price[0][1] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): label1.config( text = str( diet_selector.nour[0][1] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): label1.config( text = str( diet_selector.time[0][1] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): label1.config( text = str( diet_selector.digestibility[0][1] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): label1.config( text = str( diet_selector.calorific[0][1] ) )
        else: label1.config( text = str( diet_selector.simplicity[0][1] ) )
        
        label2 = Tkinter.Label( frame, text = '1.0' )
        label2.grid( row = 1, column = 3 )
        if( criterion == diet_selector.CRITERIA[0] ): label2.config( text = str( diet_selector.price[0][2] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): label2.config( text = str( diet_selector.nour[0][2] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): label2.config( text = str( diet_selector.time[0][2] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): label2.config( text = str( diet_selector.digestibility[0][2] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): label2.config( text = str( diet_selector.calorific[0][2] ) )
        else: label2.config( text = str( diet_selector.simplicity[0][2] ) )
        
        label3 = Tkinter.Label( frame, text = '1.0' )
        label3.grid( row = 1, column = 4 )
        if( criterion == diet_selector.CRITERIA[0] ): label3.config( text = str( diet_selector.price[0][3] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): label3.config( text = str( diet_selector.nour[0][3] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): label3.config( text = str( diet_selector.time[0][1] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): label3.config( text = str( diet_selector.digestibility[0][3] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): label3.config( text = str( diet_selector.calorific[0][3] ) )
        else: label3.config( text = str( diet_selector.simplicity[0][3] ) )
        
        label4 = Tkinter.Label( frame, text = '1.0' )
        label4.grid( row = 1, column = 5 )
        if( criterion == diet_selector.CRITERIA[0] ): label4.config( text = str( diet_selector.price[0][4] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): label4.config( text = str( diet_selector.nour[0][4] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): label4.config( text = str( diet_selector.time[0][4] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): label4.config( text = str( diet_selector.digestibility[0][4] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): label4.config( text = str( diet_selector.calorific[0][4] ) )
        else: label4.config( text = str( diet_selector.simplicity[0][4] ) )
        
        label5 = Tkinter.Label( frame, text = '1.0' )
        label5.grid( row = 2, column = 3 )
        if( criterion == diet_selector.CRITERIA[0] ): label5.config( text = str( diet_selector.price[1][2] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): label5.config( text = str( diet_selector.nour[1][2] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): label5.config( text = str( diet_selector.time[1][2] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): label5.config( text = str( diet_selector.digestibility[1][2] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): label5.config( text = str( diet_selector.calorific[1][2] ) )
        else: label5.config( text = str( diet_selector.simplicity[1][2] ) )
        
        label6 = Tkinter.Label( frame, text = '1.0' )
        label6.grid( row = 2, column = 4 )
        if( criterion == diet_selector.CRITERIA[0] ): label6.config( text = str( diet_selector.price[1][3] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): label6.config( text = str( diet_selector.nour[1][3] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): label6.config( text = str( diet_selector.time[1][3] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): label6.config( text = str( diet_selector.digestibility[1][3] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): label6.config( text = str( diet_selector.calorific[1][3] ) )
        else: label6.config( text = str( diet_selector.simplicity[1][3] ) )
        
        label7 = Tkinter.Label( frame, text = '1.0' )
        label7.grid( row = 2, column = 5 )
        if( criterion == diet_selector.CRITERIA[0] ): label7.config( text = str( diet_selector.price[1][4] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): label7.config( text = str( diet_selector.nour[1][4] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): label7.config( text = str( diet_selector.time[1][4] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): label7.config( text = str( diet_selector.digestibility[1][4] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): label7.config( text = str( diet_selector.calorific[1][4] ) )
        else: label7.config( text = str( diet_selector.simplicity[1][4] ) )
        
        label8 = Tkinter.Label( frame, text = '1.0' )
        label8.grid( row = 3, column = 4 )
        if( criterion == diet_selector.CRITERIA[0] ): label8.config( text = str( diet_selector.price[2][3] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): label8.config( text = str( diet_selector.nour[2][3] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): label8.config( text = str( diet_selector.time[2][3] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): label8.config( text = str( diet_selector.digestibility[2][3] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): label8.config( text = str( diet_selector.calorific[2][3] ) )
        else: label8.config( text = str( diet_selector.simplicity[2][3] ) )
        
        label9 = Tkinter.Label( frame, text = '1.0' )
        label9.grid( row = 3, column = 5 )
        if( criterion == diet_selector.CRITERIA[0] ): label9.config( text = str( diet_selector.price[2][4] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): label9.config( text = str( diet_selector.nour[2][4] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): label9.config( text = str( diet_selector.time[2][4] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): label9.config( text = str( diet_selector.digestibility[2][4] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): label9.config( text = str( diet_selector.calorific[2][4] ) )
        else: label9.config( text = str( diet_selector.simplicity[2][4] ) )
        
        label10 = Tkinter.Label( frame, text = '1.0' )
        label10.grid( row = 4, column = 5 )
        if( criterion == diet_selector.CRITERIA[0] ): label10.config( text = str( diet_selector.price[3][4] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): label10.config( text = str( diet_selector.nour[3][4] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): label10.config( text = str( diet_selector.time[3][4] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): label10.config( text = str( diet_selector.digestibility[3][4] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): label10.config( text = str( diet_selector.calorific[3][4] ) )
        else: label10.config( text = str( diet_selector.simplicity[3][4] ) )
        
        #--------------------------------
        realNums = ( '9.0000', '8.0000', '7.0000', '6.0000', '5.0000', '4.0000', '3.0000', '2.0000', '1.0000',
            '0.5000', '0.3333', '0.2500', '0.2000', '0.1667', '0.1429', '0.1250', '0.1111' )
        nums = ( '9', '8', '7', '6', '5', '4', '3', '2', 'EQUAL', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9' )
        v1 = Tkinter.StringVar()
        v1.trace( 'w', lambda name, index, mode, sv = v1: self.onComboboxChange( sv, 2, 1, label1, criterion ) )
        c1 = ttk.Combobox( frame, textvar = v1, values = nums, state = 'readonly', width = 14 )
        c1.grid( row = 2, column = 1 )
        if( criterion == diet_selector.CRITERIA[0] ): c1.current( realNums.index( '%.4f' % diet_selector.price[1][0] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): c1.current( realNums.index( '%.4f' % diet_selector.nour[1][0] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): c1.current( realNums.index( '%.4f' % diet_selector.time[1][0] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): c1.current( realNums.index( '%.4f' % diet_selector.digestibility[1][0] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): c1.current( realNums.index( '%.4f' % diet_selector.calorific[1][0] ) )
        else: c1.current( realNums.index( '%.4f' % diet_selector.simplicity[1][0] ) )
        
        v2 = Tkinter.StringVar()
        v2.trace( 'w', lambda name, index, mode, sv = v2: self.onComboboxChange( sv, 3, 1, label2, criterion ) )
        c2 = ttk.Combobox( frame, textvar = v2, values = nums, state = 'readonly', width = 14 )
        c2.grid( row = 3, column = 1 )
        if( criterion == diet_selector.CRITERIA[0] ): c2.current( realNums.index( '%.4f' % diet_selector.price[2][0] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): c2.current( realNums.index( '%.4f' % diet_selector.nour[2][0] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): c2.current( realNums.index( '%.4f' % diet_selector.time[2][0] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): c2.current( realNums.index( '%.4f' % diet_selector.digestibility[2][0] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): c2.current( realNums.index( '%.4f' % diet_selector.calorific[2][0] ) )
        else: c2.current( realNums.index( '%.4f' % diet_selector.simplicity[2][0] ) )
        
        v3 = Tkinter.StringVar()
        v3.trace( 'w', lambda name, index, mode, sv = v3: self.onComboboxChange( sv, 3, 2, label5, criterion ) )
        c3 = ttk.Combobox( frame, textvar = v3, values = nums, state = 'readonly', width = 14 )
        c3.grid( row = 3, column = 2 )
        if( criterion == diet_selector.CRITERIA[0] ): c3.current( realNums.index( '%.4f' % diet_selector.price[2][1] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): c3.current( realNums.index( '%.4f' % diet_selector.nour[2][1] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): c3.current( realNums.index( '%.4f' % diet_selector.time[2][1] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): c3.current( realNums.index( '%.4f' % diet_selector.digestibility[2][1] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): c3.current( realNums.index( '%.4f' % diet_selector.calorific[2][1] ) )
        else: c3.current( realNums.index( '%.4f' % diet_selector.simplicity[2][1] ) )
        
        v4 = Tkinter.StringVar()
        v4.trace( 'w', lambda name, index, mode, sv = v4: self.onComboboxChange( sv, 4, 1, label3, criterion ) )
        c4 = ttk.Combobox( frame, textvar = v4, values = nums, state = 'readonly', width = 14 )
        c4.grid( row = 4, column = 1 )
        if( criterion == diet_selector.CRITERIA[0] ): c4.current( realNums.index( '%.4f' % diet_selector.price[3][0] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): c4.current( realNums.index( '%.4f' % diet_selector.nour[3][0] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): c4.current( realNums.index( '%.4f' % diet_selector.time[3][0] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): c4.current( realNums.index( '%.4f' % diet_selector.digestibility[3][0] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): c4.current( realNums.index( '%.4f' % diet_selector.calorific[3][0] ) )
        else: c4.current( realNums.index( '%.4f' % diet_selector.simplicity[3][0] ) )
        
        v5 = Tkinter.StringVar()
        v5.trace( 'w', lambda name, index, mode, sv = v5: self.onComboboxChange( sv, 4, 2, label6, criterion ) )
        c5 = ttk.Combobox( frame, textvar = v5, values = nums, state = 'readonly', width = 14 )
        c5.grid( row = 4, column = 2 )
        if( criterion == diet_selector.CRITERIA[0] ): c5.current( realNums.index( '%.4f' % diet_selector.price[3][1] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): c5.current( realNums.index( '%.4f' % diet_selector.nour[3][1] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): c5.current( realNums.index( '%.4f' % diet_selector.time[3][1] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): c5.current( realNums.index( '%.4f' % diet_selector.digestibility[3][1] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): c5.current( realNums.index( '%.4f' % diet_selector.calorific[3][1] ) )
        else: c5.current( realNums.index( '%.4f' % diet_selector.simplicity[3][1] ) )
        
        v6 = Tkinter.StringVar()
        v6.trace( 'w', lambda name, index, mode, sv = v6: self.onComboboxChange( sv, 4, 3, label8, criterion ) )
        c6 = ttk.Combobox( frame, textvar = v6, values = nums, state = 'readonly', width = 14 )
        c6.grid( row = 4, column = 3 )
        if( criterion == diet_selector.CRITERIA[0] ): c6.current( realNums.index( '%.4f' % diet_selector.price[3][2] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): c6.current( realNums.index( '%.4f' % diet_selector.nour[3][2] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): c6.current( realNums.index( '%.4f' % diet_selector.time[3][2] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): c6.current( realNums.index( '%.4f' % diet_selector.digestibility[3][2] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): c6.current( realNums.index( '%.4f' % diet_selector.calorific[3][2] ) )
        else: c6.current( realNums.index( '%.4f' % diet_selector.simplicity[3][2] ) )
        
        v7 = Tkinter.StringVar()
        v7.trace( 'w', lambda name, index, mode, sv = v7: self.onComboboxChange( sv, 5, 1, label4, criterion ) )
        c7 = ttk.Combobox( frame, textvar = v7, values = nums, state = 'readonly', width = 14 )
        c7.grid( row = 5, column = 1 )
        if( criterion == diet_selector.CRITERIA[0] ): c7.current( realNums.index( '%.4f' % diet_selector.price[4][0] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): c7.current( realNums.index( '%.4f' % diet_selector.nour[4][0] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): c7.current( realNums.index( '%.4f' % diet_selector.time[4][0] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): c7.current( realNums.index( '%.4f' % diet_selector.digestibility[4][0] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): c7.current( realNums.index( '%.4f' % diet_selector.calorific[4][0] ) )
        else: c7.current( realNums.index( '%.4f' % diet_selector.simplicity[4][0] ) )
        
        v8 = Tkinter.StringVar()
        v8.trace( 'w', lambda name, index, mode, sv = v8: self.onComboboxChange( sv, 5, 2, label7, criterion ) )
        c8 = ttk.Combobox( frame, textvar = v8, values = nums, state = 'readonly', width = 14 )
        c8.grid( row = 5, column = 2 )
        if( criterion == diet_selector.CRITERIA[0] ): c8.current( realNums.index( '%.4f' % diet_selector.price[4][1] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): c8.current( realNums.index( '%.4f' % diet_selector.nour[4][1] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): c8.current( realNums.index( '%.4f' % diet_selector.time[4][1] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): c8.current( realNums.index( '%.4f' % diet_selector.digestibility[4][1] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): c8.current( realNums.index( '%.4f' % diet_selector.calorific[4][1] ) )
        else: c8.current( realNums.index( '%.4f' % diet_selector.simplicity[4][1] ) )
        
        v9 = Tkinter.StringVar()
        v9.trace( 'w', lambda name, index, mode, sv = v9: self.onComboboxChange( sv, 5, 3, label9, criterion ) )
        c9 = ttk.Combobox( frame, textvar = v9, values = nums, state = 'readonly', width = 14 )
        c9.grid( row = 5, column = 3 )
        if( criterion == diet_selector.CRITERIA[0] ): c9.current( realNums.index( '%.4f' % diet_selector.price[4][2] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): c9.current( realNums.index( '%.4f' % diet_selector.nour[4][2] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): c9.current( realNums.index( '%.4f' % diet_selector.time[4][2] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): c9.current( realNums.index( '%.4f' % diet_selector.digestibility[4][2] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): c9.current( realNums.index( '%.4f' % diet_selector.calorific[4][2] ) )
        else: c9.current( realNums.index( '%.4f' % diet_selector.simplicity[4][2] ) )
        
        v10 = Tkinter.StringVar()
        v10.trace( 'w', lambda name, index, mode, sv = v10: self.onComboboxChange( sv, 5, 4, label10, criterion ) )
        c10 = ttk.Combobox( frame, textvar = v10, values = nums, state = 'readonly', width = 14 )
        c10.grid( row = 5, column = 4 )
        if( criterion == diet_selector.CRITERIA[0] ): c10.current( realNums.index( '%.4f' % diet_selector.price[4][3] ) )
        elif( criterion == diet_selector.CRITERIA[1] ): c10.current( realNums.index( '%.4f' % diet_selector.nour[4][3] ) )
        elif( criterion == diet_selector.CRITERIA[2] ): c10.current( realNums.index( '%.4f' % diet_selector.time[4][3] ) )
        elif( criterion == diet_selector.CRITERIA[3] ): c10.current( realNums.index( '%.4f' % diet_selector.digestibility[4][3] ) )
        elif( criterion == diet_selector.CRITERIA[4] ): c10.current( realNums.index( '%.4f' % diet_selector.calorific[4][3] ) )
        else: c10.current( realNums.index( '%.4f' % diet_selector.simplicity[4][3] ) )
        
        applyButton = Tkinter.Button( frame, text = 'Close', relief = 'groove', command = self.destroyAll )
        applyButton.place( x = 0, y = 140, width = 657, height = 23 )
        
        wdw.transient( root )
        wdw.grab_set()
        
    def destroyAll( self ):
        self.wdw.destroy()
        
    def onComboboxChange( self, sv, i, j, label, criterion ):
        val = sv.get()
        if( len( val ) > 1 and val[1] == '/' ):
            val += '.0'
            
        if( val == 'EQUAL' ):
            if( criterion == diet_selector.CRITERIA[0] ):
                diet_selector.price[i-1][j-1] = 1.0
                diet_selector.price[j-1][i-1] = 1.0
            elif( criterion == diet_selector.CRITERIA[1] ):
                diet_selector.nour[i-1][j-1] = 1.0
                diet_selector.nour[j-1][i-1] = 1.0
            elif( criterion == diet_selector.CRITERIA[2] ):
                diet_selector.time[i-1][j-1] = 1.0
                diet_selector.time[j-1][i-1] = 1.0
            elif( criterion == diet_selector.CRITERIA[3] ):
                diet_selector.digestibility[i-1][j-1] = 1.0
                diet_selector.digestibility[j-1][i-1] = 1.0
            elif( criterion == diet_selector.CRITERIA[4] ):
                diet_selector.calorific[i-1][j-1] = 1.0
                diet_selector.calorific[j-1][i-1] = 1.0
            else:
                diet_selector.simplicity[i-1][j-1] = 1.0
                diet_selector.simplicity[j-1][i-1] = 1.0
            label.config( text = '1.0' )
        else:
            if( criterion == diet_selector.CRITERIA[0] ):
                diet_selector.price[i-1][j-1] = eval( val )
                diet_selector.price[j-1][i-1] = 1.0 / eval( val )
            elif( criterion == diet_selector.CRITERIA[1] ):
                diet_selector.nour[i-1][j-1] = eval( val )
                diet_selector.nour[j-1][i-1] = 1.0 / eval( val )
            elif( criterion == diet_selector.CRITERIA[2] ):
                diet_selector.time[i-1][j-1] = eval( val )
                diet_selector.time[j-1][i-1] = 1.0 / eval( val )
            elif( criterion == diet_selector.CRITERIA[3] ):
                diet_selector.digestibility[i-1][j-1] = eval( val )
                diet_selector.digestibility[j-1][i-1] = 1.0 / eval( val )
            elif( criterion == diet_selector.CRITERIA[4] ):
                diet_selector.calorific[i-1][j-1] = eval( val )
                diet_selector.calorific[j-1][i-1] = 1.0 / eval( val )
            else:
                diet_selector.simplicity[i-1][j-1] = eval( val )
                diet_selector.simplicity[j-1][i-1] = 1.0 / eval( val )
            label.config( text = str( 1.0 / eval( val ) ) )

        #print '-----------'
        #print diet_selector.debugMatrix( diet_selector.price )
        #print '-----------'
        
    def createSelectionQuestion( self ):
        """ Displays question text above the belt. """
    
        selectionQuestion = Tkinter.Label( text = 'What is more important?', font = ( 'Calibri', 13 ), bg = 'snow' )
        selectionQuestion.place( x = self.windowWidth / 2 - 90, y = self.beltPosOffset - 30 )
                       
    def drawCritPair( self, canvas, pairNumber ):
        """ Draws current pair that has been set by setNextCritPait(). """
    
        canvas.create_text( self.windowWidth / 2 - 280, self.beltPosOffset + 10,
                            text = self.criteriaPairs[pairNumber][0], font = ( "Calibri", 12 ), 
                            anchor = 'e', fill = 'black' )
        canvas.create_text( self.windowWidth / 2 + 280, self.beltPosOffset + 10,
                            text = self.criteriaPairs[pairNumber][1], font = ( "Calibri", 12 ),
                            anchor = 'w', fill = 'black' )
        
    def preparePairs( self ):
        """ Creates list of all possible pairs. It doesn't count (x,y) and (y,x), but only one of them. """
    
        criteriaCount = len( diet_selector.CRITERIA )
        for i in range( 0, criteriaCount ):
            for j in range( i + 1, criteriaCount ):
                self.criteriaPairs.append( [diet_selector.CRITERIA[i], diet_selector.CRITERIA[j]] )
        
    def drawBelt( self, event, canvas ):
        """ Draws the belt that allows user to choose his answer. """
    
        x = self.findIndex( event.x - self.windowWidth / 2 )
        
        if( x != 8 and x != 10 ):  # if user doesn't select -1 or 1, then draw gradient
            self.drawGrayGradient( canvas, self.windowWidth / 2, 0, self.groups[x] + self.windowWidth / 2, self.gradHeight )
        else:  # otherwise draw rectagle and text EQUAL
            canvas.create_text( self.windowWidth / 2, 15 + self.beltPosOffset, text = 'EQUAL', fill = 'red' )
            
    def drawChosenBelt( self, event, canvas, pairNumber ):
        """ Draws the belt that allows user to choose his answer. """
        
        leftIndex  = diet_selector.CRITERIA.index( self.criteriaPairs[pairNumber][0] )
        rightIndex = diet_selector.CRITERIA.index( self.criteriaPairs[pairNumber][1] )
        
        lv = self.userChoicesMatrix[leftIndex][rightIndex]
        rv = self.userChoicesMatrix[rightIndex][leftIndex]
        x = 0
        if rv < 1.0:
            x = ( 9 - lv )
        else:
            x = rv + 9

        if( x != 8 and x != 10 ):
            self.drawGreenGradient( canvas, self.windowWidth / 2, 0, self.groups[int(x)] + self.windowWidth / 2, self.gradHeight )
        else:
            #canvas.create_rectangle( self.groups[8] + self.windowWidth / 2,
            #                        0 + self.beltPosOffset, self.groups[10] + self.windowWidth / 2, 20 + self.beltPosOffset, fill = 'light grey' )
            canvas.create_text( self.windowWidth / 2, 15 + self.beltPosOffset, text = 'EQUAL', fill = 'red' )
        
    def findIndex( self, x ):
        """ Find appropriate index from the group attribute. It is assumed that the distance between groups
            is 28 pixels (255/9) - 255 is from max colour and 9 is the amount of possible answers by a user. """
    
        index = int( math.ceil( x / 28 ) ) + 10
        if( index > 18 ):
            index = 18
        elif( index < 0 ):
            index = 0
        
        if( x < 0 ):
            index -= 1 if index > 0 else 0
        return index
	
    def drawGroups( self, canvas ):
        """ Draws grouping lines as well as labels below them """
    
        bottomOffset = 15
        criticalGroupsOffset = 3
        textOffset = 13
        lineColour = 'black'
    
        # draw base lines with numbers
        for i in range( 0, len( self.groups ) ):
            groupValue = self.groups[i]
            if( i != len( self.groups ) / 2 ):
                canvas.create_line( self.windowWidth / 2 + groupValue, 5 + self.beltPosOffset,
                                    self.windowWidth / 2 + groupValue, self.gradHeight + bottomOffset + self.beltPosOffset - 12,
                                    fill = lineColour )
            # draw numbers except for "0" in the middledont draw "0" in the middle
            if( i != len( self.groups ) / 2 ):
                canvas.create_text( self.windowWidth / 2 + groupValue, self.gradHeight + bottomOffset + textOffset + self.beltPosOffset - 20,
                                    font = ( 'Calibri', 7 ), text = str( abs( i - 9 ) ) )

        # make the first, middle and last line longer
        
        # first group
        pos = self.groups[0]
        canvas.create_line( self.windowWidth / 2 + pos, 10 + self.beltPosOffset, self.windowWidth / 2 + pos,
                            self.gradHeight + criticalGroupsOffset + self.beltPosOffset, fill = lineColour )
        

        
        # last group
        pos = self.groups[len( self.groups ) - 1]
        canvas.create_line( self.windowWidth / 2 + pos, 10 + self.beltPosOffset, self.windowWidth / 2 + pos,
                            self.gradHeight + criticalGroupsOffset + self.beltPosOffset, fill = lineColour )
    
    def drawGrayGradient( self, canvas, x1, y1, x2, h ):
        """ Draws gradient as a sequence of lines """
        
        if( x1 <= x2 ):
            if( x2 - x1 > 255 ):
                x2 = x1 + 255
            for offset in range( x1, x2 ):
                color = 255 - ( offset - x1 )
                gradColor = '#%02x%02x%02x' % ( color, color, color )
                canvas.create_line( offset, y1 + self.beltPosOffset, offset, y1 + h + self.beltPosOffset, fill = gradColor )
        else:
            if( x1 - x2 > 255 ):
                x2 = x1 - 255
            for offset in range( x2, x1 ):
                color = 255 - ( x1 - offset )
                gradColor = '#%02x%02x%02x' % ( color, color, color )
                canvas.create_line( offset, y1 + self.beltPosOffset, offset, y1 + h + self.beltPosOffset, fill = gradColor )
                
    def drawGreenGradient( self, canvas, x1, y1, x2, h ):
        """ Draws gradient as a sequence of lines """
        
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