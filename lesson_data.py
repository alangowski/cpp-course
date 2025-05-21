lessons = {
    "Structure of a C++ Program": {
        "video": "https://www.youtube.com/watch?v=vLnPwxZdW4Y",
        "reading": "https://en.wikibooks.org/wiki/C%2B%2B_Programming/Structure_of_a_C%2B%2B_Program",
        "code": """#include <iostream>\nusing namespace std;\nint main() {\n    cout << \"Hello, world!\" << endl;\n    return 0;\n}""",
        "flashcards": [
            ("What is the entry point of every C++ program?", "The main() function."),
            ("Which directive includes a library?", "#include <library_name>")
        ]
    },
    "Identifiers, Data Types, Operators, Structures": {
        "video": "https://www.youtube.com/watch?v=Rub-JsjMhWY",
        "reading": "https://en.wikibooks.org/wiki/C%2B%2B_Programming/Data_Types",
        "code": """#include <iostream>\nusing namespace std;\nstruct Point {\n    int x, y;\n};\nint main() {\n    Point p = {2, 3};\n    cout << p.x + p.y << endl;\n    return 0;\n}""",
        "flashcards": [
            ("What does 'int' represent in C++?", "An integer data type."),
            ("What does the '++' operator do?", "It increments a variable by 1."),
            ("What is a struct?", "A user-defined data type that groups variables.")
        ]
    },
    "Standard Libraries": {
        "video": "https://www.youtube.com/watch?v=8jLOx1hD3_o",
        "reading": "https://en.wikibooks.org/wiki/C%2B%2B_Programming/STL",
        "code": """#include <iostream>\n#include <vector>\n#include <string>\nusing namespace std;\nint main() {\n    vector<int> nums = {1, 2, 3};\n    for (int n : nums) {\n        cout << n << endl;\n    }\n    return 0;\n}""",
        "flashcards": [
            ("Which library provides vectors?", "<vector>"),
            ("Which function generates random numbers?", "rand() from <cstdlib>"),
            ("How do you measure time?", "Use time(0) from <ctime>")
        ]
    },
    "Control Structures": {
        "video": "https://www.youtube.com/watch?v=ZyA4K2tJ1pE",
        "reading": "https://en.wikibooks.org/wiki/C%2B%2B_Programming/Control_Structures",
        "code": """#include <iostream>\nusing namespace std;\nint main() {\n    int x = 5;\n    if (x > 0) cout << \"Positive\";\n    else cout << \"Non-positive\";\n    return 0;\n}""",
        "flashcards": [
            ("What keyword is used for conditional branching?", "if"),
            ("Which structure handles multiple specific cases?", "switch"),
            ("What is the ternary syntax?", "condition ? true_expr : false_expr")
        ]
    },
    "Repetition Structures": {
        "video": "https://www.youtube.com/watch?v=YJooV6tF2aY",
        "reading": "https://en.wikibooks.org/wiki/C%2B%2B_Programming/Loops",
        "code": """#include <iostream>\nusing namespace std;\nint main() {\n    for (int i = 0; i < 5; ++i) {\n        cout << i << endl;\n    }\n    return 0;\n}""",
        "flashcards": [
            ("Which loop checks condition before execution?", "while loop"),
            ("Which loop executes at least once?", "do-while loop"),
            ("Which loop is best for counting iterations?", "for loop")
        ]
    },
    "User Defined Functions": {
        "video": "https://www.youtube.com/watch?v=WLvU5EQVZqY",
        "reading": "https://en.wikibooks.org/wiki/C%2B%2B_Programming/Functions",
        "code": """#include <iostream>\nusing namespace std;\nint add(int a, int b) {\n    return a + b;\n}\nint main() {\n    cout << add(2, 3);\n    return 0;\n}""",
        "flashcards": [
            ("What defines a function?", "return_type name(parameters) { body }"),
            ("How do you pass by reference?", "Use & in parameter type"),
            ("What is function overloading?", "Same function name, different parameters")
        ]
    },
    "Pointers and Memory": {
        "video": "https://www.youtube.com/watch?v=DTxHyVn0ODg",
        "reading": "https://en.wikibooks.org/wiki/C%2B%2B_Programming/Pointers",
        "code": """#include <iostream>\nusing namespace std;\nint main() {\n    int var = 10;\n    int* ptr = &var;\n    cout << \"Value: \" << *ptr << endl;\n    cout << \"Address: \" << ptr << endl;\n    return 0;\n}""",
        "flashcards": [
            ("What does a pointer store?", "The memory address of another variable."),
            ("What operator is used to get the address of a variable?", "The & operator."),
            ("What operator is used to access the value pointed to?", "The * operator."),
            ("What keyword represents a null pointer in modern C++?", "nullptr")
        ]
    },
    "Static and Dynamic Arrays, Vectors, Containers": {
        "video": "https://www.youtube.com/watch?v=R7vmHGAshi8",
        "reading": "https://en.wikibooks.org/wiki/C%2B%2B_Programming/Arrays",
        "code": """#include <iostream>\n#include <vector>\nusing namespace std;\nint main() {\n    int* arr = new int[5];\n    for (int i = 0; i < 5; ++i) arr[i] = i;\n    vector<int> vec = {1, 2, 3};\n    delete[] arr;\n    return 0;\n}""",
        "flashcards": [
            ("How is memory allocated dynamically?", "Using new and delete"),
            ("Which container allows dynamic resizing?", "std::vector"),
            ("What are arrays indexed from?", "Zero")
        ]
    },
    "Inheritance": {
        "video": "https://www.youtube.com/watch?v=ON0A1dsQOV0",
        "reading": "https://en.wikibooks.org/wiki/C%2B%2B_Programming/Inheritance",
        "code": """#include <iostream>\nusing namespace std;\nclass Animal {\npublic:\n    void speak() { cout << \"Animal sound\" << endl; }\n};\nclass Dog : public Animal {\npublic:\n    void bark() { cout << \"Woof\" << endl; }\n};\nint main() {\n    Dog d;\n    d.speak();\n    d.bark();\n    return 0;\n}""",
        "flashcards": [
            ("What is inheritance used for?", "To reuse and extend existing classes"),
            ("What is the base class called?", "Superclass or Parent"),
            ("What access level retains public members?", "public inheritance")
        ]
    },
    "Operator Overloading": {
        "video": "https://www.youtube.com/watch?v=9Sthkr5vHc4",
        "reading": "https://en.wikibooks.org/wiki/C%2B%2B_Programming/Operators/Operator_Overloading",
        "code": """#include <iostream>\nusing namespace std;\nclass Point {\npublic:\n    int x, y;\n    Point operator+(const Point& p) {\n        return {x + p.x, y + p.y};\n    }\n};\nint main() {\n    Point a{1, 2}, b{3, 4};\n    Point c = a + b;\n    cout << c.x << \", \" << c.y;\n    return 0;\n}""",
        "flashcards": [
            ("What is operator overloading?", "Redefining how operators work for user-defined types"),
            ("Which operator prints objects?", "<< (overloaded for ostream)"),
            ("Which function is used for addition?", "operator+")
        ]
    },
    "Recursion, Sorting & Searching": {
        "video": "https://www.youtube.com/watch?v=NgulHZJ9u7k",
        "reading": "https://en.wikibooks.org/wiki/C%2B%2B_Programming/Algorithms",
        "code": """#include <iostream>\nusing namespace std;\nint factorial(int n) {\n    if (n <= 1) return 1;\n    return n * factorial(n - 1);\n}\nint main() {\n    cout << factorial(5);\n    return 0;\n}""",
        "flashcards": [
            ("What is recursion?", "A function calling itself"),
            ("Which search halves the range each time?", "Binary search"),
            ("Which sort selects minimum each iteration?", "Selection sort")
        ]
    }
}
