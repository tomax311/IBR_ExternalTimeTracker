from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle
import time
import os
import json
import requests

# variables
urlsVar = None
urlName = None
url = None

FileName = None

Time = None


def addUrl():
	global urlName, url
	linkname = str(urlName.get())
	link = str(url.get())
	with open('urls.json', "r") as f:
		links = json.load(f)
		links.update({linkname: link})
		links = json.dumps(links,indent=1)
	file = open("urls.json", "w")
	file.write(links)
	file.close()

def milliseconds():
	nano = time.monotonic_ns()
	nanolist = list(str(nano))
	millisecond = []
	millistr = ""
	for i in range(0,3):
		millisecond.append(nanolist[-9+i])
	return int(millistr.join(millisecond))

def PlayerPos(url):
	r = requests.get(url).json()
	plAmount = r["currentcount"]

	AllPos = []
	for i in range(plAmount):
		playerPos = [r["players"][i - 1]["name"], r["players"][i - 1]["x"], r["players"][i - 1]["z"]]
		AllPos.append(playerPos)
	return AllPos


def datarec():
	global Time, FileName, urlsVar

	link = str(flink(urlsVar.get()))
	ti = int(Time.get())
	filename = str(FileName.get())
	filepath = "outpout\\" + filename +".json"
	finishtime = time.monotonic_ns() + ti * 1000000000
	currenttime = time.monotonic_ns()

	# code to delete the race data file automatically
	if os.path.exists(filepath):
		true = True
		nbr = 1
		while true:
			if os.path.exists("outpout\\" + filename + f"({nbr})" +".json"):
				nbr = nbr + 1
			else:
				true = False
				currentfilename = filename + f"({nbr})" +".json"
				filepath = "outpout\\" + currentfilename
				print(f"{filename}.json already exists. Creating {currentfilename}...")

		with open(filepath, "w") as creator:
			creator.write("{}")

	else:
		print(f"{filename}.json does not exist. Creating file...")
		with open(filepath, "w") as creator:
			creator.write("{}")

	# gets data during recording
	i = 1
	print("started recording data")
	while currenttime <= finishtime:
		ppos1 = PlayerPos(link)

		with open(filepath, "r") as infile:
			storeddata = json.load(infile)
			storeddata.update({f"pos{i}": {"time": time.asctime(time.gmtime()), "milliseconds": milliseconds(), "players": ppos1}})
			data = json.dumps(storeddata, indent=1)
		with open(filepath, "w") as outfile:
			outfile.write(data)
		i = i + 1
		currenttime = time.monotonic_ns()



	print("recording finished")


def flink(name):
	with open('urls.json') as f:
		links = json.load(f)
		linkname = str(name)
		flink = links[linkname]
	return flink


root = Tk()
root.title("IBR_DataRecorder")
style = ThemedStyle(root)
style.set_theme('equilux')
root.iconphoto(False, PhotoImage(file='images/IBR_DataRecorder-logo.png'))

# variables
urlsVar = StringVar()
urlName = StringVar()
url = StringVar()

FileName = StringVar()

Time = StringVar()

# graphical user interface
color = "#464646"
fcolor = "#a6a6a6"
filler = Label(root, background=color)
filler0 = Label(root, background=color)
filler1 = Label(root, background=color)
filler2 = Label(root, background=color)
filler3 = Label(root, background=color)
filler4 = Label(root, background=color)
filler5 = Label(root, background=color)
filler6 = Label(root, background=color)
filler7 = Label(root, background=color)
filler8 = Label(root, background=color)
filler9 = Label(root, background=color)

urlStartTxt = Label(root, background=color, text="URL:", fg=fcolor)

urls = ttk.Combobox(root, textvariable=urlsVar, background=color)
urls.state(["readonly"])
with open('urls.json') as f:
	links = json.load(f)
linknames = list(links)
for i in range(len(linknames)):
	if linknames[i] not in urls['values']:
		urls['values'] = (*urls['values'], linknames[i])
urls.current(0)

urlNameTxt = Label(root, background=color, text="          URL Name:", fg=fcolor)
urlNameInput = ttk.Entry(root, textvariable=urlName, background=color)
urlTxt = Label(root, background=color, text="      Link:", fg=fcolor)
urlInput = ttk.Entry(root, textvariable=url, background=color)
urlAdd = Button(root, text="Add", command=addUrl, background=color, fg=fcolor)

FileNameTxt = Label(root, background=color, text="FileName:", fg=fcolor)
FileNameInput = ttk.Entry(root, textvariable=FileName, background=color)
FileName.set("Test")
Json = Label(root, background=color, text=".json", fg=fcolor)

TimeTxt = Label(root, background=color, text="Time(in sec):", fg=fcolor)
TimeInput = ttk.Spinbox(root, from_=1.0, to=604800, textvariable=Time, background=color)
Time.set(str(1))

StartButton = Button(root, text="Start Recording", foreground="green", command=datarec, background=color)
StopButton = Button(root, text="Stop Recording", foreground="red", command=root.destroy, background=color)

# add to display
filler0.grid(row=0, columnspan=9, sticky="news")

urlStartTxt.grid(row=1, column=0, sticky="news")
urls.grid(row=1, column=1, sticky="news")
filler9.grid(row=1, column=2, sticky="news")
urlNameTxt.grid(row=1, column=3, sticky="news")
urlNameInput.grid(row=1, column=4, sticky="news")
urlTxt.grid(row=1, column=5, sticky="news")
urlInput.grid(row=1, column=6, sticky="news")
urlAdd.grid(row=1, column=7, sticky="news")
filler.grid(row=1, column=8, sticky="news")

filler1.grid(row=2, columnspan=9, sticky="news")

FileNameTxt.grid(row=3, column=0, sticky="news")
FileNameInput.grid(row=3, column=1, sticky="news")
Json.grid(row=3, column=2, sticky="nws")
filler2.grid(row=3, column=3, columnspan=6, sticky="news")

filler3.grid(row=4, columnspan=9, sticky="news")

TimeTxt.grid(row=5, column=0, sticky="news")
TimeInput.grid(row=5, column=1, sticky="news")
filler4.grid(row=5, column=2, columnspan=7, sticky="news")

filler5.grid(row=6, columnspan=9, sticky="news")

filler6.grid(row=7, columnspan=3, sticky="news")
StartButton.grid(row=7, column=3, sticky="news")
StopButton.grid(row=7, column=4, sticky="news")
filler7.grid(row=7, column=5, columnspan=4, sticky="news")

filler8.grid(row=8, columnspan=9, sticky="news")

root.columnconfigure(8, weight=1)
root.rowconfigure(8,weight=1)

root.mainloop()
