import tkinter
import tkinter.messagebox


# -----class definition------
class GUISec3:
    def __init__(self):
        # part 1 - create window
        self.mainwindow = tkinter.Tk()  # create an instance of the Tk class
        # use title to create a title for your window
        self.mainwindow.title('My window')
        #part2 - display text with labels (with borders)
        #relief styles - solid, flat, raised, sunken, ridge, groove
        self.label = tkinter.Label(self.mainwindow, text = 'Insert Text Here.', 
borderwidth = 5, relief = 'ridge')
        #part2 - use pack method to position label
        #default is top. Other options are left, right and bottom
        self.label.pack()
        #part 3 - create frames with borders and padding
        self.tframe = tkinter.Frame(self.mainwindow, borderwidth = 10, relief = 
'raised')
        self.bframe = tkinter.Frame(self.mainwindow, borderwidth = 8, relief = 
'groove')
        #labels for each frame
        self.tflabel = tkinter.Label(self.tframe, text = 'Top Frame Label', 
borderwidth = 3, relief = 'sunken')
        self.bflabel = tkinter.Label(self.bframe, text = 'Bottom Frame Label', 
borderwidth = 2, relief = 'solid')

        #pack frame labels
        self.tflabel.pack(side = 'top', ipadx = 60, ipady = 60)
        self.bflabel.pack(side = 'top', ipadx = 60, ipady = 60) 
        #pack frame
        self.tframe.pack(side = 'top', ipadx = 75, ipady = 75)
        self.bframe.pack(side = 'top', ipadx = 75, ipady = 75)

        # part 4 - create Button widgets
        self.button1 = tkinter.Button(self.mainwindow, text="Click me!", command
        =self.bfun)
        self.quit = tkinter.Button(self.mainwindow, text="Quit", command=
        self.mainwindow.destroy)
        # pack the buttons
        self.button1.pack(side='left')
        self.quit.pack(side='left')

        # part1 - enter the tkinter main loop
        tkinter.mainloop()

    # This function describe what happens when a Button is pressed
    def bfun(self):
        tkinter.messagebox.showinfo('Response', 'Yay! You clicked me!')

        # -----driver program------
        # create an object
        mygui = GUISec3()