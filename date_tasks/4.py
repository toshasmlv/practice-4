from datetime import datetime

date1 = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")

d1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
d2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

difference = abs((d2 - d1).total_seconds())

print("Difference in seconds:", int(difference))