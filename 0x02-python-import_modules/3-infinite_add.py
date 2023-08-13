#!/usr/bin/python3
if __name__ == "__main__":
    sum = 0
    i = 1
    import sys
    if len(sys.argv) > 1:
        while i < len(sys.argv):
            j = sys.argv[i]
            i += 1
            sum += int(j)
        print("{}".format(sum))
    else:
        print("0")
