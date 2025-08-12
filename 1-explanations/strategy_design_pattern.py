from abc import ABC, abstractmethod 

# Step 1: Define the Strategy interface 
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Step 2: Implement Concrete Strategies
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} with Credit Card."


class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} with Credit Card."



class BitcoinPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} with Credit Card."




# Step 3: Implement the Context
class ShoppingCart:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def checkout(self, amount):
        return self.payment_method.pay(amount)


# Step 4: Use the Strategy in the Context
if __name__ == "__main__":
    cart = ShoppingCart(CreditCardPayment())
    print(cart.checkout(100))  # Output: Paying 100 with Credit Card.

    cart.payment_method = PayPalPayment()
    print(cart.checkout(200))  # Output: Paying 200 with PayPal.

    cart.payment_method = BitcoinPayment()
    print(cart.checkout(300))  # Output: Paying 300 with Bitcoin.