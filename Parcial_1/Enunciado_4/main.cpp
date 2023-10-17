#include "Vector3D.h"

using namespace std;

int main(int argc, char const *argv[])
{
    Vector3D vector1(2,1,3);
    Vector3D vector2(5,2,2);

    Vector3D out = vector1 + vector2 + vector1;

    cout << "a: (2,1,3) // b: (5,2,2)" << endl << endl;
    cout << "a + b + a = " << out << endl;
    cout << "(a + b + a) * 5 = " << out * 5 << endl;
    cout << "2 * (a + b + a) = " << 2 * out << endl;
    cout << "(a + b + a) - b = " << out - vector2 << endl;
    cout << "(a + a) * (b - a) = " << (vector1 + vector1) * (vector2 - vector1) << endl;
    cout << "a * (a % b) = " << vector1 * (vector1 % vector2) << endl;
    cout << "&a = " << &vector1 << endl;
    cout << "a - 1 = " << vector1 - 1 << endl;
    cout << "b + 5 = " << vector2 + 5 << endl;

    return 0;
}
