# daily_reminder.py

# Loop ensures the user enters at least one task (demonstrates a loop)
while True:
    # Prompt for a single task
    task = input("Enter your task: ").strip()
    if task == "":
        print("Task cannot be empty. Please enter a valid task.")
        continue  # Ask again if input is empty

    # Prompt for task priority
    priority = input("Priority (high/medium/low): ").lower().strip()
    # Prompt for time sensitivity
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

    # Process the task based on priority using match-case
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            reminder = f"Reminder: '{task}' has an unspecified priority level."

    # Modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"

    # Print the customized reminder
    print(reminder)

    # Exit the loop after providing one reminder (single task requirement)
    break
