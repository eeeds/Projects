from urllib.request import urlopen
import json

base_url = "https://xkcd.com/info.0.json"

# To convert bytes in text
data = urlopen(base_url).read().decode('UTF-8')

# json.loads to decode in text
data_json_obj = json.loads(data)

print(data_json_obj["img"])