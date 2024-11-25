#include <iostream>
#include <string>
using namespace std;

// Function to simulate FA for strings of the form a(a+b)*b
bool simulate_FA(const string& input_string) {
    if (input_string.empty()) {
        return false; // Reject empty strings
    }
    // Check if the string starts with 'a' and ends with 'b'
    return (input_string[0] == 'a' && input_string[input_string.length() - 1] == 'b');
}

int main() {
    // Test strings
    string test_strings[] = {"ab", "aabb", "abab", "b", "aaab", "bb", "abc"};

    cout << "Strings of the form a(a+b)*b:" << endl;

    for (const string& test : test_strings) {
        cout << "Input: " << test << " => " << (simulate_FA(test) ? "Accepted" : "Rejected") << endl;
    }

    return 0;
