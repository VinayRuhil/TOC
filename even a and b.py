def simulate_fa(input_string):
    # Define states
    q00, q01, q10, q11 = "q00", "q01", "q10", "q11"
    current_state = q00  # Start at the initial state

    # Transition function
    for char in input_string:
        if char == "a":
            if current_state == q00:
                current_state = q10
            elif current_state == q01:
                current_state = q11
            elif current_state == q10:
                current_state = q00
            elif current_state == q11:
                current_state = q01
        elif char == "b":
            if current_state == q00:
                current_state = q01
            elif current_state == q01:
                current_state = q00
            elif current_state == q10:
                current_state = q11
            elif current_state == q11:
                current_state = q10
        else:
            # Invalid input
            return False

    # Check if the final state is accepting
    return current_state == q00

# Take input from the user
user_input = input("Enter a string over {a, b}: ")
if all(char in {"a", "b"} for char in user_input):
    result = simulate_fa(user_input)
    print(f"Input: {user_input}, Accepts: {result}")
else:
    print("Invalid input! Please enter a string containing only 'a' and 'b'.")
