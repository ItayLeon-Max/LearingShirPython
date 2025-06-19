def f_2D(x0, x1, y0, y1):
    f = []  
    for x in range(x0, x1 + 1):
        row = []
        for y in range(y0, y1 + 1):
            row.append(x**2 + y**2)
        f.append(row)

    return f


def main():
    g = f_2D(-2, 2, -2, 2)
    print(g)
    g = f_2D(-3, 0, 0, 2)
    print(g)


if __name__ == "__main__":
    main()