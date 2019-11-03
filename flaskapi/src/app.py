from flask import Flask, jsonify, request
from flask_apscheduler import APScheduler

app = Flask(__name__)

# TODO: Set up game types
# TODO: Define routes

@app.route('/')
def test():
    return 5

@app.route('/create_profile', methods=['POST'])
def create_profile():
    #return jsonify({'playerID':5})
    return jsonify({'submitted':request.json})

# After everything else is established, start the game ticking

def updateGameState():
    """
    Ticks the state machine that times out game states and advances the 
    game when all players finish making choices.
    """
    print ("Updating game state")

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
scheduler.add_job(func=updateGameState, trigger='interval', seconds=0.5, id="updateGameStateJob")