import json
import pprint

def item_generator(json_input, lookup_key):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)

with open('C:/CODE/RAW FILES/citylots.json', 'r') as f:
    distros_dict = json.load(f)
    for id, value in enumerate(item_generator(distros_dict, "coordinates")):
        if id > 200000:
            pprint.pprint(value)
            break

 #https://gist.github.com/douglasmiranda/5127251
