Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
Time_Bound = input("Is it time-bound? (yes/no): ")
Reminder = f"'{Task}' is a {Priority} priority task"
match Priority:
    case "high":
        Reminder
    case "medium":
        Reminder
    case "low":
        Reminder
    case _:
        print("enter a valid priority option")
if Time_Bound == "yes":
    message = " that requires immediate action today!"
else:
    message = " Consider completing it when you have free time."
print(Reminder + " " + message)
