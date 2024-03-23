import tkinter as tk
import calendar_class
import calendar
from calendar import monthrange, weekday
from math import ceil

class CalendarApp:
    def __init__(self, root, year = 2024, month = 3):
        self.root = root
        self.root.title("Calendar Events")
        self.data = {}
        self.year = year
        self.month = month   

        # Create the main frame with padding and pack it to expand and fill in both directions
        self.main_frame = tk.Frame(root, padx = 10, pady = 0, bg = "blue")
        self.main_frame.pack(fill = tk.BOTH, expand = True)
        
        # Create a separate frame for the month/year and title labels
        title_frame = tk.Frame(self.main_frame, pady = 10, bg = "orange")
        title_frame.pack(fill = tk.X)
        
        # Display the current month and year in the top left corner
        month_year_label = tk.Label(title_frame, text = f"{calendar.month_name[self.month]} {self.year}", font = ('Times New Roman', 12), bg = "orange")
        month_year_label.pack(side=tk.LEFT, anchor = 'nw')
        
        # Make title label bigger and centered at the very top of the main_frame
        self.title_label = tk.Label(title_frame, text = "CourseCal", font = ('Times New Roman', 20), bg = "orange")
        # Pack the label at the top of the window
        self.title_label.pack(side = tk.TOP, fill = tk.X)
        
        self.draw_calendar()
        
    def draw_calendar(self):
        days_frame = tk.Frame(self.main_frame)
        days_frame.pack(fill = tk.X, expand = True)
        days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        for day in days_of_the_week:
            day_label = tk.Label(days_frame, text = day, font = ('Times New Roman', 12), bg = "blue")
            day_label.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

        first_weekday, num_days = monthrange(self.year, self.month)
        first_weekday = (first_weekday + 1) % 7
        total_slots = first_weekday + num_days
        num_weeks = ceil(total_slots / 7)
        day_number = 1 - first_weekday

        for week in range(num_weeks):
            week_frame = tk.Frame(self.main_frame)
            week_frame.pack(fill = tk.X, expand = True)
        
            for _ in range(7):  # 7 days per week
                if day_number < 1 or day_number > num_days:
                    day_button = tk.Button(week_frame, text = "", state = "disabled", width = 20, height = 2, font = ('Times New Roman', 10), bg = "white")  # Adjust width and height as needed
                else:
                    event_text = ""
                    fg_color = "black"  # Default text color
                    if day_number in self.data:  # Check if there's any event for this day
                        event_text = "\n" + "Event!"  # Placeholder text, replace with actual event data
                        fg_color = "red"  # Change text color to red for events
                    day_button = tk.Button(week_frame, text = f"{day_number}{event_text}", fg = fg_color, width = 20, height = 2, font = ('Times New Roman', 10), bg = "white",
                                        command = lambda d = day_number: self.day_selected(d))
                day_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
                day_number += 1
                        
    def day_selected(self, day):
        # Create a pop-up window for the selected day
        popup = tk.Toplevel(self.root, bg = "white")
        popup.geometry("600x400")
        popup.title("Events")
        if self.data.get(day) is not None: 
            message_label = tk.Label(popup, text = f"Day {day}\n"+self.data[day].name+"\n" + self.data[day].location + "\n"+self.data[day].start_time 
                                     + "\n"+self.data[day].dur, font = ('Times New Roman', 14), bg = "white")
        else:
            message_label = tk.Label(popup, text = f"Day {day}\nMore soon", font = ('Times New Roman', 14), bg = "white")
        message_label.pack(pady = 20, padx = 20)
        
def main():
    root = tk.Tk()
    app = CalendarApp(root)
    root.geometry("1200x600")  # You can adjust the size as needed
    root.mainloop()

if __name__ == "__main__":
    main()


