# Chapter 6: Functions

This chapter introduces function declarations and definitions, parameters,
return values, scope, and decomposing programs into reusable parts.

## Learning path

- [ ] Read the [Chapter 6 PDF](./Chapter_06.pdf).
- [ ] Complete the checklist below.
- [ ] Finish the [Chapter 6 assignment](../../Assignments/README.md#6-chapter-6--modular-calculator).

<details>
<summary>Open the checklist</summary>

- [ ] Declare and define a function.
- [ ] Pass arguments to parameters.
- [ ] Return a calculated value.
- [ ] Explain local variable scope.
- [ ] Divide a larger problem into reusable functions.

</details>

## Try it

```cpp
#include <iostream>

double square(double value) {
    return value * value;
}

int main() {
    std::cout << square(4.0) << '\n';
}
```

<details>
<summary>Show the result</summary>

The program prints `16`.

</details>

## Continue

- [Previous: Chapter 5 — Loops and Files](../Chapter_05_Loops_and_Files/)
- [Next: Chapter 7 — Arrays](../Chapter_07_Arrays/)
- [All chapters](../README.md)
