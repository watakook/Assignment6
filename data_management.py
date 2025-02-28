#!/usr/bin/env python3
import sys
import cgi

# Get user input from URL parameters
form = cgi.FieldStorage()

try:
    numbers = [int(form.getvalue(x)) for x in ["a", "b", "c", "d", "e"]]

    # Check for negative values
    if any(n < 0 for n in numbers):
        print("Content-type: text/html\n")
        print("<h2>Error: Negative values are not allowed!</h2>")
        sys.exit()

    # Calculate average
    average = sum(numbers) / len(numbers)
    average_msg = f"<p>Average: {average}</p>"

    # Determine if count of positive numbers is even or odd using bitwise operation
    is_even = len([n for n in numbers if n > 0]) & 1 == 0
    even_odd_msg = "<p>The count of positive numbers is Even</p>" if is_even else "<p>The count is Odd</p>"

    # Create a new list with numbers greater than 10, sorted
    filtered_sorted = sorted([n for n in numbers if n > 10])
    sorted_msg = f"<p>Sorted Values: {filtered_sorted}</p>"

    # Display results
    print("Content-type: text/html\n")
    print("<h2>Results:</h2>")
    print(f"<p>Original Values: {numbers}</p>")
    print(average_msg)
    print(even_odd_msg)
    print(sorted_msg)

except Exception as e:
    print("Content-type: text/html\n")
    print("<h2>Error: Invalid Input</h2>")