import random

# CONSTANTS
# Payoff matrix used in Scodel et al. (1959)
PAYOFFMAT = [ [(3,3),(0,5)] , 
             [(5,0),(1,1)] ]

# class SimpleGame:
#     players = []
#     payoffmat = 0
#     history = 0
#
#     def run():
#         pass
#
#     def payoff():
#         pass


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
    

def main():
    # Players
    player1 = RandomMover()
    player2 = RandomMover()
    # Get a move from each player
    move1 = player1.move()
    move2 = player2.move()
    # Retrieve and print the payoffs
    pay1, pay2 = PAYOFFMAT[move1][move2]
    print("Player1 payoff: ", pay1)
    print("Player2 payoff: ", pay2)


if __name__ == "__main__":
    main()