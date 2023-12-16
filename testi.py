from lolapiclient import LolApiClient
from get_api_key import *

name = input("give name: ")
region = input("give region: ")

client = LolApiClient(get_api_key(), region, name)
print(client.get_match_info())
