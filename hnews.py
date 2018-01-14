import requests


topics = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty').json()

print topics[0]

toptopics = [topics[0], topics[1], topics[2], topics[3], topics[4]]
topics = []


for x in toptopics:
    r = requests.get('https://hacker-news.firebaseio.com/v0/item/' + str(x) + '.json?print=pretty').json() 
    topics.append(r['title'])

print topics

