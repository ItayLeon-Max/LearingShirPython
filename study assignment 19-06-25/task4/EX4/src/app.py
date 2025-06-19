def rec_mem(n, memo={0: 1, 1: 2, 2: 3}):
    if n in memo:
        return memo[n]
    memo[n] = (rec_mem(n - 1, memo) - rec_mem(n - 2, memo)) * rec_mem(n - 3, memo)
    return memo[n]

def main():
    print("0.", rec_mem(0))
    print("1.", rec_mem(1))
    print("2.", rec_mem(2))
    print("4.", rec_mem(4))
    print("7.", rec_mem(7))
    print("8.", rec_mem(8))

if __name__ == "__main__":
    main()