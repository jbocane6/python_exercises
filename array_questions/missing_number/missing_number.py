# !/usr/bin/python3


# Look for the missing number in a integer list.
if __name__ != "__main__":
    def missing_number(nList):
        if validate(nList):
            miss = ((len(nList)+1) * (len(nList) + 2) // 2)-sum(nList)
            print(f"The missing number is: {miss}")

    # check if all items are int
    def validate(nList):
        for i in nList:
            if not isinstance(i, int) or isinstance(i, bool):
                print(f"Error, there are not int values in list")
                return False
        return True
