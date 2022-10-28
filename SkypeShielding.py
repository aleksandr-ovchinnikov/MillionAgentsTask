import re

from pip import main


class SkypeShield:

    def __init__(self, symbol):
        self.symbol = symbol

    def validate(self, link):
        ##
        # Check whether skype link is valid
        ##
        pattern = r"(skype)[:]{1}[a-zA-z0-9\.]+"
        main_part = re.search(pattern, link)
        if not main_part:
            raise ValueError('Invalid skype link')
        else:
            return main_part.group(0)

    def run(self, link):
        ##
        # Validate, get main part, shield main part, return new link
        ##
        main_part = self.validate(link)
        data = main_part.split(':')
        main_part = data[0] + ':' + 'xxx'
        new_link = re.sub(r"(skype)[:]{1}[a-zA-z0-9\.]+", main_part, link)
        return new_link


a = SkypeShield('x')
a.run('<a href=\"skype:alex.max?call\">skype</a>')
