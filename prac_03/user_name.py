def main():
    name = get_name()

    print_name_part(name,5)


def print_name_part(name, step=2):
    for i in range(0, len(name), step):
        print(name[i])


def get_name():
    name = input("Enter your name")
    while len(name) == 0:
        print("name cannot be blank")
        input("Enter your name")
    return name


main()