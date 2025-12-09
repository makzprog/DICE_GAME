import random

class Dice:
    def __init__(self, dices=2):
        if dices < 1:
            raise ValueError("Please choose at least 1 die")
        self._dices = dices
        self._sides = 6
    
    @property
    def dices(self):
        return self._dices    
    
    @dices.setter    
    def dices(self, value):
        if value < 1:
            raise ValueError("Please choose at least 1 die")
        self._dices = value
        
    @property
    def sides(self):
        return self._sides

    def roll(self):
        return tuple(random.randint(1, self._sides) for _ in range(self._dices))

class Game:
    def __init__(self, dice):
        self.dice = dice
        self.count = 0
        self.sum_total = 0

    def get_user_input(self):
        user_input = input("How many dices do you want to roll? ")
        if user_input.isdigit() and int(user_input) > 0:
            self.dice.dices = int(user_input)
        else:
            raise ValueError("Please choose at least 1 die")

    def roll_dices(self):
        while True:
            ask_user = input("Roll the dices? (y/n): ").lower()
            if ask_user == 'y':
                current_roll = self.dice.roll()
                self.count += 1
                self.sum_total += sum(current_roll)
                print("You rolled:", current_roll, 
                      "| Total so far:", self.sum_total, 
                      "| Times Rolled:", self.count)
            elif ask_user == 'n':
                print("Game Over")
                print("Total rolls:", self.count)
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        return "Thanks for playing!"
    
if __name__ == "__main__":
    dice = Dice()
    game = Game(dice)
    game.get_user_input()
    print(game.roll_dices())




