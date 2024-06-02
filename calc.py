import streamlit as st
import math

# Define the operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def log(x):
    return math.log(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

# Title of the app
st.title("Mike's Calculator")

# Sidebar for advanced operations
with st.sidebar:
    
    st.write("welcome to Mike's calculator")
    st.header("Here is the list of advanced operations")
    st.markdown("""
        - Power: x^y
        - Square Root: √x
        - Logarithm: log(x)
        - Trigonometric functions: sin, cos, tan
    """)
    

# User input for numbers
num1 = st.number_input("Enter first number", format="%.2f")
operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide", "Power", "Square Root", "Logarithm", "Sin", "Cos", "Tan"))

if operation not in ["Square Root", "Logarithm", "Sin", "Cos", "Tan"]:
    num2 = st.number_input("Enter second number", format="%.2f", key='num2')
else:
    num2 = None

# Perform the calculation
result = None
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    elif operation == "Power":
        result = power(num1, num2)
    elif operation == "Square Root":
        result = sqrt(num1)
    elif operation == "Logarithm":
        result = log(num1)
    elif operation == "Sin":
        result = sin(num1)
    elif operation == "Cos":
        result = cos(num1)
    elif operation == "Tan":
        result = tan(num1)

    st.write(f"The result is: {result}")

# Adding a history of calculations
if 'history' not in st.session_state:
    st.session_state.history = []

if result is not None:
    st.session_state.history.append(f"{num1} {operation} {num2 if num2 is not None else ''} = {result}")

st.header("Calculation History")
st.write("\n".join(st.session_state.history))
