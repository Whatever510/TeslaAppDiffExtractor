import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import getDiff

class App:
    global open_filename_new
    global open_filename_old

    def __init__(self, root):
        #setting title
        root.title("Tesla App Change Detector")
        open_filename_new = ""
        open_filename_old = ""

        #setting window size
        width=538
        height=314
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.GButton_start=tk.Button(root)
        self.GButton_start["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_start["font"] = ft
        self.GButton_start["fg"] = "#000000"
        self.GButton_start["justify"] = "center"
        self.GButton_start["text"] = "Start "
        self.GButton_start.place(x=70,y=260,width=130,height=30)
        self.GButton_start["command"] = self.GButton_start_command

        self.GButton_cancel=tk.Button(root)
        self.GButton_cancel["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_cancel["font"] = ft
        self.GButton_cancel["fg"] = "#000000"
        self.GButton_cancel["justify"] = "center"
        self.GButton_cancel["text"] = "Cancel"
        self.GButton_cancel.place(x=310,y=260,width=130,height=30)
        self.GButton_cancel["command"] = self.GButton_cancel_command

        self.GLabel_819=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_819["font"] = ft
        self.GLabel_819["fg"] = "#333333"
        self.GLabel_819["justify"] = "center"
        self.GLabel_819["text"] = "Select the apk file of the old version"
        self.GLabel_819.place(x=90,y=10,width=355,height=30)

        self.GLabel_482=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_482["font"] = ft
        self.GLabel_482["fg"] = "#333333"
        self.GLabel_482["justify"] = "center"
        self.GLabel_482["text"] = "Select the apk file of the new version"
        self.GLabel_482.place(x=90,y=110,width=355,height=30)

        self.GButton_open_old=tk.Button(root)
        self.GButton_open_old["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_open_old["font"] = ft
        self.GButton_open_old["fg"] = "#000000"
        self.GButton_open_old["justify"] = "center"
        self.GButton_open_old["text"] = "Open"
        self.GButton_open_old.place(x=30,y=50,width=70,height=25)
        self.GButton_open_old["command"] = self.GButton_open_old_command

        self.GButton_open_new=tk.Button(root)
        self.GButton_open_new["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_open_new["font"] = ft
        self.GButton_open_new["fg"] = "#000000"
        self.GButton_open_new["justify"] = "center"
        self.GButton_open_new["text"] = "Open"
        self.GButton_open_new.place(x=30,y=180,width=70,height=25)
        self.GButton_open_new["command"] = self.GButton_open_new_command

        self.GLabel_old=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_old["font"] = ft
        self.GLabel_old["fg"] = "#333333"
        self.GLabel_old["justify"] = "center"
        self.GLabel_old["text"] = ""
        self.GLabel_old.place(x=120,y=50,width=370,height=25)

        self.GLabel_new=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_new["font"] = ft
        self.GLabel_new["fg"] = "#333333"
        self.GLabel_new["justify"] = "center"
        self.GLabel_new["text"] = ""
        self.GLabel_new.place(x=120,y=180,width=370,height=25)

    def GButton_start_command(self):
        if (self.GLabel_new["text"] == "" or self.GLabel_old["text"] == ""):
            tk.messagebox.showwarning(title="No Files selected", message="Please select the directory for the old and the new version")
        else:
            getDiff.main(self.GLabel_old["text"], self.GLabel_new["text"])


    def GButton_cancel_command(self):
        quit()

    def GButton_open_old_command(self):
        self.GLabel_old["text"] = self.browseFiles()

    def GButton_open_new_command(self):
        self.GLabel_new["text"] = self.browseFiles()

    def quit(self):
        self.root.destroy()

    def browseFiles(self):
        filename = filedialog.askopenfilename()
        print(filename)
        return filename





if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
