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
        self.draw_calendar()
        
    def draw_calendar(self):
        # Create a frame for the days of the week labels
        days_frame = tk.Frame(self.main_frame)
        days_frame.pack(fill=tk.X, expand=True)
        days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
        # Create and pack labels for the days of the week
        for day in days_of_the_week:
            day_label = tk.Label(days_frame, text=day)
            day_label.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Create the calendar with weeks and days
        for week in range(4):
            # Create a frame for each week
            week_frame = tk.Frame(self.main_frame)
            week_frame.pack(fill=tk.X, expand=True)

            for day in range(5):
                day_button = tk.Button(week_frame, text=f'{day + 1 + week * 5}',
                                    command=lambda d=day: self.day_selected(d))
                # Pack day buttons side by side within the week frame, ensuring they fill out the row
                day_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def day_selected(self, day):
        # Placeholder for what happens when a day is selected, such as opening a new window to add/view events
        #messagebox.showinfo("Day Selected", f"Day {day + 1} selected.")
        pass
    
def main():
    root = tk.Tk()
    app = CalendarApp(root)
    #app.draw_calendar()
    root.geometry("600x400")  # You can adjust the size as needed
    root.mainloop()

if __name__ == "__main__":
    main()


