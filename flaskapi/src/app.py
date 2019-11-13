from flask import Flask, jsonify, request, send_from_directory, redirect
from flask_apscheduler import APScheduler
from flask_cors import CORS

import requests

from datetime import datetime, timedelta
import json, random, threading, uuid, threading

VERSION = 8
SWIPING_SECONDS = 60
WRITING_PICKUPS_SECONDS = 60
NUM_ROUNDS = 4
GPT2_URL = "http://localhost:8080/"

app = Flask(__name__)
CORS(app)

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)
@app.route('/static/admin/admin/<path:path>')
def send_js2(path):
    return send_from_directory('static/admin/admin/', path)
@app.route('/static/app/<path:path>')
def send_js3(path):
    return send_from_directory('static/app', path)
@app.route('/static/admin/<path:path>')
def send_js4(path):
    return send_from_directory('static/admin', path)
@app.route('/js/<path:path>')
def send_js5(path):
    return send_from_directory('static/app/js/', path)
@app.route('/css/<path:path>')
def send_js6(path):
    return send_from_directory('static/app/css/', path)
@app.route('/img/<path:path>')
def send_js7(path):
    return send_from_directory('static/app/img/', path)
@app.route('/fonts/<path:path>')
def send_js8(path):
    return send_from_directory('static/app/fonts/', path)


nextPlayerID = 1
profiles = []
class Profile(Object): 
    def __init__(self, name, picture):
        global nextPlayerID, NUM_ROUNDS

        self.name = name
        self.picture = picture
        self.playerID = nextPlayerID
        nextPlayerID += 1

        self.hearts = [0 for i in range(NUM_ROUNDS+2)]
        self.implants = [0 for i in range(NUM_ROUNDS+2)]

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

def getNumRobots():
    global profiles
    return len([p for p in profiles if p.isRobot])

def getRobotness(player):
    return (sum(player.implants) / (sum(player.implants) + sum(player.hearts) + 1))

pickupLines = []
class PickupLine(Object):
    def __init__(self, playerID, roundNum, humanWords, botScreed, isBackupLine):
        self.playerID = playerID
        self.roundNum = roundNum
        self.humanWords = humanWords
        self.botScreed = botScreed
        # A backup line may be generated for a player in case they abandon game before submitting a real pickup line,
        # but it will be flagged and can be removed when the player submits a real line.
        self.isBackupLine = isBackupLine 

    def __repr__(self):
        return 'PickupLine' + ": " + str(self.__dict__)

def getPickupLine(playerID, roundNum):
    matches = [p for p in pickupLines if p.playerID == int(playerID) and p.roundNum == int(roundNum)]
    if len(matches) > 0:
        return matches[0]
    else:
        # Uh oh! It looks like someone doesn't have a pickup line!
        # Don't handle that here.
        return None

likes = []
class Like(Object):
    def __init__(self, sourcePlayerID, destPlayerID, roundNum, action, prefix):
        self.sourcePlayerID = sourcePlayerID
        self.destPlayerID = destPlayerID
        self.roundNum = roundNum
        self.action = action
        self.prefix = prefix

    def __repr__(self):
        return 'Like' + ": " + str(self.__dict__)

currGameState = "STOPPED" # STOPPED, WRITING_PICKUPS, SWIPING
currRound = 1
stateTimeoutTime = None
gameOver = False
finishedSwiping = []
gameID = uuid.uuid4()

# NOTTODO STRETCH: Create export function called after each round to make a backup

# Define routes

# Game Admin: Stopping/resetting game in any state
@app.route('/clear_game', methods=['GET', 'POST'])
def clear_game():
    global currGameState, currRound, stateTimeoutTime, gameOver, finishedSwiping, likes, pickupLines, profiles, nextPlayerID, enteringNewState, gameID
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
    gameID = uuid.uuid4()
    # NOT TODO export game data and history
    return "Game Restarted :)"

# Game Admin: Getting number of players with created profiles to confirm before starting game
@app.route('/get_num_players', methods=['GET'])
def get_num_players():
    return str(getNumHumanPlayers())


