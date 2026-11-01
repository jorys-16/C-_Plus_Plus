# 🚀 BMCC Computer Science Pathway Roadmap
**CSC 111 (Intro to C++)** $\rightarrow$ **CSC 211H (Advanced OOP & STL)** $\rightarrow$ **CSC 331 (Data Structures)**[cite: 1, 4, 8]

Welcome to my centralized C++ and Data Structures repository. This repository tracks my coursework, auto-graded **zyBooks** labs, textbook programming challenges (*Starting Out with C++* & *Data Structures Using C++*), and custom Abstract Data Type (ADT) implementations across my undergraduate progression at BMCC (CUNY)[cite: 1, 4, 8].

## Course Materials

Course syllabi and saved zyBooks activity pages are organized in each course's `course-materials` folder:

- `01-CSC111-Intro-to-CPP/course-materials/`
- `02-CSC211H-Advanced-CPP/course-materials/`
- `03-CSC331-Data-Structures/course-materials/`

The *Starting Out with C++* chapter PDFs are stored in the matching chapter's `book` subfolder. Chapters used by more than one course are copied into each applicable course folder.

---

## 📊 Course Dependency & Resource Flowchart

```mermaid
flowchart TD
    classDef book1 fill:#1e293b,stroke:#38bdf8,stroke-width:2px,stroke-dasharray: 5 5,color:#38bdf8
    classDef book2 fill:#1e293b,stroke:#c084fc,stroke-width:2px,stroke-dasharray: 5 5,color:#c084fc
    classDef zybook fill:#451a03,stroke:#f97316,stroke-width:2px,color:#fed7aa
    classDef csc111 fill:#1e3a8a,stroke:#3b82f6,stroke-width:2px,color:#fff
    classDef csc211 fill:#065f46,stroke:#10b981,stroke-width:2px,color:#fff
    classDef csc331 fill:#581c87,stroke:#a855f7,stroke-width:2px,color:#fff
    classDef lib fill:#881337,stroke:#f43f5e,stroke-width:2px,color:#fff

    subgraph Resources ["📚 Textbooks & Platforms"]
        G_PDF["📄 Gaddis 9th Ed. PDF"]:::book1
        ZY_211["⚡ zyBooks: CSC 211"]:::zybook
        M_PDF["📄 D.S. Malik 2nd Ed. PDF"]:::book2
        ZY_331["⚡ zyBooks: CSC 331 Data Structures"]:::zybook
    end

    subgraph Phase1 ["📘 01-CSC111: Intro to Programming"]
        A1["Ch 1–6: Basics, Loops & Functions"]:::csc111
        A2["Ch 7–20: Arrays, Pointers & Classes"]:::csc111
        A1 --> A2
    end

    subgraph Phase2 ["📗 02-CSC211H: Advanced Techniques"]
        B1["OOP, Rule of 3, Inheritance & Templates"]:::csc211
        A2 --> B1
    end

    subgraph SharedLib ["📙 include/ — Reusable ADT Library"]
        ADT["arrayListType.h | linkedList.h | myStack.h | myQueue.h"]:::lib
    end

    subgraph Phase3 ["📕 03-CSC331: Data Structures"]
        C1["Lists, Stacks, Queues, Hash Tables"]:::csc331
        C2["Trees (BST/AVL) & Graphs (Dijkstra)"]:::csc331
        B1 --> C1 --> C2
    end

    G_PDF -.-> Phase1 & Phase2
    ZY_211 -.-> Phase2
    M_PDF -.-> Phase3
    ZY_331 -.-> Phase3
    C1 -.->|"Exports .h"| ADT
    ADT -.->|"Included in"| C2