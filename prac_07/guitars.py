from prac_07.Guitar import Guitar



def main():
    guitars = []

    # name = input('please enter the name of guitar: ')
    # while name is not "":
    #     year = int(input('please enter the year of guitar: '))
    #     cost = int(input('please enter the price '))
    #     temp_guitar = Guitar(name, year, cost)
    #     guitars.append(temp_guitar)
    #     print("{} ({}) : ${} added.".format(name, year, cost))
    #     name = input('please enter the name of guitar: ')

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("3", 1922, 16035.40))
    guitars.append(Guitar("4", 2010, 1512.9))

    #print(len(guitars))

    for i in range (len(guitars)):
        if guitars[i].is_vintage() is True:
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1,
                                                                   guitars[i].name, guitars[i].year, guitars[i].cost,
                                                                   vintage_string))
    print('done')

main()

