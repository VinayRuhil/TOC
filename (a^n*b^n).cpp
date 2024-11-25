#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool simulatePDA(const string& input) {
    stack<char> st;         // Stack for the PDA
    string state = "q0";    // Start state

    for (char c : input) {
        if (state == "q0") {
            if (c == 'a') {
                st.push('a'); // Push 'a' onto the stack
            } else if (c == 'b') {
                if (!st.empty()) {
                    state = "q1"; // Transition to state q1
                    st.pop();     // Pop 'a' for the first 'b'
                } else {
                    return false; // Rejected: unmatched 'b'
                }
            } else {
                return false; // Rejected: Invalid character
            }
        } else if (state == "q1") {
            if (c == 'b') {
                if (!st.empty()) {
                    st.pop(); // Pop 'a' for each 'b'
                } else {
                    return false; // Rejected: unmatched 'b'
                }
            } else {
                return false; // Rejected: 'a' not allowed in state q1
            }
        }
    }

    // Accepted if in state q1 and stack is empty
    return state == "q1" && st.empty();
}

int main() {
    string testCases[] = {"ab", "aabb", "aaabbb", "aaaabbbb", "abb", "aab", "ba", ""};

    for (const string& test : testCases) {
        cout << "Input: \"" << test << "\" -> "
             << (simulatePDA(test) ? "Accepted" : "Rejected") << endl;
    }

    return 0;
}
