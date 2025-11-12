# PROGRAM TO CALCULATE MASS OR VOLUME (in mL) FOR A GIVEN WEIGHT PERCENTAGE

def calculate_mass(density, volume_ml, desired_percentage):
    # Convert mL → m³ (1 mL = 1e-6 m³)
    volume_m3 = volume_ml * 1e-6
    solution_mass_kg = density * volume_m3           # kg
    solution_mass_g = solution_mass_kg * 1000        # g
    required_mass = (desired_percentage / 100) * solution_mass_g
    print(f"\nThe required mass is: {required_mass:.4f} grams")


def calculate_volume(density, desired_percentage, required_mass_g):
    # required_mass_g in grams, density in kg/m³
    solution_mass_g = required_mass_g * 100 / desired_percentage
    solution_mass_kg = solution_mass_g / 1000
    volume_m3 = solution_mass_kg / density
    volume_ml = volume_m3 * 1e6                      # m³ → mL
    print(f"\nThe required volume is: {volume_ml:.4f} mL")


print("Choose calculation type:")
print("1. Calculate required mass")
print("2. Calculate required volume")

choice = input("Enter 1 or 2: ").strip()

if choice == "1":
    density = float(input("Enter the density of the solvent in kg/m³: "))
    volume_ml = float(input("Enter the volume of the solvent in mL: "))
    desired_percentage = float(input("Enter the desired weight percentage (%): "))
    calculate_mass(density, volume_ml, desired_percentage)

elif choice == "2":
    density = float(input("Enter the density of the solvent in kg/m³: "))
    desired_percentage = float(input("Enter the desired weight percentage (%): "))
    required_mass = float(input("Enter the desired solute mass in grams: "))
    calculate_volume(density, desired_percentage, required_mass)

else:
    print("Invalid choice. Please restart and enter 1 or 2.")

