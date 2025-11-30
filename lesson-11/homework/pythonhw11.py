# ===========================================================================================================
# I can't upload modules, packages and virtual environment at once, so i write steps of creating them!!!!!!!!
# ===========================================================================================================




# Task 1. Create your own virtual environment and install some python packages.

    # Step-1. Opening virtuel environment
    # In terminal(Ctrl+Shift+`) for true file path write: python -m venv env_name
    # For-example:
    # PS C:\Users\user\OneDrive\Documents\Python> python -m venv my_env

    # Step-2. Activating it.
    # Open cmd in Terminam then go into the venv file with entering complete file path and activate
    # For-Example:
    # PS C:\Users\user\OneDrive\Documents\Python>\Lesson-11\my_env\Scripts\activate

    # Step-3. Installing packages.
    # Then type there: pip install package/module name.
    # For-Example.
    # PS C:\Users\user\OneDrive\Documents\Python>pip install pandas
    # it downloads pandas
    # PS C:\Users\user\OneDrive\Documents\Python>pip install matplotilb
    # it downloads matplotilb
    # PS C:\Users\user\OneDrive\Documents\Python>pip install numpy
    # it downloads numpy

    # Step-4. Checking.
    # For checking if packages installed type: python there, and write your code
    # For-Example.
    # C:\Users\user\OneDrive\Documents\Python>python
    # Python 3.13.8 (tags/v3.13.8:a15ae61, Oct  7 2025, 12:34:25) [MSC v.1944 64 bit (AMD64)] on win32
    # Type "help", "copyright", "credits" or "license" for more information.
    # Ctrl click to launch VS Code Native REPL
    # >>> import pandas as p
    # >>> data = {"Name": ["Ali", "Vali"], "Age": [17, 18]}
    # >>> df = pd.DataFrame(data)
    # >>> print(df)

# Task 2.Create custom modules.
# I opened two python(.py) files in explorer.

    # In math.operations.py file has this functions:

def add(num1 : float, num2 : float) -> float:
    return float(num1) + float(num2)

def subtract(num1 : float, num2 : float) -> float:
    return float(num1) - float(num2)

def multiplication(num1 : float, num2 : float) -> float:
    return float(num1) * float(num2)

def division(num1 : float, num2 : float) -> float:
    return float(num1) / float(num2)

    # In string.utils.py file has this funkstions.

def reverse_string(your_string : str) -> str:
    return f"Reversed form of your string: {your_string[::-1]}"

def count_vowels(your_string: str) -> str:
    vowels = "aeiou"
    count = sum(your_string.lower().count(v) for v in vowels)
    return f"Count of vowels in your string: {count}"

# Task 3.Create custom packages.
# I opened two(geometry, file_operations) and opened two __init__.py file for each, and several functions.

    # In circle.py file has this functions.

from math import pi

def calculate_area(radius : float) -> float:
    areaa = pi * radius ** 2
    return f"Area of the circle with the radius you gave: {areaa}"

def calculate_circumference(radius : float)-> float:
    circumfrace = 2 * pi * radius
    return f"Circumfrace of the circle with the radius you gave: {circumfrace}"

    # In file_reader.py file has this function.
    
def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()
    
    # In file_writer.py file has this function.

def write_file(file_path, content : str):
    with open(file_path, 'w') as f:
        f.write(content)
        return f"File opened to write from {file_path} and {content} was added to it"

