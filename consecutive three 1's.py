#include <iostream>
 #include <string>
 using namespace std;

 bool simulate_FA(const string& input_string) {
    for (size_t i = 0; i < input_string.length() - 2; ++i) {
        if (input_string[i] == '1' && input_string[i+1] == '1' && input_string[i+2] == '1') {
            return true;
        }
    }
    return false;
 }
 int main() {
    // Test strings
    string test_strings[] = {"111", "011", "101", "111111", "010101", "10001"};
    cout << "Strings with three consecutive 1's:" << endl;
    for (const string& test : test_strings) {
        cout << "Input: " << test << " => " << (simulate_FA(test) ? "Accepted" : "Rejected") << endl;
    }
    return 0;}

