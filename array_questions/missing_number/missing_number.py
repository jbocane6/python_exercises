# !/usr/bin/python3
import validate as v


# Look for the missing number in a integer list.
if __name__ != "__main__":
    def missing_number(nList):
        if v.validate(nList):
            miss = ((len(nList)+1) * (len(nList) + 2) // 2)-sum(nList)
            return f"The missing number is: {miss}"
        else:
            return f"Error, there are not-int values in list"
