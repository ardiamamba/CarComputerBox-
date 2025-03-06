class CarComputerBoxError(Exception):
    """Custom exception for Car Computer Box errors."""
    pass

class CarComputerBox:
    def __init__(self, fuel_level=100):
        self.engine_status = False  
        self.fuel_level = fuel_level  
        self.diagnostics = []

    def start_engine(self):
        if self.engine_status:
            raise CarComputerBoxError("Engine is already running.")
        if self.fuel_level <= 0:
            raise CarComputerBoxError("Cannot start engine: Fuel level is empty.")
        self.engine_status = True
        print("Engine started.")

    def stop_engine(self):
        if not self.engine_status:
            raise CarComputerBoxError("Engine is already off.")
        self.engine_status = False
        print("Engine stopped.")

    def check_fuel(self):
        print(f"Current fuel level: {self.fuel_level}%")
        if self.fuel_level < 10:
            print("Warning: Low fuel level!")
    
    def refuel(self, amount):
        if amount < 0:
            raise CarComputerBoxError("Cannot refuel with a negative amount.")
        self.fuel_level = min(self.fuel_level + amount, 100)
        print(f"Refueled: Current fuel level is {self.fuel_level}%")

    def run_diagnostics(self):
        self.diagnostics.append("Diagnostics run successfully.")
        print("Running diagnostics...")
        
        if self.engine_status:
            self.diagnostics.append("Engine is running smoothly.")
        else:
            self.diagnostics.append("Engine is off.")
        print("Diagnostics complete.")

    def get_diagnostics(self):
        print("Diagnostics Report:")
        for report in self.diagnostics:
            print(f"- {report}")


if __name__ == "__main__":
    car = CarComputerBox()

    try:
        car.start_engine()
    except CarComputerBoxError as e:
        print(e)

    car.check_fuel()
    car.refuel(20)
    car.start_engine()
    car.run_diagnostics()
    car.get_diagnostics()
    car.stop_engine()
