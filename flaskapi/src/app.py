from flask import Flask, jsonify, request
from flask_apscheduler import APScheduler

app = Flask(__name__)

# TODO: Set up game types

nextPlayerID = 1
profiles = []
class Profile: 
    def __init__(self, name, picture):
        global nextPlayerID

        self.name = name
        self.picture = picture
        self.playerID = nextPlayerID
        nextPlayerID += 1

        self.hearts = 0
        self.implants = 0

        self.isRobot = False

    # Use this constructor to make a robot clone
    def makeClone(self, cloneBase):
        global nextPlayerID

        self.name = cloneBase.name
        self.picture = cloneBase.picture
        self.playerID = nextPlayerID
        nextPlayerID += 1

        self.hearts = cloneBase.hearts # TODO
        self.implants = cloneBase.implants # TODO


    #def __str__(self):
    #    return 'Profile' + ": " + str(self.__dict__)
    def __repr__(self):
        return 'Profile' + ": " + str(self.__dict__)

# TODO: Define routes

@app.route('/create_profile', methods=['POST'])
def create_profile():
    profiles.append(Profile(request.json["name"], request.json["picture"]))
    return jsonify({'playerID':profiles[-1].playerID}) 

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