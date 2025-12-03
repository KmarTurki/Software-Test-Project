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
- `tests/`: Contains all test documentation and automated tests.
    - `conftest.py`: Pytest configuration and fixtures.
    - `test_01_configuration.py`: Configuration Testing (2 tests).
    - `test_02_bva_ep.py`: BVA and EP tests (3 tests).
    - `test_03_state_transition.py`: State Transition tests (2 tests).
    - `test_04_additional_bva_ep.py`: Additional BVA/EP tests (7 tests).
    - `test_05_additional_state.py`: Additional State Transition tests (5 tests).
    - `test_06_additional_config.py`: Additional Configuration tests (7 tests).
    - `suites/`: High-level documentation of test suites.
        - `cross_browser_suite.md`: Tests focusing on browser compatibility.
        - `responsive_design_suite.md`: Tests focusing on device adaptability.
        - `performance_load_suite.md`: Tests focusing on system performance.
        - `stress_resilience_suite.md`: Tests focusing on system stability.
    - `cases/`: Detailed test case specifications.
- `TEST_ARCHITECTURE.md`: Full ISTQB-Certified Test Architecture Document.
- `TEST_CASES_SUMMARY.md`: Complete summary of all 28 test cases.
- `requirements.txt`: Python dependencies (pytest, selenium, webdriver-manager).

## Setup & Usage

### Installation
1. Clone the repository:
```bash
git clone https://github.com/KmarTurki/Software-Test-Project.git
cd Software-Test-Project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Tests

**Run all tests:**
```bash
pytest tests/
```

**Run with verbose output:**
```bash
pytest tests/ -v
```

**Run specific test file:**
```bash
pytest tests/test_01_configuration.py
```

**Run specific test:**
```bash
pytest tests/test_02_bva_ep.py::test_search_bva
```

### Documentation
1. Review the `TEST_ARCHITECTURE.md` for the overall strategy.
2. Navigate to `tests/suites/` to explore specific test scenarios and the techniques applied.
3. See `TEST_CASES_SUMMARY.md` for a complete list of all 28 test cases.
