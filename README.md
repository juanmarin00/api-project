
# Creating an API using Flask
In this project I created an API using Python, Flask, MongoDB and Sentiment Analysis to let users obtain data from the popular TV show "The Office"
# How does it work?
Users will have the option to load their own data using POST Methods (more on that later) or can use the data which can be found in the data folder which will load a mongo database with all the script from all the episodes in the Office. Then users can use the GET methods to get data such as how many characters where present in an episode or the setiment of any episode.


# Methods
## @POST
Endpoints:
- /newline/line
Will insert a line into the lines collection
- /newcharacter/character
Will insert a character into the character collection
- /newepisode/episode
Will insert a episode into the episode collection
- /newseason/season
Will insert a season into the season collection


# @GET
Endpoint
- /frases/<personaje>
Will return a list of all the lines for the wanted character
- /season/<season_number>
Will return a list of all the episodes for the wanted season
- /characters_episode/<ep_number>
Will return a list of all the character for the wanted episode
- /lines_episode/<ep_number>
Will return a list of all the lines for the wanted episode
- /lines_season/<seasom_number>
Will return a list of all the lines for the wanted season
- /character_sentiment/<character>
Will return character sentiment throughout the series
- /episode_sentiment/<episode_num>
Will return the sentiment throughout an episode


# Repo Organization:
src: Contains the get, post files and  modify_data.py will take the data from the data folder and import it into MongoDB

data: Contains CSVs with the script from the office where every row is a line from the script

miapi.py: The file you need to run for the api to work

notebooks: contains test_api.ipynb notebook used to test all api endpoints

