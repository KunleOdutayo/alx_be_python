from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current Date & Time:{current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    added_day = int(input("Enter the number of days to add to the current date: "))
    if added_day < 0:
        print("Please enter at least 1 day.")
        return
    
    calculate_future_date = current_date + timedelta(days=added_day)
    print("Future date: {future_date.strftime('%Y-%m-%d')}")
    

def main():
    print("Date and Time Explorer")
    display_current_datetime()
    print("Future Date")
    calculate_future_date

if __name__ == "__main__":
    main()