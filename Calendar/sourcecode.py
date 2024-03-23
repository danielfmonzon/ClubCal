import tkinter as tk
import calendar

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
        
    def draw_calendar(self):
        # Assuming a simple 4x5 grid for the calendar to keep things straightforward
        for week in range(4):
            for day in range(5):
                day_button = tk.Button(self.main_frame, text = f'{day + 1 + week * 5}', command = lambda d = day: self.day_selected(d))
                day_button.grid(row = week + 1, column = day, sticky = "nsew", padx = 5, pady = 5)
                # Expand the grid cells evenly
                self.main_frame.grid_columnconfigure(day, weight = 1)
            self.main_frame.grid_rowconfigure(week + 1, weight = 1)

    def day_selected(self, day):
        # Placeholder for what happens when a day is selected, such as opening a new window to add/view events
        messagebox.showinfo("Day Selected", f"Day {day + 1} selected.")

def main():
    root = tk.Tk()
    app = CalendarApp(root)
    root.geometry("600x400")  # You can adjust the size as needed
    root.mainloop()

if __name__ == "__main__":
    main()


