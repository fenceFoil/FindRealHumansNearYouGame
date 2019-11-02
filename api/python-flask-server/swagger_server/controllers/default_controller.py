import connexion
import six
import json
import sqlite3
from flask import jsonify
import random

# import gpt_2_simple as gpt2

from swagger_server.models.likes import Likes  # noqa: E501
from swagger_server.models.pickup_lines import PickupLines  # noqa: E501
from swagger_server.models.profiles import Profiles  # noqa: E501
from swagger_server import util

db = sqlite3.connect('game.db', check_same_thread=False)

cursor = db.cursor()
try:
    cursor.execute('''CREATE TABLE profiles(id INTEGER PRIMARY KEY, is_robot BOOL, name TEXT, waifu_image_url TEXT, hearts INTEGER, implants INTEGER)''')
    cursor.execute('''CREATE TABLE pickup_lines(id INTEGER PRIMARY KEY, player_id INTEGER, round_num INTEGER, human_words TEXT, robot_words TEXT)''')
    cursor.execute('''CREATE TABLE likes(id INTEGER PRIMARY KEY, source_player_id INTEGER, dest_player_id INTEGER, round_num INTEGER, action TEXT)''')
    db.commit()
except Exception:
    pass

# model_name = "124M"
# gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/

# sess = gpt2.start_tf_sess()


def createlikes(body):  # noqa: E501
    """Create a likes

    Creates a new instance of a &#x60;likes&#x60;. # noqa: E501

    :param body: A new &#x60;likes&#x60; to be created.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Likes.from_dict(connexion.request.get_json())  # noqa: E501
        print(body)
        cursor.execute('''INSERT INTO likes(source_player_id, dest_player_id, round_num, action)
                  VALUES(?,?,?,?)''', (body.source_player_id, body.dest_player_id, body.round_num, body.action))
        db.commit()
    return cursor.lastrowid


def createpickup_lines(body):  # noqa: E501
    """Create a pickup_lines

    Creates a new instance of a &#x60;pickup_lines&#x60;. # noqa: E501

    :param body: A new &#x60;pickup_lines&#x60; to be created.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PickupLines.from_dict(connexion.request.get_json())  # noqa: E501
        print(body)
        cursor.execute('''INSERT INTO pickup_lines(player_id, round_num, human_words, robot_words)
                  VALUES(?,?,?,?)''', (body.player_id, body.round_num, body.human_words, body.robot_words))
        db.commit()
    return cursor.lastrowid


