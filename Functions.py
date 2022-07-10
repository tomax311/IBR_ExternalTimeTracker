import requests

#Gets the players position on a given server link with the dynmap
def PlayerPos(url):

	r = requests.get(url).json()
	plAmount = r["currentcount"]

	AllPos = []
	for i in range(plAmount):


		playerPos = []
		playerPos.append(r["players"][0]["name"])
		playerPos.append(r["players"][0]["x"])
		playerPos.append(r["players"][0]["y"])


		AllPos.append(playerPos)
	return AllPos

print(PlayerPos("http://mc.mythcosmos.de:8123/up/world/bootsrennen2/0"))