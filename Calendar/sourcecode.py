import tkinter as tk
from tkinter import ttk

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CourseCal")
        
        # Create the main frame
        self.main_frame = ttk.Frame(root, padding = "10") 
        self.main_frame.grid(row = 0, column = 0, sticky = (tk.W, tk.E, tk.N, tk.S))
        
        self.title_label = ttk.Label(self.main_frame, text="CourseCal", font=('Times New Roman', 12))
        self.title_label.grid(row=0, column=0, sticky=tk.W)

        # Create a label
        self.label = ttk.Label(self.main_frame, text="Calendar Events")
        self.label.grid(row=0, column=0, sticky=tk.W)
        
        # TODO: Add more UI components here

def main():
    root = tk.Tk()
    app = CalendarApp(root)
    root.geometry("500x500")
    root.mainloop()

if __name__ == "__main__":
    main()

