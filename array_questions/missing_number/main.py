# !/usr/bin/python3
import random
import missingNumber as m


def main():
    for n in [100, 253, 5235, 800000]:
        miss = random.randrange(1, n)
        print(f"The number to remove is: {miss}")
        print(m.missingNumber(
            [y for y in [x for x in range(1, n+1)] if y != miss]))

    print(m.missingNumber([1, 2, True]))
    print(m.missingNumber([1, 2, ""]))
    print(m.missingNumber([1, 2, []]))


if __name__ == "__main__":
    main()
