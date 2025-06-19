# Q3.1
def count_c_in_l(l, c, index=0):
    if index >= len(l):
        return 0
    return (1 if l[index] == c else 0) + count_c_in_l(l, c, index + 1)

# Q3.2
def is_c_n_in_l(l, c, n=0):
    return count_c_in_l(l, c) == n

def main():
    # Q3 test
    l = [1, 4, 7, 1, 2, 1]

    # Q3.1
    print(f"count_c_in_l({l}, 1) = {count_c_in_l(l, 1)}")
    print(f"count_c_in_l({l}, 7) = {count_c_in_l(l, 7)}")
    print(f"count_c_in_l({l}, 8) = {count_c_in_l(l, 8)}")
    print(f"count_c_in_l({l}, -2) = {count_c_in_l(l, -2)}")

    # Q3.2
    print(f"is_c_n_in_l({l}, 1, 3) = {is_c_n_in_l(l, 1, 3)}")
    print(f"is_c_n_in_l({l}, 1, 0) = {is_c_n_in_l(l, 1, 0)}")
    print(f"is_c_n_in_l({l}, 1, 2) = {is_c_n_in_l(l, 1, 2)}")
    print(f"is_c_n_in_l({l}, 7, 1) = {is_c_n_in_l(l, 7, 1)}")
    print(f"is_c_n_in_l({l}, 8, 3) = {is_c_n_in_l(l, 8, 3)}")
    print(f"is_c_n_in_l({l}, 8) = {is_c_n_in_l(l, 8)}")

if __name__ == "__main__":
    main()