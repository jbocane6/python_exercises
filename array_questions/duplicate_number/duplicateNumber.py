# !/usr/bin/python3
import validateIntList as v


if __name__ != "__main__":
    # Look for the duplicate number in a integer list.
    def duplicateNumber(nList):
        if v.validate(nList):
            duplicate = list({x for x in nList if nList.count(x) > 1})
            if len(duplicate) == 0:
                return f"There aren't duplicate numbers"
            elif len(duplicate) == 1:
                return f"There is a duplicate number: {duplicate[0]}"
            else:
                return f"There are duplicate numbers: {duplicate}"
        else:
            return f"Error, there are not-int values in list"
