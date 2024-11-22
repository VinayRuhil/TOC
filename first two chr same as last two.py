def simulate_fa(input_string):
    # Ensure the string has a minimum length of 4
    if len(input_string) < 4:
        return False

    # Process the string
    first_two = input_string[:2]  # First two characters
    last_two = input_string[-2:]  # Last two characters

    # Check if first two match the last two
    return first_two == last_two

# Take input from the user
user_input = input("Enter a string over {a, b}: ")
if all(char in {'a', 'b'} for char in user_input):
    result = simulate_fa(user_input)
    print(f"Input: {user_input}, Accepts: {result}")
else:
    print("Invalid input! Please enter a string containing only 'a' and 'b'.")
