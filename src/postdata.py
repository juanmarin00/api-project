from config.configuration import db
from pymongo import MongoClient

def insertLine(episode_id,character_name,line, season):
    """
    insert a line by a characer on a certain episode
    """
    collection = db["lines"]
    dict_insert = { "episode" : f"{episode_id}",
    "season" : f"{season}",
    "character_name" : f"{character_name}",
    "dialogue": f"{line}"
    }
    collection.insert_one(dict_insert)


def insertCharacter(character_name, lines):
    """
    Takes a characters name and a list of episodes they feature in
    and creates a document for that character
    """
    collection = db["character"]
    dict_insert = {"character_name" : f"{character_name}",
    "lines": lines
    }
    collection.insert_one(dict_insert)


def insertEpisode(episode_id, characters):
    """
    Takes an episode name and a list of characters featured in
    and creates a document for that episode
    """
    collection = db["episode"]
    dict_insert = {"episode_id" : f"{episode_id}",
    "characters": characters
    }
    collection.insert_one(dict_insert)


def insertSeason(season_num, episodes):
    """
    Takes an season number and a list of episodes featured in
    and creates a document for that season
    """
    collection = db["season"]
    dict_insert = {"season_num" : f"{season_num}",
    "episodes": episodes
    }
    collection.insert_one(dict_insert)

