import json

# Looping through JSON
with open('states.json') as file:
  data = json.load(file)

for state in data['states']:
  del state['area_codes']
  
with open('new_states.json', 'w') as file:
  json.dump(data, file, indent=2)