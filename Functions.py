import requests
import os
import time
import json


# Gets the players position on a given server link with the dynmap
def PlayerPos(url):
	r = requests.get(url).json()
	plAmount = r["currentcount"]

	AllPos = []
	for i in range(plAmount):
		playerPos = [r["players"][i - 1]["name"],r["players"][i - 1]["x"],r["players"][i - 1]["z"]]
		AllPos.append(playerPos)
	return AllPos

#return a clean player list with coordinates
def playerdict(url):
	r  = requests.get(url).json()
	pldict = []
	for i in range(plAmount(url)):
		x = {r["players"][i - 1]["name"],r["players"][i - 1]["x"],r["players"][i - 1]["z"]}
		pldict.append(x)
	return pldict

# this function returns a current player count on a given server
def plAmount(url):
	r = requests.get(url).json()
	plAmount = r["currentcount"]
	return plAmount

# checkpoint detector for minecraft on the y axis
def CPTrackerY(CPx, CPy1, CPy2, POSx1, POSy1, POSx2, POSy2):
	r = (CPx - POSx1) / (POSx2 - POSx1)
	post = (POSy2 - POSy1) * r + POSy1

	if CPy1 <= post and CPy2 >= post:
		return True
	else:
		return False


# checkpoint detector for minecraft on the x axis
def CPTrackerX(CPy, CPx1, CPx2, POSx1, POSy1, POSx2, POSy2):
	r = (CPy - POSy1) / (POSy2 - POSy1)
	post = (POSx2 - POSx1) * r + POSx1

	if CPx1 <= post and CPx2 >= post:
		return True
	else:
		return False


# This function is to choose witch way the checkpoint is (use "X"/"Z")
# CP variable example CP = [direction,the lonely coord,the first coord,the second coord]
def CP( CP, PlayerPos1, PlayerPos2 ):
	POSx1 = int(PlayerPos1[1])
	POSy1 = int(PlayerPos1[2])
	POSx2 = int(PlayerPos2[1])
	POSy2 = int(PlayerPos2[2])

	if CP[0] == "X":

		CPy = CP[1]
		CPx1 = CP[2]
		CPx2 = CP[3]

		r = (CPy - POSy1) / (POSy2 - POSy1)
		post = (POSx2 - POSx1) * r + POSx1

		if CPx1 <= post and CPx2 >= post:
			return True
		else:
			return False

	else:
		CPx = CP[1]
		CPy1 = CP[2]
		CPy2 = CP[3]

		r = (CPx - POSx1) / (POSx2 - POSx1)
		post = (POSy2 - POSy1) * r + POSy1

		if CPy1 <= post and CPy2 >= post:
			return True
		else:
			return False

# this functions records all players positions on a given server during a set time (all times in seconds)
def datarec(filename,ti,url):

	finishtime = time.monotonic_ns() + ti * 1000000000
	currenttime = time.monotonic_ns()

	# code to delete the race data file automatically
	if os.path.exists(filename):
		print(f"{filename} already exists. Do you want to overwrite the file ?(y/n)")
		if input() == "y":
			os.remove(filename)
		else:
			print("Recording trial interupted")
			return
	else:
		print(f"{filename} does not exist. Creating file...")

	# gets data during recording
	ppos2 = PlayerPos(url)
	i = 1
	with open(filename, "w") as outfile:
		print("started recording data")
		d = {}
		while currenttime <= finishtime:
			ppos1 = PlayerPos(url)
			d[f"pos{i}"] = {"time": time.asctime(time.gmtime()), "players": ppos1}
			i = i + 1
			currenttime = time.monotonic_ns()
			ppos2 = PlayerPos(url)
		json.dump(d,outfile,indent=1)

	print("recording finished")

def	datatotime(filename,cp):

	f = open(filename)
	pos = json.load(f)


	for i in range(0,len(pos)):
		print(i)
		print(pos[f"pos{i+1}"])

