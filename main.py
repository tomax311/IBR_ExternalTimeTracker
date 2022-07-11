import Functions
import time
import os


# this saves data during 2 minutes on a given server

ms = time.time_ns() // 1_000_000  # time since epoch(january 1 1970 00h00 on my computer


if Functions.plAmount("http://mc.mythcosmos.de:8123/up/world/bootsrennen2/0") >> 0:
	Functions.datarec("test.txt",30,"http://mc.mythcosmos.de:8123/up/world/bootsrennen2/0")
else:
	print("No players are online there is no point of recording data")
