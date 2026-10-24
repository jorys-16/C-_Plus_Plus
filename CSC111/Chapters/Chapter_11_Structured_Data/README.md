# Chapter 11: Structured Data

This chapter introduces structures and other techniques for grouping related
data into meaningful records.

## Learning path

- [ ] Read the [Chapter 11 PDF](./Chapter_11.pdf).
- [ ] Complete the checklist below.
- [ ] Finish the [Chapter 11 assignment](../../Assignments/README.md#11-chapter-11--inventory-records).

<details>
<summary>Open the checklist</summary>

- [ ] Define a `struct` with related fields.
- [ ] Create and initialize structure variables.
- [ ] Access members with the dot operator.
- [ ] Store multiple records in an array.
- [ ] Pass structured data to a function.

</details>

## Try it

```cpp
#include <iostream>
#include <string>

struct Student {
    std::string name;
    double average;
};

int main() {
    Student student{"Alex", 91.5};
    std::cout << student.name << ": " << student.average << '\n';
}
```

<details>
<summary>Show the result</summary>

The program prints `Alex: 91.5`.

</details>

## Continue

- [Previous: Chapter 10 — Characters and Strings](../Chapter_10_Characters_and_Strings/)
- [Next: Chapter 13 — Intro to Classes](../Chapter_13_Intro_to_Classes/)
- [All chapters](../README.md)
