import requests


# Gets the players position on a given server link with the dynmap
def PlayerPos(url):
	r = requests.get(url).json()
	plAmount = r["currentcount"]

	AllPos = []
	for i in range(plAmount):
		playerPos = []
		playerPos.append(r["players"][i - 1]["name"])
		playerPos.append(r["players"][i - 1]["x"])
		playerPos.append(r["players"][i - 1]["z"])

		AllPos.append(playerPos)
	return AllPos


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


# This function is to choose witch way the checkpoint is (use "X"/"Y")
# CP variable example CP = [the lonely coord,the first coord,the second coord]
def CP(direction, CP, PlayerPos1, PlayerPos2):
	POSx1 = int(PlayerPos1[1])
	POSy1 = int(PlayerPos1[2])
	POSx2 = int(PlayerPos2[1])
	POSy2 = int(PlayerPos2[2])

	if direction == "X":

		CPy = CP[0]
		CPx1 = CP[1]
		CPx2 = CP[2]

		r = (CPy - POSy1) / (POSy2 - POSy1)
		post = (POSx2 - POSx1) * r + POSx1

		if CPx1 <= post and CPx2 >= post:
			return True
		else:
			return False

	else:
		CPx = CP[0]
		CPy1 = CP[1]
		CPy2 = CP[2]

		r = (CPx - POSx1) / (POSx2 - POSx1)
		post = (POSy2 - POSy1) * r + POSy1

		if CPy1 <= post and CPy2 >= post:
			return True
		else:
			return False
