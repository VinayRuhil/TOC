def simulate_fa(input_string):
    # Start at the initial state
    state = "q0"

    for i, char in enumerate(input_string):
        if state == "q0":
            if char == "a":
                state = "q1"
            else:
                return False  # Reject if the string doesn't start with 'a'
        elif state == "q1":
            if char in {"a", "b"}:
                state = "q2"
        elif state == "q2":
            if char == "b" and i == len(input_string) - 1:  # Ensure 'b' is the last character
                state = "q3"
            elif char not in {"a", "b"}:
                return False  # Reject if any invalid character is found
        elif state == "q3":
            return False  # No further input is allowed after accepting

    # Check if we ended in the accepting state
    return state == "q3"

# Take input from the user
user_input = input("Enter a string over {a, b}: ")
if all(char in {"a", "b"} for char in user_input):
    result = simulate_fa(user_input)
    print(f"Input: {user_input}, Accepts: {result}")
else:
    print("Invalid input! Please enter a string containing only 'a' and 'b'.")
