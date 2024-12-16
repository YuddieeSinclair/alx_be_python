Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
Time_Bound = input("Is it time-bound? (yes/no): ")
Reminder = f"'{Task}' is a {Priority} priority task that requires immediate attention today!"
match Priority:
    case "high":
        if Time_Bound == "yes":
            print(Reminder)
        else:
            Reminder = f"'{Task}' is a {Priority} priority task that requires immediate attention today!"
    case "medium":
        if Time_Bound == "yes":
            print(Reminder)
        else:
            print(f"'{Task}' is a mid-level priority task, Consider completing it when you have free time")
    case "low":
        if Time_Bound == "yes":
            print(Reminder)
        else:
            print(f"'{Task}' is a low priority task, Consider completing it when you have free time")
