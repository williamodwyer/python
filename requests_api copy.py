import requests

# interact with NASA api, to pull 'people in space' data in json
'''
request = requests.get('http://api.open-notify.org')
#request = requests.get('http://api.open-notify.org/fake-endpoint')
print(request.status_code)

print("\n")

#convert into json format
people = requests.get('http://api.open-notify.org/astros.json')
people_json = people.json()
print(people_json)

print("\nNumber of people in space is:", people_json['number'])

print('\n')

#print out each name
for p in people_json['people']:
    print(p['name'])


for c in people_json['people']:
    print(c['craft'])
'''

#Test that works, Words that rhyme with 'jingle'

'''
jingle = requests.get('http://api.datamuse.com/words?rel_rhy=jingle')
jingle_json = jingle.json()
print(jingle_json)

'''

#Variable Parameter
parameter = {"rel_rhy":"jingle"}
jingle = requests.get('http://api.datamuse.com/words?',parameter)
jingle_json = jingle.json()
print(jingle_json)

for i in jingle_json[0:3]:
    print(i['word'])




