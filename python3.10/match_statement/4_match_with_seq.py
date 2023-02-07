# Match example with list structure
# Sequence Pattern

# Explain orPattern
# Explain asPattern
# Adding conditions to patterns

# PEP 634, PEP 635, PEP 636



# command = ["quit"]
command = ["go", "left"]
# command = ["drop", "sword", "knife", "cheese"]

match command:
    case ["quit"]:
        print("Goodbye!")
    case ["go", direction]:
        print(f"Go to {direction=}")
    case ["drop", *items]:
        for item in items:
            print(f"drop {item=}")
    case _:
        print('Nothing matched')
