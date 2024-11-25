#include <iostream>
#include <string>
using namespace std;

bool simulate_FA(const string& input_string) {
    if (input_string.length() < 4) {
        return false; // Rejected if length is less than 4
    }
    return (input_string[0] == input_string[input_string.length() - 2] && 
            input_string[1] == input_string[input_string.length() - 1]);
}

int main() {
    string test_strings[] = {"aabb", "abab", "baba", "abccba", "abcd", "bbaa"};

    cout << "Strings where the first two characters are the same as the last two:" << endl;

    for (const string& test : test_strings) {
        cout << "Input: " << test << " => " << (simulate_FA(test) ? "Accepted" : "Rejected") << endl;
    }

    return 0;
}
