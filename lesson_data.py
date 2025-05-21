lessons = {
    "Structure of a C++ Program": {
        "video": "https://www.youtube.com/watch?v=vLnPwxZdW4Y",
        "reading": "https://www.geeksforgeeks.org/structure-of-cpp-program/",
        "code": """#include <iostream>
using namespace std;
int main() {
    cout << "Hello, world!" << endl;
    return 0;
}""",
        "flashcards": [
            ("What is the entry point of every C++ program?", "The main() function."),
            ("Which directive includes a library?", "#include <library_name>")
        ]
    },
    "Identifiers, Data Types, Operators, Structures": {
        "video": "https://www.youtube.com/watch?v=Rub-JsjMhWY",
        "reading": {
            "Identifiers": "https://www.geeksforgeeks.org/cpp-identifiers/",
            "Data Types": "https://www.geeksforgeeks.org/cpp-data-types/",
            "Operators": "https://www.geeksforgeeks.org/cpp-tokens/",
            "Structures": "https://www.geeksforgeeks.org/structures-in-cpp/"
        },
        "code": """#include <iostream>
using namespace std;
struct Point {
    int x, y;
};
int main() {
    Point p = {2, 3};
    cout << p.x + p.y << endl;
    return 0;
}""",
        "flashcards": [
            ("What does 'int' represent in C++?", "An integer data type."),
            ("What does the '++' operator do?", "It increments a variable by 1."),
            ("What is a struct?", "A user-defined data type that groups variables.")
        ]
    },
    "Standard Libraries": {
        "video": "https://www.youtube.com/watch?v=8jLOx1hD3_o",
        "reading": "https://en.wikibooks.org/w/index.php?title=C%2B%2B_Programming/STL&stable=1",
        "code": """#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main() {
    vector<int> nums = {1, 2, 3};
    for (int n : nums) {
        cout << n << endl;
    }
    return 0;
}""",
        "flashcards": [
            ("Which library provides vectors?", "<vector>"),
            ("Which function generates random numbers?", "rand() from <cstdlib>"),
            ("How do you measure time?", "Use time(0) from <ctime>")
        ]
    },
    "Control Structures": {
        "video": "https://www.youtube.com/watch?v=0YS8mLNrqhw",
        "reading": "https://www.geeksforgeeks.org/control-structures-in-programming-languages/",
        "code": """#include <iostream>
using namespace std;
int main() {
    int x = 5;
    if (x > 0) cout << "Positive";
    else cout << "Non-positive";
    return 0;
}""",
        "flashcards": [
            ("What keyword is used for conditional branching?", "if"),
            ("Which structure handles multiple specific cases?", "switch"),
            ("What is the ternary syntax?", "condition ? true_expr : false_expr")
        ]
    },
    "Repetition Structures": {
        "video": "https://www.youtube.com/watch?v=axXSQcASD-Y",
        "reading": "https://www.geeksforgeeks.org/cpp-loops/",
        "code": """#include <iostream>
using namespace std;
int main() {
    for (int i = 0; i < 5; ++i) {
        cout << i << endl;
    }
    return 0;
}""",
        "flashcards": [
            ("Which loop checks condition before execution?", "while loop"),
            ("Which loop executes at least once?", "do-while loop"),
            ("Which loop is best for counting iterations?", "for loop")
        ]
    },
    "User Defined Functions": {
        "video": "https://www.youtube.com/watch?v=kauJP582PEs",
        "reading": "https://www.programiz.com/cpp-programming/function",
        "code": """#include <iostream>
using namespace std;
int add(int a, int b) {
    return a + b;
}
int main() {
    cout << add(2, 3);
    return 0;
}""",
        "flashcards": [
            ("What defines a function?", "return_type name(parameters) { body }"),
            ("How do you pass by reference?", "Use & in parameter type"),
            ("What is function overloading?", "Same function name, different parameters")
        ]
    },
    "Pointers and Memory": {
        "video": "https://www.youtube.com/watch?v=DTxHyVn0ODg",
        "reading": "https://en.wikibooks.org/w/index.php?title=C%2B%2B_Programming/Operators/Pointers&stable=1",
        "code": """#include <iostream>
using namespace std;
int main() {
    int var = 10;
    int* ptr = &var;
    cout << "Value: " << *ptr << endl;
    cout << "Address: " << ptr << endl;
    return 0;
}""",
        "flashcards": [
            ("What does a pointer store?", "The memory address of another variable."),
            ("What operator is used to get the address of a variable?", "The & operator."),
            ("What operator is used to access the value pointed to?", "The * operator."),
            ("What keyword represents a null pointer in modern C++?", "nullptr")
        ]
    },
    "Static and Dynamic Arrays, Vectors, Containers": {
        "video": "https://www.youtube.com/watch?v=4nLZizG2lBk",
        "reading": "https://www.geeksforgeeks.org/difference-between-static-arrays-and-dynamic-arrays/",
        "code": """#include <iostream>
#include <vector>
using namespace std;
int main() {
    int* arr = new int[5];
    for (int i = 0; i < 5; ++i) arr[i] = i;
    vector<int> vec = {1, 2, 3};
    delete[] arr;
    return 0;
}""",
        "flashcards": [
            ("How is memory allocated dynamically?", "Using new and delete"),
            ("Which container allows dynamic resizing?", "std::vector"),
            ("What are arrays indexed from?", "Zero")
        ]
    },
    "Inheritance": {
        "video": "https://www.youtube.com/watch?v=qYY9eR7Ldek",
        "reading": "https://www.geeksforgeeks.org/inheritance-in-c/",
        "code": """#include <iostream>
using namespace std;
class Animal {
public:
    void speak() { cout << "Animal sound" << endl; }
};
class Dog : public Animal {
public:
    void bark() { cout << "Woof" << endl; }
};
int main() {
    Dog d;
    d.speak();
    d.bark();
    return 0;
}""",
        "flashcards": [
            ("What is inheritance used for?", "To reuse and extend existing classes"),
            ("What is the base class called?", "Superclass or Parent"),
            ("What access level retains public members?", "public inheritance")
        ]
    },
    "Operator Overloading": {
        "video": "https://www.youtube.com/watch?v=ZoO_oA6-0_0",
        "reading": "https://www.programiz.com/cpp-programming/operator-overloading",
        "code": """#include <iostream>
using namespace std;
class Point {
public:
    int x, y;
    Point operator+(const Point& p) {
        return {x + p.x, y + p.y};
    }
};
int main() {
    Point a{1, 2}, b{3, 4};
    Point c = a + b;
    cout << c.x << ", " << c.y;
    return 0;
}""",
        "flashcards": [
            ("What is operator overloading?", "Redefining how operators work for user-defined types"),
            ("Which operator prints objects?", "<< (overloaded for ostream)"),
            ("Which function is used for addition?", "operator+")
        ]
    },
    "Recursion, Sorting & Searching": {
        "video": "https://www.youtube.com/watch?v=A6sUupg8ylE",
        "reading": {
            "Recursion": "https://www.geeksforgeeks.org/recursion/",
            "Sorting Algorithms": "https://www.geeksforgeeks.org/sorting-algorithms/",
            "Searching Algorithms": "https://www.geeksforgeeks.org/searching-algorithms/"
        },
        "code": """#include <iostream>
using namespace std;
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
int main() {
    cout << factorial(5);
    return 0;
}""",
        "flashcards": [
            ("What is recursion?", "A function calling itself"),
            ("Which search halves the range each time?", "Binary search"),
            ("Which sort selects minimum each iteration?", "Selection sort")
        ]
    }
}
