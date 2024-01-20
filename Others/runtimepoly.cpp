#include <iostream>

class Base {
public:
    virtual void foo() {
        std::cout << "Base::foo\n";
    }
};

class Derived : public Base {
public:
    void foo() {
        std::cout << "Derived::foo\n";
    }
};

int main() {
    Base* b;
    Derived d;
    b=&d;
    b->foo();  // Output: Derived::foo
    return 0;
}