#include <iostream>
 #include <string>
 using namespace std;
 // Function to simulate the Turing Machine
 bool simulateTuringMachine(string tape) {
    size_t head = 0;
    while (true) {
        // Step 1: Mark the first unmarked 'a'
        while (head < tape.size() && tape[head] != 'a') {
            if (tape[head] != 'X' && tape[head] != 'b' && tape[head] != 'Y' && tape[head] != 'c' && 
tape[head] != 'Z') {
                return false; // Invalid character found
            }
            head++;
        }
        if (head >= tape.size()) break;
        tape[head] = 'X'; 
        head++;
        // Step 2: Find and mark the first unmarked 'b'
        while (head < tape.size() && tape[head] != 'b') {
            if (tape[head] != 'Y' && tape[head] != 'c' && tape[head] != 'Z') {
                return false; // Invalid character or order
            }
            head++;
        }
        if (head >= tape.size()) return false; 
        tape[head] = 'Y'; 
        head++;
        // Step 3: Find and mark the first unmarked 'c'
        while (head < tape.size() && tape[head] != 'c') {
            if (tape[head] != 'Z') {
                return false; // Invalid character or order
            }
            head++;
        }
        if (head >= tape.size()) return false;
        tape[head] = 'Z';
        head = 0;
    }
    for (char ch : tape) {
        if (ch != 'X' && ch != 'Y' && ch != 'Z') {
            return false; 
        }
    }
    return true; 
}
 int main() {
    string testCases[] = {"abc", "aabbcc", "aaabbbccc", "abccba", "aabbc", "abcabc", ""};
    for (const string& test : testCases) {
        cout << "Input: \"" << test << "\" -> "
             << (simulateTuringMachine(test) ? "Accepted" : "Rejected") << endl;
    }
    return 0;
 }
