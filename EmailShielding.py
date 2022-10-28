import re


class EmailShield:

    def __init__(self, symbol):
        self.symbol = symbol

    def validate(self, email):
        ##
        # Check whether the email is valid
        ##
        pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
        if not re.match(pattern, email):
            raise ValueError('Invalid email adress')
        return

    def run(self, email):
        ##
        # Validate email, get main parts of it, shield and return shielded email
        ##
        self.validate(email)
        main_part, domain_part = email.split('@')
        shielded_email = re.sub(
            r'.', self.symbol, main_part) + '@' + domain_part
        return shielded_email


a = EmailShield('y')
a.run('aaa@aaa.com')
