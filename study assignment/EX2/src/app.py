def int2bin(x):
    if x == 0:
        return "0b0"
    binary = ''
    while x > 0:
        binary = str(x % 2) + binary
        x = x // 2
    binary = "0b" + binary
    return binary

def main():
    print(f"bin({0}) = {bin(0)}, int2bin(0) = {int2bin(0)}")
    print(f"bin({1}) = {bin(1)}, int2bin(1) = {int2bin(1)}")
    print(f"bin({2}) = {bin(2)}, int2bin(2) = {int2bin(2)}")
    print(f"bin({5}) = {bin(5)}, int2bin(5) = {int2bin(5)}")
    print(f"bin({10}) = {bin(10)}, int2bin(10) = {int2bin(10)}")
    print(f"bin({1024}) = {bin(1024)}, int2bin(1024) = {int2bin(1024)}")

if __name__=="__main__":
    main()