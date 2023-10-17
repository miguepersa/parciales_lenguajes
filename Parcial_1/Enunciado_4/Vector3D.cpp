#include "Vector3D.h"

Vector3D::Vector3D()
{
    x = 0;
    y = 0;
    z = 0;
}

Vector3D::Vector3D(int a, int b, int c)
{
    x = a;
    y = b;
    z = c;
}

Vector3D::~Vector3D()
{

}

void Vector3D::setX(int in)
{
    x = in;
}
int Vector3D::getX()
{
    return x;
}
void Vector3D::setY(int in)
{
    y = in;
}
int Vector3D::getY()
{
    return y;
}
void Vector3D::setZ(int in)
{
    z = in;
}
int Vector3D::getZ()
{
    return z;
}

Vector3D Vector3D::operator+(Vector3D const &other)
{
    Vector3D out(x + other.x, y + other.y, z + other.z);
    return out;
}

Vector3D Vector3D::operator*(Vector3D const &other)
{
    // Formula: https://es.khanacademy.org/math/multivariable-calculus/thinking-about-multivariable-function/x786f2022:vectors-and-matrices/a/cross-products-mvc#:~:text=tiene%20ninguna%20ambig%C3%BCedad.-,La,-f%C3%B3rmula%20no%20tan
    Vector3D out(y * other.z - z * other.y, z * other.x - x * other.z, x * other.y - y * other.x);
    return out;
}

Vector3D Vector3D::operator*(int e)
{
    Vector3D out(e * x, e * y, e * z);
    return out;
}

Vector3D Vector3D::operator*(float e)
{
    Vector3D out(e * x, e * y, e * z);
    return out;
}

Vector3D Vector3D::operator+(int e)
{
    Vector3D out(x + e, y + e, z + e);
    return out;
}

Vector3D Vector3D::operator+(float e)
{
    Vector3D out(x + e, y + e, z + e);
    return out;
}

Vector3D Vector3D::operator-(int e)
{
    Vector3D out(x - e, y - e, z - e);
    return out;
}

Vector3D Vector3D::operator-(float e)
{
    Vector3D out(x - e, y - e, z - e);
    return out;
}


Vector3D Vector3D::operator-(Vector3D const &other)
{
    Vector3D out(x - other.x, y - other.y, z - other.z);
    return out;
}

int Vector3D::operator%(Vector3D const &other)
{
    int out = x * other.x + y * other.y + z * other.z;
    return out;
}

ostream & operator<<(ostream &s , Vector3D v)
{
    s << "[" << v.getX() << ", " << v.getY() << ", " << v.getZ() << "]";
    return s;
}

Vector3D operator*(float e, Vector3D v)
{
    Vector3D out(e * v.getX(), e * v.getY(), e * v.getZ());
    return out;
}

float operator&(Vector3D v)
{
    float n = (v.getX() * v.getX()) + (v.getY() * v.getY()) + (v.getZ() * v.getZ());
    return sqrt(n);
}