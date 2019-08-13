

import sys
import os
import pygame
from tinytag import TinyTag
from tkinter.filedialog import askdirectory
from  tkinter import messagebox
import time
import tkinter as Tk
from tkinter import *

global index
index = 0

listofsongs=[]
realname=[]

def dirch():
    directory = askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):
        if files.endswith("mp3"):
            global  realdir
            realdir=os.path.realpath(files)
            tag = TinyTag.get(realdir)
            realname.append(tag.title)
            listofsongs.append(files)
    throwlist()
    

    
pygame.mixer.init() 
pygame.init()  

def nextSong():
    global index
    if len(listofsongs)==0:
        messagebox.showinfo("Warning","No songs has been added")
    else:
        if index==len(listofsongs)-1:
            index=0
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.play()
            currentS()
            
      
        else:   
            index+=1
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.play()
            currentS()
            
               

def prevSong():
    global index
    if len(listofsongs)==0:
        messagebox.showinfo("Warning","No songs has been added")
    else:
        if index==0:
            index=len(listofsongs)-1
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.play()
            currentS()
            
    

        else:
            index-=1
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.play()
            currentS()
            
        
    

def playFs():
    if len(listofsongs)==0:
        messagebox.showinfo("Warning","No song listed, try again!")
    else:
        pygame.mixer.music.load(listofsongs[0])
        pygame.mixer.music.play()
        currentS()
        

    


def pauseS():
    if len(listofsongs)==0:
        messagebox.showinfo("Warning","No songs has been added")
    else:  
        pygame.mixer.music.pause()
        stopProgress()

def resumeS():
    if len(listofsongs)==0:
        messagebox.showinfo("Warning","No songs has been added")
    else:
        pygame.mixer.music.unpause()


def ext():
    exit()
    

def throwlist():
	realname.reverse()
	for x in range(0,len(listofsongs)):
		Listbox1.insert(0,realname[x])
    	



        
def currentS():
	showlist=[]
	for x in range(len(listofsongs)-1,-1,-1):
		showlist.append(realname[x])
	Listbox1.insert(END,"Current Song : "+showlist[index])


    	
        
        


def stopProgress():
    TProgressbar1.pause()
 

   
def sin():
	i=1.0
	x = pygame.mixer.music.get_volume()
	if x<i:
		if x<=1.0:
			x+=0.1
			pygame.mixer.music.set_volume(x)

def sde():
	i=0.0
	x=pygame.mixer.music.get_volume()
	if x>i:
		if x>=0:
			x-=0.1
			pygame.mixer.music.set_volume(x)
					

def hlp():
	messagebox.showinfo("Help","For any Queries related to code implementation visit: https://github.com/insynchronous")

def abt():
	messagebox.showinfo("About La Musique","La Musique is a simple python based desktop application devloped using some frameworks: \n 1.tkinter \n 2.pygame \n 3.TinyTag \n4.Pyinstaller (For packaging) ")

def dev():
	messagebox.showinfo("About Developer: Ankit","Visit my repo at: https://github.com/insynchronous ")

def reload():
	pygame.mixer.music.rewind()

def Stop():
	pygame.mixer.music.stop()

      					



      			

      			

			
			
			
			
	        
	       

	







	
	




	





try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import LM_support

def vp_start_gui():

    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    global v
    v = StringVar()
    top = Toplevel1 (root)
    LM_support.init(root, top)
    root.mainloop()
    
    return v


w = None