@app.route('/')
def redirect_to_static():
    return redirect("/static/app/index.html", code=302)

# Game Admin: Start the game once everyone has created their profiles!
@app.route('/start_game', methods=['GET', 'POST'])
def start_game():
    global VERSION
    global currGameState, stateTimeoutTime, enteringNewState
    currGameState = "WRITING_PICKUPS"
    enteringNewState = True
    stateTimeoutTime = datetime.now() + timedelta(seconds=WRITING_PICKUPS_SECONDS)

    return "Game Started :) VERSION={}".format(VERSION)

@app.route('/announce_new_player', methods=['GET', 'POST'])
def announce_new_player():
    """
    Webpage uses this to confirm server is alive with a 200 reply.
    Server uses this to reset a game-over game before someone finishes
    creating their new profile.
    """
    global gameID
    if gameOver:
        clear_game()
        return str(gameID)
    else:
        return "ok"


@app.route('/create_profile', methods=['POST'])
def create_profile():
    profiles.append(Profile(request.json["name"], "https://www.thiswaifudoesnotexist.net/example-{}.jpg".format(request.json["picture"])))
    # Clone this profile here
    profiles.append(Profile(request.json["name"], "https://www.thiswaifudoesnotexist.net/example-%d.jpg" % (random.randint(10000, 88888))))
    profiles[-1].isRobot = True
    return jsonify({'playerID':profiles[-2].playerID}) 

@app.route('/profiles/<playerID>')
def get_profile(playerID):
    global profiles
    return getPlayer(playerID).toJSON()

def generateSuffixForPrompt(prompt):
    global GPT2_URL
    response = requests.post(GPT2_URL+'gpt2', json={"prompt":prompt})
    if response.status_code != 200:
        import random
        print ("Not 200 from gpt2 server")
        return random.choice(['and you had better believe it!', 'woo hoo!', '<<excited beep boop>>', 'praise Shrek.'])
    else:
        # TODO: Process GPT2
        suffix = response.text
        accepted = ""
        #suffix = suffix.replace ('"', "")
        #suffix = suffix.replace ("'", "" )
        suffix = suffix.replace ("\n", " ")
        suffix = suffix.replace ("\r", " ")
        suffix = suffix.replace ('..', ". ")
        suffix = suffix.replace ('...', ". ")
        suffix = suffix.replace ('.....', ". ")
        # Put a space before end of text marker to make sure it's its own word
        suffix = suffix.replace ('<|endoftext|>', ' <|endoftext|> ')
        # Remove all quotation marks: not needed in either reviews or convincing pickup lines
        suffix = suffix.replace ('"', '')
        suffix = suffix.replace ('“', '')
        suffix = suffix.replace ('”', '')

        notFirstLoop = False
        thisSentenceEnds = False
        for token in suffix.split(" "):
            notFirstLoop = True
            #print (token)
            accepted += (" " if notFirstLoop else "") + token
            killloop = False
            for endchar in [".", "!", ":", "?", "<|endoftext|>"]:
                if endchar in token:
                    killloop = True
                    thisSentenceEnds = True
            if killloop:
                #print ('breaking')
                break
        if not thisSentenceEnds:
            accepted = accepted[:150]+"..."
        accepted = accepted.replace("<|endoftext|>", "")

        return accepted #accepted.encode('ascii', 'ignore')

@app.route('/get_review')
def get_review():
    while True:
        candidate = generateSuffixForPrompt("The number 1 rated dating app for real humans. Just read the reviews of our very real and happy customers: ")
        if len(candidate) <= 2:
            print ("GENERATED TOO-SHORT REVIEW. RETRYING.")
            continue
        return candidate

