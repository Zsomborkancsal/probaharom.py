# import module
import streamlit as st
 
# Title
st.title("Hello GeeksForGeeks !!!")
import streamlit as st
import math

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
        return "Cannot divide by zero."

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return x ** y

def trig_function(x, function):
    if function == "Sin":
        return math.sin(math.radians(x))
    elif function == "Cos":
        return math.cos(math.radians(x))
    elif function == "Tan":
        return math.tan(math.radians(x))

def main():
    st.title("Advanced Calculator")

    num1 = st.number_input("Enter first number")
    num2 = st.number_input("Enter second number")

    operation = st.selectbox("Select operation", (
        "Addition", "Subtraction", "Multiplication", "Division",
        "Square Root", "Power", "Sin", "Cos", "Tan"
    ))

    result = 0

    if operation in ("Addition", "Subtraction", "Multiplication", "Division", "Power"):
        if st.button("Calculate"):
            if operation == "Addition":
                result = add(num1, num2)
            elif operation == "Subtraction":
                result = subtract(num1, num2)
            elif operation == "Multiplication":
                result = multiply(num1, num2)
            elif operation == "Division":
                result = divide(num1, num2)
            elif operation == "Power":
                result = power(num1, num2)
    else:
        if st.button("Calculate"):
            if operation == "Square Root":
                result = square_root(num1)
            elif operation in ("Sin", "Cos", "Tan"):
                result = trig_function(num1, operation)

    st.write(f"Result: {result}")

if __name__ == "__main__":
    main()
