def f_2D(x0, x1, y0, y1):
    """
    generate a 2D list (f) of the function: x^2 + y^2
    where x ranges between x0 and x1 including,
    y ranges between y0 and y1 including
    where x and y contain only integers
    """
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