class Event:
    def __init__(self, name, description, location, start_time, end_time):
        self.name = name
        self.description = description
        self.location = location
        self.start_time = start_time
        self.end_time = end_time

    def event_print(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Location: {self.location}")
        print(f"Start Time: {self.start_time}")
        print(f"End Time: {self.end_time}")

class Day:
    def __init__(self, day_of_week, date):
        self.day_of_week = day_of_week
        self.date = date
        self.events = []

    def add_event(self, e_name, e_description, e_location, e_start_time, e_end_time):
        self.events.append(Event(e_name, e_description, e_location, e_start_time, e_end_time))


class Calendar:
    def __init__(self):

        day_map = {
            0: "Sunday",
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday"
        }

        self.weeks = [[], [], [], [], []]
        for i in range(4):
            for j in range(5):
                self.weeks[i].append(Day(day_map[j], "day"))
