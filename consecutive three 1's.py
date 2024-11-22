def simulate_fa(input_string):
    # States
    q0, q1, q2, q3 = 0, 1, 2, 3
    current_state = q0  # Start at the initial state
    
    # Transition function
    for char in input_string:
        if current_state == q0:
            if char == '1':
                current_state = q1
        elif current_state == q1:
            if char == '1':
                current_state = q2
            elif char == '0':
                current_state = q0
        elif current_state == q2:
            if char == '1':
                current_state = q3
            elif char == '0':
                current_state = q0
        elif current_state == q3:
            # Stay in the accepting state
            current_state = q3
    
    # Check if we are in the accepting state
    return current_state == q3

# Take input from the user
user_input = input("Enter a binary string (over {0, 1}): ")
if all(char in {'0', '1'} for char in user_input):
    result = simulate_fa(user_input)
    print(f"Input: {user_input}, Accepts: {result}")
else:
    print("Invalid input! Please enter a binary string containing only 0s and 1s.")
