from my_classes import Subject, Supervisor, Experiment, Person
from datetime import datetime

if __name__ == "__main__":
    # Erstellen eines Leistungstests
    supervisor = Supervisor("FirstName", "LastName")
    subject = Subject("FirstName", "LastName", "female", "2000-01-01")
    subject.estimate_max_hr(subject.age_years, subject.sex)

    experiment = Experiment("Leistungstest", "2021-01-01")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    print()
    print(experiment)
    print()
    print(experiment.__dict__) 
    print(supervisor.__dict__)
    print(subject.__dict__)
    print()
    print(subject.age_years)
    print(subject.max_hr_bpm)
