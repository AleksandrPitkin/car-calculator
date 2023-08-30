from apis import get_gas_price, get_power_price  # Importing necessary API functions for gas and power prices


class Calculator:
    def __init__(self, mileage=15000, years=3, year_loss=10):
        """
        Initializes a Calculator object with default values for mileage, number of years, and year loss.

        :param mileage: The yearly mileage of the car (default: 15000)
        :param years: The number of years for calculation (default: 3)
        :param year_loss: The yearly depreciation rate as a percentage (default: 10)
        """
        self.mileage = mileage
        self.cars = {}  # Dictionary to store car objects along with their calculated costs
        self.years = years
        self.year_loss = year_loss / 100  # Converting percentage to decimal

    def add_car(self, car):
        """
        Adds a car object to the calculator along with its calculated yearly cost.

        :param car: A Car or ElectricCar object to be added
        """
        year_cost = car.year_cost(self.mileage)
        price_per_year = car.price / self.years
        left_price = self.get_left_price(car) / self.years
        self.cars[car] = year_cost + price_per_year - left_price

    def get_left_price(self, car):
        """
        Calculates the estimated remaining price of the car after a number of years.

        :param car: A Car or ElectricCar object
        :return: Estimated remaining price of the car
        """
        initial_price = car.price
        for i in range(self.years):
            initial_price -= initial_price * self.year_loss
        return initial_price

    def print_cars(self):
        """Prints the calculated yearly costs of all added cars."""
        for car, year_price in self.cars.items():
            print(f"{car.name}:\t\t{year_price}")


class Car:
    def __init__(self,
                 name: str,
                 price: int,
                 fuel_economy: float,
                 service_cost: int,
                 insurance_cost: int):
        """
        Initializes a Car object with basic attributes.

        :param name: Name of the car
        :param price: Initial price of the car
        :param fuel_economy: Fuel economy of the car in liters per 100 km
        :param service_cost: Yearly service cost of the car
        :param insurance_cost: Yearly insurance cost of the car
        """
        self.name = name
        self.price = price
        self.fuel_economy = fuel_economy  # l / 100 km
        self.service_cost = service_cost
        self.insurance_cost = insurance_cost

    def static_year_cost(self):
        """Calculates the static yearly cost of owning the car."""
        return self.service_cost + self.insurance_cost

    def dynamic_year_cost(self, mileage: int):
        """
        Calculates the dynamic yearly cost of owning the car based on fuel consumption and gas price.

        :param mileage: Yearly mileage of the car
        """
        return self.fuel_economy * mileage / 100 * get_gas_price()

    def year_cost(self, mileage):
        """
        Calculates the total yearly cost of owning the car.

        :param mileage: Yearly mileage of the car
        """
        return self.static_year_cost() + self.dynamic_year_cost(mileage)


class ElectricCar(Car):
    def __init__(self, name: str, price: int, insurance_cost: int, power_consumption: int):
        """
        Initializes an ElectricCar object, inheriting from the Car class.

        :param name: Name of the electric car
        :param price: Initial price of the electric car
        :param insurance_cost: Yearly insurance cost of the electric car
        :param power_consumption: Power consumption of the electric car in watts per kilometer
        """
        super().__init__(name=name, price=price,
                         fuel_economy=0, service_cost=0,  # Electric cars have no fuel or service costs
                         insurance_cost=insurance_cost)
        self.power_consumption = power_consumption  # Wt / 1km

    def dynamic_year_cost(self, mileage: int):
        """
        Calculates the dynamic yearly cost of owning the electric car based on power consumption and power price.

        :param mileage: Yearly mileage of the electric car
        """
        return self.power_consumption * mileage / 1000 * get_power_price()
