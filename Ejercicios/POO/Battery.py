class Battery:
    def __init__(self, size, temperature):
        self.size = size # value in KWh
        self.cycles = 0
        self.temperature = temperature
        self.charge = 0

    def describe_battery(self):
        print(f"This battery is a {self.size}-kWh battery, current charge is {self.charge}% cycles={self.cycles}, temperature={self.temperature}")

    def recharge(self):
        if self.charge < 100:
            self.charge = 100
            self.cycles = self.cycles + 1