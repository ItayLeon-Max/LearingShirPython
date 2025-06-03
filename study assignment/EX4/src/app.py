def maze_func():
    i = 0
    while True:
        user_input = input("what is current condition?\n")
        if user_input == "free pass ahead":
            print("keep straight")
        elif user_input == "wall in front":
            print("turn left")
        elif user_input == "wall on the right corner":
            print("turn right")
        elif user_input == "end of wall":
            print("make a U turn")
        elif user_input == "reached the target":
            print(f"number of iterations is {i}")
            break
        else:
            print("Invalid input, try again.")
            continue
        i += 1

if __name__ == "__main__":
    maze_func()