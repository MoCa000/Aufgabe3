if __name__ == "__main__":
    from my_functions import estimate_max_hr, build_person, build_experiment

    estimate_max_hr(age_years = 25, sex = "male")
    build_person("Moritz", "Bestermann", "männlich", 25)
    build_experiment("Experiment Test", "21.03.2025", "Samuel", "SWE")

    print("Hat funktioniert") 