"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


# Print level - "error" > "info" > "trace" > "debug"
gLevel = "none"

""" Debug print control mechanism.
    TODO: Need to find faster way, use  new file.
    
    Parameters
    ----------
    level : level of the print
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    str
        String to be printed

    Returns
    -------
    none
        
    """
def debug_print (level, str):
    if level == "none":
        return
    if level == "error" and (gLevel == "debug" or  gLevel == "trace" or gLevel == "info" or gLevel == "error"):
        print ("Error !!! " + str)
        return
            
    if level == "info" and (gLevel == "debug" or gLevel == "info" or gLevel == "trace"):
        print ("info: " + str)
        return
        
    if level == "trace"  and (gLevel == "debug" or  gLevel == "trace"):
        print (str)
        return



    if level == "debug" and gLevel == "debug":
        print ("$$$:" + str)
        return
    


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves)

    raise NotImplementedError


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    
    return (float(own_moves))
    raise NotImplementedError


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    debug_print ("debug",float(own_moves - opp_moves))
    return float(own_moves - opp_moves)
    raise NotImplementedError


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=4, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout
        self.bestmove = (-1,-1)


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            raise 
            debug_print ("error","Exception Raised")
            #pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move
    

    """ minimum for the recursive minimax.
        TODO: implementation returns moves also can be avoided.
        
        Parameters
        ----------
        game : game instance of board
        player: 
            current active player for the given board instance in 'game'
        depth: Current depth

        Returns
        -------
        score: Score
        move : move in tuple format
            
        """        

    def minimum (self, game, player, depth):
        """
           Get the minimum of all the scores
        """
        #Tag for prints
        strTag = "Min:"+"<"+str(depth)+">:"
        
        #Check timeout before proceding every time.
        if self.time_left() < self.TIMER_THRESHOLD:
            debug_print ("error",strTag+"-->timeout" +  str (self.bestmove))
            raise SearchTimeout()
        
        #legal moves
        moves =  game.get_legal_moves()
        debug_print ("trace","-->"+strTag+" for moves " + str(moves))
        
        #end of tree
        if not moves:
            debug_print ("debug","<--"+strTag+"Min: No moves left " + str(self.score (game, self)) )
            return (self.score (game,self),(-1,-1))
        
        #end of tree depth.
        if depth == 0:
            debug_print ("trace","<--"+strTag+" depth exhausted")
            #return (-2,(-1,-1))
            return (self.score (game, self), moves[0])
            
            
        #initialization
        tScore = -1
        scores = []
        nextMoves = []
        
        #Recursion for all moves, get score and put in array
        # TODO: nextMoves can be removed.
        for m in moves:
            newgame = game.forecast_move(m)
            debug_print ("debug",strTag+" max called for " + str(m))
            tScore,tMove = self.maximum(newgame, game.get_opponent(player), depth-1)
            debug_print ("debug",strTag+" Adding " + str(tScore) + " move " + str(m))
            scores.append(tScore)
            nextMoves.append(m)    
        
        #Minimize score, unrolling of recursion
        debug_print ("debug",strTag+" Minimizing " + str(scores) + " moves " +  str(nextMoves))
        tScore,tMove = min([(scores[i], nextMoves[i]) for i in range (0,len(scores))])
            
        debug_print ("trace","<--"+strTag+" Score is " + str(tScore) + " tMove" + str(tMove))
        
        return (tScore,tMove)
    """ maximum for the recursive minimax.
        TODO: implementation returns moves also can be avoided.
        It is better to have seperate maximum and minimum. 
        Visualization of code is easier.
        
        Parameters
        ----------
        game : game instance of board
        player: 
            current active player for the given board instance in 'game'
        depth: Current depth

        Returns
        -------
        score: Score
        move : move in tuple format
            
        """  
    def maximum (self, game, player,depth):
        """
           Get the minimum of all the scores
        """
        #Tag for prints
        strTag = "Max:"+"<"+str(depth)+">:"
        
        #Check timeout before proceding every time.
        if self.time_left() < self.TIMER_THRESHOLD:
            debug_print ("error","-->"+strTag+" timeout " + str (self.bestmove))
            raise SearchTimeout()
            
        #legal moves
        moves =  game.get_legal_moves()
        debug_print ("trace","-->"+strTag+" for moves " + str(moves))

        #end of tree
        if not moves:
            debug_print ("debug","<--"+strTag+" No moves left " + str(self.score (game, self)))
            return (self.score(game,self),(-1,-1))
        
        #end of tree depth.
        if depth == 0:
            debug_print ("trace","<--"+strTag+" depth exhausted")
            #return (self.score(self.bestmove,self),self.bestmove)
            return (self.score (game, self), moves[0])
        
        #initialization
        tScore = -1
        tMove = ()
        scores = []
        nextMoves = []
        
        #Recursion for all moves, get score and put in array
        # TODO: nextMoves can be removed.
        for m in moves:
            newgame = game.forecast_move(m)
            debug_print ("debug",strTag+" min called for " + str(m))
            tScore,tMove = self.minimum(newgame, game.get_opponent(player), depth-1)
                 
            debug_print ("debug",strTag+" Adding " + str(tScore) + " move " + str(m))
            scores.append(tScore)
            nextMoves.append(m)
        
        #Maximize score, unrolling of recursion
        debug_print ("debug",strTag+" Maximizing " + str(scores) + " moves " +  str(nextMoves))
        tScore,tMove = max([(scores[i], nextMoves[i]) for i in range (0,len(scores))])
            
        debug_print ("trace","<--"+strTag+" Score is " + str(tScore) + " tMove " + str(tMove))
        #Store best move available in case of errors like timeout
        self.bestmove = tMove
        return (tScore,tMove)

     

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        debug_print ("trace","Called MiniMax")
        
 
        if self.time_left() < self.TIMER_THRESHOLD:
            debug_print ("error","timeout")
            raise SearchTimeout()

        

        score = -1
        move= (-1,-1)
        try:
            debug_print ("debug","Maximum called " + str(depth))
            score, move = self.maximum(game, self, depth)
        except SearchTimeout:
            move = self.bestmove
            debug_print ("trace","MinMax: Exception" + str(move))
          
            
                
        return (move)


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left
        debug_print ("info", "Alpha-Beta-Search");
        bestMove = (-1,-1)
        try:
        #TODO how to get infinite number for int. 'import sys' is not allowed?
            for iDepth in range (0, 100000000000000000000000000):
                move = self.alphabeta (game, iDepth)
                if (move) != (-1,-1):
                    bestMove = move

        except SearchTimeout:
            pass
             
        
        
        #print ("Timeout: getMove result " + str (bestMove))
        return (bestMove)
        raise NotImplementedError

    """ minimum for the AlphaBeta.
        taken from minimum from MimiMax
        TODO: implementation returns moves also can be avoided.
        
        Parameters
        ----------
        game : game instance of board
        player: 
            current active player for the given board instance in 'game'
        depth: Current depth

        Returns
        -------
        score: Score
        move : move in tuple format
            
        """        
        
    def minimum (self, game, player,depth, alpha, beta):
        """
           Get the minimum of all the scores
        """
        #string for prints
        strTag = "Min:"+"<"+str(depth)+">:"
        
        #Check timeout before proceding every time.
        if self.time_left() < self.TIMER_THRESHOLD:
            debug_print ("error","-->"+strTag+" timeout " + str (self.bestmove))
            raise SearchTimeout()
        
        #legal moves
        moves =  game.get_legal_moves()
        debug_print ("trace","-->"+strTag+" for moves " + str(moves))
        
        #end of tree
        if not moves:
            debug_print ("debug","<--"+strTag+" No moves left " + str(self.score (game, self)))
            return (self.score(game,self),(-1,-1))
        
        #end of tree depth
        if depth == 0:
            debug_print ("trace","<--"+strTag+" depth exhausted")
            return (self.score (game, self), moves[0])
        
        #Initialize ready to go
        tScore = -1
        tMove = ()
        scores = []
        
        #Recursion for all moves, get scores and put in list.
        #nextMoves removed. 
        for m in moves:
            newgame = game.forecast_move(m)
            debug_print ("debug",strTag+" min called for " + str(m))
            tScore,tMove = self.maximum(newgame, game.get_opponent(player), depth-1, alpha, beta)
                 
            debug_print ("debug",strTag+" Adding " + str(tScore) + " move " + str(m))
            
            #Pruning
            if (tScore <= alpha):
                return (tScore, m)
               
            beta = min (tScore, beta)
            scores.append(tScore)       
        
        #Minimize move unrolling of recursion.
        debug_print ("info",strTag+" Minimizing " + str(scores) + " moves " +  str(moves))
        tScore,tMove = min([(scores[i], moves[i]) for i in range (0,len(scores))])
            
        debug_print ("trace","<--"+strTag+" Score is " + str(tScore) + " move " + str(tMove))
        
        return (tScore,tMove)
  
    """ maximum for the AlphaBeta.
        taken from minimum from MimiMax
        TODO: implementation returns moves also can be avoided.
        
        Parameters
        ----------
        game : game instance of board
        player: 
            current active player for the given board instance in 'game'
        depth: Current depth

        Returns
        -------
        score: Score
        move : move in tuple format
            
        """           
    def maximum (self, game, player,depth, alpha, beta):
        """
           Get the maximum of all the scores
        """
        
        #string for prints
        strTag = "Max:"+"<"+str(depth)+">:"
        
        #Check timeout before proceding every time. 
        if self.time_left() < self.TIMER_THRESHOLD:
            debug_print ("error","-->"+strTag+" timeout " + str (self.bestmove))
            raise SearchTimeout()
        
        #legal moves
        moves =  game.get_legal_moves()
        debug_print ("trace","-->"+strTag+" for moves " + str(moves))
        
        #end of tree
        if not moves:
            debug_print ("debug","<--"+strTag+" No moves left " + str(self.score (game, self)))
            return (self.score(game,self),(-1,-1))
        
        #end of tree depth       
        if depth == 0:
            debug_print ("trace","<--"+strTag+" depth exhausted")          
            return (self.score (game, self), moves[0])
        
        #Initialize ready to go
        tScore = -1
        tMove = ()
        scores = []
        
        #Recursion for all moves, get scores and put in list.
        #nextMoves removed.
        for m in moves:
            newgame = game.forecast_move(m)
            debug_print ("debug",strTag+" min called for " + str(m))
            tScore,tMove = self.minimum(newgame, game.get_opponent(player), depth-1, alpha, beta)
                 
            debug_print ("debug",strTag+" Adding " + str(tScore) + " move " + str(m))
            
            #Pruning
            if (tScore >= beta):
                return (tScore, m)
            alpha = max (alpha, tScore)
            scores.append(tScore)
        
        #Maximize move unrolling of recursion.
        debug_print ("info",strTag+" Maximizing " + str(scores) + " moves " +  str(moves))
        tScore,tMove = max([(scores[i], moves[i]) for i in range (0,len(scores))])
            
        debug_print ("trace","<--"+strTag+" Score is " + str(tScore) + " move " + str(tMove))
        self.bestmove = tMove
        return (tScore,tMove)

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        score = -1
        move= (-1,-1)
        try:
            score,move = self.maximum (game, self,depth, alpha, beta)
        except SearchTimeout:
            move = self.bestmove
            debug_print ("error","MinMax: Exception, best move found" + str(move))
            
        #print ("TimeOut: AphaBeta Return value " + str (move))
        return (move)
        # TODO: finish this function!
        raise NotImplementedError
