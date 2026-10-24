# Chapter 7: Arrays

This chapter introduces fixed-size arrays, indexing, traversal, and common
patterns for processing collections of values.

## Learning path

- [ ] Read the [Chapter 7 PDF](./Chapter_07.pdf).
- [ ] Complete the checklist below.
- [ ] Finish the [Chapter 7 assignment](../../Assignments/README.md#7-chapter-7--monthly-temperatures).

<details>
<summary>Open the checklist</summary>

- [ ] Declare and initialize an array.
- [ ] Access elements with zero-based indexes.
- [ ] Traverse an array with a loop.
- [ ] Calculate a sum and average.
- [ ] Find the largest and smallest values.

</details>

## Try it

```cpp
#include <iostream>

int main() {
    int scores[] = {72, 88, 91, 65};
    int total = 0;

    for (int score : scores) {
        total += score;
    }

    std::cout << total << '\n';
}
```

<details>
<summary>Show the result</summary>

The program prints `316`.

</details>

## Continue

- [Previous: Chapter 6 — Functions](../Chapter_06_Functions/)
- [Next: Chapter 8 — Searching and Sorting](../Chapter_08_Searching_and_Sorting/)
- [All chapters](../README.md)
