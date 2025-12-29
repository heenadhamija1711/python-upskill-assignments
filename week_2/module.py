# Using datetime, ​​add a week and 12 hours to a date.  Given date: March 22, 2020, at 10:00 AM. print original date time and new date time

from datetime import datetime, timedelta

# Original date
original_date = datetime(2020, 3, 22, 10, 0)  # March 22, 2020, 10:00 AM
print("Original DateTime:", original_date)

# Time delta: 1 week + 12 hours
delta = timedelta(weeks=1, hours=12)

# New date
new_date = original_date + delta
print("New DateTime:", new_date)

#
# Code to get the dates of yesterday, today, and tomorrow.
from datetime import datetime, timedelta

today = datetime.today().date()  # Today's date
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#
# Write a code snippet using os module, to get the current working directory and print and create a folder “test”. List all the files and folders in the current working directory and remove the directory “test” that was created.
import os

# Get and print current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Create a folder named "test"
os.mkdir("test")
print('"test" folder created.')

# List all files and folders in the current directory
items = os.listdir(cwd)
print("Files and Folders:", items)

# Remove the "test" directory
os.rmdir("test")
print('"test" folder removed.')

#
# Write a Python program to rename a file from old_name.txt to new_name.txt.
import os

# Rename file
old_name = "old_name.txt"
new_name = "new_name.txt"

# Check if the old file exists
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"File renamed from {old_name} to {new_name}")
else:
    print(f"{old_name} does not exist")

#
# Create a file and Write a Python program to get the size of a file named example.txt
import os

# Create a file and write some content
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")

# Get size of the file
file_size = os.path.getsize("example.txt")
print(f"Size of 'example.txt': {file_size} bytes")

#
# Convert the string "Feb 25 2020 4:20PM" into a Python datetime object
# O/P: 2020-02-25 16:20:00
from datetime import datetime

date_str = "Feb 25 2020 4:20PM"

# Convert string to datetime
date_obj = datetime.strptime(date_str, "%b %d %Y %I:%M%p")
print(date_obj)

#
# Subtract 7 days from the date 2025-02-25 and print the result.
# O/P: New date: 2025-02-18
from datetime import datetime, timedelta

# Given date
date_str = "2025-02-25"
date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

# Subtract 7 days
new_date = date_obj - timedelta(days=7)

print("New date:", new_date)

#
# Format the date 2020-02-25 as "Tuesday 25 February 2020"
from datetime import datetime

# Original date
date_str = "2020-02-25"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")

# Format date
formatted_date = date_obj.strftime("%A %d %B %Y")
print(formatted_date)

#
