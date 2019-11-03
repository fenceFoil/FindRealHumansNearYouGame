from flask import Flask, jsonify, request
from flask_apscheduler import APScheduler
import json
from datetime import datetime, timedelta

SWIPING_SECONDS = 30
WRITING_PICKUPS_SECONDS = 60

app = Flask(__name__)

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

def getNumHumanPlayers():
    global profiles
    return len([p for p in profiles if not p.isRobot])

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
finishedSwiping = []

# TODO STRETCH: Create export function called after each round to make a backup

# Define routes

# Game Admin: Stopping/resetting game in any state
@app.route('/clear_game', methods=['GET', 'POST'])
def clear_game():
    global currGameState, currRound, stateTimeoutTime, gameOver, finishedSwiping, likes, pickupLines, profiles, nextPlayerID, enteringNewState
    currGameState = "STOPPED"
    currRound = 1
    stateTimeoutTime = None
    gameOver = False
    finishedSwiping = []
    likes = []
    pickupLines = []
    profiles = []
    nextPlayerID = 1
    enteringNewState = True
    # TODO export game data and history
    return "Game Restarted :)"

# Game Admin: Getting number of players with created profiles to confirm before starting game
@app.route('/get_num_players', methods=['GET'])
def get_num_players():
    return getNumHumanPlayers()

# Game Admin: Start the game once everyone has created their profiles!
@app.route('/start_game', methods=['GET', 'POST'])
def start_game():
    global currGameState, stateTimeoutTime, enteringNewState
    currGameState = "WRITING_PICKUPS"
    enteringNewState = True
    stateTimeoutTime = datetime.now() + timedelta(seconds=WRITING_PICKUPS_SECONDS)

    return "Game Started :)"

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
    profilesTwo = [p for p in profiles if p.playerID != int(playerID)]
    for p in profilesTwo:
        p.pickupLine = getPickupLine(p.playerID, currRound)
    return convert_to_json(profilesTwo)

@app.route('/commit_new_pickup', methods=['POST'])
def commit_new_pickup():
    global currRound
    playerID = request.json["playerID"]
    humanWords = request.json["humanWords"]
    botScreed = request.json["botScreed"]

    pickupLines.append(PickupLine(playerID, currRound, humanWords, botScreed))

    return "added pickupline"

@app.route('/is_it_swipe_time')
def move_to_swipe_time():
    return jsonify({"isItTime":currGameState == "SWIPING"})

@app.route('/swipes', methods=["POST"])
def do_swipe():
    global currRound
    likes.append(Like(request.json["playerID"], request.json["targetID"], currRound, request.json["action"]))
    return "ok"

@app.route('/finished_swiping', methods=["POST"])
def finished_swiping():
    global finished_swiping
    finished_swiping.append(request.json["playerID"])
    return "ok"

@app.route('/is_it_results_time')
def is_it_results_time():
    return jsonify({"isItTime":currGameState == "WRITING_PICKUPS"})

@app.route('/results')
def get_results():
    global currRound
    playerID = request.json["playerID"]
    roundNum = currRound - 1
    numBotsDated = len([l for l in likes if l.playerID == playerID and l.roundNum == roundNum and l.action == "RIGHT" and getPlayer(l.destPlayerID).isRobot])
    numHumansDated = len([l for l in likes if l.playerID == playerID and l.roundNum == roundNum and l.action == "RIGHT" and (not getPlayer(l.destPlayerID).isRobot)])
    newHearts = 0 # TODO
    newImplants = 0 # TODO, and we Should provide list of bots that gave you hearts and implants for flavor
    youDatedList = []
    return jsonify({
        "roundNum": roundNum,
        "isFinalResults": gameOver,
        "numBotsDated": numBotsDated,
        "numHumansDated": numHumansDated,
        "newHearts": newHearts,
        "newImplants": newImplants,
        "youDated": youDatedList
    })

# After everything else is established, start the game ticking

enteringNewState = True

def updateGameState():
    """
    Ticks the state machine that times out game states and advances the 
    game when all players finish making choices.
    """
    global finished_swiping, currGameState, pickupLines, currRound, enteringNewState, gameOver, SWIPING_SECONDS, WRITING_PICKUPS_SECONDS

    if currGameState == "STOPPED":
        print ("Game is stopped")
    elif currGameState == "WRITING_PICKUPS":
        if enteringNewState:
            # Make robots write their pickups
            # TODO
            # TODO: Also make this state wait until all the GPT 2 robot lines have come back in
            enteringNewState = False
        # If all human players have finished submitting pickup lines this round OR time is up...
        if (len([p for p in pickupLines if p.roundNum == currRound]) >= getNumHumanPlayers()) or datetime.now() > stateTimeoutTime:
            # Move to swiping time
            currGameState = "SWIPING"
            enteringNewState = True
            stateTimeoutTime = datetime.now() + timedelta(seconds=SWIPING_SECONDS)
            finished_swiping = []
    elif currGameState == "SWIPING":
        # If all human players are finished swiping OR time is up...
        if (len(finished_swiping) >= getNumHumanPlayers()) or datetime.now() > stateTimeoutTime:
            # Move to round results and writing pickup lines
            currGameState = "WRITING_PICKUPS"
            enteringNewState = True
            stateTimeoutTime = datetime.now() + timedelta(seconds=WRITING_PICKUPS_SECONDS)
            currRound += 1
            if currRound > 5:
                gameOver = True

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
scheduler.add_job(func=updateGameState, trigger='interval', seconds=0.5, id="updateGameStateJob")