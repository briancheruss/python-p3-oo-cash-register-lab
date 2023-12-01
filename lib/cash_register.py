#!/usr/bin/env python3

class CashRegister:
    pass
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.last_transaction = None
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
            self.total += price
            self.last_transaction = {'title': title, 'price': price, 'quantity': quantity}

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction:
            last_transaction_total = self.last_transaction['price'] * self.last_transaction['quantity']
            self.total -= last_transaction_total
            self.items = self.items[:-self.last_transaction['quantity']]
            self.last_transaction = None
        else:
            print("No transactions to void.")
