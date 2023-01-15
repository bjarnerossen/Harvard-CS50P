
import sys
from datetime import date, datetime, timedelta
import inflect
import operator


def main():
    try:
        birth = input("Date of Birth: ")
        birth = datetime.strptime(birth, '%Y-%m-%d')

    except (TypeError, ValueError):
        sys.exit("Not a valid date format")

    print(num_to_txt(get_minutes(birth)))


def get_minutes(birth):
    now = date.fromisoformat('2000-01-01')
    now = datetime.combine(now, datetime.min.time())

    minutes = round((now - birth).total_seconds() / 60)
    # minutes = int((now - birth) / timedelta(minutes=1))

    return minutes


def num_to_txt(minutes):
    p = inflect.engine()
    sentence = p.number_to_words(minutes, andword="") + " minutes"
    return sentence.capitalize()


if __name__ == "__main__":
    main()
