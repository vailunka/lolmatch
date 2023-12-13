from LolApiClient import LolApiClient
from get_api_key import get_api_key



class summoner_info():
    def __init__(self, id, accountId, puuId, name, profileIconId, revisionDate, summonerLevel):
        self.id = id
        self.accountId = accountId
        self.puuId = puuId
        self.name = name
        self.profileIconId = profileIconId
        self.revisionDate = revisionDate
        self.summonerLevel = summonerLevel
        


    def match_info(self, id):
        pass


client = LolApiClient(get_api_key(), "EUW1")
id, accountId, puuid, name, profileIconId, revisionDate, summonerlevel = client.get_encrypted_summoner_name("TurboGnome")
new_summoner_info = summoner_info(id, accountId, puuid, name, profileIconId, revisionDate, summonerlevel)
print(new_summoner_info.__dict__)






    