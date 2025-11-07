class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        if len(self.card_num) <= 1:
            return False
        striped = self.card_num.replace(" ", "")
        if len(striped) <= 1:
            return False
        if not striped.isdigit():
            return False
        reversed_striped = striped[::-1]
        total = 0
        count = 1
        for item in reversed_striped:
            digit = int(item)
            if count % 2 == 0:
                doubled = self._luhn_doubling(digit)
                total += doubled
            else:
                total += digit
            count += 1
        return total % 10 == 0

    def _luhn_doubling(self, num):  
        doubled = num * 2
        return doubled if doubled <= 9 else doubled - 9
            
