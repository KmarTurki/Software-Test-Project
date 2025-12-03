# Suite 2: Responsive Design Suite

**Objective:** Ensure proper rendering and functionality across device resolutions
**Priority:** Medium
**Execution Environment:** Desktop (1920x1080), Tablet (768x1024), Mobile (375x667)

## Test Cases & ISTQB Techniques

| Test Case ID | Title | ISTQB Technique | Description |
| :--- | :--- | :--- | :--- |
| **TC-004** | Add to Cart - Quantity | **1️⃣ Boundary Value Analysis (BVA)** | Validate quantity inputs: 0 (min-1), 1 (min), 999 (max), 1000 (max+1). |
| **TC-008** | Guest Checkout Flow | **3️⃣ State Transition Testing** | Validate flow states: Cart → Billing → Payment → Confirmation. |
| **TC-013** | Account Dashboard Navigation | **3️⃣ State Transition Testing** | Verify transitions between dashboard sections (Orders, Wishlist, Address). |
| **TC-018** | Network Error Handling | **3️⃣ State Transition Testing** | Test system behavior during network failure states in checkout. |
| **TC-021** | Page Load Performance | **4️⃣ Configuration Testing** | Measure load times across different viewports (Mobile vs Desktop). |
