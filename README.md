# Software Test Project: OpenCart Automation Framework

## Project Overview
This project implements a comprehensive **Black-Box Test Architecture** for the [OpenCart E-commerce Platform](https://demo.opencart.com/). It is designed to validate the functionality, usability, performance, and security of the application without internal code knowledge.

The framework is structured around **ISTQB (International Software Testing Qualifications Board)** principles, specifically applying four key black-box testing techniques to ensure robust coverage.

## ISTQB Black-Box Testing Techniques Applied
This project explicitly utilizes the following four techniques to design test cases:

### 1️⃣ Analyse des valeurs limites (Boundary Value Analysis – BVA)
**Focus:** Testing the boundaries of input ranges where errors are most likely to occur.
**Application:** Used for fields like quantity inputs (min/max), search string lengths, and price filters.
**Example:** Testing cart quantity with 0, 1, 999, 1000.

### 2️⃣ Partition d'équivalence (Equivalence Partitioning – EP)
**Focus:** Grouping inputs into valid and invalid partitions, assuming all values in a partition behave similarly.
**Application:** Used for form validation (email formats, phone numbers) and product filtering (price ranges).
**Example:** Testing email with valid format (`user@test.com`) vs. invalid format (`user@`).

### 3️⃣ Tests de transition d'état (State Transition Testing)
**Focus:** Validating the system's behavior as it transitions between different states based on events.
**Application:** Used for complex flows like Checkout (Cart -> Billing -> Payment -> Success) and Order History.
**Example:** Verifying a product moves from "In Stock" to "Reserved" or "Sold" states.

### 4️⃣ Tests de configuration (Configuration Testing)
**Focus:** Verifying the system functions correctly across different hardware and software configurations.
**Application:** Used for Cross-Browser Compatibility (Chrome, Firefox, Edge) and Responsive Design (Mobile, Tablet, Desktop).
**Example:** Verifying the layout adapts correctly on an iPhone SE viewport vs. a Desktop monitor.

## Project Structure
- `src/`: Source code (placeholder).
- `tests/`: Contains all test documentation and cases.
    - `suites/`: High-level documentation of test suites.
        - `cross_browser_suite.md`: Tests focusing on browser compatibility.
        - `responsive_design_suite.md`: Tests focusing on device adaptability.
        - `performance_load_suite.md`: Tests focusing on system performance.
        - `stress_resilience_suite.md`: Tests focusing on system stability.
    - `cases/`: Detailed test case specifications (to be implemented).
- `TEST_ARCHITECTURE.md`: Full ISTQB-Certified Test Architecture Document.

## Setup & Usage
1.  Clone the repository.
2.  Review the `TEST_ARCHITECTURE.md` for the overall strategy.
3.  Navigate to `tests/suites/` to explore specific test scenarios and the techniques applied.
