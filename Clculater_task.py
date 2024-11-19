# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kjeSpI03lQJNziXnUfsz_7whWGb8Gh92
"""

def simple_calculator():
    while True:
        print("\n=== Simple Calculator ===")
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        user_choice = input("Enter your choice (1-5): ")

        if user_choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        try:
            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))

            if user_choice == '1':
                addition_result = first_number + second_number
                print(f"The result of addition is: {addition_result}")
            elif user_choice == '2':
                subtraction_result = first_number - second_number
                print(f"The result of subtraction is: {subtraction_result}")
            elif user_choice == '3':
                multiplication_result = first_number * second_number
                print(f"The result of multiplication is: {multiplication_result}")
            elif user_choice == '4':
                if second_number != 0:
                    division_result = first_number / second_number
                    print(f"The result of division is: {division_result}")
                else:
                    print("Error: Division by zero is not allowed.")
            else:
                print("Invalid operation choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")


simple_calculator()