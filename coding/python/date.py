from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print(f"Now: {now}, type(now): {type(now)}")

# Current date only
today = datetime.today()
print(f"Today: {today}")

# Formatted datetime -> string
formatted = now.strftime("%Y/%m/%d %H:%M:%S")
print(f"Formatted time: {formatted}")

# Parsing datetime -> string
dt = datetime.strptime("2025-09-14 19:03:00", "%Y-%m-%d %H:%M:%S")
print(f"Parsed datetime: {dt.hour}")

# Adding / subtracting time
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print(f"Yesterday = {yesterday}, Tomorrow = {tomorrow}")
