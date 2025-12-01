class BankAccount:
    def __init__(self):
        self.balance = 0
        self.status = 'closed'

    def get_balance(self):
        if self.status == 'open':
            return self.balance
        else:
            raise ValueError('account not open')
    def open(self):
        if not self.status == 'open':
            self.status = 'open'
        else:
            raise ValueError('account already open')

    def deposit(self, amount):
        if self.status == 'open':
            if amount > 0:
                self.balance += amount
            else:
                raise ValueError('amount must be greater than 0')
        else:
            raise ValueError('account not open')

    def withdraw(self, amount):
        if self.status == 'open':
            if amount > 0 and amount <= self.balance:
                self.balance -= amount 
            elif amount <= 0:
                raise ValueError('amount must be greater than 0')
            else:
                raise ValueError('amount must be less than balance')
        else:
            raise ValueError('account not open')
    
            
            

    def close(self):
        if self.status == 'open':
            final_balance = self.balance
            self.balance = 0
            self.status = 'closed'
            return final_balance  # Return money to customer
        else:
            raise ValueError('account not open')
