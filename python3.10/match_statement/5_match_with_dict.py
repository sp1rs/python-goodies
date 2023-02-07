# Match against dictionary
# Mapping pattern

# PEP 634, PEP 635, PEP 636


country_city_mapping = {'Germany': 'Berlin', 'France': 'Paris'}

match country_city_mapping:
    case {'Germany': city}:
        print(f'Country Germany and {city=}')
    case {'France': 'Paris', **rest}:
        print(f'Country France and rest is {rest=}')
    case _:
        print(f'Nothing matched')
