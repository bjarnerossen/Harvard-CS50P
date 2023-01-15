import re
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()
        month, day, year = date.split('/')
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            old_month, old_day, year = date.split(" ")
            # find the number in month
            if old_month in months:
                month = months.index(old_month)+1
            # remove comma from day
            day = old_day.replace(',', '')
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            pass

print(f"{year}-{int(month):02}-{int(day):02}")