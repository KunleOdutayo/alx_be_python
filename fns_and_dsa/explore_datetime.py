from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current Date & Time:{current_date.strftime('%Y-%m-%d %H:%M:%S')}")
def main():
    print("Date and Time Explorer")
    display_current_datetime()
if __name__ == "__main__":
    main()