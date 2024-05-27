import json
#--------------python to json
person = {"Name": "Lucky", "Age": 25, "City": "Kisumu", "hasChildren": "False",
          "Titles": ["Software developer", "Programmer", "Ethical harcker"]}

personJSON = json.dumps(person, indent=4, separators=('; ', '='), sort_keys = True)
print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent = 4)

#---------------json to python
person = json.loads(personJSON)
print(person)

with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)