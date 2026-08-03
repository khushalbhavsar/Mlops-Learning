# What is Exception Handling in Python?
# Exception handling is a mechanism in Python that allows you to handle runtime errors gracefully.
# It enables you to catch and respond to exceptions, preventing your program from crashing and allowing you to provide meaningful error messages or alternative actions.

# Exception Handling Keywords in Python
# | Keyword          | Short Explanation                                   |
# | ---------------- | --------------------------------------------------- |
# | `try`            | Contains code that may cause an exception           |
# | `except`         | Handles the exception                               |
# | `else`           | Executes if no exception occurs                     |
# | `finally`        | Always executes, whether an exception occurs or not |
# | `raise`          | Manually raises an exception                        |
# | `Exception as e` | Captures the exception object and its message       |


# ==========================================
# Python Exception Handling - One Complete Example
# ==========================================

# ------------------------------------------
# 1. Create a Custom Exception Class
# ------------------------------------------
class InvalidAgeError(Exception):
    pass


# Dictionary and List
student = {
    "name": "Khushal",
    "age": 22
}

numbers = [10, 20, 30]


try:
    # ------------------------------------------
    # 2. Handle Invalid Integer Input
    # ------------------------------------------
    num = int(input("Enter a number: "))

    # ------------------------------------------
    # 3. Handle Division by Zero
    # ------------------------------------------
    result = 100 / num
    print("Division Result:", result)

    # ------------------------------------------
    # 4. Handle File Not Found
    # ------------------------------------------
    file = open("data.txt", "r")
    print(file.read())
    file.close()

    # ------------------------------------------
    # 5. Handle Index Error
    # ------------------------------------------
    print("List Value:", numbers[5])

    # ------------------------------------------
    # 6. Handle Key Error
    # ------------------------------------------
    print("City:", student["city"])

    # ------------------------------------------
    # 7. Raise a Custom Exception
    # ------------------------------------------
    age = -5

    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

# ------------------------------------------
# 8. Catch Multiple Exceptions
# ------------------------------------------
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except FileNotFoundError:
    print("Error: File not found.")

except ValueError:
    print("Error: Please enter a valid integer.")

except IndexError:
    print("Error: List index out of range.")

except KeyError:
    print("Error: Key does not exist.")

except InvalidAgeError as e:
    print("Custom Exception:", e)

except Exception as e:
    print("Unexpected Error:", e)

# ------------------------------------------
# 9. else -> Executes if no exception occurs
# ------------------------------------------
else:
    print("Everything executed successfully.")

# ------------------------------------------
# 10. finally -> Always executes
# ------------------------------------------
finally:
    print("Program Finished.")