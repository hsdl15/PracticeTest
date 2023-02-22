def work():
    a = [0]*6
    a[0] = "陈昶旭"
    return a


if __name__ == "__main__":
    output = work()
    for i in output:
        print(f"{i}")
