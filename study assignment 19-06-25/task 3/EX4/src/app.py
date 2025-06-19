def power_func(a, b, *args, c=1):
    values = (a, b) + args
    total = sum(x ** c for x in values)
    count = len(values)
    return total, count


def main():
    res, l = power_func(2, 3, 6, 5, c=2)
    print(res, l)

    res, l = power_func(3, 2)
    print(res, l)

    res, l = power_func(3, 2, 5, 6, c=0)
    print(res, l)


if __name__ == "__main__":
    main()