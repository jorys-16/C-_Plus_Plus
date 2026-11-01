# Create Shared Library & Docs
New-Item -ItemType Directory -Force -Path "include", "docs-and-notes/uml-diagrams", "docs-and-notes/textbooks"

# CSC 111
$csc111 = @(
    "Ch01-02-Intro-and-IO", "Ch03-04-Expressions-Decisions", "Ch05-Loops-and-Files",
    "Ch06-Functions", "Ch07-08-Arrays-Search-Sort", "Ch09-Pointers",
    "Ch10-Strings", "Ch11-Structures", "Ch13-Intro-Classes", "Ch20-Intro-Recursion"
)
foreach ($ch in $csc111) {
    New-Item -ItemType Directory -Force -Path "01-CSC111-Intro-to-CPP/$ch/book"
}

# CSC 211H
$csc211h = @(
    "Ch13-OOP-Classes", "Ch07-Arrays-and-Vectors", "Ch09-Dynamic-Memory",
    "Ch12-Advanced-Files", "Ch14-Operator-Overloading", "Ch15-Inheritance-Polymorphism",
    "Ch16-Exceptions-Templates", "Ch17-STL", "Ch20-Advanced-Recursion"
)
foreach ($ch in $csc211h) {
    New-Item -ItemType Directory -Force -Path "02-CSC211H-Advanced-CPP/$ch/book", "02-CSC211H-Advanced-CPP/$ch/zylabs"
}
New-Item -ItemType Directory -Force -Path "02-CSC211H-Advanced-CPP/Honors-Capstones"

# CSC 331
$csc331 = @(
    "Ch03-Array-Based-Lists", "Ch05-Linked-Lists", "Ch06-Recursion",
    "Ch07-Stacks", "Ch08-Queues", "Ch09-Searching-and-Hashing",
    "Ch10-Sorting-Algorithms", "Ch11-Trees-BST-AVL", "Ch12-Graphs"
)
foreach ($ch in $csc331) {
    New-Item -ItemType Directory -Force -Path "03-CSC331-Data-Structures/$ch/book", "03-CSC331-Data-Structures/$ch/exercises", "03-CSC331-Data-Structures/$ch/zylabs", "03-CSC331-Data-Structures/$ch/project-capstone"
}

Write-Host "All Windows directories created successfully!" -ForegroundColor Green