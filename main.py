import tkinter as tk
import math
import time
import pygame

"""
Class JosephusGUI:
This class defines a GUI for a Josephus Flavius simulation.
The GUI is implemented using the Tkinter module in Python.

    ...
    Constructor
    -------
    __init__(self, master)
    The constructor for the JosephusGUI class. It initializes the GUI with the specified master window.
    The constructor creates a number of widgets and sets their properties using the Tkinter module.
    The widgets include:
    A label to display the title of the simulation.
    * A scale to allow the user to select the number of soldiers.
    * A scale to allow the user to select the jump size.
    * A scale to allow the user to select the number of survivors.
    * A scale to allow the user to select the soldier to start with.
    * A scale to allow the user to select the speed of the simulation.
    * A check button to allow the user to choose whether to include a clock in the simulation.
    * A "Start" button to begin the simulation.
    * A "Clear" button to reset the scales and clear the canvas.
    * A canvas to display the simulation.
    ...
    Methods
    -------
    clear(self)
        This method clears the check button in the GUI.

    restart(self)
        This method resets all scales in the GUI to their initial values and clears the canvas.

    updateLimitByUserInput(self, event):
        Updates the limit for the scale widgets based on the user's input.

    yp(self,n, m, k,s):
       Performs the Josephus problem algorithm with the given parameters.

    yp1(self,n, m, k,s):
       Performs the Josephus problem algorithm with the given parameters, but the list of elements in the circle is reversed.

    update(self,s):
        Updates the canvas by changing the image of the soldier at the given index.

    start(self):
        Initializes the canvas with soldiers and starts the Josephus problem algorithm.
    ...
    Functionality
    -------
    This GUI allows the user to input various parameters for a Josephus Flavius simulation,
    including the number of soldiers, the jump size, the number of survivors,
    the soldier to start with, and the speed of the simulation.
    The user can also choose whether to include a clock in the simulation.
    Once the user has input the desired parameters, they can click the "Start" button to begin the simulation.
    The simulation is displayed on a canvas in the GUI.
    The "Clear" button can be used to reset the scales and clear the canvas.
"""


