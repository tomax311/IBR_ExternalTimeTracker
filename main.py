import Functions

url = "http://mc.mythcosmos.de:8123/up/world/bootsrennen2/0"
zandvoortcp = ["Z",-1389,-259,-251]

Functions.datatotime("test1.json",1)

if Functions.plAmount(url) >> 0:
	Functions.datarec("test1.json",10,url)
else:
	print("No players are online there is no point of recording data")

