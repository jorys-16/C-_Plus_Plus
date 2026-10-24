# Chapter 3: Expressions and Interactivity

This chapter covers variables, constants, data types, arithmetic expressions,
formatted output, and reading input from the user.

## Learning path

- [ ] Read the [Chapter 3 PDF](./Chapter_03.pdf).
- [ ] Complete the checklist below.
- [ ] Finish the [Chapter 3 assignment](../../Assignments/README.md#3-chapter-3--interactive-receipt).

<details>
<summary>Open the checklist</summary>

- [ ] Declare variables using appropriate data types.
- [ ] Read values with `std::cin`.
- [ ] Build arithmetic expressions with the correct order of operations.
- [ ] Format output with labels and meaningful precision.

</details>

## Try it

```cpp
#include <iostream>

int main() {
    double price;
    int quantity;
    std::cin >> price >> quantity;
    std::cout << "Total: $" << price * quantity << '\n';
}
```

<details>
<summary>Try an input example</summary>

Input `12.50 3` should produce a total of `$37.5`.

</details>

## Continue

- [Previous: Chapter 2 — Intro to C++](../Chapter_02_Intro_to_C++/)
- [Next: Chapter 4 — Making Decisions](../Chapter_04_Making_Decisions/)
- [All chapters](../README.md)
