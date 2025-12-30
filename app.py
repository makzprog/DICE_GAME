from flask import Flask, render_template, jsonify
from game_logic import Dice, GameEngine

app = Flask(__name__)

# Initialize our logic just like before
dice = Dice(num_dice=2)
engine = GameEngine(dice=dice)

@app.route('/')
def home():
    # This sends the HTML file to the user's browser
    return render_template('index.html')

@app.route('/roll', methods=['POST'])
def roll():
    # This is the "API" - it runs the logic and returns JSON (data)
    current_roll = engine.play_round()
    stats = engine.get_stats()
    
    return jsonify({
        "roll": current_roll,
        "total": stats['total'],
        "count": stats['rolls']
    })

@app.route('/reset', methods=['POST'])
def reset():
    engine.reset()  # Call the new logic method
    stats = engine.get_stats()
    return jsonify({
        "total": stats['total'],
        "count": stats['rolls'],
        "message": "Game Reset"
    })

if __name__ == '__main__':
    app.run(debug=True)