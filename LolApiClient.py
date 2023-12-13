import requests
from get_api_key import *
class LolApiClient():

    def __init__(self, api_key, region) -> None:
        self.api_key = api_key
        self.region = region

    #api_key = ""
    #testi_region = "euw1"
    #testi_summoner_name = "TurboGnome"

    

    def build_url(self, summoner_name):
        api_url = "https://" + self.region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/"
        api_url_key = api_url + summoner_name + '?api_key=' + self.api_key
        return api_url_key
    

    def get_encrypted_summoner_name(self, summoner_name):
        """This function return player info"""
        r = requests.get(self.build_url(summoner_name))  
        info = r.json()
        return info["id"], info["accountId"], info["puuid"], info["name"], info["profileIconId"], info["revisionDate"], info["summonerLevel"]


    def game_info(self):
        pass

    

client = LolApiClient(get_api_key(), "EUW1")
print(client.get_encrypted_summoner_name("TurboGnome"))




