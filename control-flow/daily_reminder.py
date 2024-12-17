Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
Time_Bound = input("Is it time-bound? (yes/no): ")
match Priority:
    case "high":
        Reminder = f"{Task} is a high priority task"
    case "medium":
         Reminder = f"{Task} is a mid-level priority task"
    case "low":
         Reminder = f"{Task} is a low priority task"
    case _:
        print("enter a valid priority option")
if Time_Bound == "yes":
    Reminder = f"{Task} is a {Priority} priority task, that requires immediate action today!"
else:
    Reminder = f"{Task} is a {Priority} priority task,Consider completing it when you have free time."
print(Reminder)
