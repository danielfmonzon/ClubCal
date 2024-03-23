import tkinter as tk
import calendar_class
import calendar
from calendar import monthrange, weekday

class CalendarApp:
    def __init__(self, root, year = 2024, month = 4):
        self.root = root
        self.root.title("Calendar Events")
        self.data = {}
        self.year = year
        self.month = month   

        # Create the main frame with padding and pack it to expand and fill in both directions
        self.main_frame = tk.Frame(root, padx = 10, pady = 0)
        self.main_frame.pack(fill = tk.BOTH, expand = True)
        
        # Create a separate frame for the month/year and title labels
        title_frame = tk.Frame(self.main_frame, pady = 10)
        title_frame.pack(fill = tk.X)
        
        # Display the current month and year in the top left corner
        month_year_label = tk.Label(title_frame, text = f"{calendar.month_name[self.month]} {self.year}", font = ('Times New Roman', 12))
        month_year_label.pack(side=tk.LEFT, anchor = 'nw')
        
        # Make title label bigger and centered at the very top of the main_frame
        self.title_label = tk.Label(title_frame, text = "CourseCal", font = ('Times New Roman', 20))
        # Pack the label at the top of the window
        self.title_label.pack(side = tk.TOP, fill = tk.X)
        
        self.draw_calendar()
        
    def draw_calendar(self):
        # Create a frame for the days of the week labels
        days_frame = tk.Frame(self.main_frame)
        days_frame.pack(fill = tk.X, expand = True)
        days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
        # Create and pack labels for the days of the week
        for day in days_of_the_week:
            day_label = tk.Label(days_frame, text = day)
            day_label.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
            
        # Get the first day of the week (0 for Monday, 6 for Sunday)
        first_weekday, num_days = monthrange(self.year, self.month)
        # Adjust start_day based on the first_weekday
        start_day = -first_weekday

        # Calculate the total number of buttons to create
        total_days = num_days + (4 - first_weekday) % 7 + (6 - ((first_weekday + num_days - 1) % 7))
        
        day_number = start_day
        # Create the calendar with weeks and days
        for week in range(6):
            # Create a frame for each week
            week_frame = tk.Frame(self.main_frame)
            week_frame.pack(fill = tk.X, expand = True)

            for _ in range(7): # 7 days per week
                if day_number < 1 or day_number > num_days:
                    day_button = tk.Button(week_frame, text = "", state = "disabled")
                else:
                    day_button = tk.Button(week_frame, text = str(day_number),
                                           command = lambda d = day_number: self.day_selected(d))
                # Pack day buttons side by side within the week frame, ensuring they fill out the row
                day_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
                day_number += 1
                
            
    def day_selected(self, day):
        # Create a pop-up window for the selected day
        popup = tk.Toplevel(self.root)
        popup.geometry("400x200")
        popup.title("Events")
        if self.data.get(day) is not None:
            message_label = tk.Label(popup, text=f"Day {day}\n"+self.data[day].name+"\n"+self.data[day].location+"\n"+self.data[day].start_time+"\n"+self.data[day].dur, font = ('Times New Roman', 14))
        else:
            message_label = tk.Label(popup, text = f"Day {day}\nMore soon", font = ('Times New Roman', 14))
        message_label.pack(pady = 20, padx = 20)
        
def main():
    root = tk.Tk()
    app = CalendarApp(root)
    root.geometry("600x400")  # You can adjust the size as needed
    root.mainloop()

if __name__ == "__main__":
    main()


