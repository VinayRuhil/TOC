#include <iostream>
#include <string>
using namespace std;

// Function to simulate FA for Language L1 (starts with 'a' and ends with 'b')
bool simulate_L1(const string& input_string) {
    if (input_string.length() < 2) {
        return false; // Rejected if string length is less than 2
    }
    return (input_string[0] == 'a' && input_string[input_string.length() - 1] == 'b');
}

// Function to simulate FA for Language L2 (contains at least one 'a')
bool simulate_L2(const string& input_string) {
    return (input_string.find('a') != string::npos); // 'a' is present in the string
}

// Function to simulate Union of L1 and L2
bool simulate_union(const string& input_string) {
    return simulate_L1(input_string) || simulate_L2(input_string); // Accepted if either L1 or L2 accepts the string
}

// Function to simulate Intersection of L1 and L2
bool simulate_intersection(const string& input_string) {
    return simulate_L1(input_string) && simulate_L2(input_string); // Accepted if both L1 and L2 accept the string
}

// Function to simulate Concatenation of L1 and L2
bool simulate_concatenation(const string& input_string) {
    for (size_t i = 1; i < input_string.length(); i++) {
        string part1 = input_string.substr(0, i);
        string part2 = input_string.substr(i);

        // Check if part1 is accepted by L1 and part2 is accepted by L2
        if (simulate_L1(part1) && simulate_L2(part2)) {
            return true; // Accepted if concatenation of valid L1 and L2 parts
        }
    }
    return false; // Rejected if no valid split is found
}

int main() {
    // Test strings
    string test_strings[] = {"ab", "aab", "ba",  "a", "baa", "bb"};
    
    cout << "Union of L1 and L2:" << endl;
    for (const string& test : test_strings) {
        cout << "Input: " << test << " => " << (simulate_union(test) ? "Accepted" : "Rejected") << endl;
    }

    cout << "\nIntersection of L1 and L2:" << endl;
    for (const string& test : test_strings) {
        cout << "Input: " << test << " => " << (simulate_intersection(test) ? "Accepted" : "Rejected") << endl;
    }

    cout << "\nConcatenation of L1 and L2:" << endl;
    for (const string& test : test_strings) {
        cout << "Input: " << test << " => " << (simulate_concatenation(test) ? "Accepted" : "Rejected") << endl;
    }

    return 0;
}