def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    LM_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:




    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font11 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
            "italic -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x393+478+91")
        top.title("La Musique")
        top.configure(background="#8299d8")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")


        self.menubar = tk.Menu(top,font=font9,bg='#99a4d8',fg=_fgcolor)
        top.configure(menu = self.menubar)


        self.sub_menu = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="File")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Browse",
                command=dirch)
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Help",
                command=hlp)
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Exit",
                command = ext )
        self.sub_menu1 = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Actions")
        self.sub_menu1.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Play",
                command= playFs)
        self.sub_menu1.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Pause",
                command = pauseS)
        self.sub_menu1.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Next",
                command = nextSong)
        self.sub_menu1.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Previous",
                command = prevSong)
        self.sub_menu12 = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu12,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="About")
        self.sub_menu12.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="La Musique",
                command=abt)
        self.sub_menu12.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Developer",
                command=dev)

        global Listbox1

        Listbox1 = tk.Listbox(top)
        Listbox1.place(relx=0.017, rely=0.025, relheight=0.936
                  , relwidth=0.657)
        Listbox1.configure(background="#dbeaff")
        Listbox1.configure(disabledforeground="#a3a3a3")
        Listbox1.configure(font="TkFixedFont")
        Listbox1.configure(foreground="#000000")
        Listbox1.configure(highlightbackground="#d9d9d9")
        Listbox1.configure(highlightcolor="black")
        Listbox1.configure(selectbackground="#c4c4c4")
        Listbox1.configure(selectforeground="black")
        Listbox1.configure(width=384)
        




        self.Play = tk.Button(top)
        self.Play.place(relx=0.7, rely=0.025, height=83, width=86)
        self.Play.configure(activebackground="#ececec")
        self.Play.configure(activeforeground="#000000")
        self.Play.configure(background="#2b4ed8")
        self.Play.configure(disabledforeground="#a3a3a3")
        self.Play.configure(font=font11)
        self.Play.configure(foreground="#000000")
        self.Play.configure(highlightbackground="#d9d9d9")
        self.Play.configure(highlightcolor="black")
        self.Play.configure(pady="0")
        self.Play.configure(text='''Play''')
        self.Play.configure(command=playFs)

        self.Pause = tk.Button(top)
        self.Pause.place(relx=0.85, rely=0.025, height=83, width=76)
        self.Pause.configure(activebackground="#ececec")
        self.Pause.configure(activeforeground="#000000")
        self.Pause.configure(background="#2b4ed8")
        self.Pause.configure(disabledforeground="#a3a3a3")
        self.Pause.configure(font=font11)
        self.Pause.configure(foreground="#000000")
        self.Pause.configure(highlightbackground="#d9d9d9")
        self.Pause.configure(highlightcolor="black")
        self.Pause.configure(pady="0")
        self.Pause.configure(text='''Pause''')
        self.Pause.configure(command=pauseS)

        self.Prev = tk.Button(top)
        self.Prev.place(relx=0.7, rely=0.254, height=83, width=86)
        self.Prev.configure(activebackground="#ececec")
        self.Prev.configure(activeforeground="#000000")
        self.Prev.configure(background="#2b4ed8")
        self.Prev.configure(disabledforeground="#a3a3a3")
        self.Prev.configure(font=font11)
        self.Prev.configure(foreground="#000000")
        self.Prev.configure(highlightbackground="#d9d9d9")
        self.Prev.configure(highlightcolor="black")
        self.Prev.configure(pady="0")
        self.Prev.configure(text='''Previous''')
        self.Prev.configure(command=prevSong)

        self.Nxt = tk.Button(top)
        self.Nxt.place(relx=0.85, rely=0.254, height=83, width=76)
        self.Nxt.configure(activebackground="#ececec")
        self.Nxt.configure(activeforeground="#000000")
        self.Nxt.configure(background="#2b4ed8")
        self.Nxt.configure(disabledforeground="#a3a3a3")
        self.Nxt.configure(font=font11)
        self.Nxt.configure(foreground="#000000")
        self.Nxt.configure(highlightbackground="#d9d9d9")
        self.Nxt.configure(highlightcolor="black")
        self.Nxt.configure(pady="0")
        self.Nxt.configure(text='''Next''')
        self.Nxt.configure(command=nextSong)

        self.Open = tk.Button(top)
        self.Open.place(relx=0.7, rely=0.483, height=43, width=166)
        self.Open.configure(activebackground="#ececec")
        self.Open.configure(activeforeground="#000000")
        self.Open.configure(background="#2b4ed8")
        self.Open.configure(disabledforeground="#a3a3a3")
        self.Open.configure(font=font11)
        self.Open.configure(foreground="#000000")
        self.Open.configure(highlightbackground="#d9d9d9")
        self.Open.configure(highlightcolor="black")
        self.Open.configure(pady="0")
        self.Open.configure(text='''Open''')
        self.Open.configure(command= dirch)





        self.Close = tk.Button(top)
        self.Close.place(relx=0.7, rely=0.611, height=43, width=166)
        self.Close.configure(activebackground="#ececec")
        self.Close.configure(activeforeground="#000000")
        self.Close.configure(background="#2b4ed8")
        self.Close.configure(disabledforeground="#a3a3a3")
        self.Close.configure(font=font11)
        self.Close.configure(foreground="#000000")
        self.Close.configure(highlightbackground="#d9d9d9")
        self.Close.configure(highlightcolor="black")
        self.Close.configure(pady="0")
        self.Close.configure(text='''Resume''')
        self.Close.configure(command=resumeS)




        self.Speed1 = tk.Button(top)
        self.Speed1.place(relx=0.7, rely=0.738, height=43, width=80)
        self.Speed1.configure(activebackground="#ececec")
        self.Speed1.configure(activeforeground="#000000")
        self.Speed1.configure(background="#2b4ed8")
        self.Speed1.configure(disabledforeground="#a3a3a3")
        self.Speed1.configure(font=font11)
        self.Speed1.configure(foreground="#000000")
        self.Speed1.configure(highlightbackground="#d9d9d9")
        self.Speed1.configure(highlightcolor="black")
        self.Speed1.configure(pady="0")
        self.Speed1.configure(text='''Vol -''')
        self.Speed1.configure(width=76)
        self.Speed1.configure(command=sde)
 
        self.Speed2 = tk.Button(top)
        self.Speed2.place(relx=0.842, rely=0.738, height=43, width=80)
        self.Speed2.configure(activebackground="#ececec")
        self.Speed2.configure(activeforeground="#000000")
        self.Speed2.configure(background="#2b4ed8")
        self.Speed2.configure(disabledforeground="#a3a3a3")
        self.Speed2.configure(font=font11)
        self.Speed2.configure(foreground="#000000")
        self.Speed2.configure(highlightbackground="#d9d9d9")
        self.Speed2.configure(highlightcolor="black")
        self.Speed2.configure(pady="0")
        self.Speed2.configure(text='''Vol +''')
        self.Speed2.configure(width=76)
        self.Speed2.configure(command=sin)


        self.Random = tk.Button(top)
        self.Random.place(relx=0.7, rely=0.865, height=38, width=80)
        self.Random.configure(activebackground="#ececec")
        self.Random.configure(activeforeground="#000000")
        self.Random.configure(background="#2b4ed8")
        self.Random.configure(disabledforeground="#a3a3a3")
        self.Random.configure(font=font11)
        self.Random.configure(foreground="#000000")
        self.Random.configure(highlightbackground="#d9d9d9")
        self.Random.configure(highlightcolor="black")
        self.Random.configure(pady="0")
        self.Random.configure(text='''Reload''')
        self.Random.configure(width=76)
        self.Random.configure(command=reload)



        self.Queue = tk.Button(top)
        self.Queue.place(relx=0.842, rely=0.865, height=38, width=80)
        self.Queue.configure(activebackground="#ececec")
        self.Queue.configure(activeforeground="#000000")
        self.Queue.configure(background="#2b4ed8")
        self.Queue.configure(disabledforeground="#a3a3a3")
        self.Queue.configure(font=font11)
        self.Queue.configure(foreground="#000000")
        self.Queue.configure(highlightbackground="#d9d9d9")
        self.Queue.configure(highlightcolor="black")
        self.Queue.configure(pady="0")
        self.Queue.configure(text='''Stop''')
        self.Queue.configure(width=76)
        self.Queue.configure(command=Stop)
        





































       






if __name__ == '__main__':
    vp_start_gui()





