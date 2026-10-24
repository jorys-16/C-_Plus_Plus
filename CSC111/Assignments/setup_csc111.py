from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parent.parent
COURSE = ROOT / "CSC111"

# Proposed chapter content: adjust to match your syllabus.
CHAPTERS = [
    (
        "Chapter_01_Intro_to_Computers",
        "Introduction to Computers",
        ["Hardware and software", "Algorithms", "Compilation", "Types of errors"],
        "Write pseudocode for calculating the total cost of a purchase.",
    ),
    (
        "Chapter_02_Intro_to_C++",
        "Introduction to C++",
        ["Program structure", "Variables and types", "Output", "Arithmetic"],
        "Write a program that calculates the area and perimeter of a rectangle.",
    ),
    (
        "Chapter_03_Expressions_and_Interactivity",
        "Expressions and Interactivity",
        ["Input", "Expressions", "Type conversions", "Formatted output"],
        "Read a temperature in Celsius and display its Fahrenheit equivalent.",
    ),
    (
        "Chapter_04_Making_Decisions",
        "Making Decisions",
        ["Comparisons", "if and else", "Logical operators", "switch"],
        "Read a score from 0 to 100, validate it, and display a letter grade.",
    ),
    (
        "Chapter_05_Loops_and_Files",
        "Loops and Files",
        ["Loop types", "Input validation", "Accumulators", "File input/output"],
        "Read numbers from a file and report their count, sum, and average. "
        "Handle an unavailable file and a file containing no numbers.",
    ),
    (
        "Chapter_06_Functions",
        "Functions",
        ["Declarations and definitions", "Arguments and parameters",
         "Return values", "Pass by value and reference"],
        "Write and test a function that determines whether an integer is prime.",
    ),
    (
        "Chapter_07_Arrays",
        "Arrays",
        ["Indexing", "Traversal", "Arrays and functions", "Two-dimensional arrays"],
        "For a nonempty array of scores, calculate the minimum, maximum, "
        "and average using functions.",
    ),
    (
        "Chapter_08_Searching_and_Sorting",
        "Searching and Sorting",
        ["Linear search", "Binary search", "Selection sort", "Algorithm tracing"],
        "Implement linear search and selection sort. Test duplicates, "
        "missing values, and a single-element array.",
    ),
    (
        "Chapter_09_Pointers",
        "Pointers",
        ["Addresses", "Dereferencing", "nullptr", "Pointers and arrays"],
        "Write a function that modifies an integer through a pointer. "
        "Define how your function handles nullptr.",
    ),
    (
        "Chapter_10_Characters_and_Strings",
        "Characters and Strings",
        ["Character processing", "std::string", "getline", "C-style strings"],
        "Read a line of text and count its letters, digits, and spaces.",
    ),
    (
        "Chapter_11_Structured_Data",
        "Structured Data",
        ["Struct definitions", "Member access", "Arrays of records",
         "Passing records to functions"],
        "Define a Student struct and write functions to display a student "
        "and find a student by ID.",
    ),
    (
        "Chapter_13_Intro_to_Classes",
        "Introduction to Classes",
        ["Objects", "Public and private members", "Constructors",
         "Header and implementation files"],
        "Create a Rectangle class with validated dimensions and functions "
        "that calculate area and perimeter.",
    ),
    (
        "Chapter_20_Recursion_Intro",
        "Introduction to Recursion",
        ["Base cases", "Recursive cases", "Termination", "Tracing calls"],
        "Write recursive and iterative functions that sum integers from "
        "1 to n. Define behavior for n = 0 and reject negative input.",
    ),
]

parser = argparse.ArgumentParser(description="Create CSC111 learning templates.")
parser.add_argument(
    "--apply",
    action="store_true",
    help="Create missing files. Without this flag, only preview changes.",
)
args = parser.parse_args()

created = 0
skipped = 0


def create_file(path, content):
    global created, skipped

    if path.exists():
        skipped += 1
        print(f"KEEP    {path.relative_to(ROOT)}")
        return

    if not args.apply:
        created += 1
        print(f"PREVIEW {path.relative_to(ROOT)}")
        return

    path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with path.open("x", encoding="utf-8") as file:
            file.write(content)
    except FileExistsError:
        skipped += 1
        print(f"KEEP    {path.relative_to(ROOT)}")
    else:
        created += 1
        print(f"CREATE  {path.relative_to(ROOT)}")


for folder, title, topics, exercise in CHAPTERS:
    chapter = COURSE / "Chapters" / folder
    objectives = "\n".join(f"- [ ] {topic}" for topic in topics)

    create_file(
        chapter / "README.md",
        f"""# {title}

## Topics
{objectives}

## Completion checklist
- [ ] Explain the concepts in my own words.
- [ ] Write and run a small example.
- [ ] Predict output before running the example.
- [ ] Attempt the exercise independently.
- [ ] Test normal inputs and edge cases.
- [ ] Record mistakes and corrections.
- [ ] Revisit the topic in a later session.

## Files
- Notes.md: my explanations and observations.
- Examples/: small demonstrations.
- Exercises/: prompts and my attempts.
- Solutions/: corrected work after an independent attempt.
- Review.md: recall questions and debugging notes.
""",
    )

    create_file(
        chapter / "Notes.md",
        f"""# {title}: Notes

## Explanation in my own words

## Important syntax

## Example walkthrough

## Common mistakes

## Questions I still have
""",
    )

    create_file(
        chapter / "Examples" / "README.md",
        "# Examples\n\nAdd small programs demonstrating one concept at a time.\n",
    )

    create_file(
        chapter / "Exercises" / "exercise_01.md",
        f"""# Exercise 1

{exercise}

## My plan

## Test cases

| Input | Expected result | Actual result |
|---|---|---|

## What I found difficult
""",
    )

    create_file(
        chapter / "Exercises" / "attempt_01.cpp",
        """// Read exercise_01.md and write your own implementation.
// This is a starter, not a completed solution.

int main()
{
    // TODO: implement and test your program.
    return 0;
}
""",
    )

    create_file(
        chapter / "Solutions" / "README.md",
        "# Solutions\n\nAdd corrected solutions after attempting the exercises.\n",
    )

    create_file(
        chapter / "Review.md",
        """# Review

## Questions
1. What problem does this topic help me solve?
2. Can I explain it without looking at my notes?
3. Can I trace a short example?
4. Can I solve a new variation independently?

## A bug I fixed
- Symptom:
- Cause:
- Correction:
- Test confirming the correction:

## Next review
- Date:
- What I need to practice:
""",
    )

create_file(
    COURSE / "Assignments" / "README.md",
    """# Assignments

Create one folder per actual instructor assignment.

Suggested contents:
- README.md: your summary of the requirements.
- main.cpp: your implementation.
- tests.md: inputs and expected/actual results.
- reflection.md: difficulties and corrections.

Check course rules before publishing assignment materials or solutions.
""",
)

create_file(
    COURSE / "Projects" / "Gradebook" / "README.md",
    """# Gradebook Project

Build this incrementally:

- [ ] Read scores and calculate an average.
- [ ] Assign a letter grade.
- [ ] Validate input.
- [ ] Organize the program into functions.
- [ ] Store multiple scores.
- [ ] Search and sort records.
- [ ] Add student names and structured records.
- [ ] Save and load data.
- [ ] Refactor an appropriate part into a class.

Write your own requirements and test cases before implementing each stage.
""",
)

mode = "created" if args.apply else "planned"
print(f"Done: {created} files {mode}; {skipped} existing paths preserved.")