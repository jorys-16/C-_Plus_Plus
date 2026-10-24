# Chapter 9: Pointers

This chapter introduces memory addresses, pointer variables, indirection,
pointer parameters, and the relationship between pointers and arrays.

## Learning path

- [ ] Read the [Chapter 9 PDF](./Chapter_09.pdf).
- [ ] Complete the checklist below.
- [ ] Finish the [Chapter 9 assignment](../../Assignments/README.md#9-chapter-9--pointer-swap-lab).

<details>
<summary>Open the checklist</summary>

- [ ] Use `&` to obtain an address.
- [ ] Use `*` to declare and dereference a pointer.
- [ ] Pass an address to a function.
- [ ] Explain how arrays and pointers are related.
- [ ] Avoid dereferencing a null or uninitialized pointer.

</details>

## Try it

```cpp
#include <iostream>

void doubleValue(int* value) {
    if (value != nullptr) {
        *value *= 2;
    }
}

int main() {
    int number = 7;
    doubleValue(&number);
    std::cout << number << '\n';
}
```

<details>
<summary>Show the result</summary>

The program prints `14`. The function changes the original variable through
its address.

</details>

## Continue

- [Previous: Chapter 8 — Searching and Sorting](../Chapter_08_Searching_and_Sorting/)
- [Next: Chapter 10 — Characters and Strings](../Chapter_10_Characters_and_Strings/)
- [All chapters](../README.md)
