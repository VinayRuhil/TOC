def is_in_L1(string):
    # L1: Starts with 'a' and ends with 'b'
    return string.startswith("a") and string.endswith("b")

def is_in_L2(string):
    # L2: Even number of 'a's and 'b's
    a_count = string.count("a")
    b_count = string.count("b")
    return a_count % 2 == 0 and b_count % 2 == 0

def union_L1_L2(string):
    return is_in_L1(string) or is_in_L2(string)

# Test Union
test_string = input("Enter a string for UNION of L1 and L2: ")
print(f"Union Result: {union_L1_L2(test_string)}")







def intersection_L1_L2(string):
    return is_in_L1(string) and is_in_L2(string)

# Test Intersection
test_string = input("Enter a string for INTERSECTION of L1 and L2: ")
print(f"Intersection Result: {intersection_L1_L2(test_string)}")





def is_concatenation_L1_L2(string):
    # Check all possible splits of the string
    for i in range(1, len(string)):
        part1 = string[:i]  # First part
        part2 = string[i:]  # Second part
        if is_in_L1(part1) and is_in_L2(part2):
            return True
    return False

# Test Concatenation
test_string = input("Enter a string for CONCATENATION of L1 and L2: ")
print(f"Concatenation Result: {is_concatenation_L1_L2(test_string)}")
