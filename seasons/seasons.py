from datetime import date
import datetime
import re
import sys
import inflect
p = inflect.engine()

class Date:
    def __sub__(self, other):
        return self - other


    @staticmethod
    def get_today():
        return datetime.date.today()


    @staticmethod
    def get_date(request_message, exit_message):
        date = input(request_message).strip()
        pattern = r"^([0-9]+)-([0-9]+)-([0-9]+)$"
        if match := re.match(pattern, date):
            year, month, day = int(match.group(1)), int(match.group(2)), int(match.group(3))
            try:
                datetime.date(year, month, day)
                return datetime.date(year, month, day)
            except ValueError:
                sys.exit(exit_message)
        else:
            sys.exit(exit_message)


    @staticmethod
    def convert_to_minutes(time, decimal_places):
        return(int(round(time.total_seconds()/60, decimal_places)))


    @staticmethod
    def convert_min_to_text(min):
        return p.number_to_words(min, andword="")


def main():
    birth_date = Date.get_date("Date of Birth: ", "Invalid date")
    print(time_from_birth_in_text(birth_date))

def time_from_birth_in_text(input_date):
    current_date = Date.get_today()
    return(Date.convert_min_to_text(Date.convert_to_minutes(current_date - input_date, 0)).capitalize() + " minutes")


if __name__ == "__main__":
    main()
