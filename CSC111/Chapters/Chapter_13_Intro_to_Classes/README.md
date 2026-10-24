# Chapter 13: Introduction to Classes

This chapter introduces classes and objects, data members, member functions,
constructors, and encapsulation.

## Learning path

- [ ] Read the [Chapter 13 PDF](./Chapter_13.pdf).
- [ ] Complete the checklist below.
- [ ] Finish the [Chapter 13 assignment](../../Assignments/README.md#12-chapter-13--bank-account-class).

<details>
<summary>Open the checklist</summary>

- [ ] Define a class with private data.
- [ ] Write public member functions.
- [ ] Initialize objects with a constructor.
- [ ] Protect object state through validation.
- [ ] Explain the difference between a class and an object.

</details>

## Try it

```cpp
#include <iostream>

class Counter {
public:
    void increment() {
        ++value;
    }

    int get() const {
        return value;
    }

private:
    int value = 0;
};

int main() {
    Counter counter;
    counter.increment();
    std::cout << counter.get() << '\n';
}
```

<details>
<summary>Show the result</summary>

The program prints `1`. The `value` member is private and can only be changed
through the class interface.

</details>

## Continue

- [Previous: Chapter 11 — Structured Data](../Chapter_11_Structured_Data/)
- [Next: Chapter 20 — Recursion Intro](../Chapter_20_Recursion_Intro/)
- [All chapters](../README.md)
