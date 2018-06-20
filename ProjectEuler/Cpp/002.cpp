#include <iostream>

using namespace std;

int main()
{
    int a = 1;
    int b = 2;
    int total = 0;

    while (b <= 4000000)
    {
        if (b % 2 == 0)
        {
            total += b;
        }
        b += a;
        a = b - a;
    }
    cout << total << endl;
}