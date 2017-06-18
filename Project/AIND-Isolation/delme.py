def score(a,b):
    return float(1)

scores = [(1,4),(2,2),(2,2),(2,2)]
print (max(scores))
"""
    def maximum2(self, game, player):
        """
           Get the minimum of all the scores
        """
        #print ("<Max>")
        
        moves =  game.get_legal_moves()
        if len(moves) == 0:
            return ((-1,-1))
        print ("-->Max: for moves " + str(moves))
        if not moves:
            return ((-1,-1))
        nextMoves = []
        for m in moves:
            tNm = self.minimum(game.forecast_move(m), game.get_opponent(player))
            
            if tNm == (-1,-1):
                continue
            print ("Max: Adding " + str(tNm))
            nextMoves.append(tNm)
        #print ("Max: for moves" + str(moves) + " submove is " + str(nextMoves))
        if len(nextMoves) == 0:
            print ("Max: No moves left");
            nextMoves = moves
            
        if len(nextMoves) > 0:
            print ("Max: for moves" + str(moves) + " submove is " + str(nextMoves))
            
            newgame = game.forecast_move(m) 
            _,moves = max([(self.score(newgame, self), m) for m in nextMoves])
            
            print ("Max: Selected max move" + str(moves))
            
        
        print ("<--Max: " + str (moves) + " len = " + str(len(moves)))
        return (moves)
        
            def minimum1 (self, game, player):
        """
           Get the minimum of all the scores
        """
        #print ("<Min>")

        moves =  game.get_legal_moves()
        print ("-->" + minStr +  " for moves " + str(moves))
        nextMoves = []
        if len(moves) == 0:
            return ((-1,-1))
        if not moves:
            return ((-1,-1))        
        for m in moves:
            tNm = self.maximum(game.forecast_move(m), game.get_opponent(player))
            if tNm == (-1,-1):
                continue #this move can be discarded 
            print (minStr + " Adding " + str(tNm))
            nextMoves.append(tNm)
        if len(nextMoves) == 0:
            print (minStr + " No moves left");
            nextMoves = moves
            
        if len(nextMoves) > 0: 
            print (minStr +  " for moves" + str(moves) + " submove is " + str(nextMoves))
            
            newgame = game.forecast_move(m)
            _,moves = min([(self.score(newgame, self), m) for m in nextMoves])
            
            print (minStr + " Selected min move" + str(moves))

        print ("<-- " + minStr +    str (moves)+" len = " + str(len(moves)))
        return (moves)
    
    
        def getMinOrMax (self, game, player, moves, type):
        """
           Get the minimum of all the scores
        """
        if type == 1:
            debug_print ("info","--> In Min")
            _,move = max([(self.score(game.forecast_move(m), self), m) for m in moves])
        if type == 0:
            debug_print ("info", "--> In Max")
            _,move = min([(self.score(game.forecast_move(m), self), m) for m in moves])
        return (move)
        
        """
