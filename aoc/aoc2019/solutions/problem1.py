def fuel_needed_for_mass(mass, recursive):
    fuel = max((mass // 3) - 2, 0)
    if (recursive and fuel > 0):
        fuel += fuel_needed_for_mass(fuel, recursive)
    return fuel

def get_total_fuel_needed(masses, recursive):
    return sum(fuel_needed_for_mass(int(mass), recursive) for mass in masses.splitlines())

with open("DataFiles/1.txt") as f:
    input = f.read()
    
totalFuel = get_total_fuel_needed(input, False)
print("Part 1: ", totalFuel)
totalFuel = get_total_fuel_needed(input, True)
print("Part 2: ", totalFuel)
