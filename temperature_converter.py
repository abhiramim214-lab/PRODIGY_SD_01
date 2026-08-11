def convert_temperature(temperature, unit):
    """
    Convert a temperature from the given unit to the other two units.
    Supported units: Celsius (C), Fahrenheit (F), Kelvin (K)
    """

    unit = unit.upper()

    if unit == "C":
        celsius = temperature
        fahrenheit = (temperature * 9 / 5) + 32
        kelvin = temperature + 273.15

    elif unit == "F":
        fahrenheit = temperature
        celsius = (temperature - 32) * 5 / 9
        kelvin = celsius + 273.15

    elif unit == "K":
        if temperature < 0:
            raise ValueError("Kelvin temperature cannot be below 0 K.")

        kelvin = temperature
        celsius = temperature - 273.15
        fahrenheit = (celsius * 9 / 5) + 32

    else:
        raise ValueError("Invalid unit. Please use C, F, or K.")

    return celsius, fahrenheit, kelvin


def main():
    print("=" * 40)
    print("      TEMPERATURE CONVERTER")
    print("=" * 40)

    try:
        temperature = float(input("Enter temperature: "))
        unit = input("Enter original unit (C/F/K): ").strip()

        celsius, fahrenheit, kelvin = convert_temperature(
            temperature, unit
        )

        print("\nConversion Results")
        print("-" * 40)
        print(f"Celsius:    {celsius:.2f} °C")
        print(f"Fahrenheit: {fahrenheit:.2f} °F")
        print(f"Kelvin:     {kelvin:.2f} K")

    except ValueError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()