def createprofiles(body):  # noqa: E501
    """Create a profiles

    Creates a new instance of a &#x60;profiles&#x60;. # noqa: E501

    :param body: A new &#x60;profiles&#x60; to be created.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Profiles.from_dict(connexion.request.get_json())  # noqa: E501
        print(body)
        body.waifu_image_url = ("https://www.thiswaifudoesnotexist.net/example-%d.jpg" % (random.randint(10000,99999)))
        cursor.execute('''INSERT INTO profiles(name, is_robot, waifu_image_url, hearts, implants)
                  VALUES(?,?,?,?,?)''', (body.name, body.is_robot, body.waifu_image_url, body.hearts, body.implants))
        db.commit()
    return cursor.lastrowid


def deletelikes(likesId):  # noqa: E501
    """Delete a likes

    Deletes an existing &#x60;likes&#x60;. # noqa: E501

    :param likesId: A unique identifier for a &#x60;likes&#x60;.
    :type likesId: str

    :rtype: None
    """
    return 'do some magic!'


def deletepickup_lines(pickup_linesId):  # noqa: E501
    """Delete a pickup_lines

    Deletes an existing &#x60;pickup_lines&#x60;. # noqa: E501

    :param pickup_linesId: A unique identifier for a &#x60;pickup_lines&#x60;.
    :type pickup_linesId: str

    :rtype: None
    """
    return 'do some magic!'


def deleteprofiles(profilesId):  # noqa: E501
    """Delete a profiles

    Deletes an existing &#x60;profiles&#x60;. # noqa: E501

    :param profilesId: A unique identifier for a &#x60;profiles&#x60;.
    :type profilesId: str

    :rtype: None
    """
    return 'do some magic!'


def getalllikes():  # noqa: E501
    """List All likes

    Gets a list of all &#x60;likes&#x60; entities. # noqa: E501


    :rtype: List[Likes]
    """
    cursor.execute('''SELECT source_player_id, dest_player_id, round_num, action from likes''')
    all_rows = cursor.fetchall()
    jsonUserList = []
    for row in all_rows:
        jsonObject = {}
        # name, role, long, lat, health, lastOnline, deviceId
        jsonObject['source_player_id'] = row[0]
        jsonObject['dest_player_id'] = row[1]
        jsonObject['round_num'] = row[2]
        jsonObject['action'] = row[3]
        jsonUserList.append(jsonObject)
    return jsonify(jsonUserList)


def getallpickup_lines():  # noqa: E501
    """List All pickup_lines

    Gets a list of all &#x60;pickup_lines&#x60; entities. # noqa: E501


    :rtype: List[PickupLines]
    """
    cursor.execute('''SELECT player_id, round_num, human_words, robot_words from pickup_lines''')
    all_rows = cursor.fetchall()
    jsonUserList = []
    for row in all_rows:
        jsonObject = {}
        jsonObject['player_id'] = row[0]
        jsonObject['round_num'] = row[1]
        jsonObject['human_words'] = row[2]
        jsonObject['robot_words'] = row[3]
        jsonUserList.append(jsonObject)
    return jsonify(jsonUserList)


def getallprofiles():  # noqa: E501
    """List All profiles

    Gets a list of all &#x60;profiles&#x60; entities. # noqa: E501


    :rtype: List[Profiles]
    """
    cursor.execute('''SELECT id, name, is_robot, waifu_image_url, hearts, implants from profiles''')
    all_rows = cursor.fetchall()
    jsonUserList = []
    for row in all_rows:
        jsonObject = {}
        jsonObject['id'] = row[0]
        jsonObject['name'] = row[1]
        jsonObject['is_robot'] = row[2]
        jsonObject['waifu_image_url'] = row[3]
        jsonObject['hearts'] = row[4]
        jsonObject['implants'] = row[5]
        jsonUserList.append(jsonObject)
    return jsonify(jsonUserList)


def getlikes(likesId):  # noqa: E501
    """Get a likes

    Gets the details of a single instance of a &#x60;likes&#x60;. # noqa: E501

    :param likesId: A unique identifier for a &#x60;likes&#x60;.
    :type likesId: str

    :rtype: Likes
    """
    cursor.execute('''SELECT source_player_id, dest_player_id, round_num, action, id from likes WHERE id=?''', (likesId))
    row = cursor.fetchone()
    jsonObject = {}
    jsonObject['source_player_id'] = row[0]
    jsonObject['dest_player_id'] = row[1]
    jsonObject['round_num'] = row[2]
    jsonObject['action'] = row[3]
    jsonObject['id'] = row[3]
    return jsonify(jsonObject)


def getpickup_lines(pickup_linesId):  # noqa: E501
    """Get a pickup_lines

    Gets the details of a single instance of a &#x60;pickup_lines&#x60;. # noqa: E501

    :param pickup_linesId: A unique identifier for a &#x60;pickup_lines&#x60;.
    :type pickup_linesId: str

    :rtype: PickupLines
    """
    cursor.execute('''SELECT player_id, round_num, human_words, robot_words from pickup_lines,id WHERE id=?''', (pickup_linesId))
    row = cursor.fetchone()
    jsonObject = {}
    jsonObject['player_id'] = row[0]
    jsonObject['round_num'] = row[1]
    jsonObject['human_words'] = row[2]
    jsonObject['robot_words'] = row[3]
    jsonObject['id'] = row[4]
    return jsonify(jsonObject)


def getprofiles(profilesId):  # noqa: E501
    """Get a profiles

    Gets the details of a single instance of a &#x60;profiles&#x60;. # noqa: E501

    :param profilesId: A unique identifier for a &#x60;profiles&#x60;.
    :type profilesId: str

    :rtype: Profiles
    """
    cursor.execute('''SELECT name, is_robot, waifu_image_url, hearts, implants, id from profiles WHERE id=?''', (profilesId))
    row = cursor.fetchone()
    jsonObject = {}
    jsonObject['name'] = row[0]
    jsonObject['is_robot'] = row[1]
    jsonObject['waifu_image_url'] = row[2]
    jsonObject['hearts'] = row[3]
    jsonObject['implants'] = row[4]
    jsonObject['id'] = row[5]
    return jsonify(jsonObject)


def updatelikes(likesId, body):  # noqa: E501
    """Update a likes

    Updates an existing &#x60;likes&#x60;. # noqa: E501

    :param likesId: A unique identifier for a &#x60;likes&#x60;.
    :type likesId: str
    :param body: Updated &#x60;likes&#x60; information.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        # dmg, endLat, endLong, hp, lat, long, name, radius, speed, startLat, startLong
        json = connexion.request.get_json()
        body = Likes.from_dict(json)
    if ('source_player_id' in json):
        cursor.execute('''UPDATE likes SET source_player_id = ? WHERE id = ? ''', (body.source_player_id, likesId))
    if ('dest_player_id' in json):
        cursor.execute('''UPDATE likes SET dest_player_id = ? WHERE id = ? ''', (body.dest_player_id, likesId))
    if ('round_num' in json):
        cursor.execute('''UPDATE likes SET round_num = ? WHERE id = ? ''', (body.round_num, likesId))
    if ('action' in json):
        cursor.execute('''UPDATE likes SET action = ? WHERE id = ? ''', (body.action, likesId))
    db.commit()
    return getlikes(likesId)


