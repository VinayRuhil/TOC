#include <iostream>
#include <string>
using namespace std;


bool simulate_FA(const string& input_string) {
    if (input_string.empty()) {
        return false; 
    }
    return (input_string[0] == 'a' && input_string[input_string.length() - 1] == 'b');
}

int main() {
  
    string test_strings[] = {"ab", "aabb", "abab", "b", "aaab", "bb", "abc"};

    cout << "Strings of the form a(a+b)*b:" << endl;

    for (const string& test : test_strings) {
        cout << "Input: " << test << " => " << (simulate_FA(test) ? "Accepted" : "Rejected") << endl;
    }

    return 0;
