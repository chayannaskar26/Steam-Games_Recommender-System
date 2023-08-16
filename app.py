from flask import Flask
from flask import render_template
from flask import send_from_directory
import pandas as pd
import numpy as np
import json
from urllib.request import urlopen

import pickle
games = pickle.load(open('Games.pkl', 'rb'))
games_data = games[['appid', 'title']].to_json(orient="records")

similarity = pickle.load(open('Similarity.pkl', 'rb'))

def recommendGame(game_index):
   recommended_games = []
   distances = sorted(list(enumerate(similarity[game_index])), reverse=True, key=lambda x: x[1])
   
   for i in distances[1:7]:
      recommended_games.append({'appid': games.iloc[i[0]].appid, 'title': games.iloc[i[0]].title})

   return recommended_games

def getSelectedGameData(appid):
   res = urlopen(f'https://store.steampowered.com/api/appdetails?appids={appid}&l=english')
   res_json = json.load(res)
   json_data = res_json[f'{appid}']['data']

   return json_data

title = 'Steam Game Recommender'

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html', games_data = games_data, title=title)

@app.route('/game/<appid>')
def game(appid):
   game_index = games[games['appid']==int(appid)].index[0]
   recommended_games = recommendGame(game_index)

   json_data = getSelectedGameData(appid)

   selected_game_data = {
      'title': json_data['name'],
      'description': json_data['short_description'],
      'is_free': json_data['is_free'],
      'supported_languages': json_data['supported_languages'],
      'developers': json_data['developers'],
      'publishers': json_data['publishers'],
      'platforms': json_data['platforms'],
      'categories': json_data['categories'],
      'genres': json_data['genres'],
      'release_date': json_data['release_date']['date'],
   }

   return render_template('game.html', title = title, appid = appid, recommended_games = recommended_games, selected_game_data = selected_game_data)


# main driver function
if __name__ == '__main__':
   app.run()