import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'(.*)https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)'
    match = re.match(pattern, s)
    if match and re.search("<iframe ", match.group(1)) and re.search('src="', match.group(1)):
        return "https://youtu.be/" + match.group(3)
    else:
        return None


if __name__ == "__main__":
    main()