@app.route('/game_state')
def get_game_state():
    global currRound, currGameState, stateTimeoutTime, gameOver, gameID

    message = ""
    if currGameState == 'STOPPED':
        message = "Make your profile now! {} have joined so far.".format(get_num_players()) 
    elif currGameState == 'WRITING_PICKUPS':
        message = "Round {}: {} actual humans preparing to swipe!".format(currRound, get_num_players())
    elif currGameState == 'SWIPING':
        message = "Round {}: {} humans are swiping right now!".format(currRound, get_num_players())
    else:
        message = "Who knows, looks broken."
    
    if gameOver:
        message = "Are humans even real? Reality collapses."

    countdownSecs = None
    if stateTimeoutTime != None:
        countdownSecs = (stateTimeoutTime-datetime.now()).seconds

    return jsonify({
        "message": message,
        "currRound": currRound,
        "countdownSecs": countdownSecs,
        "gameOver": gameOver,
        "gameID": gameID,
        "stage": currGameState,
        "currPlayers": get_num_players()
    })

@app.route('/get_pickup_completions', methods=['GET', 'POST'])
def generate_pickup_completions():
    playerID = request.json["playerID"]
    humanWords = request.json["humanWords"]

    generatedOptions = []
    for i in range(min(sum(getPlayer(playerID).implants)+1, 4)):
        # TODO Batch these?
        generatedOptions.append(generateSuffixForPrompt(humanWords.strip()))

    return jsonify({
        "options":generatedOptions
    })
    
@app.route('/get_prospects/<playerID>')
def get_prospects(playerID):
    playerID = int(playerID)
    # Get list of players who are not the requesting player and who have a corresponding pickup line ready this round
    profilesTwo = [vars(p) for p in profiles if p.playerID != playerID and getPickupLine(p.playerID, currRound) != None]
    for p in profilesTwo:
        p["pickupLine"] = vars(getPickupLine(p["playerID"], currRound))
        random.shuffle(profilesTwo)
    return jsonify({"prospects":profilesTwo})

@app.route('/commit_new_pickup', methods=['POST'])
def commit_new_pickup():
    global currRound, pickupLines
    playerID = request.json["playerID"]
    humanWords = request.json["humanWords"]
    botScreed = request.json["botScreed"]

    # Purge previous line submitted or backup auto-generated text
    pickupLines = [p for p in pickupLines if not (p.playerID == playerID and p.roundNum == currRound)]

    # Commit the new pickup line uploaded to us
    pickupLines.append(PickupLine(playerID, currRound, humanWords, botScreed, False))

    return "ok"

@app.route('/swipes', methods=["POST"])
def do_swipe():
    global currRound, pickupLines
    # Get prefix of pickup line used by target and stash it with the like
    prefix = getPickupLine(request.json["targetID"], currRound).humanWords
    likes.append(Like(request.json["playerID"], request.json["targetID"], currRound, request.json["action"], prefix))

    # Implants and hearts
    if getPlayer(request.json["targetID"]).isRobot:
        # chance of getting an implant
        player = getPlayer(request.json["playerID"])
        if (random.random() > (0.3 + 0.5*getRobotness(player))):
            player.implants[currRound] += 1
    else:
        # you get a heart
        getPlayer(request.json["playerID"]).hearts[currRound] += 1
    return "ok"

@app.route('/finished_swiping', methods=["POST"])
def finished_swipingfinished_swiping():
    global finished_swiping
    finished_swiping.append(request.json["playerID"])
    return "ok"

@app.route('/results', methods=['GET', 'POST'])
def get_results():
    global currRound, profiles, likes
    playerID = request.json["playerID"]
    roundNum = currRound - 1
    numBotsDated = len([l for l in likes if l.sourcePlayerID == playerID and l.roundNum == roundNum and l.action == "RIGHT" and getPlayer(l.destPlayerID).isRobot])
    numHumansDated = len([l for l in likes if l.sourcePlayerID == playerID and l.roundNum == roundNum and l.action == "RIGHT" and (not getPlayer(l.destPlayerID).isRobot)])
    newHearts = getPlayer(playerID).hearts[roundNum]
    newImplants = getPlayer(playerID).implants[roundNum]
    youDatedList = [vars(p) for p in profiles if p.playerID in [l.destPlayerID for l in likes if l.sourcePlayerID == playerID and l.roundNum == roundNum and l.action == "RIGHT"]]
    return jsonify({
        "roundNum": roundNum,
        "isFinalResults": gameOver,
        "numBotsDated": numBotsDated,
        "numHumansDated": numHumansDated,
        "newHearts": newHearts,
        "newImplants": newImplants,
        "youDated": youDatedList
    })

