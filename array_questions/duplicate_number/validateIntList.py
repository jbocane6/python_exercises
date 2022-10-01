# !/usr/bin/python3


if __name__ != "__main__":
    # check if all items are int
    def validate(nList):
        for i in nList:
            if not isinstance(i, int) or isinstance(i, bool):
                return False
        return True
