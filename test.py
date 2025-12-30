import unittest
from game_logic import Dice, GameEngine

class TestDiceGame(unittest.TestCase):
        
    def test_dice_initialization(self):
        """Test that the cup rejects invalid dice numbers."""
        with self.assertRaises(ValueError):
            Dice(num_dice=0)
            
    def test_game_scoring(self):
        """Test that the game engine correctly adds up scores."""
        # Setup
        dice = Dice(num_dice=1) 
        game = GameEngine(dice=dice)
        
        # Action: Play one round
        result = game.play_round()
        stats = game.get_stats()

        # Assertions
        self.assertEqual(stats['rolls'], 1)
        self.assertEqual(stats['total'], sum(result))
        
        # Play another round
        result_2 = game.play_round()
        stats_2 = game.get_stats()
        
        # Check that totals accumulated
        expected_total = sum(result) + sum(result_2)
        self.assertEqual(stats_2['total'], expected_total)
        self.assertEqual(stats_2['rolls'], 2)
        
if __name__ == '__main__':
    unittest.main()