from flask import Flask, render_template, jsonify, request
import pymongo
from bson.json_util import loads
from bson.json_util import dumps
import pprint

#################################################

# Application Setup

#################################################


#################################################

# Flask Setup

#################################################

app = Flask(__name__)


#################################################

# Flask Routes

#################################################

conn = "mongodb://system:system@ds127936.mlab.com:27936/heroku_njlc7ffz"

client = pymongo.MongoClient(conn)

db = client.heroku_njlc7ffz.tedtalks_1

# 'technology', 'science', 'global issues', 'culture'

#Default Route#
@app.route("/")
def welcome():
    Complete = "<p>Please Click <a href='/api/All_Data'>Here</a> for the Complete Data API</p>"
    Technology = "<p>Please Click <a href='/api/technology'>Here</a> for the Technology related Talks API</p>"
    Science = "<p>Please Click <a href='/api/science'>Here</a> for the Science related Talks API</p>"
    Global = "<p>Please Click <a href='/api/global'>Here</a> for the Global Issues related Talks API</p>"
    Culture = "<p>Please Click <a href='/api/culture'>Here</a> for the Culture related Talks API</p>"
    return Complete + Technology + Science + Global + Culture

# All_Data Route


@app.route("/api/All_Data")
def All_Data():

    mylist = []
    for x in db.find():
        mylist.append(x)

    return jsonify(mylist)


@app.route("/api/technology")
def technology():
    my_data = db.find({'tags': {'$in': ['technology']}})

    mylist = []
    for x in my_data:
        mylist.append(x)

    return jsonify(mylist)


@app.route("/api/science")
def science():
    my_data = db.find({'tags': {'$in': ['science']}})

    mylist = []
    for x in my_data:
        mylist.append(x)

    return jsonify(mylist)


@app.route("/api/global")
def global_issues():
    my_data = db.find({'tags': {'$in': ['global issues']}})

    mylist = []
    for x in my_data:
        mylist.append(x)

    return jsonify(mylist)


@app.route("/api/culture")
def culture():
    # pprint.pprint(db.find({{"tags": { '$in': ['technology'] } }}).count())
    my_data = db.find({'tags': {'$in': ['culture']}})

    mylist = []
    for x in my_data:
        mylist.append(x)

    return jsonify(mylist)


if __name__ == '__main__':
    app.run(debug=True)
