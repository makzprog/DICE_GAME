import random
from typing import Tuple, List

class Dice:
    """
    Responsible ONLY for rolling and maintaining dice configuration
    """
    def __init__(self, num_dice: int = 2, sides: int = 6):
        if num_dice < 1:
            raise ValueError("Must have at least one die")
        self._num_dice = num_dice
        self._sides = sides
        
    @property
    def num_dice(self) -> int:
        return self._num_dice
    
    def roll(self) -> Tuple[int, ...]:
        """Generates random numbers based on configuration."""
        return tuple(random.randint(1, self._sides) for _ in range(self._num_dice))
    
    
class GameEngine:
    """
    Responsible ONLY for Game State and Rules.
    """
    def __init__(self, dice: Dice):
        self.dice = dice
        self.roll_cout = 0
        self.total_score = 0
        self.history: List[Tuple[int, ...]] = []
        
    def play_round(self) -> Tuple[int, ...]:
        """
        Logic for executing a single round
        """
        current_roll = self.dice.roll()
    
        self.roll_cout += 1
        self.total_score += sum(current_roll)
        self.history.append(current_roll)
        
        return current_roll
    
    def get_stats(self) -> dict:
        return {
            "rolls": self.roll_cout,
            "total": self.total_score
        }
    
    def reset(self):
        """Resets the game state to zero."""
        self.roll_count = 0
        self.total_score = 0
        self.history = []
        
    @staticmethod
    def get_valid_die_input(prompt: str) -> int:
        """Helper function to handle input validation for number of die"""
        while True:
            user_input = input(prompt)
            if user_input.isdigit() and int(user_input) > 0:
                return int(user_input)
            print("Invalid input. Please enter a positive number.")
