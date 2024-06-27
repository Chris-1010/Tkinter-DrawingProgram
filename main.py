import tkinter as tk

class Main:
    def __init__(self):
        self._window = tk.Tk()
        self._window.geometry("900x600")  # set window size
        self._window.title("Assignment 2")
        self._window.config(bg="black")  # set window background colour

        self._colour = tk.StringVar(value="")
        self._shape = tk.StringVar(value="")

        self._drawingOrigin = None

        self.create_widgets()

        self._window.mainloop()   # run window

    def create_widgets(self):
        leftFrame = tk.Frame(self._window, bg="green", width=200, height=580) # create left frame
        leftFrame.grid(row=0, column=0, padx=10, pady=10)    # add left frame to window
        leftFrame.grid_propagate(False)

        rightFrame = tk.Frame(self._window, bg="white", width=690, height=600) # create right frame
        rightFrame.grid(row=0, column=1)    # add right frame to window
        rightFrame.grid_propagate(False)

        colourLabel = tk.Label(leftFrame, text="Colour", font=("Arial", 25), width=10)    # create label object
        colourLabel.grid(row=0, column=0)
        self._colours = ["Red", "Blue", "Yellow"]

        shapeLabel = tk.Label(leftFrame, text="Shape", font=("Arial", 25), width=10)    # create label object
        shapeLabel.grid(row=4, column=0)
        self._shapes = ["Line", "Rectangle", "Oval"]

        for colour in self._colours:
            colourButton = tk.Radiobutton(leftFrame, width=9, height=1, text=colour, font=("Arial", 20), bg=colour, variable=self._colour, value=colour)
            colourButton.grid(row=self._colours.index(colour) + 1, column=0, padx=10, pady=10)
            colourButton.bind("<Button-1>", self.newSelection)
        for shape in self._shapes:
            shapeButton = tk.Radiobutton(leftFrame, width=9, height=1, text=shape, font=("Arial", 20), bg="white", variable=self._shape, value=shape)
            shapeButton.grid(row=self._shapes.index(shape) + 5, column=0, padx=10, pady=10)
            shapeButton.bind("<Button-1>", self.newSelection)

        self._eventsLog = tk.Label(leftFrame, text="Waiting for shape and colour to be selected", font=("Arial", 15), width=18, height=4, wraplength=180, bg="black", fg="white")
        self._eventsLog.grid(row=8, column=0)


        self._canvas = tk.Canvas(rightFrame, width=690, height=600, bg="black")
        self._canvas.grid(row=0, column=1)
        self._canvas.bind("<Button-1>", self.drawShape)

    def newSelection(self, event):
            if event.widget["text"] in self._colours:   # colour chosen
                self._colour = event.widget["text"]
                print(f"{self._colour} Selected")
                if not isinstance(self._shape, str):
                    self._eventsLog["text"] = "Waiting for shape to be selected"
                else:
                    self._eventsLog["text"] = "Colour: " + self._colour + "\nShape: " + self._shape
            elif event.widget["text"] in self._shapes:  # shape chosen
                self._shape = event.widget["text"]
                print(f"{self._shape} Selected")
                if not isinstance(self._colour, str):
                    self._eventsLog["text"] = "Waiting for colour to be selected"
                else:
                    self._eventsLog["text"] = "Colour: " + self._colour + "\nShape: " + self._shape



    def drawShape(self, event):
        if not isinstance(self._colour, str) or not isinstance(self._shape, str):
            print("Tried to draw but colour or shape not selected")
            return
        
        if self._drawingOrigin == None:
            self._drawingOrigin = (event.x, event.y)
            self._eventsLog["text"] = "Start of shape drawn\nWaiting for end of shape to be drawn"
            print(f"Start of {self._shape} drawn")
            return

        if self._shape == "Line":
            self._canvas.create_line(self._drawingOrigin[0], self._drawingOrigin[1], event.x, event.y, fill=self._colour, width=5)
        elif self._shape == "Rectangle":
            self._canvas.create_rectangle(self._drawingOrigin[0], self._drawingOrigin[1], event.x, event.y, fill=self._colour)
        elif self._shape == "Oval":
            self._canvas.create_oval(self._drawingOrigin[0], self._drawingOrigin[1], event.x, event.y, fill=self._colour)
        
        self._eventsLog["text"] = "Colour: " + self._colour + "\nShape: " + self._shape
        print(f"{self._colour} {self._shape} drawn")
        self._drawingOrigin = None





    
game = Main()