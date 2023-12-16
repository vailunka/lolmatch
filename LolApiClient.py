import requests
from get_api_key import *


class LolApiClient():

    def __init__(self, api_key, region, summoner_name) -> None:
        self.api_key = api_key
        self.region = region
        self.summoner_name = summoner_name

    def build_url_to_get_summoner_info(self):
        api_url = "https://" + self.region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/"
        api_url_key = api_url + self.summoner_name + '?api_key=' + self.api_key
        return api_url_key
    
    def build_url_to_get_summoner_match_info(self, encrypted_summoner_id):
        api_url = "https://" + self.region + ".api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"
        api_url_key = api_url + encrypted_summoner_id + '?api_key=' + self.api_key
        return api_url_key
    

    def get_summoner_info(self):
        """This function return player info"""
        r = requests.get(self.build_url_to_get_summoner_info())  
        info = r.json()
        print(info)
        return info["id"], info["accountId"], info["puuid"], info["name"], info["profileIconId"], info["revisionDate"], info["summonerLevel"]
    
    def get_encrypted_summoner_id(self):
        """This function return player info"""
        r = requests.get(self.build_url_to_get_summoner_info())
        info = r.json()
        return info["id"]

    def get_match_info(self):
        r = requests.get(self.build_url_to_get_summoner_match_info(self.get_encrypted_summoner_id()))
        info = r.json()
        print(info)
        


