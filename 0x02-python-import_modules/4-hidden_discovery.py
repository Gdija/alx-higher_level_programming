#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lists = dir(hidden_4)
    for i in range(len(lists)):
        if lists[i][:2] != "__":
            print("{}".format(lists[i]))
