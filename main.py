import Functions
import time
import os


# this saves data during 2 minutes on a given server


finishtime = time.monotonic_ns() + 120_000_000_000
currenttime = time.monotonic_ns()

filetime = time.strftime("%Y.%d.%m.%Hh.%Mm.%Ss")
print(filetime)
filename = f"{filetime}_RaceDataTest"

# temporary code to delete the race data file automatically
if os.path.exists(filename):
	os.remove(filename)
else:
	print(f"{filename} does not exist")

# get data during race and storing it for after
file = open(filename, "x")
print("Started writing the players positions")
file.write("Started saving positions on " + time.asctime(time.gmtime()) + " :\n")

while currenttime <= finishtime:
	file.write(str(Functions.PlayerPos("http://mc.mythcosmos.de:8123/up/world/bootsrennen2/0")) + "\n")
	time.sleep(0.1)
	currenttime = time.monotonic_ns()
file.close()
print("process finished")
