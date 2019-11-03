from flask import Flask, jsonify, request
from flask_apscheduler import APScheduler
import json

app = Flask(__name__)

# TODO: Set up game types

#    # Use this constructor to make a robot clone
#    def makeClone(self, cloneBase):
#        global nextPlayerID
#
#        self.name = cloneBase.name
#        self.picture = cloneBase.picture
#        self.playerID = nextPlayerID
#        nextPlayerID += 1
#
#        self.hearts = cloneBase.hearts # TODO
#        self.implants = cloneBase.implants # TODO

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

nextPlayerID = 1
profiles = []
class Profile(Object): 
    def __init__(self, name, picture):
        global nextPlayerID

        self.name = name
        self.picture = picture
        self.playerID = nextPlayerID
        nextPlayerID += 1

        self.hearts = 0
        self.implants = 0

        self.isRobot = False

    def __repr__(self):
        return 'Profile' + ": " + str(self.__dict__)
        
def convert_to_json(thing):
    return json.dumps(thing, default=lambda o: o.__dict__, sort_keys=True, indent=4)

# TODO: Define routes

@app.route('/create_profile', methods=['POST'])
def create_profile():
    profiles.append(Profile(request.json["name"], request.json["picture"]))
    return jsonify({'playerID':profiles[-1].playerID}) 

def getPlayer(playerID):
    return [p for p in profiles if p.playerID == int(playerID)][0]

@app.route('/profiles/<playerID>')
def get_profile(playerID):
    global profiles
    return getPlayer(playerID).toJSON()

@app.route('/get_pickup_completions')
def generate_pickup_completions():
    playerID = request.json["playerID"]
    humanWords = request.json["humanWords"]

    generatedOptions = []
    # TODO: Call GPT-2 here.
    for i in range(getPlayer(playerID).implants):
        import random
        generatedOptions.append(random.choice(["word lol.", "words lol", "more words lol"]))

    return jsonify({
        "options":generatedOptions
    })
    
@app.route('/get_prospects/<playerID>')
def get_prospects(playerID):
    playerID = int(playerID)
    return convert_to_json([p for p in profiles if p.playerID != int(playerID)])

# After everything else is established, start the game ticking

def updateGameState():
    """
    Ticks the state machine that times out game states and advances the 
    game when all players finish making choices.
    """
    global profiles
    print ("Updating game state")
    print(profiles)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
scheduler.add_job(func=updateGameState, trigger='interval', seconds=0.5, id="updateGameStateJob")