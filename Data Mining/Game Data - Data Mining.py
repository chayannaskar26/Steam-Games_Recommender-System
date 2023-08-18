# Importing required libraries
import pandas as pd
import json
from urllib.request import urlopen

# Fetch Game Data Methods
def getGameData(appid):
    res = urlopen(f'https://store.steampowered.com/api/appdetails?appids={appid}&l=english')
    res_json = json.load(res)
    json_data = res_json[f'{appid}']['data']
    return [
        appid,
        json_data['name'],
        json_data['short_description'],
        json_data['is_free'],
        json_data['supported_languages'],
        json_data['developers'],
        json_data['publishers'],
        json_data['platforms'],
        json_data['categories'],
        json_data['genres'],
        json_data['release_date']['date'],
    ]
    
# Declaring Coloumn Names
column_names = ['appid', 'title', 'short_description', 'is_free', 'supported_languages', 'developers', 'publishers' ,'platforms', 'categories', 'genres', 'release_date']

# Ubisoft Dataset Game Data 
def getUbisoftDetailsData():
    ubisoft_df = pd.read_csv('Steam Ubisoft Games.csv')

    req_json_list = []

    for appid in ubisoft_df['appid']:
        req_json_list.append(getGameData(appid))
        
    ubisoft_details_df = pd.DataFrame(req_json_list, columns=column_names)

    return ubisoft_details_df 


# Valve Dataset Game Data
def getValveDetailsData():
    valve_df = pd.read_csv('Steam Valve Games.csv')

    req_json_list = []

    for appid in valve_df['appid']:
        req_json_list.append(getGameData(appid))
        
    valve_details_df = pd.DataFrame(req_json_list, columns=column_names)

    return valve_details_df 


# Activision Dataset Game Data
def getActivisionDetailsData():
    activision_df = pd.read_csv('Steam Activision Games.csv')

    req_json_list = []

    for appid in activision_df['appid']:
        req_json_list.append(getGameData(appid))
        
    activision_details_df = pd.DataFrame(req_json_list, columns=column_names)

    return activision_details_df 


# Bethesda Dataset Game Data
def getBethesdaDetailsData():
    bethesda_df = pd.read_csv('Steam Bethesda Games.csv')

    req_json_list = []

    for appid in bethesda_df['appid']:
        req_json_list.append(getGameData(appid))
    bethesda_details_df = pd.DataFrame(req_json_list, columns=column_names)

    return bethesda_details_df 


# EA Dataset Game Data 
def getEADetailsData():
    ea_df = pd.read_csv('Steam EA Games.csv')

    req_json_list = []

    for appid in ea_df['appid']:
        req_json_list.append(getGameData(appid))
    ea_details_df = pd.DataFrame(req_json_list, columns=column_names)

    return ea_details_df 


# Other Dataset Game Data 
def getOtherDetailsData():
    other_df = pd.read_csv('Steam Other Games.csv')
    req_json_list = []

    for appid in other_df['appid']:
        req_json_list.append(getGameData(appid))
    other_details_df = pd.DataFrame(req_json_list, columns=column_names)

    return other_details_df 


def main():
    valve_details_df = getValveDetailsData()
    activision_details_df = getActivisionDetailsData()
    ubisoft_details_df = getUbisoftDetailsData()
    bethesda_details_df = getBethesdaDetailsData()
    ea_details_df = getEADetailsData()
    other_details_df = getOtherDetailsData()
    
    # Concating to final dataframe
    final_df = pd.concat([valve_details_df, activision_details_df, ubisoft_details_df, bethesda_details_df, ea_details_df, other_details_df])
    final_df.reset_index(inplace=True, drop=True) 
    final_df.to_csv('../Steam Game Details.csv')


if __name__ == "__main__":
    main()