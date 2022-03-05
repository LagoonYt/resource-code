from pathlib import Path
from tkinter import *
from tkinter import filedialog
import os
import sys

def resource_path0(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
	
screen = Tk()
def main_screen():
	path = resource_path0("mountain.png")
	screen.geometry("700x500")
	screen.title("ResourceBuilder")
	screen.resizable(False, False)
	c = Canvas(screen, bg="gray16", height=200, width=200)
	c.pack()
	filename = PhotoImage(file=path)
	background_label = Label(screen, image=filename)
	background_label.place(x=0, y=0, relwidth=1, relheight=1)
	canvas = Canvas(width=400, height=330)
	canvas.place(x=150, y=70)
	button = Button(text="How to use!\n1. Click anywhere in this box!\n2.Select the carpacks folder (folder that includes data)!\n3.resource.lua should be created in your carpack ready to use!", width=57, height=23, border=0,command = lambda:[write()])
	button.place(x=150, y=70)
	screen.mainloop()


def write():
	folder_selected = filedialog.askdirectory()
	manifest = "resource_manifest_version '44febabe-d386-4d18-afbe-5e627f4af937'"

	path = Path(folder_selected + "\data")
	strange = Path(folder_selected + "")
	print(path)
	location = str(strange)+r'\__resource.lua'
	


	ab = [f for f in path.iterdir() if f.is_dir()]

	with open('folders.txt', "w") as file:
		for path in ab:
			print(path.name)

			file.writelines(path.name + "\n")

	file = open(location, "a")
	file.write(manifest + 3 * "\n")
	file.write("files {" + 2 * "\n")
	myfile = open("./folders.txt", 'r')
	myline = myfile.readline().strip()
	while myline:
		file.write("'data/"+myline+"/*.meta',\n")
		myline = myfile.readline().strip()

	myfile.close()   

	file.write("\n")     
	file.write("}" + 2 * "\n")						
	file.close

	file = open(location, "a")
	
	with open("./folders.txt", 'r') as fp:
		for count, folder in enumerate(fp):
			for filename, filename2 in (('handling.meta', 'HANDLING_FILE'), ('vehicles.meta', 'VEHICLE_METADATA_FILE'), ('carcols.meta','CARCOLS_FILE'), ('carvariations.meta', 'VEHICLE_VARIATION_FILE'),('vehiclelayouts.meta','VEHICLE_LAYOUTS_FILE')):		
				file.write(f"data_file '{filename2}' 'data/{folder.strip()}/{filename}',\n")	
	file.close

main_screen()
screen.mainloop()

