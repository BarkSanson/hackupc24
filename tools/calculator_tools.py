from langchain.tools import tool

class CalculatorTools:
    
    @tool("Make a calculation")
    def calculate(operation):
        """
        Useful to perform any mathematical calculations, like sum, minus, multiplication, division, etc.
        The input should be a mathematical expression, e.g., `200*7` or `5000/2*10`.
        This tool can be used for travel budgeting or other numerical operations.
        
        Args:
            operation (str): A mathematical expression to evaluate.

        Returns:
            str: The result of the calculation.
        """
        allowed_chars = "0123456789+-*/(). "
        if all(c in allowed_chars for c in operation):
            try:
                return eval(operation)
            except Exception as e:
                return f"Error: {str(e)}"
        else:
            return "Error: Unsupported characters in mathematical expression"

# Example of an additional utility function for distance calculations
@tool("Calculate travel distance")
def calculate_travel_distance(distance_km, conversion_factor=0.621371):
    """
    Convert distance from kilometers to miles or other units.

    Args:
        distance_km (float): The distance in kilometers.
        conversion_factor (float): Conversion factor to miles (default: 0.621371).

    Returns:
        str: Converted distance.
    """
    try:
        distance_miles = distance_km * conversion_factor
        return f"The distance is {distance_miles:.2f} miles."
    except Exception as e:
        return f"Error: {str(e)}"
