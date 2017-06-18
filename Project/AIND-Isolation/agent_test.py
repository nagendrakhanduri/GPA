"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import sample_players
import timeit

from importlib import reload

class TestCase:
    def test1(self):
        print ("this is testing")

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        print ("Setup called")
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"

        #self.player1 = game_agent.MinimaxPlayer(score_fn=game_agent.custom_score)
        self.player1 = game_agent.AlphaBetaPlayer(score_fn=game_agent.custom_score)
        self.player2 = sample_players.RandomPlayer()
        self.game = isolation.Board(self.player1, self.player2)

    def test_1(self):
        time_limit = 4000
        time_millis = lambda: 1000 * timeit.default_timer()
        move_start = time_millis()
        time_left = lambda : time_limit - (time_millis() - move_start)
        print ("This is unit test")
        legal_player_moves = self.game.get_legal_moves()
        print (legal_player_moves)
        myMove = self.player1.get_move(self.game, time_left)
        print ("Result ---> " + str(myMove))
        
if __name__ == '__main__':    
    unittest.main()
    
    
    
