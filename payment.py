

from abc import ABC, abstractmethod



class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        """Process a payment of `amount` and return a result string."""
        pass



class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount):
        masked = f"**** **** **** {self.card_number[-4:]}"
        return f"Debited Amount ${amount:.2f} from debit card {masked}"


class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Charged ${amount:.2f} via PhonePe account {self.email}"


class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        return f"Transferred ${amount:.2f} worth of crypto to wallet {self.wallet_address[:6]}..."


  
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy = None):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        """Swap the payment method at runtime."""
        if not isinstance(strategy, PaymentStrategy):
            raise TypeError("strategy must implement PaymentStrategy")
        self._strategy = strategy

    def checkout(self, amount):
        if self._strategy is None:
            raise ValueError("No payment strategy set")
        print(f"Processing order for ${amount:.2f}...")
        result = self._strategy.pay(amount)
        print(result)
        return result


if __name__ == "__main__":
    processor = PaymentProcessor()

    processor.set_strategy(CreditCardPayment("4111111111111234", "123"))
    processor.checkout(49.99)

    print()
    processor.set_strategy(PayPalPayment("naman@example.com"))
    processor.checkout(19.99)

    print()
    processor.set_strategy(CryptoPayment("0xA1B2C3D4E5F6"))
    processor.checkout(120.00)