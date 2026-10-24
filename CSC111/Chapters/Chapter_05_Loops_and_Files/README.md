# Chapter 5: Loops and Files

This chapter covers `while`, `do-while`, and `for` loops, nested repetition,
and reading from and writing to files.

## Learning path

- [ ] Read the chapter PDF.
- [ ] Complete the loop warm-up below.
- [ ] Try the file-processing example.
- [ ] Finish the [Chapter 5 assignment](../../Assignments/README.md#5-chapter-5--data-summary).

<details>
<summary>Open the chapter checklist</summary>

| Skill | I can... |
| --- | --- |
| `while` | Repeat while a condition remains true. |
| `do-while` | Run a loop body at least once. |
| `for` | Express a counter-controlled loop clearly. |
| Nested loops | Place one loop inside another safely. |
| File input | Open a file and read values until input ends. |
| File output | Write calculated results to a separate file. |

</details>

## Read

**[Open Chapter 5 PDF](./Chapter_05.pdf)**

Use the PDF for the complete explanations, worked examples, review questions,
and programming challenges.

## Try it: loop warm-up

Before reading the answer, predict what the program prints:

```cpp
#include <iostream>

int main() {
    int total = 0;

    for (int value = 1; value <= 5; ++value) {
        total += value;
    }

    std::cout << total << '\n';
}
```

<details>
<summary>Show the answer</summary>

It prints `15`, because the loop adds `1 + 2 + 3 + 4 + 5`.

</details>

## Try it: file summary

Create a file named `numbers.txt` with one number per line:

```text
12
7
19
4
```

Then compile and run this program from the same directory:

```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ifstream input("numbers.txt");
    std::ofstream output("summary.txt");

    if (!input || !output) {
        std::cerr << "Unable to open a required file.\n";
        return 1;
    }

    int number;
    int count = 0;
    int sum = 0;

    while (input >> number) {
        sum += number;
        ++count;
    }

    output << "Count: " << count << '\n';
    output << "Sum: " << sum << '\n';
}
```

Compile with:

```text
g++ -std=c++17 -Wall -Wextra -pedantic file_summary.cpp -o file_summary
```

<details>
<summary>Show the expected output file</summary>

`summary.txt` should contain:

```text
Count: 4
Sum: 42
```

</details>

## Quick check

Answer these questions without looking back:

1. Which loop is guaranteed to execute its body at least once?
2. What condition should a file-reading loop usually test?
3. Why should a program check whether a file opened successfully?

<details>
<summary>Show answers</summary>

1. A `do-while` loop.
2. The result of the input operation, such as `while (input >> number)`.
3. The program should report the error instead of silently reading or writing
   invalid data.

</details>

## Continue

- [Previous: Chapter 4 — Making Decisions](../Chapter_04_Making_Decisions/)
- [Next: Chapter 6 — Functions](../Chapter_06_Functions/)
- [All chapters](../README.md)
