# Q2.a
def break_digits(n):
    if n < 10:
        return [n]
    return break_digits(n // 10) + [n % 10]

# Q2.b
def list2num(lst):
    num = 0
    for digit in lst:
        num = num * 10 + digit
    return num

# Q2.c
def min_nums(x, y):
    dx = break_digits(x)
    dy = break_digits(y)
    if len(dx) != len(dy):
        print("digits are not of the same size")
        return None
    min_digits = [min(a, b) for a, b in zip(dx, dy)]
    return list2num(min_digits)

def main():
    # Q2.a
    # test 1:
    print(f"{0} is broken into {break_digits(0)}")
    print(f"{5} is broken into {break_digits(5)}")

    # test 2:
    num = 123
    print(f"{num} is broken into {break_digits(num)}")

    # test 3:
    num = 987654321
    print(f"{num} is broken into {break_digits(num)}")

    # Q2.b
    # test 4:
    print(f"[0] is assembled into {list2num([0])}")
    # test 5:
    print(f"[5] is assembled into {list2num([5])}")
    # test 6:
    l = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"{l} is assembled into {list2num(l)}")

    # Q2.c
    # test 7
    n1 = 185
    n2 = 437
    print(f"from {n1} and {n2} you get the minimal valued digits: {min_nums(n1,n2)}")

    # test 8
    n1 = 1
    n2 = 123
    print(f"from {n1} and {n2} you get the minimal valued digits: {min_nums(n1,n2)}")

if __name__ == "__main__":
    main()