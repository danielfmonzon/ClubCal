class Event:
    def __init__(self, name, start_time, duration):
        self.name = name
        self.start_time = start_time
        self.duration = duration

class Day:
    def __init__(self, day_of_week, date):
        self.day_of_week = day_of_week
        self.date = date
        self.events = []

    def add_event(self, event):
        self.events.append(event)


class Calendar:
    def __init__(self):
        self.weeks = [[], [], [], [], []]
        for i in range(4):
            for j in range(5):
                self.weeks[i].append(Day(j, "day"))



'''class Calendar_old:
    def __init__(self):
        self.weeks = [[None] * 5 for _ in range(4)]

class Day_old:
    def __init__(self, date):
        self.date = date
        self.event_labels = []
        self.event_times = []

    def add_event(self, event_label, event_time):
        self.event_labels.append(event_label)
        self.event_times.append(event_time)

    def edit_event(self, old_label, old_time, new_label, new_time):
        print("editing event")
'''
