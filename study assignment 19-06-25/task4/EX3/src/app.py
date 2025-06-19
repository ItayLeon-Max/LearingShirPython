d = {'a': 2, 'b': 1, 'c': 2, 'd': 1, 'e': 3, 'f': 4}

def switch_key_val():
    global d
    new_dict = {}
    for key, value in d.items():
        if value not in new_dict:
            new_dict[value] = []
        new_dict[value].append(key)
    return new_dict

def main():
    global d
    print(d)
    print(switch_key_val())

if __name__ == "__main__":
    main()