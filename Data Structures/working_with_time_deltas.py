from datetime import datetime, timedelta

dt1 = datetime(2018, 1, 1) + timedelta(days=5, seconds=1000)
print(dt1)
dt2 = datetime.now()


duration = dt2 - dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total_seconds", duration.total_seconds())