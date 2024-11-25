#include <iostream>
 #include <string>
 using namespace std;

 bool simulate_FA(const string& input_string) {
 int count = 0;
 for (char c : input_string) {
        if (c == '1') {
            count++;
        }
    }
    return (count == 2 || count == 3);
 }
 int main() {
   
    string test_strings[] = {"110", "111", "10101", "10001", "111111", "00101"};
    cout << "Strings with exactly two or exactly three 1's:" << endl;
    for (const string& test : test_strings) {
        cout << "Input: " << test << " => " << (simulate_FA(test) ? "Accepted" : 
"Rejected") << endl;
    }
    return 0;
 }
