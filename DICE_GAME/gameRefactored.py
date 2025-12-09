import random

class Dice:
    def __init__(self, dices=2):
        if dices < 1:
            raise ValueError("Please choose atleast 1 die")
        self._dices = dices
        self._sides = 6
    
    @property
    def dices(self):
        return self._dices    
    
    @property
    def sides(self):
        return self._sides
    
    @dices.setter    
    def dices(self, value):
        if value < 1:
            raise ValueError("please choose atleast 1 dice")
        self._dices = value
        
class Game:
    def __init__(self, dice):
        self.dice = dice
        self.roll = 0
        self.count = 0
        self.sum_total = 0
            
    def get_user_input(self):
        user_input = input("How many dices do you want to roll? ")
        if user_input.isdigit() and int(user_input) > 0:
            self.dice.dices = int(user_input)
            return f"You have chosen: {user_input}"
        else:
            raise ValueError("please choose atleast 1 dice")
    
    def roll_dices(self):
        while True:
            ask_user = input("Roll the dices? (y/n): ").lower()
            if ask_user == 'y':
                self.roll = tuple(random.randint(1, self.dice.sides) for _ in range(self.dice.dices))
                self.count += 1
                self.sum_total += sum(self.roll)
                print("You rolled:", self.roll, " | Total:", self.sum_total, " | Times Rolled:", self.count)
                self.sum_total = 0
            elif ask_user == 'n':
                print("Game Over")
                print("Total rolls:",  self.count)
                break
            else:
               print("Invalid input. Please enter 'y' or 'n'.")
        return "Thanks for playing!"
    
if __name__ == "__main__":
    dice = Dice()
    game = Game(dice)
    print(game.get_user_input())
    print(game.roll_dices())





