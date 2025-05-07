from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D

class Andreas(Player):
    """
    Win–Stay, Lose–Shift (Pavlov):

    - Cooperates on the first move.
    - Thereafter, if both players did the same last round (CC or DD) → cooperate.
    - Otherwise (CD or DC) → defect.
    """

    name = "Andreas"
    classifier = {
        "memory_depth": 1,      # only needs last round
        "stochastic": False,    
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def strategy(self, opponent):
        # First move
        if not self.history:
            return C

        # If last round was mutual (CC or DD), "stay" → cooperate
        if self.history[-1] == opponent.history[-1]:
            return C
        # Otherwise "shift" → defect
        return D
