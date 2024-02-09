import tkinter as tk

class DPS_Tracker_GUI:
    def __init__(self, root):
        self.root = root

        self.root.geometry("500x400")
        self.root.title("Numby DPS Tracker")

        self.label = tk.Label(root, text="Total Damage:", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)
        self.dps_label = tk.Label(root, text="DPS: 0")
        self.dps_label.pack()

        self.button = tk.Button(root, text="Reset", font=('Arial', 18), command=self.reset_dps)
        self.button.pack(pady=150, padx=50)

        self.current_dps = 0
        self.update_dps()

    def update_dps(self):
        self.current_dps += 1 ##TESTING ONLY 
        self.dps_label.config(text="DPS: {}".format(self.current_dps))

        #DPS values updated every half-second.
        self.root.after(500, self.update_dps)
    
    def reset_dps(self):
        self.current_dps = 0
        self.dps_label.confit(text="DPS: {}".format(self.current_dps))
        

#------------------#
## INITIALIZE GUI ##
#------------------#
if __name__ == "__main__":
    root = tk.Tk()
    app = DPS_Tracker_GUI(root)
    root.mainloop()