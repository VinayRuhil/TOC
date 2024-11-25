#include <iostream>
 #include <string>
 using namespace std;
 string incrementBinary(string tape) {
    int head = tape.length() - 1; // Start at the rightmost bit (LSB)
    while (head >= 0) {
        if (tape[head] == '0') {
            // If the current bit is 0, change it to 1 and halt
            tape[head] = '1';
            return tape;
        } else if (tape[head] == '1') {
            // If the current bit is 1, change it to 0 and move left
            tape[head] = '0';
        } else {
            // Invalid character in the tape
            throw invalid_argument("Invalid binary number");
        }
        head--; // Move the head left
    }
    return "1" + tape;
 }
 int main() {
    string testCases[] = {"0", "1", "10", "11", "101", "111", "1000", ""};
    for (const string& test : testCases) {
        try {
cout << "Input: \"" << test << "\" -> Output: \"" << incrementBinary(test) << "\"" << endl;
 } catch (const invalid_argument& e) {
 cout << "Input: \"" << test << "\" -> Error: " << e.what() << endl;
 }
 }
 return 0;
 }