def updatepickup_lines(pickup_linesId, body):  # noqa: E501
    """Update a pickup_lines

    Updates an existing &#x60;pickup_lines&#x60;. # noqa: E501

    :param pickup_linesId: A unique identifier for a &#x60;pickup_lines&#x60;.
    :type pickup_linesId: str
    :param body: Updated &#x60;pickup_lines&#x60; information.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        # dmg, endLat, endLong, hp, lat, long, name, radius, speed, startLat, startLong
        json = connexion.request.get_json()
        body = PickupLines.from_dict(json)
    if ('player_id' in json):
        cursor.execute('''UPDATE pickup_lines SET player_id = ? WHERE id = ? ''', (body.player_id, pickup_linesId))
    if ('human_words' in json):
        cursor.execute('''UPDATE pickup_lines SET human_words = ? WHERE id = ? ''', (body.human_words, pickup_linesId))
    if ('round_num' in json):
        cursor.execute('''UPDATE pickup_lines SET round_num = ? WHERE id = ? ''', (body.round_num, pickup_linesId))
    if ('robot_words' in json):
        cursor.execute('''UPDATE pickup_lines SET robot_words = ? WHERE id = ? ''', (body.robot_words, pickup_linesId))
    db.commit()
    return getpickup_lines(pickup_linesId)


def updateprofiles(profilesId, body):  # noqa: E501
    """Update a profiles

    Updates an existing &#x60;profiles&#x60;. # noqa: E501

    :param profilesId: A unique identifier for a &#x60;profiles&#x60;.
    :type profilesId: str
    :param body: Updated &#x60;profiles&#x60; information.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        # dmg, endLat, endLong, hp, lat, long, name, radius, speed, startLat, startLong
        json = connexion.request.get_json()
        body = Profiles.from_dict(json)
    if ('name' in json):
        cursor.execute('''UPDATE profiles SET name = ? WHERE id = ? ''', (body.name, profilesId))
    if ('is_robot' in json):
        cursor.execute('''UPDATE profiles SET is_robot = ? WHERE id = ? ''', (body.is_robot, profilesId))
    if ('waifu_image_url' in json):
        cursor.execute('''UPDATE profiles SET waifu_image_url = ? WHERE id = ? ''', (body.waifu_image_url, profilesId))
    if ('hearts' in json):
        cursor.execute('''UPDATE profiles SET hearts = ? WHERE id = ? ''', (body.hearts, profilesId))
    if ('implants' in json):
        cursor.execute('''UPDATE profiles SET implants = ? WHERE id = ? ''', (body.implants, profilesId))
    db.commit()
    return getprofiles(profilesId)
