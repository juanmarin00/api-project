from flask import Flask, request
#instalar librería md ojito
import markdown.extensions.fenced_code
import random
import json
import src.getdata as get
import src.postdata as pos

app = Flask(__name__)


@app.route("/")
def index():
    readme_file = open("README.md","r")
    md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template_string



#######################GET endpoints:#######################

#Get all lines of a character
@app.route("/frases/<personaje>")
def character_lines(personaje):
    #la función get.pensajepersonaje viene de tools getdata.py
    frases = get.get_character_lines(personaje)
    return json.dumps(frases)

#Get all episodes in a season
@app.route("/season/<season_number>")
def season_episodes(season_number):
    #la función get.pensajepersonaje viene de tools getdata.py
    episodes = get.get_season_episodes(season_number)
    return json.dumps(episodes)

#Get all characters in an episode
@app.route("/characters_episode/<ep_number>")
def episode_characters(ep_number):
    #la función get.pensajepersonaje viene de tools getdata.py
    characters = get.get_all_characters_from_episode(ep_number)
    return json.dumps(characters)


#Get all the lines in an episode by all characters
@app.route("/lines_episode/<ep_number>")
def get_char_lines_ep(ep_number):
    #la función get.pensajepersonaje viene de tools getdata.py
    lines = get.get_all_lines_episode(ep_number)
    return json.dumps(lines)


#Get all the lines in a season
@app.route("/lines_season/<seasom_number>")
def get_all_lines_season(seasom_number):
    #la función get.pensajepersonaje viene de tools getdata.py
    lines = get.get_all_lines_season(seasom_number)
    return json.dumps(lines)


#Get character sentiment throughout the series
@app.route("/character_sentiment/<character>")
def get_character_sentiment(character):
    #la función get.pensajepersonaje viene de tools getdata.py
    sentiment = get.average_sentiment_character(character)
    return json.dumps(sentiment)


#Get sentiment throughout an episode
@app.route("/episode_sentiment/<episode_num>")
def get_episode_sentiment(episode_num):
    #la función get.pensajepersonaje viene de tools getdata.py
    sentiment = get.average_sentiment_episode(episode_num)
    return json.dumps(sentiment)





#######################POSt endpoints:#######################


#Insert a line in the lines collection
@app.route("/newline",methods=["POST"])
def insertamensaje():
    episode = request.form.get("episode")
    season = request.form.get("season")
    character_name = request.form.get("character_name")
    line = request.form.get("dialogue")
    pos.insertLine(episode, character_name, line, season)
    return "Line correctly introduced in database"


#Insert a new character in the characters collection
@app.route("/newcharacter",methods=["POST"])
def insert_character():
    character_name = request.form.get("character_name")
    lines = request.form.get("lines")
    pos.insertCharacter(character_name, lines)
    return "Episode correctly introduced in database"


#Insert a new episode in the episode collection
@app.route("/newepisode",methods=["POST"])
def insert_epi():
    episode_id = request.form.get("episode_id")
    characters = request.form.get("characters")
    pos.insertEpisode(episode_id, characters)
    return "Episode correctly introduced in database"


#Insert a new season in the seasons collection
@app.route("/newseason",methods=["POST"])
def insert_season():
    season_num = request.form.get("season_num")
    episodes = request.form.get("episodes")
    pos.insertSeason(season_num, episodes)
    return "Line correctly introduced in database"





#Run our app
app.run(debug=True)