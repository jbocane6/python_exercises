# !/usr/bin/python3
import random
import duplicateNumber as d


def main():
    for count in range(5):
        iList = []
        for len in range(random.randrange(1, 100)):
            iList.append(random.randrange(1, 100))
        print(d.duplicateNumber(iList))

    print(d.duplicateNumber([1, 2, True]))
    print(d.duplicateNumber([1, 2, ""]))
    print(d.duplicateNumber([1, 2, []]))


if __name__ == "__main__":
    main()
