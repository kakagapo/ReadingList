# Programming languages

## Table of equivalent features

### Garbage collection

Used in

1) Java
2) C#
3) Haskell

## C\#

- Attributes
- Reflection
- [Volatile keyword in C# – memory model explained](https://igoro.com/archive/volatile-keyword-in-c-memory-model-explained/)
- [Dependency resolution](https://learn.microsoft.com/en-us/nuget/concepts/dependency-resolution)

## Java

## Python

- [Memory Management in Python](https://realpython.com/python-memory-management/)
- [Memory Management](https://docs.python.org/3/c-api/memory.html)
- [Garbage Collector Design](https://devguide.python.org/internals/garbage-collector/index.html)
  - Mainly based on reference counts (won't help with cycles)
  - Since cycles are limited container objects they are tracked separately and scanned periodically for reachability. To be able to scan through all the objects they should have a link between them. That is done by maintaining pointers to prev and next objects, thereby making it a doubly linked-list.
- [GC Module](https://docs.python.org/3/library/gc.html)

## Go

## Rust

- Ownership is used to eliminate the following classes of bugs
  - dangling pointers
  - double frees
  - using uninitialized memory

### Books

- [Programming Rust, 2nd Edition](https://learning.oreilly.com/library/view/programming-rust-2nd/9781492052586/)
- [Rust Atomics and Locks](https://learning.oreilly.com/library/view/rust-atomics-and/9781098119430/)

## PHP

## Javascript and variants

## C++

- https://en.cppreference.com/w/cpp/memory
- https://en.wikibooks.org/wiki/C%2B%2B_Programming/Memory_Management
- https://isocpp.org/wiki/faq/freestore-mgmt

### Learning resources

- https://developers.google.com/edu/c++/getting-started

```cpp
using namespace std;
vector<string> a = { "hi", "how", "are", "you" };
vector<string> b = a;
```

The above code ends up making deep copies of `a`.

## Object Oriented Programming