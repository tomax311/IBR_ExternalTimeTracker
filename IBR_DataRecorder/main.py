from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle
import time
import os
import json
import requests


def milliseconds():
	nanolist = list(str(time.monotonic_ns()))
	millisecond = []
	millistr = ""
	def test():
		print("test")
	test()
	for i in range(0,3):
		millisecond.append(nanolist[-9+i])
	return int(millistr.join(millisecond))


def add_url():
	global main

	linkname = str(main.url_name.get())
	link = str(main.url.get())

	with open('urls.json', "r") as readfile:
		links = json.load(readfile)
		links.update({linkname: link})
		links = json.dumps(links, indent=1)

	with open("urls.json", "w") as writefile:
		writefile.write(links)


def flink(name):
	with open('urls.json') as f:
		links = json.load(f)
	return links[str(name)]


def PlayerPos(url):
	data = requests.get(url).json()
	plAmount = data["currentcount"]

	AllPos = []
	for i in range(plAmount):
		playerPos = [data["players"][i - 1]["name"], data["players"][i - 1]["x"], data["players"][i - 1]["z"]]
		AllPos.append(playerPos)
	return AllPos


def datarec():
	global main

	filename = str(main.file_name.get())
	filepath = "output\\" + filename + ".json"
	finishtime = time.perf_counter_ns() + int(main.definetime.get()) * 1000000000

	# code to delete the race data file automatically
	if os.path.exists(filepath):
		nbr = 1
		while os.path.exists("output\\" + filename + f"({nbr})" + ".json"):
			nbr = nbr + 1

		currentfilename = filename + f"({nbr})" + ".json"
		filepath = "output\\" + currentfilename
		print(f"{filename}.json already exists. Creating {currentfilename}...")

		with open(filepath, "w") as creator:
			creator.write("{}")

	else:
		print(f"{filename}.json does not exist. Creating file...")
		with open(filepath, "w") as creator:
			creator.write("{}")

	# gets data during recording
	i = 1
	storeddata = {}
	print("started recording data")
	while time.perf_counter_ns() <= finishtime:
		ppos = PlayerPos(str(flink(main.urls_var.get())))

		storeddata.update(
				{f"pos{i}":{
					"time": time.asctime(time.gmtime()),
					"milliseconds": milliseconds(),
					"players": ppos}})
		data = json.dumps(storeddata, indent=1)

		with open(filepath, "w") as outfile:
			outfile.write(data)
		i = i + 1

	print("recording finished")


def main():
	root = Tk()
	root.title("IBR_DataRecorder")
	style = ThemedStyle(root)
	style.set_theme('equilux')
	root.iconphoto(False, PhotoImage(file='images/IBR_DataRecorder-logo.png'))

	# variables
	main.urls_var = StringVar()
	main.url_name = StringVar()
	main.url = StringVar()

	main.file_name = StringVar()

	main.definetime = StringVar()

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

	urls = ttk.Combobox(root, textvariable=main.urls_var, background=color)
	urls.state(["readonly"])
	with open('urls.json') as f:
		links = json.load(f)
		linknames = list(links)
		for i in range(len(linknames)):
			if linknames[i] not in urls['values']:
				urls['values'] = (*urls['values'], linknames[i])
	urls.current(2)

	urlNameTxt = Label(root, background=color, text="          URL Name:", fg=fcolor)
	urlNameInput = ttk.Entry(root, textvariable=main.url_name, background=color)
	urlTxt = Label(root, background=color, text="      Link:", fg=fcolor)
	urlInput = ttk.Entry(root, textvariable=main.url, background=color)
	urlAdd = Button(root, text="Add", command=add_url, background=color, fg=fcolor)

	FileNameTxt = Label(root, background=color, text="FileName:", fg=fcolor)
	FileNameInput = ttk.Entry(root, textvariable=main.file_name, background=color)
	main.file_name.set("Test")
	Json = Label(root, background=color, text=".json", fg=fcolor)

	TimeTxt = Label(root, background=color, text="Time(in sec):", fg=fcolor)
	TimeInput = ttk.Spinbox(root, from_=1.0, to=604800, textvariable=main.definetime, background=color)
	main.definetime.set(str(1))

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
	root.rowconfigure(8, weight=1)

	root.mainloop()


if __name__ == "__main__":
	main()
