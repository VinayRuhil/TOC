#include <iostream>
#include <stack>
#include <string>

using namespace std;

// Function to check if the string is accepted by the PDA
bool simulatePDA(const string& input) {
    stack<char> st;
    st.push('Z'); // Push initial stack symbol

    int i = 0;
    while (i < input.length()) {
        char current = input[i];
        
        if (current == 'a') {
            st.push('A'); // Push 'A' for each 'a'
        } else if (current == 'b') {
            if (!st.empty() && st.top() == 'A') {
                st.pop(); // Pop 'A' for each 'b'
            } else {
                return false; // If stack is empty or top is not 'A', reject
            }
        } else {
            return false; // Reject if character is not 'a' or 'b'
        }
        i++;
    }

    // After processing input, check if stack has only the initial symbol
    return st.size() == 1 && st.top() == 'Z';
}

int main() {
    string input;
    cout << "Enter a string (only 'a' and 'b'): ";
    cin >> input;

    // Check if input contains at least one 'a' and 'b'
    if (input.empty() || input.find('a') == string::npos || input.find('b') == string::npos) {
        cout << "Rejected: Input must contain at least one 'a' and one 'b'.\n";
        return 0;
    }

    if (simulatePDA(input)) {
        cout << "Accepted: The string belongs to the language {a^n b^n | n > 0}.\n";
    } else {
        cout << "Rejected: The string does not belong to the language.\n";
    }

    return 0;
}
