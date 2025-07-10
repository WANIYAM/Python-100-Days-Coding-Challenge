# 75.Format date and time using strftime.

from datetime import datetime

# Get current date and time
now = datetime.now()

# Format date and time using strftime
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted)
