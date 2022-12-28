import requests




#Test that works, Words that rhyme with 'jingle'


jingle = requests.get('http://api.datamuse.com/words?rel_rhy=jingle')
jingle_json = jingle.json()
print(jingle_json)



#Variable Parameter
parameter = {"rel_rhy":"jingle"}
jingle = requests.get('http://api.datamuse.com/words?',parameter)
jingle_json = jingle.json()
print(jingle_json)

for i in jingle_json[0:3]:
    print(i['word'])




