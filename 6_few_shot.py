# Example 1: Greeting message for morning
# Input: 9 AM
# Output: "Good morning!"

# Example 2: Greeting message for afternoon
# Input: 2 PM
# Output: "Good afternoon!"

# Example 3: Greeting message for evening
# Input: 7 PM
# Output: "Good evening!"

# Now, generate a python code that takes the current time as input using the datetime module
# and returns the appropriate greeting message

# Solution:
# Import datetime module
import datetime as dt

# Get current time
current_time = dt.datetime.now()

# Get current hour
current_hour = current_time.hour

# Check if it is morning (before 12 PM)
if current_hour < 12:
    print("Good Morning!")

# Check if it is afternoon (between 12 PM and 4 PM)
if current_hour >= 12 and current_hour < 16:
    print("Good Afternoon!")

# Check if it is evening (after 4 PM)
if current_hour >= 16:
    print("Good Evening!")

# Else it is night time
else:
    print("Good Night!")
