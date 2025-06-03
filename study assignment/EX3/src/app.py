def bin2int(b):
    binary = b[2:]  # Remove the '0b' prefix
    result = 0
    for i, digit in enumerate(reversed(binary)):
        result += int(digit) * (2 ** i)
    return result

def main():
    print(f"int(0b0) = {int(0b0)}, bin2int('0b0') = {bin2int('0b0')}")
    print(f"int(0b1) = {int(0b1)}, bin2int('0b1') = {bin2int('0b1')}")
    print(f"int(0b10) = {int(0b10)}, bin2int('0b10') = {bin2int('0b10')}")
    print(f"int(0b101) = {int(0b101)}, bin2int('0b101') = {bin2int('0b101')}")
    print(f"int(0b1010) = {int(0b1010)}, bin2int('0b1010') = {bin2int('0b1010')}")
    print(f"int(0b10000000000) = {int(0b10000000000)}, bin2int('0b10000000000') = {bin2int('0b10000000000')}")

if __name__ == "__main__":
    main()