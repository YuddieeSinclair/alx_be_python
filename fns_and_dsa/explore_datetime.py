import datetime

def display_current_datetime():
    current_date = datetime.date.now()
    print(current_date)


user = int(input("Enter the number of days: "))

def calculate_future_date():
    future_date = display_current_datetime() + timedelate(days=user)
    print(future_date)
