from game_logic import Dice, GameEngine

def get_valid_integer(prompt: str) -> int:
    """Helper function to handle input validation"""
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print("Invalid input. Please enter a positive number.")
        
def main():
    print("--- Welcome to the Dice Game ---")
    
    # Configuration Phase
    num_dice = get_valid_integer("How many dice do you want to roll? ")
    
    # Dependency Injection
    dice = Dice(num_dice=num_dice)
    game = GameEngine(dice=dice)
    
    # Game Loop
    while True:
        command = input("Roll the dice? (y/n): ").lower()
        
        if command == 'y':
            roll_result = game.play_round()
            stats = game.get_stats()
        
            print(f"You rolled: {roll_result} | Total: {stats['total']} | Rounds: {stats['rolls']}")
        
        elif command == 'n':
            stats = game.get_stats()
            print("Game Over")
            print(f"You rolled: {roll_result} | Total: {stats['total']} | Rounds: {stats['rolls']}")
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
    