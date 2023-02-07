# Match against Class
# Class pattern (type matching)

# PEP 634, PEP 635, PEP 636


class Country:

    # __match_args__ = ('country', )

    def __init__(self, country):
        self.country = country

    def get_country(self):
        return self.country


match = Country(country='Germany')

match match:
    case Country(country='France'):
        print(f'Country is {match.get_country()}')
    case Country(country='Germany'):
        print(f'Country is {match.get_country()}')
    case _:
        print(f'Nothing Matched.')


