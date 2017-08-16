"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_c_to_f(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            # TODO: Write this section to convert F to C and display the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            fahrenheit = float(input("Farenheit"))
            celsius = convert_f_to_c(fahrenheit)
            print("Result: {:2f} C".format(celsius))
            # Remove the "pass" statement when you are done. It's a placeholder.

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_f_to_c(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


def convert_c_to_f(celsius):
    return celsius * 9.0 / 5 + 32


main()
