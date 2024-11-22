#include <iostream>
#include <stack>
#include <string>

using namespace std;

// Function to simulate the PDA
bool simulatePDA(const string& input) {
    stack<char> st;
    int n = input.size();
    int i = 0;

    // Read w and push to stack
    while (i < n && input[i] != 'X') {
        if (input[i] == 'a' || input[i] == 'b') {
            st.push(input[i]);
        } else {
            return false; // Invalid character
        }
        i++;
    }

    // Check if X is present
    if (i == n || input[i] != 'X') {
        return false;
    }
    i++; // Skip the X

    // Read w^r and pop from stack
    while (i < n) {
        if (st.empty() || (input[i] != st.top())) {
            return false; // Mismatch or stack empty prematurely
        }
        st.pop();
        i++;
    }

    // Accept if stack is empty
    return st.empty();
}

int main() {
    string input;
    cout << "Enter a string (format wXwr where w is over {a, b}): ";
    cin >> input;

    if (simulatePDA(input)) {
        cout << "Accepted: The string belongs to the language {wXwr | w is any string over {a, b}}.\n";
    } else {
        cout << "Rejected: The string does not belong to the language.\n";
    }

    return 0;
}