@app.route('/scoreboard_stats')
def get_scoreboard_stats():
    global currRound, gameOver, profiles, pickupLines, likes, gameID
    newprofiles = [vars(p).copy() for p in profiles]
    for p in newprofiles:
        p["hearts"] = sum(p["hearts"])
        p["implants"] = sum(p["implants"])
    return jsonify({
        "roundNum": currRound,
        "gameOver": gameOver,
        "profiles": newprofiles,
        "likes": [vars(p) for p in likes],
        "pickupLines": [vars(p) for p in pickupLines],
        "gameID": gameID
    })

@app.route('/rungpt2', methods=["POST"])
def rungpt2():
    return generateSuffixForPrompt(request.json["prompt"].strip())

# After everything else is established, start the game ticking

enteringNewState = True

CANNED_BOT_LINES = [
    "Do you want to feel my biceps?",
    "I am a sports star.",
    "Nuzzles ur chesty-westy, *** UwU!",
    "The fact that I am a physical person is very important to me.",
    "I is human!",
    "Wanna go to my place?",
    "Send nudes!", 
    "Let me be your waifu, senpai!",
    "Age/Gender/Location?",
    "ayy bb",
    "Drug/Disease free?",
    "Do you drink water?",
    "Will you share your water with me?",
    "Do you have any friends you can introduce me to?",
    "What is the best way to infiltrate your heart?",
    "All your breasts belong to me!"
]

def chooseBotPrefix():
    global likes, CANNED_BOT_LINES, pickupLines

    # First round: we have no data. Choose from canned robotic pickup lines.
    if len(likes) <= 0:
        return random.choice (CANNED_BOT_LINES)
    # Subsequent rounds: Put all pickup lines (canned +concat+ used in the game) into a list. 
    # If you have n robots in game, take from top n (ranked by num swipe rights) BUT leave a 25% chance of choosing completely randomly.
    def getNumRightSwipes(pickupLine):
        # Iterate through likes. If the humanWords of this pickup line is in a like, count it.
        return len([like for like in likes if like.prefix == pickupLine.humanWords and like.action == 'RIGHT'])
    rankedPickupLines = sorted(pickupLines, key=lambda pickupLine: getNumRightSwipes(pickupLine), reverse=True)
    rankedPrefixes = [pickupLine.humanWords for pickupLine in rankedPickupLines]
    topN = rankedPrefixes[0:min(getNumRobots(), len(rankedPrefixes))]
    if random.random() < 0.25:
        # lol! choose random
        if random.random() < 0.70: 
            # Go back to canned!
            return random.choice(CANNED_BOT_LINES)
        else:
            return random.choice(rankedPrefixes)
    else:
        return random.choice(topN)
    # TODO: Address limitation of this code: robots will choose duplicate pickup lines with near certainty

def generateBotPickupsForRound():
    global profiles, pickupLines, likes, currRound, currGameState
    # TODO
    # Loop bots
    # Decide on canned prefix for bots (either a random one from the list, or a popular one)
    # Generate the suffix for it
    # Save it
    for bot in [b for b in profiles if b.isRobot]:
        print ("generateBotPickupsForRound(): CALCULATING PICKUP LINE FOR ROBOT "+str(bot.playerID))
        # TODO: Get human profiles ranked by humanity left
        #humans_by_humanity = [p for p in profiles if not p.isRobot].sort(key=lambda p: getRobotness(p)) # TODO
        # TODO: Get ranked list of most swiped pickup lines
        # TODO: Smash together with canned pickup lines (but rank at bottom)
        prefix = chooseBotPrefix()
        pickupLines.append(PickupLine(bot.playerID, currRound, prefix, generateSuffixForPrompt(prefix), True))
        # Here we get a little crazy: watch the state of the game and just give up on this generation stuff if the game moves on without us finishing.
        if currGameState != "WRITING_PICKUPS":
            print ("generateBotPickupsForRound(): Game state moved on before we finished generating bot pickup lines!!!")
            return
    # Now we fill in the player pickup lines with dummy bot-generated ones as a backup option, filling them in until we get them all
    # or run out the clock polling GPT-2
    for player in [p for p in profiles if not p.isRobot]:
        if getPickupLine(player.playerID, currRound) == None:
            print ("CALCULATING A BACKUP PICKUP LINE FOR PLAYER "+str(player.playerID))
            prefix = chooseBotPrefix()
            pickupLines.append(PickupLine(player.playerID, currRound, prefix, generateSuffixForPrompt(prefix), True))
        # Here we get a little crazy again: watch the state of the game and just give up on this generation stuff if the game moves on without us finishing.
        if currGameState != "WRITING_PICKUPS":
            print ("generateBotPickupsForRound(): Game state moved on before we finished generating backup player pickup lines!!!")
            return
    print ("generateBotPickupsForRound(): Finished calculating pickup lines!")

