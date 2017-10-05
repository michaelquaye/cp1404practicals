from prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.flagfall = 4.5
        self.price_per_km = self.price_per_km * fanciness
    # def calc_fare_price(self):
    #     fare_price = self.price_per_km * super().current_fare_distance
    #     return fare_price
    def get_fare(self):
        """Return the price for the taxi trip."""
        return "{:.2f}".format(round(self.price_per_km * self.current_fare_distance + self.flagfall,1))

    def __str__(self):
        #prise = self.price_per_km*self.current_fare_distance+self.flagfall
        return "{} plus flagfall of ${:.2f} ".format(super().__str__(), self.flagfall)