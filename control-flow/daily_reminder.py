task = input("Enter your task: ")
priority = input("high, low, medium: ")
time_bound = input("yes or no: ")
reminder = ""
match priority:
    case 'high':
        reminder = (f"'{task}' is a HIGH priority task.")
    case 'medium':
        reminder = (f"'{task}' is a Medium priority task.")
    case 'low':
        reminder = (f"'{task}' is a low priority task.")
    case _:
        print("Please input valid priority level.")
        print(reminder, end="")
if time_bound == 'yes':
    reminder += "It requires immediate attention."
elif time_bound == no:
    reminder += "Complete it in your free time."
else:
    print("Please enter yes or no")

print(reminder)