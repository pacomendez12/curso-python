from Car import Car
from Battery import Battery


class ElectricCar(Car):

    def __init__(self, trademark, model, year):
        super().__init__(trademark, model, year)
        self.battery = Battery(75, 30)


    def fill_gas_tank(self):
        print("This is an electric car, you don't need to fill the tank")

    def describe_battery(self):
        self.battery.describe_battery()

    def recharge_battery(self):
        self.battery.recharge()

    

my_tesla = ElectricCar('Tesla', 'S', 2020)

print(my_tesla.get_decriptive_name())
my_tesla.describe_battery()

my_tesla.recharge_battery()
my_tesla.recharge_battery()

my_tesla.describe_battery()

