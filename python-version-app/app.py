import sys
from datetime import datetime
from zoneinfo import ZoneInfo

current_time = datetime.now(ZoneInfo("Asia/Kolkata"))

print(f"Python Version: {sys.version}")
print(f"Current Date & Time (IST): {current_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
print(f"Current Date: {current_time.date()}")
print(f"Current Time: {current_time.time()}")