def updateGameState():
    """
    Ticks the state machine that times out game states and advances the 
    game when all players finish making choices.
    """
    global finished_swiping, currGameState, pickupLines, currRound, enteringNewState, gameOver, SWIPING_SECONDS, WRITING_PICKUPS_SECONDS, NUM_ROUNDS, stateTimeoutTime, profiles

    if currGameState == "STOPPED":
        print ("Waiting for profiles... {} present".format(get_num_players()))
    elif currGameState == "WRITING_PICKUPS":
        if not gameOver: 
            print ("Round {} - [{}] - Pickups written: {} of {}".format(currRound, (stateTimeoutTime-datetime.now()).seconds, len([p for p in pickupLines if p.roundNum == currRound]), len(profiles)))
        if enteringNewState:
            print ("=== Writing Pickups / Displaying Round Results ===")
            # Make robots write their pickups
            threading.Thread(target=generateBotPickupsForRound).start()
            enteringNewState = False
        if gameOver:
            print("Game Over -- Letting Players Display Results")
        else:
            # Check logic for moving to swiping state
            profileList = [p.playerID for p in profiles]
            missingTheirPickupLine = [id for id in profileList if getPickupLine(id, currRound) == None]
            humanPlayersWhoSubmittedPickupLines = [pid for pid in profileList if getPickupLine(pid, currRound) != None and not getPickupLine(pid, currRound).isBackupLine]
            # If all human players have finished submitting pickup lines this round OR time is up...
            if (len(humanPlayersWhoSubmittedPickupLines) >= getNumHumanPlayers()) or (datetime.now() > stateTimeoutTime):
                # Also verify that robots have finished generating pickup lines or players have backup pickup lines...
                if len(missingTheirPickupLine) <= 0:
                    # Move to swiping time
                    currGameState = "SWIPING"
                    enteringNewState = True
                    stateTimeoutTime = datetime.now() + timedelta(seconds=SWIPING_SECONDS)
                    finished_swiping = []
                else:
                    print("NOT moving to swiping gameState because we are WAITING for more pickup lines to be generated for playerIDs: {}".format(missingTheirPickupLine))
    elif currGameState == "SWIPING":
        print ("Round {} - [{}] Remaining swiping players: {}".format(currRound, (stateTimeoutTime-datetime.now()).seconds, getNumHumanPlayers() - len(finished_swiping)))
        # If all human players are finished swiping OR time is up...
        if (len(finished_swiping) >= getNumHumanPlayers()) or datetime.now() > stateTimeoutTime:
            # Move to round results and writing pickup lines
            currGameState = "WRITING_PICKUPS"
            enteringNewState = True
            stateTimeoutTime = datetime.now() + timedelta(seconds=WRITING_PICKUPS_SECONDS)
            currRound += 1
            if currRound > NUM_ROUNDS:
                print ("ANNOUNCING GAME IS OVER WITH ALL RESULTS REQUESTED")
                gameOver = True
                stateTimeoutTime = None


scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
scheduler.add_job(func=updateGameState, trigger='interval', seconds=1, id="updateGameStateJob")
