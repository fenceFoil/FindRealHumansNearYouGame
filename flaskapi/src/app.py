from flask import Flask, jsonify, request
from flask_apscheduler import APScheduler
import json
import datetime

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

def getPlayer(playerID):
    return [p for p in profiles if p.playerID == int(playerID)][0]

pickupLines = []
class PickupLine(Object):
    def __init__(self, playerID, roundNum, humanWords, botScreed):
        self.playerID = playerID
        self.roundNum = roundNum
        self.humanWords = humanWords
        self.botScreed = botScreed

    def __repr__(self):
        return 'PickupLine' + ": " + str(self.__dict__)

def getPickupLine(playerID, roundNum):
    return [p for p in pickupLines if p.playerID == int(playerID) and p.roundNum == int(roundNum)][0]

likes = []
class Like(Object):
    def __init__(self, sourcePlayerID, destPlayerID, roundNum, action):
        self.sourcePlayerID = sourcePlayerID
        self.destPlayerID = destPlayerID
        self.roundNum = roundNum
        self.action = action

    def __repr__(self):
        return 'Like' + ": " + str(self.__dict__)

currGameState = "STOPPED" # STOPPED, WRITING_PICKUPS, SWIPING
currRound = 1
stateTimeoutTime = None
gameOver = False

# TODO STRETCH: Create export function called after each round to make a backup

# TODO: Define routes

@app.route('/create_profile', methods=['POST'])
def create_profile():
    profiles.append(Profile(request.json["name"], request.json["picture"]))
    return jsonify({'playerID':profiles[-1].playerID}) 



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
    for i in range(getPlayer(playerID).implants+3):
        import random
        generatedOptions.append(humanWords+random.choice(["word lol.", "words lol", "more words lol"]))

    return jsonify({
        "options":generatedOptions
    })
    
@app.route('/get_prospects/<playerID>')
def get_prospects(playerID):
    playerID = int(playerID)
    return convert_to_json([p for p in profiles if p.playerID != int(playerID)])

@app.route('/commit_new_pickup', methods=['POST'])
def commit_new_pickup():
    global currRound
    playerID = request.json["playerID"]
    humanWords = request.json["humanWords"]
    botScreed = request.json["botScreed"]

    pickupLines.append(PickupLine(playerID, currRound, humanWords, botScreed))

    return "added pickupline"

@app.route('/move_to_swipe_time')
def move_to_swipe_time():
    return jsonify({"isItTime":currGameState == "SWIPING"})

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