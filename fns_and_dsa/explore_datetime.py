from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return(current_date.strftime("%Y-%m-%d %H:%M:%S"))

display_current_datetime()

user = int(input("Enter the number of days to add to the current date:"))

def calculate_future_date():
    today = datetime.now()
    future_date = today + timedelta(days=user)
    return(future_date.strftime("%Y-%m-%d"))

calculate_future_date()
