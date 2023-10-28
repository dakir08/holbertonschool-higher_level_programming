#!/usr/bin/python3
def add_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print(f"{n}")
        return
    else:
        i = 1
        sum = 0
        while i <= n:
            sum += int(argv[i])
            i += 1
        print(f"{sum}")


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
