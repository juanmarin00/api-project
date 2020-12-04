import pandas as pd
import postdata as post

data = pd.read_csv("../data/office_modified_sentiment.csv", index_col=0)

data['episode'] = data['episode'].apply(str)
data['scene'] = data['scene'].apply(str)
data['season'] = data['season'].apply(str)




#Insert into mongodb all rows into the line collection using pandas
for index, row in data.iterrows():
    ep_id = row["episode_id"]
    char = row["speaker"]
    line = row["line_text"]
    post.insertLine(ep_id, char, line)





#Insert all episodes with all their characters into the "episode" collection
ep_dict = {}
for index, row in data.iterrows():
    character = row["speaker"]
    episode = row["episode_id"]
    #No key for that episode
    #create key
    if episode in ep_dict.keys() and character not in ep_dict.get(episode):
        ep_dict[episode].append(character)
    
    elif episode not in ep_dict.keys():
        ep_dict[episode] = []
    
    else:
        pass


#Add all episodes to episode collection
for key, value in ep_dict.items():
    episode_id = key
    character_list = value
    post.insertEpisode(episode_id, character_list)






#Insert all seasons and their episodes into "season" collection
season_dict = {}
for index, row in data.iterrows():
    season = row["episode_id"][0]
    episode = row["episode_id"]
    
    if season in season_dict.keys() and episode not in season_dict.get(season):
        season_dict[season].append(episode)
    
    elif season not in season_dict.keys():
        season_dict[season] = []
    
    else:
        pass

#Add all seasons to season collection
for key, value in season_dict.items():
    season_id = key
    episode_list = value
    post.insertSeason(season_id, episode_list)





#Insert all characters and their lines into "character" collection
character_dict = {}
for index, row in data.iterrows():
    character = row["speaker"]
    line = row["line_text"]
    
    if character not in character_dict.keys():
        character_dict[character] = []
    
    else:
        character_dict[character].append(line)
    


#add all characters and their lines to collection
for key, value in character_dict.items():
    character = key
    lines = value
    post.insertCharacter(character, lines)