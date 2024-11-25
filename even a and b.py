
#include <iostream>
#include <string>
using namespace std;


bool simulate_FA(const string& input_string) {
    int count_a = 0, count_b = 0;

    for (char c : input_string) {
        if (c == 'a') {
            count_a++;
        } else if (c == 'b') {
            count_b++;
        }
    }

    return (count_a % 2 == 0 && count_b % 2 == 0);
}

int main() {
 
    string test_strings[] = {"ab", "aabb", "bbaa", "aab", "abab", "aaa", "bb"};

    cout << "Strings with even number of 'a's and even number of 'b's:" << endl;

    for (const string& test : test_strings) {
        cout << "Input: " << test << " => " << (simulate_FA(test) ? "Accepted" : "Rejected") << endl;
    }

    return 0;
}
