# Temperature Conversion Program

A Python-based temperature conversion program developed as part of the Prodigy Infotech Software Development Internship - Task 01.

## Project Overview

This program converts temperatures between three commonly used temperature scales:

- Celsius (°C)
- Fahrenheit (°F)
- Kelvin (K)

The user enters a temperature value and specifies the original unit. The program then converts the temperature into the other two units and displays all three values.

## Features

- Convert Celsius to Fahrenheit and Kelvin
- Convert Fahrenheit to Celsius and Kelvin
- Convert Kelvin to Celsius and Fahrenheit
- Accepts both uppercase and lowercase unit inputs
- Validates invalid temperature units
- Prevents temperatures below 0 Kelvin
- Handles decimal temperature values
- Displays results rounded to two decimal places

## Conversion Formulas

### Celsius

- Fahrenheit = (Celsius × 9/5) + 32
- Kelvin = Celsius + 273.15

### Fahrenheit

- Celsius = (Fahrenheit - 32) × 5/9
- Kelvin = (Fahrenheit - 32) × 5/9 + 273.15

### Kelvin

- Celsius = Kelvin - 273.15
- Fahrenheit = (Kelvin - 273.15) × 9/5 + 32

## Technologies Used

- Python 3
- Google Colab for development and testing
- GitHub for version control and project management

## How to Run

1. Make sure Python 3 is installed on your system.
2. Download or clone this repository.
3. Open `temperature_converter.py`.
4. Run the program.
5. Enter the temperature value.
6. Enter the original unit using:
   - `C` for Celsius
   - `F` for Fahrenheit
   - `K` for Kelvin

## Sample Input

```text
Enter temperature: 25
Enter original unit (C/F/K): C

## Testing

The program was tested using all three supported temperature units.

### Test 1: Celsius

Input:
- Temperature: 25
- Unit: C

Output:
- Celsius: 25.00 °C
- Fahrenheit: 77.00 °F
- Kelvin: 298.15 K

### Test 2: Fahrenheit

Input:
- Temperature: 32
- Unit: F

Output:
- Celsius: 0.00 °C
- Fahrenheit: 32.00 °F
- Kelvin: 273.15 K

### Test 3: Kelvin

Input:
- Temperature: 273.15
- Unit: K

Output:
- Celsius: 0.00 °C
- Fahrenheit: 32.00 °F
- Kelvin: 273.15 K

All three conversion tests produced the expected results.

## Project Status

Task 01 completed successfully as part of the Prodigy Infotech Software Development Internship.
