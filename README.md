# 🤖 Employee Management System - Comprehensive OOP Implementation

**A required project submission for the AI Diploma, in collaboration with AItronix and Eduzah.**

---

## 🎯 Project Overview

This project is a practical and robust application of **Object-Oriented Programming (OOP)** principles using Python. It demonstrates a scalable and maintainable structure for managing employee data, departments, and complex salary calculation processes.

### Core Objectives:

- **Demonstrate OOP Mastery:** Apply all core OOP concepts (Abstraction, Inheritance, Polymorphism, Encapsulation).
- **Implement Relationships:** Correctly establish complex relationships between classes (Composition, Aggregation, Association).
- **Design First:** Utilize full UML diagrams (Class, Sequence, Activity, Use Case) as a blueprint for the code implementation.

---

## 🏛️ Design & Architecture (UML Diagrams)

The system was fully designed using the Unified Modeling Language (UML) before coding began, ensuring alignment with the required academic standards.

### Key Diagrams Included:

| Diagram              | Focus                                                                  | Key OOP Concept Highlighted                    |
| :------------------- | :--------------------------------------------------------------------- | :--------------------------------------------- |
| **Class Diagram**    | System structure, attributes, methods, and relationships.              | Inheritance, Composition, Aggregation.         |
| **Sequence Diagram** | The step-by-step interaction for **"Add Employee"**.                   | Object creation and method calls sequence.     |
| **Activity Diagram** | The workflow for **"Calculate and Display All Salaries"**.             | Decision logic (if/else) and Iteration (Loop). |
| **Use Case Diagram** | Defining system scope and user interactions (HR Manager vs. Employee). | System requirements and boundaries.            |

---

## 💻 OOP Implementation Details

The following concepts were strictly enforced throughout the Python codebase:

| Concept           | Implementation in Python                                                                                                                                               |
| :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Abstraction**   | The **`Employee`** class is defined as an **Abstract Base Class (ABC)** using the `abc` module, enforcing the **`Calculate_Salary`** method in subclasses.             |
| **Polymorphism**  | Achieved through method **Overriding**: `FullTimeEmployee` and `PartTimeEmployee` provide their unique implementation of the abstract **`Calculate_Salary()`** method. |
| **Inheritance**   | **`FullTimeEmployee`** and **`PartTimeEmployee`** extend the base **`Employee`** class.                                                                                |
| **Encapsulation** | Use of **Private** (`__attribute`) and **Protected** (`_attribute`) naming conventions, controlling access to internal state.                                          |
| **Relationships** | **Composition** (Strong ownership: `Company` owns `Department` objects) and **Aggregation** (Weak ownership: `Company` contains `Employee` objects).                   |

---

## ⚙️ Project Structure and Execution

The code is organized into a Python package structure for modularity and professional code management.

### File Structure:

Employee_Management_Project /
|--- Main.py
|--ReadMe.md
|--.gitignore
|--Employee_System/
|-- \***\*init\*\***.py
|-- Employee.py
|-- Company.py
|-- Department.py
|-- FulltimeEmployee.py
|-- PartTimeEmployee.py

## 🧑‍💻 Author and Acknowledgements

This project was developed by **[Ahmed Hafez Said ]** as part of the **AI Diploma** requirements, a collaboration between **AItronix** and **Eduzah**.

For any inquiries, please contact me via [My LinkedIn Profile](https://www.linkedin.com/feed/?trk=guest_homepage-basic_google-one-tap-submit).
