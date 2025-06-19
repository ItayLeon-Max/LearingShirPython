# Q1.a
chrs = []

def update_chrs():
    global chrs
    chrs = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    return

# Q1.b
def mod_chr(l, n=0):
    update_chrs()
    index = chrs.index(l)
    new_index = (index + n) % 26
    return chrs[new_index]

# Q1.c
def mod_str(s, n=0):
    return ''.join(mod_chr(c, n) for c in s)

def main():
    global chrs
    # Q1.a
    update_chrs()
    print(chrs)

    # Q1.b
    print(f"'a' was shifted to '{mod_chr('a', 0)}' with n=0")
    print(f"'a' was shifted to '{mod_chr('a', 5)}' with n=5")
    print(f"'z' was shifted to '{mod_chr('z', 4)}' with n=4")

    # Q1.c
    s = "story"
    print(f"'{s}' is modified to '{mod_str(s)}' with no specified n")
    print(f"'{s}' is modified to '{mod_str(s,2)}' with n=2")
    s = "anaconda"
    print(f"'{s}' is modified to '{mod_str(s,10)}' with n=10")

if __name__ == "__main__":
    main()