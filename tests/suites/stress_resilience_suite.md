# Suite 4: Stress & Resilience Suite

**Objective:** Test system limits and recovery mechanisms
**Priority:** Medium
**Execution Environment:** Extreme load conditions (100+ users), boundary inputs

## Test Cases & ISTQB Techniques

| Test Case ID | Title | ISTQB Technique | Description |
| :--- | :--- | :--- | :--- |
| **TC-006** | Cart Stress Test | **1️⃣ Boundary Value Analysis (BVA)** | Test cart with 1, 50, 100 (boundary) unique items. |
| **TC-010** | Checkout Session Timeout | **3️⃣ State Transition Testing** | Test transition from Active Session → Timed Out → Login Required. |
| **TC-011** | User Registration Inputs | **1️⃣ Boundary Value Analysis (BVA)** | Test name/password fields with min/max character lengths. |
| **TC-016** | Malicious Input Injection | **2️⃣ Equivalence Partitioning (EP)** | Partition inputs into Safe vs. Malicious (SQL/XSS payloads). |
| **TC-017** | Out of Stock Handling | **3️⃣ State Transition Testing** | Verify state change: In Stock → Out of Stock → Add to Cart Disabled. |
| **TC-020** | Accessibility Compliance | **4️⃣ Configuration Testing** | Verify compliance with WCAG 2.1 AA configuration standards. |
