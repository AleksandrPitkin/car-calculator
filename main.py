import calculator  # Importing custom module named 'calculator'

if __name__ == '__main__':
    # Create a Calculator instance
    calc = calculator.Calculator()

    # Add Car objects to the calculator
    calc.add_car(
        calculator.Car("Toyota Corolla", 120000, 7,
                       1200, 2500),
    )
    calc.add_car(
        calculator.ElectricCar("Tesla Model 3", 200000, 5500, 150),
    )
    calc.add_car(
        calculator.Car("Range Rover", 650000, 3,
                       3000, 7000),
    )

    # Print the calculated maintenance costs of all added cars
    calc.print_cars()
