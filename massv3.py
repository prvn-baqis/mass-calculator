# Fully consistent solution calculator using Definition A:
# wt% = mass_solute / (mass_solute + mass_solvent)

def calc_solvent_mass(density, volume_ml):
    volume_m3 = volume_ml * 1e-6
    return density * volume_m3 * 1000  # kg → g

def calculate_mass(density, volume_ml, percent):
    solvent_mass = calc_solvent_mass(density, volume_ml)
    # m_s = p/(100-p) * m_solvent
    required_mass = (percent / (100 - percent)) * solvent_mass
    print(f"\nRequired mass: {required_mass:.4f} g")

def calculate_volume(density, percent, solute_mass):
    # m_solvent = m_s * (100-p)/p
    solvent_mass = solute_mass * (100 - percent) / percent
    # V = m_solvent / density   (convert g→kg, m3→mL)
    volume_m3 = (solvent_mass / 1000) / density
    volume_ml = volume_m3 * 1e6
    print(f"\nRequired volume: {volume_ml:.4f} mL")

def calculate_percentage(density, volume_ml, solute_mass):
    solvent_mass = calc_solvent_mass(density, volume_ml)
    percent = solute_mass / (solute_mass + solvent_mass) * 100
    print(f"\nWeight percentage: {percent:.4f} %")

print("Choose calculation type:")
print("1. Calculate required mass")
print("2. Calculate required volume")
print("3. Calculate weight percentage")

choice = input("Enter 1, 2, or 3: ").strip()

if choice == "1":
    density = float(input("Density (kg/m³): "))
    volume_ml = float(input("Volume (mL): "))
    percent = float(input("Weight percentage (%): "))
    calculate_mass(density, volume_ml, percent)

elif choice == "2":
    density = float(input("Density (kg/m³): "))
    percent = float(input("Weight percentage (%): "))
    solute_mass = float(input("Solute mass (g): "))
    calculate_volume(density, percent, solute_mass)

elif choice == "3":
    density = float(input("Density (kg/m³): "))
    volume_ml = float(input("Volume (mL): "))
    solute_mass = float(input("Solute mass (g): "))
    calculate_percentage(density, volume_ml, solute_mass)

else:
    print("Invalid choice. Enter 1, 2, or 3.")

