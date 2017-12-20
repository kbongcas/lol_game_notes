
## @TODO make a better way to do these

import secrets

BASE_URL_NA = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"
API_KEY_PORTION = "?api_key=" + secrets.MY_RIOT_API_KEY

BASE_URL_RECENT_MATCH = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/"
RECENT_MATCH_INDEX_PORTION ="?beginIndex=0&endIndex=1&api_key=" + secrets.MY_RIOT_API_KEY

BASE_URL_MATCH_DATA = "https://na1.api.riotgames.com/lol/match/v3/matches/"


BASE_URL_MATCH = "https://na1.api.riotgames.com/lol/match/v3/matches/"

