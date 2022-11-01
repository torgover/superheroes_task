import requests
url = 'https://akabab.github.io/superhero-api/api/all.json'

response = requests.get(url)
heroes = response.json()


heroes_ = filter(lambda hero: hero['name'] in ['Hulk','Thanos', 'Captain America'], heroes)

diction = {hero['name']:hero['powerstats']['intelligence'] for hero in heroes_}
print(max(diction))

        