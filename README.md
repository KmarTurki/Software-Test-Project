# Software Test Project: OpenCart Automation Framework

## 📋 Project Overview

A comprehensive **ISTQB-compliant Black-Box Test Automation Framework** for OpenCart E-commerce Platform, implementing all four key ISTQB testing techniques with **25 test functions** covering **28 test cases**.

**Test Target**: [tutorialsninja.com/demo](https://tutorialsninja.com/demo/)

> **Why tutorialsninja?** The official demo.opencart.com uses Cloudflare bot protection that blocks Selenium. Tutorialsninja provides the same functionality without restrictions.

**Key Metrics:**
- ✅ 25 automated test functions
- ✅ 28 documented test cases
- ✅ 4 ISTQB techniques applied
- ✅ 6 test files organized by technique
- ✅ Cross-browser & responsive testing

---

## 🎯 ISTQB Techniques Applied

### 1️⃣ Boundary Value Analysis (BVA)
Testing boundaries of input ranges where errors are most likely.
- **Examples**: Cart quantity (0, 1, 999, 1000), search length (empty, 1 char, 255 chars), form fields (min/max)
- **7 test cases** in `test_02_bva_ep.py` and `test_04_additional_bva_ep.py`

### 2️⃣ Equivalence Partitioning (EP)
Grouping inputs into valid/invalid partitions.
- **Examples**: Email formats, price ranges, user roles (guest vs logged-in)
- **6 test cases** in `test_02_bva_ep.py` and `test_04_additional_bva_ep.py`

### 3️⃣ State Transition Testing
Validating system behavior through state changes.
- **Examples**: Cart flow (Empty → Added → Updated → Removed), Login flow, Checkout process
- **7 test cases** in `test_03_state_transition.py` and `test_05_additional_state.py`

### 4️⃣ Configuration Testing
Verifying functionality across different configurations.
- **Examples**: Cross-browser (Chrome, Firefox, Edge), Responsive (Desktop, Tablet, Mobile)
- **8 test cases** in `test_01_configuration.py` and `test_06_additional_config.py`

---

## 📁 Project Structure

```
Software-Test-Project/
├── tests/
│   ├── conftest.py                    # Pytest fixtures & configuration
│   ├── test_01_configuration.py       # Configuration tests (2 functions)
│   ├── test_02_bva_ep.py             # BVA & EP tests (3 functions)
│   ├── test_03_state_transition.py   # State transition tests (2 functions)
│   ├── test_04_additional_bva_ep.py  # Additional BVA/EP (6 functions)
│   ├── test_05_additional_state.py   # Additional state tests (5 functions)
│   ├── test_06_additional_config.py  # Additional config tests (7 functions)
│   └── suites/                        # Test suite documentation
│       ├── cross_browser_suite.md
│       ├── responsive_design_suite.md
│       ├── performance_load_suite.md
│       └── stress_resilience_suite.md
└── README.md                          # This file
```

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/KmarTurki/Software-Test-Project.git
cd Software-Test-Project

# Install dependencies
pip install pytest selenium webdriver-manager
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_01_configuration.py

# Run specific test
pytest tests/test_02_bva_ep.py::test_search_bva

# Generate HTML report
pip install pytest-html
pytest tests/ --html=report.html

# View all tests
pytest --collect-only tests/
```

---

## 📊 Test Coverage Summary

### By ISTQB Technique

| Technique | Files | Count | Status |
|-----------|-------|-------|--------|
| **BVA** | test_02, test_04 | 7 | ✅ Comprehensive |
| **EP** | test_02, test_04 | 6 | ✅ Comprehensive |
| **State Transition** | test_03, test_05 | 7 | ✅ Comprehensive |
| **Configuration** | test_01, test_06 | 8 | ✅ Comprehensive |

### Complete Test List

<details>
<summary><b>Click to expand all 25 test functions</b></summary>

**Configuration Tests (2 functions)**
1. `test_responsive_layout` - Desktop/Tablet/Mobile (parametrized 3x)
2. `test_cross_browser_compatibility` - Chrome

**BVA & EP Tests (3 functions)**
3. `test_search_bva` - Search boundary values
4. `test_cart_quantity_bva` - Cart quantity boundaries
5. `test_contact_form_ep` - Email validation partitions

**State Transition Tests (2 functions)**
6. `test_cart_state_transition` - Cart state flow
7. `test_login_state_transition` - Login state flow

**Additional BVA/EP Tests (6 functions)**
8. `test_product_price_filter_ep` - Price filter partitions
9. `test_registration_form_bva` - Registration boundaries
10. `test_wishlist_functionality_ep` - Wishlist partitions
11. `test_product_comparison_bva` - Comparison boundaries
12. `test_checkout_form_validation_ep` - Checkout validation
13. `test_negative_quantity_bva` - Negative quantity handling

**Additional State Tests (5 functions)**
14. `test_product_category_navigation_state` - Category navigation
15. `test_account_dashboard_navigation_state` - Dashboard navigation
16. `test_guest_checkout_flow_state` - Guest checkout flow
17. `test_session_timeout_state` - Session timeout handling
18. `test_out_of_stock_state` - Stock state transitions

**Additional Configuration Tests (7 functions)**
19. `test_firefox_compatibility` - Firefox browser
20. `test_edge_compatibility` - Edge browser (skipped)
21. `test_mobile_landscape_orientation` - Mobile landscape
22. `test_tablet_portrait_orientation` - Tablet portrait
23. `test_large_desktop_resolution` - Large desktop (2560x1440)
24. `test_page_load_performance` - Page load < 5s
25. `test_accessibility_basic_checks` - WCAG compliance

</details>

---

## 🗺️ Building Your Own Framework

Want to create a similar ISTQB-compliant framework? Follow this roadmap:

### Phase 1: Setup (Week 1)
1. **Choose test target** - E-commerce site, SaaS platform, etc.
2. **Set up environment** - Python, pytest, selenium, webdriver-manager
3. **Create structure** - tests/, conftest.py, requirements.txt

### Phase 2: Architecture (Week 1-2)
4. **Define test architecture** - SUT, test levels, risk analysis, scope
5. **Design test cases** - Identify scenarios for each ISTQB technique

### Phase 3: Implementation (Week 2-4)
6. **Configure pytest** - Create fixtures for driver and base_url
7. **Implement tests** - Start with Configuration, then BVA/EP, finally State Transition
8. **Follow conventions** - Use technique suffixes (_BVA, _EP, _STATE, _CONFIG)

### Phase 4: Documentation (Week 4)
9. **Document everything** - README, architecture, test cases
10. **Add quality checks** - HTML reports, coverage analysis

### Success Metrics
- ✅ 20+ test cases covering all 4 ISTQB techniques
- ✅ Clear naming with technique markers
- ✅ Comprehensive documentation
- ✅ Fully automated with Selenium + Pytest

**Estimated Time**: 35-45 hours total

---

## 📚 Detailed Reference Guide

### Test Architecture

**System Under Test (SUT)**
- Application: OpenCart E-commerce Platform
- URL: https://tutorialsninja.com/demo/
- Type: Web-based online store
- Access: Black-box testing
- Browsers: Chrome, Firefox, Edge

**Test Scope**
- ✅ In Scope: Product browsing, cart operations, checkout, user accounts, search, wishlist, form validation, cross-browser, responsive design, performance
- ❌ Out of Scope: Admin panel, database testing, live payment transactions, email server, source code review, advanced security testing

**Risk Analysis** (8 identified risks)
- High Priority: Payment failures, session timeouts, inventory sync, performance degradation
- Medium Priority: Cross-browser issues, cart data loss, mobile responsiveness, search accuracy

### Test Suites

**Suite 1: Cross-Browser Compatibility** (High Priority)
- Chrome 120+, Firefox 121+, Edge 120+
- Test Cases: TC-001, TC-002, TC-003, TC-007, TC-012, TC-015

**Suite 2: Responsive Design** (Medium Priority)
- Desktop (1920x1080), Tablet (768x1024), Mobile (375x667)
- Test Cases: TC-004, TC-008, TC-013, TC-018, TC-021

**Suite 3: Performance & Load** (High Priority)
- 10-50 concurrent users
- Test Cases: TC-005, TC-009, TC-014, TC-019, TC-022

**Suite 4: Stress & Resilience** (Medium Priority)
- 100+ users, boundary inputs
- Test Cases: TC-006, TC-010, TC-011, TC-016, TC-017, TC-020, TC-023

### Cloudflare Workaround

**Problem**: demo.opencart.com blocks Selenium with bot detection

**Solution**: Use tutorialsninja.com/demo (same functionality, no blocking)

**Alternatives if needed**:
- **Option A**: Manually solve Cloudflare challenge when it appears
- **Option B**: Use local OpenCart instance via Docker
  ```bash
  docker run -d -p 8080:80 bitnami/opencart:latest
  ```
- **Option C**: Use Selenium Grid with residential proxies (BrowserStack, Sauce Labs)

### Best Practices

1. **Use explicit waits** - `WebDriverWait` instead of `time.sleep()`
2. **Keep tests independent** - Each test runs standalone
3. **Meaningful assertions** - Clear error messages
4. **Page Object Model** - For larger projects
5. **CI/CD integration** - GitHub Actions, Jenkins
6. **Document workarounds** - Track special configurations

---

## 📖 Additional Documentation

- **tests/suites/** - Detailed test suite specifications for each testing category

---

## 🤝 Contributing

This project demonstrates ISTQB best practices for black-box test automation. Feel free to use it as a reference for your own testing projects.

**Repository**: [github.com/KmarTurki/Software-Test-Project](https://github.com/KmarTurki/Software-Test-Project)

---

**Built with**: Python • Pytest • Selenium • ISTQB Principles
