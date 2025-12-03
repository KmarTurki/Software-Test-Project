# Suite 1: Cross-Browser Compatibility Suite

**Objective:** Validate consistent functionality across different browsers
**Priority:** High
**Execution Environment:** Chrome 120+, Firefox 121+, Edge 120+

## Test Cases & ISTQB Techniques

| Test Case ID | Title | ISTQB Technique | Description |
| :--- | :--- | :--- | :--- |
| **TC-001** | Product Search with Boundary Value Analysis | **1️⃣ Boundary Value Analysis (BVA)** | Validate search with empty, single char, max length (255), and exceeded length strings. |
| **TC-002** | Product Category Navigation | **3️⃣ State Transition Testing** | Verify navigation states: Home → Category → Subcategory → Product and back. |
| **TC-003** | Product Filtering | **2️⃣ Equivalence Partitioning (EP)** | Test price filters with valid ranges ($0-$100) and invalid partitions (negative, text). |
| **TC-007** | Cart Persistence Across Browser Sessions | **4️⃣ Configuration Testing** | Verify cart state persists when closing and reopening different browsers. |
| **TC-012** | Login Functionality | **3️⃣ State Transition Testing** | Test transitions: Logged Out → Login Attempt → Logged In or Failed. |
| **TC-015** | Product Comparison | **1️⃣ Boundary Value Analysis (BVA)** | Test comparison limits: 1 (min), 4 (max), 5 (exceed). |
