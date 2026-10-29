def calculate_energy_charge(units):
    """Calculate slab-wise electricity energy charges."""
    if units < 0:
        raise ValueError("Units cannot be negative.")

    if units <= 100:
        return units * 3
    elif units <= 200:
        return (100 * 3) + ((units - 100) * 5)
    else:
        return (100 * 3) + (100 * 5) + ((units - 200) * 8)


def generate_bill(consumer_name, units):
    """Calculate and return the bill components."""
    energy_charge = calculate_energy_charge(units)
    fixed_charge = 50.00
    tax = (energy_charge + fixed_charge) * 0.05
    total_bill = energy_charge + fixed_charge + tax

    return {
        "consumer_name": consumer_name,
        "units": units,
        "energy_charge": energy_charge,
        "fixed_charge": fixed_charge,
        "tax": tax,
        "total_bill": total_bill,
    }


def main():
    print("=" * 44)
    print("        ELECTRICITY BILL CALCULATOR")
    print("=" * 44)

    consumer_name = input("Enter consumer name: ").strip()
    if not consumer_name:
        consumer_name = "Customer"

    try:
        units = float(input("Enter units consumed: ").strip())
        if units < 0:
            print("Invalid units. Enter a non-negative number.")
            return
    except ValueError:
        print("Invalid units. Enter a non-negative number.")
        return

    bill = generate_bill(consumer_name, units)

    print("\n--------------- ELECTRICITY BILL ---------------")
    print(f"Consumer Name : {bill['consumer_name']}")
    print(f"Units Consumed: {bill['units']:g}")
    print(f"Energy Charge : Rs. {bill['energy_charge']:.2f}")
    print(f"Fixed Charge  : Rs. {bill['fixed_charge']:.2f}")
    print(f"Tax (5%)      : Rs. {bill['tax']:.2f}")
    print("-" * 49)
    print(f"TOTAL BILL    : Rs. {bill['total_bill']:.2f}")
    print("------------------------------------------------")


if __name__ == "__main__":
    main()
