# PROGRAM TO CALCULATE MASS OR VOLUME FOR A GIVEN WEIGHT PERCENTAGE

def calculate_mass(density, volume, desired_percentage):
    solution_mass = density * volume
    required_mass = (desired_percentage / 100) * solution_mass
    print(f"\nThe required mass is: {required_mass:.4f} grams")


def calculate_volume(density, desired_percentage, required_mass):
    # desired_percentage is in %, density in kg/m3, required_mass in grams
    solution_mass = required_mass * 100 / desired_percentage
    volume = solution_mass / density  # volume in m³
    volume_liters = volume * 1000
    print(f"\nThe required volume is: {volume_liters:.4f} Litres")


print("Choose calculation type:")
print("1. Calculate required mass")
print("2. Calculate required volume")

choice = input("Enter 1 or 2: ").strip()

if choice == "1":
    density = float(input("Enter the density of the solvent in kg/m³: "))
    volume = float(input("Enter the volume of the solvent in Litres: "))
    desired_percentage = float(input("Enter the desired weight percentage (%): "))
    calculate_mass(density, volume, desired_percentage)

elif choice == "2":
    density = float(input("Enter the density of the solvent in kg/m³: "))
    desired_percentage = float(input("Enter the desired weight percentage (%): "))
    required_mass = float(input("Enter the desired solute mass in grams: "))
    calculate_volume(density, desired_percentage, required_mass)

else:
    print("Invalid choice. Please restart and enter 1 or 2.")

