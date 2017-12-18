import riotConstants
import requests
import json

def getSumID(sumName):
    requestURL = riotConstants.BASE_URL_NA + sumName + riotConstants.API_KEY_PORTION
    response = requests.get(requestURL)
    return str(response.json()['accountId'])

def getRecentGameID(accountId):
    requestURL = riotConstants.BASE_URL_RECENT_MATCH + accountId + riotConstants.RECENT_MATCH_INDEX_PORTION
    response = requests.get(requestURL)
    matches = response.json()['matches']
    return str(matches[0]['gameId'])




