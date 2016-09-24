def get_user_input():
    numbers = []
    while True:
        inputted = input('enter 6 numbers:')
        print("{s} numbers entered".format(s=len(inputted.split())))
        if len(inputted.split()) == 6:
            numbers = []
            numbers.extend(inputted.split())
            break
    return numbers


if __name__ == '__main__':
    numbers = get_user_input()
