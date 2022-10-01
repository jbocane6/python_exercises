# !/usr/bin/python3
import random
import missing_number as m


def main():
    for n in [100, 253, 5235, 800000]:
        miss = random.randrange(1, n)
        print(f"The number to remove is: {miss}")
        list = [x for x in range(1, n+1)]
        m.missing_number([y for y in list if y != miss])

    m.missing_number([1, 2, True])
    m.missing_number([1, 2, ""])
    m.missing_number([1, 2, []])


if __name__ == "__main__":
    main()
