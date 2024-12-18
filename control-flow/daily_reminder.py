Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
Time_Bound = input("Is it time-bound? (yes/no): ")
Reminder = ""
match Priority:
    case "high":
        Reminder += f"'{Task}' is a {Priority} priority task"
    case "medium":
        Reminder += f"'{Task}' is a {Priority} priority task"
    case "low":
        Reminder += f"'{Task}' is a {Priority} priority task"
    case _:
        print("enter a valid priority option")
        exit()
if Time_Bound == "yes":
    Reminder += " that requires immediate action today!"
    print(f"Reminder: {Reminder}")
else:
    Reminder += ".Consider completing it when you have free time."
    print(f"Note: {Reminder}")
