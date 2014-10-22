import requests


r = requests.get('http://api.wunderground.com/api/63577728b0e9ae1f/conditions/q/CA/San_Francisco.json'

print r.status_code

# j = r.json()

# temperature = j['current_observation']['temperature_string']
# print temperature