class JosephusGUI:
    def __init__(self, master):
        self.master = master

        self.radio_var = tk.IntVar()
        self.logo = tk.PhotoImage(file="logo.png")

        right_frame = tk.Frame(root, width=200, height=600)
        right_frame.grid(row=0, column=2, padx=10, pady=10)

        self.master = right_frame
        master.title("Josephus Flavius Simulation")
        master.configure(bg='black')
        self.l=tk.Label(right_frame, text="Josephus Flavius")
        self.l.config(font=("Courier", 20))
        self.l.grid(row=0, column=0)
        self.label1 = tk.Label(right_frame, text="Number of Soldiers:")
        self.label1.grid(row=2, column=0)
        self.label = tk.Label(right_frame, image=self.logo)
        self.label.grid(row=1, column=0)

        self.soldier_count = tk.Scale(right_frame, from_=1, to=60, tickinterval=9, orient='horizontal', length=250)
        self.soldier_count.grid(row=3, column=0)
        self.soldier_count.bind("<ButtonRelease-1>", self.updateLimitByUserInput)



        self.label2 = tk.Label(right_frame, text="Jump Size:")
        self.label2.grid(row=4, column=0)

        self.jump_size = tk.Scale(right_frame, from_=1, to=60, tickinterval=10,
                                  orient='horizontal', length=250)
        self.jump_size.grid(row=5, column=0)



        self.label3 = tk.Label(right_frame, text="Number of survivers:")
        self.label3.grid(row=6, column=0)

        self.number_survivors = tk.Scale(right_frame, from_=1, to=60, tickinterval=10,
                                         orient='horizontal', length=250)
        self.number_survivors.grid(row=7, column=0)


        self.label4 = tk.Label(right_frame, text="Soldier to start with:")
        self.label4.grid(row=8, column=0)

        self.start_soldier = tk.Scale(right_frame, from_=1, to=60, tickinterval=10,
                                         orient='horizontal', length=250)
        self.start_soldier.grid(row=9, column=0)

        self.label5 = tk.Label(right_frame, text="Speed:")
        self.label5.grid(row=10, column=0)

        self.speed = tk.Scale(right_frame, from_=1, to=3, tickinterval=1,
                               orient='horizontal', length=250)
        self.speed.grid(row=11, column=0)



        self.r1 = tk.Checkbutton(right_frame, text='counter clockwise', variable=self.radio_var)
        self.r1.grid(row=12, column=0)
        self.r1.pack

        self.start_button = tk.Button(right_frame, text="Start", command=self.start)
        self.start_button.grid(row=13, column=0, columnspan=2)

        self.reStart_button = tk.Button(right_frame, command=lambda:[self.clear(), self.restart()], text="clear")#, command=self.reStart
        self.reStart_button.grid(row=14, column=0, columnspan=2)

        left_frame = tk.Frame(root, width=800, height=800, bg="black")
        left_frame.grid(row=0, column=1, padx=50, pady=50)
        self.canvas = tk.Canvas(left_frame, width=800, height=750)

        self.canvas.configure(bg='black')
        self.canvas.grid(row=0, column=0)

    def clear(self):
        self.radio_var.set(0)

    def restart(self):
        self.number_survivors.set("0")
        self.jump_size.set("0")
        self.soldier_count.set("0")
        self.canvas.delete("all")
        self.clear()
        self.start_soldier.set("0")
        self.speed.set("0")

    def updateLimitByUserInput(self, event):
        """
                Updates the limit for the scale widgets based on the user's input.

                Args:
                - event: the event that triggers the function.

                Returns:
                None
                """
        self.jump_size = tk.Scale(self.master, from_=1, to=self.soldier_count.get(), tickinterval=10,
                                  orient='horizontal', length=250)
        self.jump_size.grid(row=5, column=0)

        self.number_survivors = tk.Scale(self.master, from_=1, to=self.soldier_count.get(), tickinterval=10,
                                         orient='horizontal', length=250)
        self.number_survivors.grid(row=7, column=0)

        self.start_soldier = tk.Scale(self.master, from_=1, to=self.soldier_count.get(), tickinterval=10,
                                      orient='horizontal', length=250)
        self.start_soldier.grid(row=9, column=0)

    def yp(self,n, m, k,s):
        """
                   Performs the Josephus problem algorithm with the given parameters.

                   Args:
                   - n: an integer representing the number of elements in the circle.
                   - m: an integer representing the step size for reducing elements in the circle.
                   - k: an integer representing the number of elements that should remain in the circle.
                   - s: an integer representing the starting index for counting elements in the circle.

                   Returns:
                   None
                   """
        # 0<n     n elements in the circle
        # 1<=m<=n    reduce the m element after the current existing element
        # 1<=k<=n k elements remain in the circle at the end of process

        self.l = [i for i in range(1, n + 1)]
        i = s-1
        while (len(self.l) > k and len(self.l)>k):
            i = (i + m) % len(self.l)
            self.master.update()
            if self.speed.get() == 1:
                time.sleep(2)
            elif self.speed.get() == 2:
                time.sleep(1)
            else:
                time.sleep(0.5)
            self.update(self.l[i]-1)
            self.l.remove(self.l[i])


    def yp1(self,n, m, k,s):
        """
                  Performs the Josephus problem algorithm with the given parameters, but the list of elements in the circle is reversed.

                  Args:
                  - n: an integer representing the number of elements in the circle.
                  - m: an integer representing the step size for reducing elements in the circle.
                  - k: an integer representing the number of elements that should remain in the circle.
                  - s: an integer representing the starting index for counting elements in the circle.

                  Returns:
                  None
                  """
        # 0<n     n elements in the circle
        # 1<=m<=n    reduce the m element after the current existing element
        # 1<=k<=n k elements remain in the circle at the end of process
        self.l = [i for i in range(1, n + 1)]
        i = s-1
        while (len(self.l) > k and len(self.l) > k):
            i = (i - m) % len(self.l)
            self.master.update()
            if self.speed.get() == 1:
                time.sleep(2)
            elif self.speed.get() == 2:
                time.sleep(1)
            else:
                time.sleep(0.5)
            self.update(self.l[i] - 1)
            self.l.remove(self.l[i])
            i=i-1


    def update(self,s):
        """
              Updates the canvas by changing the image of the soldier at the given index.

              Args:
              - s: an integer representing the index of the soldier to be updated.

              Returns:
              None
              """
        soldier_id = self.soldier_ids[s][1]
        pygame.mixer.music.play(-1)
        self.canvas.itemconfig(soldier_id, image=self.image1)


    def start(self):
        """
                Initializes the canvas with soldiers and starts the Josephus problem algorithm.

                Args:
                None

                Returns:
                None
                """
        self.canvas.delete('all')
        self.n = int(self.soldier_count.get())
        self.k = int(self.jump_size.get())
        self.m=int(self.number_survivors.get())
        self.start=int(self.start_soldier.get())

        x0, y0,r= 420, 370,330
        angle = 2 * math.pi / self.n

        image = tk.PhotoImage(file="aa.png")

        self.soldier_ids = []


        def draw_soldier(i):
            """
                         Draws a soldier on the canvas with the given index `i`.

                         Args:
                         i : int
                         The index of the soldier to draw.

                         Returns:
                         None

                         Functuality:
                         This function draws a soldier on the canvas using the given parameters.
                         It first disables the restart button to prevent the user from interacting with it during the drawing process.
                         It then calculates the x and y coordinates of the soldier using the provided formulas based on the index `i`,
                         the center of the circle `x0` and `y0`, and the radius `r`.
                         It creates an image of the soldier using the provided image,
                         and then creates a text label near the soldier indicating its index.
                         The function adds the soldier id to a list of soldier ids and updates the canvas.
                         Finally, it waits for 0.2 seconds and calls itself with the next index `i+1` until all soldiers
                         have been drawn or until the drawing process is interrupted.

                     """
            self.reStart_button.config(state=tk.DISABLED)
            self.start_button.config(state=tk.DISABLED)

            if i >= self.n:
                return
            x = x0 + r * math.sin(i * angle)
            y = y0 - r * math.cos(i * angle)
            soldier_id = self.canvas.create_image(x, y, image=image)
            self.canvas.create_text(x+3, y, text=str(i + 1),fill="white", font=("Arial", 10))
            self.soldier_ids.append((i + 1, soldier_id))
            self.master.update()
            time.sleep(0.2)
            draw_soldier(i+1)
        draw_soldier(0)

        self.master.update()
        pygame.init()
        pygame.mixer.music.load('music.mp3')

        self.image1 = tk.PhotoImage(file="r.png")

        # Kill the soldiers one by one
        if (self.radio_var.get() == 1):
            self.yp1(self.n, self.k, self.m, self.start)
        else:
            self.yp(self.n,self.k,self.m,self.start)


        pygame.quit()

        # Show the winner
        self.canvas.create_text(x0, y0, text="Winner: " + str(sorted(self.l)), font=("Arial", 24), fill='white',width=r)
        self.reStart_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)


root = tk.Tk()

# create an instance of JosephusGUI and start the simulation
josephus_gui = JosephusGUI(root)
root.mainloop()
