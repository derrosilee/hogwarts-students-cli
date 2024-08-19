
def main():
    ans = get_int("Enter a number: ")


def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a number")
        return get_int(prompt)


if __name__ == '__main__':
    main()