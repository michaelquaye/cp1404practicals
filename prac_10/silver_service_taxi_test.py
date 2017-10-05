from prac_08.SilverServiceTaxi import SilverServiceTaxi

def main():

    taxi_1 = SilverServiceTaxi('“Hummer', 200, 2)
    taxi_1.drive(18)
    print(taxi_1)
    print(taxi_1.get_fare())

main()