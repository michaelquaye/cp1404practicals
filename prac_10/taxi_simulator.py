from prac_08.taxi import Taxi
from prac_08.SilverServiceTaxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"
def main():

    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]


    # for i in range(len(taxis)):
    #     print(taxis[i])
    fare = 0
    total_fare = 0
    print("Let's drive")
    print(MENU)
    choice = input(">>>").upper()
    #print(choice)

    while choice != "Q":
        if choice == 'C':
            taxi_number = choose_taxi(taxis)
            print("Bill to date: ${:.2f}".format(total_fare))
        else:
            fare = float(calc_fare(taxis, taxi_number))
            total_fare += fare
            print("ur trip cost ${:.2f}".format(fare))
            print("Bill to date: ${:.2f}".format(total_fare))

        print(MENU)
        choice = input(">>>").upper()


    print('done')
    print("Total trip cost: ${:.2f}".format(total_fare))
    print("Taxis are now: ")
    for i,taxi in enumerate(taxis):
        print("{} {}".format(i, taxi))

def choose_taxi(taxis):
    print('Taxis available: ')
    for i,taxi in enumerate(taxis):
        print("{} {}".format(i, taxi))
    taxi_number = int(input("Choose taxi: "))
    return taxi_number

def calc_fare(taxis, taxi_number):
    distance = int(input("drive how far? "))
    taxis[taxi_number].drive(distance)
    print(taxis[taxi_number])
    return taxis[taxi_number].get_fare()

main()