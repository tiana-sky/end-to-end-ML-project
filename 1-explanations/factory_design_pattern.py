from abc import ABC, abstractmethod

# Step 1: Define the Product interface
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass

# Step 2: Implement Concrete Products
class Espresso(Coffee):
    def prepare(self):
        return "Preparing Espresso."


class Latte(Coffee):
    def prepare(self):
        return "Preparing Latte."


class Cappuccino(Coffee):
    def prepare(self):
        return "Preparing Cappuccino."


# Step 3: Implement the Factory (CoffeeMachine)
class CoffeeMachine:
    def create_coffee(self, coffee_type):
        if coffee_type == "Espresso":
            return Espresso().prepare()
        elif coffee_type == "Latte":
            return Latte().prepare()
        elif coffee_type == "Cappuccino":
            return Cappuccino().prepare()
        else:
            raise ValueError(f"Unknown coffee type: {coffee_type}")



# Step 4: Use the Factory to Create Products
if __name__ == "__main__":
    machine = CoffeeMachine()

    coffee = machine.create_coffee("Espresso")
    print(coffee)  # Output: Preparing Espresso.
    coffee = machine.create_coffee("Latte")
    print(coffee)  # Output: Preparing Latte.      
    coffee = machine.create_coffee("Cappuccino")
    print(coffee)  # Output: Preparing Cappuccino.