import requests


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




