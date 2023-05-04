from datetime import datetime
import time

dt1 = datetime(2023, 5, 4)
dt2 = datetime.now()
dt = datetime.strptime("2023/05/04", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))

print(dt2 >= dt1)