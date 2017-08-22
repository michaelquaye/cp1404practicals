import random


def main():
    draw_number = int(input("How many draws?"))
    for i in range(draw_number):
        quick_pick = []
        for j in range(6):
            quick_pick.append(random.randint(1,45))
            print(quick_pick)


main()