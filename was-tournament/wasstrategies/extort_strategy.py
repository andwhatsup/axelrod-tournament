import random
import axelrod as axl
from axelrod.action import Action

C, D = Action.C, Action.D

class Extort(axl.Player):
    """
    Extort: a memory-1 zero-determinant extortionate strategy.
    Forces a payoff ratio of roughly 2:1 in its favor using phi=0.5 and chi=0.1
    These values implement an extortionate strategy according to the ZD theory.
    """

    name = "Extort"
    classifier = {
        "memory_depth": 1,
        "stochastic": True,          # probabilities in play
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self):
        super().__init__()
        # Use phi and chi parameters instead of slope
        # phi=0.5 and chi=0.1 create an extortionate strategy
        self.extorter = axl.ZDExtortion(phi=0.5, chi=0.1)

    def strategy(self, opponent):
        # Delegate to the ZD helper, which uses history to choose C or D
        return self.extorter.strategy(self.history, opponent.history)