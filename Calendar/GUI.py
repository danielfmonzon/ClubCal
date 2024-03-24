import tkinter as tk
import calendar_class
import calendar
from calendar_class import Event
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from calendar import monthrange, weekday
from math import ceil

# The blue color code for the Florida Gators logo is Pantone: PMS 287 C, Hex Color: #0021A5, RGB: (0, 33, 165), CMYK: (100, 60, 0, 20). 
# The orange color code for the Florida Gators logo is Pantone: PMS 172 C, Hex Color: #FA4616, RGB: (250, 70, 22), CMYK: (0, 70, 100, 0).
# Gentona is the primary workhorse for UF communications.

class CalendarApp:
    def __init__(self, root, data,  year = 2024, month = 3):
        self.root = root
        self.root.title("Calendar Events")
        self.data = data
        self.year = year
        self.month = month

        # Create the main frame with padding and pack it to expand and fill in both directions
        self.main_frame = tk.Frame(root, padx = 10, pady = 0, bg = "#C9D2D5")
        self.main_frame.pack(fill = tk.BOTH, expand = True)
        
        # Create a separate frame for the month/year and title labels
        title_frame = tk.Frame(self.main_frame, pady = 10, bg = "#0021A5")
        title_frame.pack(fill = tk.X)
        
        # Display the current month and year in the top left corner
        month_year_label = tk.Label(title_frame, text = f"{calendar.month_name[self.month]} {self.year}", font = ('Gentona', 14), bg = "#0021A5", fg = "white")
        month_year_label.pack(side=tk.LEFT, anchor = 'nw')
        
        # Make title label bigger and centered at the very top of the main_frame
        self.title_label = tk.Label(title_frame, text = "CourseCal", font = ('Gentona', 20), bg = "#0021A5", fg = "white")
        # Pack the label at the top of the window
        self.title_label.pack(side = tk.TOP, fill = tk.X)
        
        self.draw_calendar()
        
    def draw_calendar(self):
        days_frame = tk.Frame(self.main_frame)
        days_frame.pack(fill = tk.X, expand = True)
        days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        for day in days_of_the_week:
            day_label = tk.Label(days_frame, text = day, font = ('Gentona', 12), bg = "#FA4616")
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
                    day_button = tk.Button(week_frame, text = "", state = "disabled", width = 20, height = 2, font = ('Gentona', 10), bg = "white")  # Adjust width and height as needed
                else:
                    event_text = ""
                    fg_color = "black"  # Default text color
                    if day_number in self.data:  # Check if there's any event for this day
                        event_text = "\n" + "Event!"  # Placeholder text, replace with actual event data
                        fg_color = "#D0342C"  # Change text color to red for events
                    day_button = tk.Button(week_frame, text = f"{day_number}{event_text}", fg = fg_color, width = 20, height = 2, font = ('Gentona', 10), bg = "white",
                                        command = lambda d = day_number: self.day_selected(d))
                day_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
                day_number += 1
                        
    def day_selected(self, day):
        # Create a pop-up window for the selected day
        popup = tk.Toplevel(self.root, bg = "#C9D2D5")
        popup.geometry("600x400")
        popup.title("Events")
        
        # Use a Text widget for complex formatting
        text_widget = tk.Text(popup, font=('Times New Roman', 14), bg = "white", height = 10, width = 50)
        text_widget.tag_configure('center', justify = 'center')
        text_widget.tag_configure('left', justify = 'left')
        text_widget.insert('1.0', f"Day {day}\n", 'center')
        if self.data.get(day) is not None:
            for i in range(len(self.data[day])):
                event_text = f"{self.data[day][i].name}\n{self.data[day][i].description}\n{self.data[day][i].location}\n{self.data[day][i].start_time}\n{self.data[day][i].end_time}"
                text_widget.insert('end', event_text, 'left')
        else:
            text_widget.insert('end', "No Events, Hooray!\n", 'center')

        text_widget.configure(state = 'disabled')  # Make the Text widget read-only
        text_widget.pack(pady = 20, padx = 20, fill = 'x', expand = True)
        
def main():
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("CourseCal_dataset").sheet1

    # data = sheet.get_all_records()
    # testcol = sheet.col_values(3)

    still_receiving = True
    col_i = 3
    event_dict = {}

    while still_receiving:
        cur_col = sheet.col_values(col_i)

        if len(cur_col) == 0:
            still_receiving = False

        elif len(cur_col) != 1:
            event_dict[col_i - 2] = []
            chunk_i = 1

            while len(cur_col) % 5 != 1:
                cur_col.append('')

            while chunk_i < len(cur_col):
                event_dict[col_i - 2].append(Event(cur_col[chunk_i], cur_col[chunk_i + 1], cur_col[chunk_i + 2], cur_col[chunk_i + 3], cur_col[chunk_i + 4]))
                chunk_i += 5
        col_i += 1
    root = tk.Tk()
    app = CalendarApp(root, event_dict)
    root.geometry("1200x600")  # You can adjust the size as needed
    root.mainloop()

if __name__ == "__main__":
    main()


