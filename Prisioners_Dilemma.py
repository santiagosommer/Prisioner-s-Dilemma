"""
Explicar literalmente que hace paso a paso como ejemplo
"""

import random

from statistics import mean
import numpy as np

# CONSTANTS
# Payoff matrix used in Scodel et al. (1959)
PAYOFFMAT = [ [(3,3),(0,5)] , 
             [(5,0),(1,1)] ]

class RandomPlayer:

    def __init__(self, probability: float=0.5) -> None:
        self.defect_probability = probability

    def move(self, game):
        return random.uniform(0,1) < self.defect_probability

    def record(self):
        pass

class RandomMover:
    """
    A "random" number defines one of two behaviors, "defection" represented by
    1(True) or "cooperation" represented by 0(False)
    """
    def move(self):
        return random.uniform(0,1) < 0.5
    
class SimpleGame:

    def __init__(self, player1, player2, payoffmat):
        # Initialize instance attributes
        self.players = [player1, player2]
        self.payoffmat = payoffmat
        self.history = []

    def run(self, game_iter=4):
        # Unpack the two players
        player1, player2 = self.players

        # Each iteration, gets a random move and append it to history
        new_moves = player1.move(self), player2.move(self)
        self.history.append(new_moves)
        player1.record() ; player2.record() 

    def payoff(self):
        # Unpack the two players
        player1, player2 = self.players

        # Generate a payoff pair for each game iteration        
        payoffs = (self.payoffmat[m1][m2] for (m1,m2) in self.history)

        # Transpose to get a payoff sequence for each player
        # From payoffs = [(a1, b1), (a2, b2), (a3, b3), ...]
        # To pay1 = (a1, a2, a3, ...) pay2 = (b1, b2, b3, ...)
        pay1, pay2 = transpose(payoffs)
        
        # return a mapping of each player to its mean payoff
        return { player1:mean(pay1), player2:mean(pay2) }





def transpose(matrix):
    tuple1 = ()
    tuple2 = ()
    for element in matrix:
        tuple1 = tuple1 + (element[0])
        tuple2 = tuple2 + (element[0])
    

def main():
    ## GAME: SimpleGame with RandomPlayer
    # create a payoff matrix and two players
    PAYOFFMAT = [ [(3,3),(0,5)] , [(5,0),(1,1)] ]
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    # create and run the game
    game = SimpleGame(player1, player2, PAYOFFMAT)
    game.run()
    # retrieve and print the payoffs
    payoffs = game.payoff()
    print("Player1 payoff: ", payoffs[player1])
    print("Player2 payoff: ", payoffs[player2])

if __name__ == "__main__":
    main()