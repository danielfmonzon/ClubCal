import tkinter as tk

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar Events")

        # Create the main frame with padding and pack it to expand and fill in both directions
        self.main_frame = tk.Frame(root, padx = 10, pady = 0)
        self.main_frame.pack(fill = tk.BOTH, expand = True)

        # Make title label bigger and centered at the very top of the main_frame
        self.title_label = tk.Label(self.main_frame, text = "CourseCal", font = ('Times New Roman', 20))
        # Pack the label at the top of the window
        self.title_label.pack(side = tk.TOP)

def main():
    root = tk.Tk()
    app = CalendarApp(root)
    root.geometry("500x500")  # You can adjust the size as needed
    root.mainloop()

if __name__ == "__main__":
    main()


