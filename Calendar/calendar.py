class Calendar:
    def __init__(self):
        self.weeks = [[None] * 5 for _ in range(4)]

class Day:
    def __init__(self, date):
        self.date = date
        self.event_labels = []
        self.event_times = []

    def add_event(self, event_label, event_time):
        self.event_labels.append(event_label)
        self.event_times.append(event_time)
