# Chapter 4: Making Decisions

## Overview

Programs often need to choose what to do based on information or conditions.
In this chapter, you will learn how to use conditional statements to make
decisions in C++.

## Learning objectives

By the end of this chapter, you should be able to:

- Compare values with comparison operators.
- Combine conditions with logical operators.
- Use `if`, `else if`, and `else` statements.
- Write nested conditional statements.
- Validate user input with conditions.

## Comparison operators

| Operator | Meaning |
| --- | --- |
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

## Basic conditional statement

```cpp
int temperature = 75;

if (temperature >= 70) {
    std::cout << "It is warm outside.\n";
} else {
    std::cout << "It is cool outside.\n";
}
```

The code inside the braces runs only when its condition is true.

## Multiple decisions

Use `else if` when there are several possible conditions:

```cpp
int score = 85;
char letter_grade;

if (score >= 90) {
    letter_grade = 'A';
} else if (score >= 80) {
    letter_grade = 'B';
} else if (score >= 70) {
    letter_grade = 'C';
} else {
    letter_grade = 'F';
}

std::cout << letter_grade << '\n';
```

C++ checks the conditions from top to bottom and runs the first matching
branch.

## Logical operators

Logical operators combine conditions:

```cpp
int age = 20;
bool has_id = true;

if (age >= 18 && has_id) {
    std::cout << "Entry approved.\n";
}
```

- `&&` requires every condition to be true.
- `||` requires at least one condition to be true.
- `!` reverses a condition.

## Input validation example

```python
int number;
std::cout << "Enter a positive number: ";
std::cin >> number;

if (number > 0) {
    std::cout << "Thank you.\n";
} else {
    std::cout << "The number must be positive.\n";
}
```

## Key idea

Decision-making allows a program to respond differently depending on the
current data. A condition produces either `true` or `false`, and C++ uses that
result to decide which block of code to execute.

## Learning path

- [ ] Read the [Chapter 4 PDF](./Chapter_04.pdf).
- [ ] Complete the examples and quick checks above.
- [ ] Finish the [Chapter 4 assignment](../../Assignments/README.md#4-chapter-4--grade-classifier).

<details>
<summary>Open the checklist</summary>

- [ ] Compare values with relational operators.
- [ ] Write `if`, `else if`, and `else` branches.
- [ ] Combine conditions with `&&`, `||`, and `!`.
- [ ] Validate input before using it.

</details>

## Continue

- [Previous: Chapter 3 — Expressions and Interactivity](../Chapter_03_Expressions_and_Interactivity/)
- [Next: Chapter 5 — Loops and Files](../Chapter_05_Loops_and_Files/)
- [All chapters](../README.md)
