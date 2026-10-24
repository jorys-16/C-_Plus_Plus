# Chapter 10: Characters and Strings

This chapter covers character values, C-style strings, `std::string`, and
common operations for processing text.

## Learning path

- [ ] Read the [Chapter 10 PDF](./Chapter_10.pdf).
- [ ] Complete the checklist below.
- [ ] Finish the [Chapter 10 assignment](../../Assignments/README.md#10-chapter-10--text-analyzer).

<details>
<summary>Open the checklist</summary>

- [ ] Distinguish a character from a string.
- [ ] Use `std::string` for text.
- [ ] Traverse text one character at a time.
- [ ] Count letters, digits, spaces, or vowels.
- [ ] Read a complete line with `std::getline`.

</details>

## Try it

```cpp
#include <iostream>
#include <string>

int main() {
    std::string message;
    std::getline(std::cin, message);
    std::cout << "Characters: " << message.length() << '\n';
}
```

<details>
<summary>Try an input example</summary>

For the input `C++ is fun!`, the program reports `11` characters, including
spaces and punctuation.

</details>

## Continue

- [Previous: Chapter 9 — Pointers](../Chapter_09_Pointers/)
- [Next: Chapter 11 — Structured Data](../Chapter_11_Structured_Data/)
- [All chapters](../README.md)
