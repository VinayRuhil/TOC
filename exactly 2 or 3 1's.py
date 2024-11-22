def simulate_fa(input_string):
    # States
    q0, q1, q2, q3, q4 = 0, 1, 2, 3, 4
    current_state = q0  # Start at the initial state

    # Transition function
    for char in input_string:
        if char == '0':
            # Stay in the same state for input 0
            pass
        elif char == '1':
            if current_state == q0:
                current_state = q1
            elif current_state == q1:
                current_state = q2
            elif current_state == q2:
                current_state = q3
            elif current_state == q3:
                current_state = q4
            elif current_state == q4:
                current_state = q4  # Stay in reject state
        else:
            # Invalid input
            return False

    # Check if we are in an accepting state
    return current_state == q2 or current_state == q3

# Take input from the user
user_input = input("Enter a binary string (over {0, 1}): ")
if all(char in {'0', '1'} for char in user_input):
    result = simulate_fa(user_input)
    print(f"Input: {user_input}, Accepts: {result}")
else:
    print("Invalid input! Please enter a binary string containing only 0s and 1s.")
