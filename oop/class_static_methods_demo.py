
class Calculator:
    """
    A class demonstrating the difference between static methods and class methods.
    """
    # Class Attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method to calculate the sum of two numbers.
        It does not take 'self' or 'cls' and cannot access class or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method to calculate the product of two numbers.
        It takes 'cls' as the first argument, allowing it to access class attributes.
        """
        # Accessing the class attribute 'calculation_type' using the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# End of class_static_methods_demo.py
