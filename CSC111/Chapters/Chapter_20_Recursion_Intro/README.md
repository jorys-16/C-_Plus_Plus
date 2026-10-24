# Chapter 20: Introduction to Recursion

This chapter introduces recursive functions, base cases, recursive cases, and
how to trace recursive problem-solving steps.

## Learning path

- [ ] Read the [Chapter 20 PDF](./Chapter_20.pdf).
- [ ] Complete the checklist below.
- [ ] Finish the [Chapter 20 assignment](../../Assignments/README.md#13-chapter-20--recursive-toolkit).

<details>
<summary>Open the checklist</summary>

- [ ] Identify a recursive case and a base case.
- [ ] Trace recursive calls on paper.
- [ ] Confirm that each call moves toward the base case.
- [ ] Explain when an iterative solution may be simpler.

</details>

## Try it

```cpp
#include <iostream>

int factorial(int value) {
    if (value <= 1) {
        return 1;
    }
    return value * factorial(value - 1);
}

int main() {
    std::cout << factorial(5) << '\n';
}
```

<details>
<summary>Show the result</summary>

The program prints `120`. The base case is `factorial(1)`, and every other
call reduces the argument by one.

</details>

## Quick check

What could happen if a recursive function never reaches its base case?

<details>
<summary>Show the answer</summary>

The function can keep creating calls until the program runs out of call-stack
space, causing a stack overflow.

</details>

## Continue

- [Previous: Chapter 13 — Intro to Classes](../Chapter_13_Intro_to_Classes/)
- [All chapters](../README.md)
