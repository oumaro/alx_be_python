# This script provides a customized daily reminder based on user input for a single task.

# Prompt the user to enter the task description.
task = input("Enter your task: ")

# Prompt for the task's priority.
priority = input("Priority (high/medium/low): ").lower()

# Prompt whether the task is time-bound.
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message.
reminder_message = ""

# Use a match case statement to handle different priority levels.
match priority:
    case 'high':
        reminder_message = f"'{task}' is a high priority task"
    case 'medium':
        reminder_message = f"'{task}' is a medium priority task"
    case 'low':
        # Special message for low priority, as per the example.
        if time_bound == 'no':
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
            # We can return here since this is a complete message.
            exit()
        reminder_message = f"'{task}' is a low priority task"
    case _:
        # Handle invalid priority input.
        print("Invalid priority entered. Please choose from high, medium, or low.")
        # Exit the script if the priority is invalid.
        exit()

# If the task is time-bound, add the immediate attention phrase.
if time_bound == 'yes':
    reminder_message += " that requires immediate attention today!"

# Print the final reminder message.
print(f"Reminder: {reminder_message}")
