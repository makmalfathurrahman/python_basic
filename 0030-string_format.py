import datetime

world = "World!"
date = datetime.datetime.now()

print("Hello", world, "Date:", date)
print(f"Hello {world} Date: {date}")
print("Hello {} Date: {}".format(world, date))
print("Hello {w} Date: {d}".format(w=world, d=date))
