from axelrod.actions import Action, Actions
from axelrod.player import Player

from math import pi, sin
import random

C, D = Actions.C, Actions.D


class SelfSteem(Player):
    """
    This strategy is based on the feeling with the same name.
    It is modeled on the sine curve(f = sin( 2* pi * n / 10 )), which varies
    with the current iteration.
    
    If f > 0.95, 'ego' of the algorithm is inflated; always defects.
    If 0.95 > abs(f) > 0.3, rational behavior; follows TitForTat algortithm.
    If 0.3 > f > -0.3; random behavior.
    If f < -0.95, algorithm is at rock bottom; always cooperates.
    
    Names:
    
    - SelfSteem: [Andre2013]_
    """

    name = 'SelfSteem'
    classifier = {
        'memory_depth': 1,
        'stochastic': False,
        'makes_use_of': set(),
        'long_run_time': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def strategy(self, opponent: Player) -> Action:
        turns_number = len(self.history)
        sine_value =  sin( 2 * pi * turns_number / 10 )
          
        if sine_value > 0.95:
            return D
        
        elif abs(sine_value) < 0.95 and abs(sine_value) > 0.3:
            return opponent.history[-1]
        
        elif sine_value < 0.3 and sine_value > -0.3:
            return random.choice((C, D))
            
        else:
            return C
            
        
