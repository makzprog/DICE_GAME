import random

class Dice:
    def __init__(self, dices=2):
        if dices < 1:
            raise ValueError("Please choose atleast 1 die")
        self._sides = 6
        self._dices = dices
        
    def get_amount(self):
        return self._dices
        
    def set_amount(self, value):
        if value < 1:
            raise ValueError("please choose atleast 1 dice")
        self._dices = value
        
class Game:
    def __init__(self, dice):
        self._dice = dice
            
    def get_user_input(self):
        user_input = input("How many dices do you want to roll? ")
        if user_input.isdigit() and int(user_input) > 0:
            self._dice.set_amount(int(user_input))
            return int(user_input)
        else:
            raise ValueError("please choose atleast 1 dice")
        
dice = Dice()
game = Game(dice)
print(game.get_user_input())
print(f"Number of dices: {dice.get_amount()}")




      
"""
dice = Dice(6)
print(f"Number of sides: {dice.get_sides()}")
print(f"Number of dices: {dice.get_amount()}")

dice.set_sides(12)
print(f"Number of sides: {dice.get_sides()}")
print(f"Number of dices: {dice.get_amount()}")

dice.set_amount(12)
print(f"Number of sides: {dice.get_sides()}")
print(f"Number of dices: {dice.get_amount()}")    

"""
    




  


