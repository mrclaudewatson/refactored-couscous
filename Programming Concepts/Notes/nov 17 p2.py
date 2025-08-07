# intro to GUI (guided user interface)

import tkinter


# ---class definition---
class GUI:
    def __init__(self):
        # part 1 - create a window
        self.mainwindow = tkinter.Tk()

        # use title to create a title
        self.mainwindow.title("ur boobies")
        '''

        # part 2 - display text with labels (with borders)
        # relief styles - sold, flat, raised, sunken, ridge, groove
#        self.label = tkinter.Label(self.mainwindow, text="Insert ur boobies.", borderwidth=15, relief="flat")

        # part 2 - use pack method to position label
        # default it top. other options are left, right and bottom
#        self.label.pack(side='left')

        # part 3 - creates frame with borders and padding
        self.tframe = tkinter.Frame(self.mainwindow, borderwidth=10, relief="solid")
        self.bframe = tkinter.Frame(self.mainwindow, borderwidth=10, relief="solid")

        #labels for each frame
        self.tflabel = tkinter.Label(self.tframe, text="Top Frame Label")
        self.bflabel = tkinter.Label(self.bframe, text="Bottom Frame Label")

        # pack frame labels
        self.tflabel.pack(side="top", ipadx=60, ipady=60)
        self.bflabel.pack(side="top", ipadx=60, ipady=60)

        #pack frames
        self.tframe.pack(side="top", ipadx=60, ipady=60)
        self.bframe.pack(side="top", ipadx=60, ipady=60)

        # part 1 still - enter the tkinter main loop
        tkinter.mainloop()
        '''

        # part 4 - create Button widgets
        self.button1 = tkinter.Button(self.mainwindow, text="Click me!", command=self.bfun)
        self.quit = tkinter.Button(self.mainwindow, text="Quit", command=self.mainwindow.destroy)
        # pack the buttons
        self.button1.pack(side='left')
        self.quit.pack(side='left')

        # part1 - enter the tkinter main loop
        tkinter.mainloop()

        # This function describe what happens when a Button is pressed

    def bfun(self):
        tkinter.messagebox.showinfo('Response', 'Yay! You clicked me!')



# ---driver program---
# create an object
mygui = GUI()