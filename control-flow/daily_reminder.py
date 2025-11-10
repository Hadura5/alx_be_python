# Getting task description
task = input("Enter your task: ")

# Getting task priority
priority = input("Priority (high/medium/low): ")

# Checking if task is time-bound
time_bound = input("Is it time-bound? (yes/no): ")

# Processing task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an invalid priority level"

# Modifying reminder if task is time-bound
if time_bound.lower() == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Printing the reminder
print("Reminder:", reminder)