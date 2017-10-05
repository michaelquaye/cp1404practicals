from prac_08.unreliable_car import UnreliableCar

def main():

    car_1 = UnreliableCar('Prius 1', 100)

    for i in range (1,10):
        car_1.drive(1)
        print("{} {}".format(i, car_1))


main()