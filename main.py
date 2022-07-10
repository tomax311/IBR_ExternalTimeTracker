import dynmap_api
import time
import os

#Gets the players position on a given server link with the dynmap
def PlayerPos(url,world):
	ServerData = dynmap_api.net.fetchServerUpdate(dynmap_url=url, world=world)
	plAmount = ServerData.currentcount
	AllPos = []
	for i in range(plAmount):
		players = ServerData.players
		print(players)
		player1 = str(players[i-1])
		player1 = player1.replace("=", " ")
		player1 = player1.replace("'", " ")
		x = player1.split()

		playerPos = []
		playerPos.append(x[3])
		playerPos.append(x[7])
		playerPos.append(x[11])


		AllPos.append(playerPos)
	return AllPos


#checkpoint detctor for minecraft on the y axis
def CPTrackerY(CPx,CPy1,CPy2,POSx1,POSy1,POSx2,POSy2):
		r = (CPx - POSx1) / (POSx2 - POSx1)
		post = (POSy2 - POSy1) * r + POSy1

		if CPy1 <= post and CPy2 >= post:
			return True
		else:
			return False


#checkpoint detctor for minecraft on the x axis
def CPTrackerX(CPy,CPx1,CPx2,POSx1,POSy1,POSx2,POSy2):
		r = (CPy - POSy1) / (POSy2 - POSy1)
		post = (POSx2 - POSx1) * r + POSx1

		if CPx1 <= post and CPx2 >= post:
			return True
		else:
			return False

#This function is to choose witch way the checpoint is (use "X"/"Y")
#CP variable example CP = [the lonely coord,the first coord,the second coord]
def CP(direction,CP,PlayerPos1,PlayerPos2):

	POSx1 = int(PlayerPos1[1])
	POSy1 = int(PlayerPos1[2])
	POSx2 = int(PlayerPos2[1])
	POSy2 = int(PlayerPos2[2])

	if direction == "X" :

		CPy = CP[0]
		CPx1 = CP[1]
		CPx2 = CP[2]

		return CPTrackerX(CPy, CPx1, CPx2, POSx1, POSy1, POSx2, POSy2)

	else:
		CPx = CP[0]
		CPy1 = CP[1]
		CPy2 = CP[2]

		return CPTrackerY(CPx, CPy1, CPy2, POSx1, POSy1, POSx2, POSy2)

#while True:
	#PlayerPos1 = PlayerPos("https://earthmc.net/map/aurora/","earth")[0]
	#print(PlayerPos1)
	#time.sleep(0.5)
	#PlayerPos2 = PlayerPos("https://earthmc.net/map/aurora/","earth")[0]
	#print(PlayerPos2)

#print(PlayerPos("https://earthmc.net/map/aurora/","earth"))
#print(len(PlayerPos("https://earthmc.net/map/aurora/","earth")))

#PlayerPos1 = PlayerPos("https://earthmc.net/map/aurora/","earth")
#print(len(PlayerPos1))


PlayerPos("https://earthmc.net/map/aurora/","earth")


#temporary code to delete the race data file automaticly

if os.path.exists("RaceDataTest.txt"):
  os.remove("RaceDataTest.txt")
else:
  print("RaceDataTest.txt does not exist")

#get data during race
file = open("RaceDataTest.txt", "x")
print("Started writting the players positions")
file.write("test:\n")

while True :
	#file.write(PlayerPos("http://localhost:8123/","world"))
	#file.write(PlayerPos("http://mc.mythcosmos.de:8123/","Boatrace"))
	#file.write(str(PlayerPos("https://earthmc.net/map/aurora/", "earth"))+"\n")
	file.write(str(PlayerPos("http://mc.mythcosmos.de:8123/up/world/bootsrennen2/0", "bootsrennen2"))+"\n")
	time.sleep(0.1)
file.close()