import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^([0-9]{1,2})(:[0-9]{1,2})? (AM|PM)? to ([0-9]{1,2})(:[0-9]{1,2})? (AM|PM)?$"
    match = re.match(pattern, s.strip())
    if match and (1 <= int(match.group(1)) <= 12) and (match.group(2) == None or 0 <= int(match.group(2)[1:]) <= 59) and (1 <= int(match.group(4)) <= 12) and (match.group(5) == None or 0 <= int(match.group(5)[1:]) <= 59):

        hours1 = int(match.group(1))
        hours2 = int(match.group(4))
        abbr1 = match.group(3)
        abbr2 = match.group(6)

        if match.group(2) == None:
            min1 = 0
        else:
            min1 = int(match.group(2)[1:])

        if match.group(5) == None:
            min2 = 0
        else:
            min2 = int(match.group(5)[1:])


        time = ""

        if abbr1 == "AM":
            if hours1 == 12:
                time += "00"
            else:
                time += f"{(hours1):02}"
        else:   #abbr1 == "PM"
            if hours1 == 12:
                time += "12"
            else:
                time += f"{(hours1+12):02}"

        time += f":{(min1):02} to "

        if abbr2 == "AM":
            if hours2 == 12:
                time += "00"
            else:
                time += f"{(hours2):02}"
        else:   #abbr1 == "PM"
            if hours2 == 12:
                time += "12"
            else:
                time += f"{(hours2+12):02}"

        time += f":{(min2):02}"
        return time


    else:
        raise ValueError()




if __name__ == "__main__":
    main()
