Task = input("Enter your task: ")
Priority = input("priority level;(high/medium/low): ")
Time_Bound = input("Is it time-bound? (yes/no): ")
match Priority:
    case "high":
        if Time_Bound == "yes":
            print(f"'{Task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{Task}' is a high priority task, Consider completing it when you have free time")
    case "medium":
        if Time_Bound == "yes":
            print(f"'{Task}' is a mid-level priority task that requires immediate attention today!")
        else:
            print(f"'{Task}' is a mid-level priority task, Consider completing it when you have free time")
    case "low":
        if Time_Bound == "yes":
            print(f"'{Task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"'{Task}' is a low priority task, Consider completing it when you have free time")
