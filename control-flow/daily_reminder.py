Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
Time_Bound = input("Is it time-bound? (yes/no): ")
Reminder = f"'{Task}' is a {Priority} priority task"
match Priority:
    case "high":
        Priority = "high"
    case "medium":
        Priority = "medium"
    case "low":
        Priority = "low"
    case _:
        print("enter a valid priority option")
if Time_Bound == "yes":
    Reminder = Reminder + " that requires immediate action today!"
else:
    Reminder = Reminder + " ,Consider completing it when you have free time."
print(Reminder)
