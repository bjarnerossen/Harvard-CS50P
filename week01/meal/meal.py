# meal schedule
schedule = [
    {"meal": "breakfast time", "start hour": 7, "end hour": 8},
    {"meal": "lunch time", "start hour": 12, "end hour": 13},
    {"meal": "dinner time", "start hour": 18, "end hour": 19},
]


def main():
    time = input("what time is it? ")
    time = float(convert(time))

    for meal in schedule:
        if time >= float(meal["start hour"]) and time <= float(meal["end hour"]):
            print(meal["meal"])
        else:
            continue


def convert(time):
    hours, minutes = time.strip().split(":")
    time = float(hours) + (float(minutes) / 60)
    return f"{time:.2f}"


if __name__ == "__main__":
    main()