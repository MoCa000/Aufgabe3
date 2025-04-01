class Subject():

    def __init__(self, first_name, last_name, sex, age_years):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age_years = age_years
        self.max_hr_bpm = None

    def estimate_max_hr(self, age_years : int , sex : str) -> int:
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age_years
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 * age_years
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        self.max_hr_bpm = int(max_hr_bpm)


class Supervisor():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Experiment():
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def add_subject(self, subject):
        self.subject = subject

    def add_supervisor(self, supervisor):
        self.supervisor = supervisor

    def __str__(self):
        return f"Experiment: {self.name}, Date: {self.date}, Supervisor: {self.supervisor.first_name} {self.supervisor.last_name}, Subject: {self.subject.first_name} {self.subject.last_name}, Max HR: {self.subject.max_hr_bpm} bpm"
    def __repr__(self):
        return f"Experiment({self.name}, {self.date}, {self.supervisor}, {self.subject})"