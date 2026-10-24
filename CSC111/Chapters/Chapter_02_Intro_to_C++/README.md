# Chapter 2: Introduction to C++

This chapter introduces the structure of a C++ program, source files,
compilation, standard output, comments, and basic program execution.

## Learning path

- [ ] Read the [Chapter 2 PDF](./Chapter_02.pdf).
- [ ] Compile and run a first C++ program.
- [ ] Complete the checklist below.
- [ ] Finish the [Chapter 2 assignment](../../Assignments/README.md#2-chapter-2--first-c-program).

<details>
<summary>Open the checklist</summary>

- [ ] Identify `main`, headers, statements, and comments.
- [ ] Explain why C++ statements end with semicolons.
- [ ] Compile a source file and run the executable.
- [ ] Use `std::cout` to display formatted output.

</details>

## Try it

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, CSC111!\n";
}
```

<details>
<summary>Show a compile command</summary>

```text
g++ -std=c++17 -Wall -Wextra -pedantic hello.cpp -o hello
```

</details>

## Continue

- [Previous: Chapter 1 — Intro to Computers](../Chapter_01_Intro_to_Computers/)
- [Next: Chapter 3 — Expressions and Interactivity](../Chapter_03_Expressions_and_Interactivity/)
- [All chapters](../README.md)
