import riotConstants
import requests
import json

def getAccountID(sumName):
    requestURL = riotConstants.BASE_URL_NA + sumName + riotConstants.API_KEY_PORTION
    response = requests.get(requestURL)
    return response.json()['accountId']

def getRecentGameID(accountId):
    requestURL = riotConstants.BASE_URL_RECENT_MATCH + str(accountId) + riotConstants.RECENT_MATCH_INDEX_PORTION
    response = requests.get(requestURL)
    matches = response.json()['matches']
    return str(matches[0]['gameId'])

def getMatchData(gameId):
    requestURL = riotConstants.BASE_URL_MATCH_DATA + gameId + riotConstants.API_KEY_PORTION
    response = requests.get(requestURL)
    return response.json()

def getChampionInfo():
    requestURL = riotConstants.CHAMPION_DATA
    response = requests.get(requestURL)
    return response.json()


def getPlayerStats(gameId,accountId):
# @TODO handle if participant not in game

    gameStats_json = getMatchData(gameId) 
    participantId = None 
    
    participantsId_array = gameStats_json['participantIdentities']

    ## make into own method 
    for p in participantsId_array:
        
        tempId = p['player']['accountId']

        if tempId == accountId:
            participantId = p['participantId']

    playersStats_array= gameStats_json['participants']
     
    if participantId is not None:

        for p in playersStats_array:
            temp = p['participantId'] 
            if temp == participantId:
                return p['stats']
    return None 

def getChampNameFromGame(gameId,accountId):

    gameStats_json = getMatchData(gameId) 
    participantId = None 
    
    participantsId_array = gameStats_json['participantIdentities']

    ## make into own method 
    for p in participantsId_array:
        
        tempId = p['player']['accountId']

        if tempId == accountId:
            participantId = p['participantId']

    playersStats_array= gameStats_json['participants']
    champId = None 

    if participantId is not None:

        for p in playersStats_array:
            temp = p['participantId'] 
            if temp == participantId:
                champId = p['championId']

    print(type(champId))
    if champId is not None: 
        
        champId = str(champId)
        champ_info_json = getChampionInfo()

        for p, n in champ_info_json['data'].items():
            temp = n['key']
            if temp == champId:
                return n['name']
    return None 




def getGameStatsFormGame(playerStats, accountId, gameId):
## using strings to test

    win = "win: " + str(playerStats['win'])
    roleplayed = "roleplayed: " + 'need to implement'
    champlayed = "champlayed: " + str(getChampNameFromGame(gameId, accountId))
    kda = "kda: " + str(playerStats['kills']) + "/" + str(playerStats['deaths']) + "/" + str(playerStats['assists']) 
    cs = "cs: " + 'need to implement'
    goldCount = "goldCount: " + str(playerStats['goldEarned'])

    return win +"\n" + roleplayed +"\n" + champlayed +"\n" +  win +"\n" + kda + "\n" + cs + "\n" + goldCount





       



