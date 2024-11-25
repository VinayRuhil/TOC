#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool simulateMachine(const string& input) {
    stack<char> st; // Stack to store 'w'
    size_t len = input.length();
    size_t posX = input.find('X');

    if (posX == string::npos) {
        return false; // No 'X' found, invalid string
    }

    // Process the first part (w)
    for (size_t i = 0; i < posX; ++i) {
        if (input[i] == 'a' || input[i] == 'b') {
            st.push(input[i]); // Push characters of w onto the stack
        } else {
            return false; // Invalid character
        }
    }

    // Process the second part (w^R)
    for (size_t i = posX + 1; i < len; ++i) {
        if (st.empty() || input[i] != st.top()) {
            return false; // Mismatch between w and w^R
        }
        st.pop(); 
    }

    // String is accepted if the stack is empty after processing
    return st.empty();
}

int main() {
    string testCases[] = {
        "aXa", "abXba", "abbXbba", "aabbXbbaa", "abXab", "aX", "X", "abXa"
    };

    for (const string& test : testCases) {
        cout << "Input: \"" << test << "\" -> "
             << (simulateMachine(test) ? "Accepted" : "Rejected") << endl;
    }

    return 0;
}
