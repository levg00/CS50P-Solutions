import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
    match = re.match(pattern, ip)
    if match and 0 < int(match.group(1)) <= 255 and int(match.group(2)) <= 255 and int(match.group(3)) <= 255 and int(match.group(4)) <= 255:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
