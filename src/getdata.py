from config.configuration import db
from pymongo import MongoClient
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


#Get all lines for any character
def get_character_lines(name):
    """
    Hacemos una query a la base de datos para sacar las frases de un personaje
    """
    lines = db["lines"]
    query = {"character_name":f"{name}"}
    frases = list(lines.find(query,{"_id":0}))
    lines_list = []
    for frase in frases:
        lines_list.append(frase.get("dialogue"))
    return lines_list


#Get episode numbers for each season
def get_season_episodes(season_number):
    season = db["season"]
    query = {"season_num":f"{season_number}"}
    episodes = list(season.find(query,{"_id":0}))
    ep_numbers = []
    for epi in episodes:
        ep_numbers.append(epi.get("episodes"))
    return ep_numbers

#Get all of the characters in an episode
def get_all_characters_from_episode(episode_numer):
    episode = db["episode"]
    query = {"episode_id":f"{episode_numer}"}
    characters = list(episode.find(query,{"_id":0}))
    character_list = []
    for character in characters:
        character_list.append(character.get("characters"))
    return character_list


#get all the lines in an episode by a character
def get_character_lines_episode(episode_id, name):
    lines = db["lines"]
    query = {"character_name":f"{name}", "episode":f"{episode_id}"}
    frases = list(lines.find(query,{"_id":0}))
    lines_list = []
    for frase in frases:
        lines_list.append(frase.get("dialogue"))
    return lines_list

#Get all lines in an episode
def get_all_lines_episode(episode_id):
    
    lines = db["lines"]
    query = {"episode":f"{episode_id}"}
    frases = list(lines.find(query,{"_id":0}))
    lines_list = []
    for frase in frases:
        lines_list.append(frase.get("dialogue"))
    return lines_list


#Get all lines in a season by character
def get_all_lines_season_character(season, name):
        
    lines = db["lines"]
    query = {"character_name":f"{name}","season":f"{season}"}
    frases = list(lines.find(query,{"_id":0}))
    lines_list = []
    for frase in frases:
        lines_list.append(frase.get("dialogue"))
    return lines_list


#Get all lines in a season
def get_all_lines_season(season):
        
    lines = db["lines"]
    query = {"season":f"{season}"}
    frases = list(lines.find(query,{"_id":0}))
    lines_list = []
    for frase in frases:
        lines_list.append(frase.get("dialogue"))
    return lines_list


#Auxiliary function for sentiment of a line of dialogue
def sentimentAnalysis_one_line(line):
    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(line)
    pol = polarity['compound']
    return pol

#Get average sentiment of a character throughout the series
def average_sentiment_character(character):
    all_lines = get_character_lines(character)
    total_polarity = 0
    no_polarity = 0
    
    for line in all_lines:
        if sentimentAnalysis_one_line(line) == 0.0:
            no_polarity += 1
            pass
        else:
            total_polarity += sentimentAnalysis_one_line(line)
    
    avg_polarity = total_polarity/(len(all_lines) - no_polarity)
    return avg_polarity


#Get average sentiment of an episode
def average_sentiment_episode(episode):
    all_lines = get_all_lines_episode(episode)
    total_polarity = 0
    no_polarity = 0
    
    for line in all_lines:
        if sentimentAnalysis_one_line(line) == 0.0:
            no_polarity += 1
            pass
        else:
            total_polarity += sentimentAnalysis_one_line(line)
    
    avg_polarity = total_polarity/(len(all_lines) - no_polarity)
    return avg_polarity