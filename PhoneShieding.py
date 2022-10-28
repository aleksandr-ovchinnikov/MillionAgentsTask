import re


class PhoneSheild:

    def __init__(self, symbol, amount=3):
        self.symbol = symbol
        self.amount = amount

    def validate(self, phone_number):
        ##
        # Validate phone number
        ##
        pattern = r'\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})'
        if not re.match(pattern, phone_number):
            raise ValueError('Invalid phone number')
        return

    def run(self, phone_number):
        ##
        # Remove multiple spaces, validate number, shield symbols
        ##
        stripped_number = re.sub(r'\s+', ' ', phone_number)
        self.validate(stripped_number)
        number_list = list(stripped_number)
        i = 1
        count = 0
        while count != self.amount:
            if number_list[-i] != ' ':
                number_list[-i] = self.symbol
                count += 1
            i += 1
        return ''.join(number_list)


a = PhoneSheild('x')
a.run("+7 904 255    6830")
