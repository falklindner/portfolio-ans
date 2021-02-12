import secrets as secrets
import json
from comdirect_api.comdirect_client import ComdirectClient

client = ComdirectClient(secrets.api_key["comdirect"], secrets.api_secret["comdirect"])

client.fetch_tan(secrets.username["comdirect"], secrets.password["comdirect"])
client.activate_session(tan="")

depot_json_object = client.get_all_depots()

depot_list= depot_json_object["values"]
depot_id_list = []

for depot in depot_list:
    depot_id_list += [depot["depotId"]]