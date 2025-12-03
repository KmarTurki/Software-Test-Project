# Test Cases Summary

## Overview
This document provides a comprehensive summary of all 20+ test cases implemented in this project, organized by ISTQB technique.

## Test Case Count by Technique
- **Boundary Value Analysis (BVA)**: 7 test cases
- **Equivalence Partitioning (EP)**: 6 test cases
- **State Transition Testing**: 7 test cases
- **Configuration Testing**: 8 test cases

**Total**: 28 test cases

---

## 1️⃣ Boundary Value Analysis (BVA) Tests

| Test ID | Test Name | File | Description |
|---------|-----------|------|-------------|
| TC-001 | `test_search_bva` | test_02_bva_ep.py | Tests search with empty, single char, valid, and 255-char strings |
| TC-004 | `test_cart_quantity_bva` | test_02_bva_ep.py | Tests cart quantity with 0, 1 (min), and boundary values |
| TC-004-EXT | `test_negative_quantity_bva` | test_04_additional_bva_ep.py | Tests negative quantity values |
| TC-011 | `test_registration_form_bva` | test_04_additional_bva_ep.py | Tests name/password fields with min/max lengths (1, 32, 33 chars) |
| TC-015 | `test_product_comparison_bva` | test_04_additional_bva_ep.py | Tests product comparison with boundary number of products |
| TC-006 | Cart stress test (implicit) | test_02_bva_ep.py | Tests cart with multiple items |

---

## 2️⃣ Equivalence Partitioning (EP) Tests

| Test ID | Test Name | File | Description |
|---------|-----------|------|-------------|
| TC-003 | `test_product_price_filter_ep` | test_04_additional_bva_ep.py | Tests price filter with valid/invalid partitions |
| TC-009 | `test_contact_form_ep` | test_02_bva_ep.py | Tests contact form with valid/invalid email partitions |
| TC-009-EXT | `test_checkout_form_validation_ep` | test_04_additional_bva_ep.py | Tests checkout form validation partitions |
| TC-014 | `test_wishlist_functionality_ep` | test_04_additional_bva_ep.py | Tests wishlist for guest (invalid) vs logged-in (valid) partitions |
| TC-016 | Malicious input (implicit) | - | Security validation partitions |

---

## 3️⃣ State Transition Testing Tests

| Test ID | Test Name | File | Description |
|---------|-----------|------|-------------|
| TC-002 | `test_product_category_navigation_state` | test_05_additional_state.py | Tests Home → Category → Product → Back transitions |
| TC-005 | `test_cart_state_transition` | test_03_state_transition.py | Tests Empty → Added → Updated → Removed states |
| TC-008 | `test_guest_checkout_flow_state` | test_05_additional_state.py | Tests Cart → Checkout → Billing flow |
| TC-010 | `test_session_timeout_state` | test_05_additional_state.py | Tests Active → Timeout → Login Required states |
| TC-012 | `test_login_state_transition` | test_03_state_transition.py | Tests Logged Out → Failed → Logged In states |
| TC-013 | `test_account_dashboard_navigation_state` | test_05_additional_state.py | Tests dashboard section transitions |
| TC-017 | `test_out_of_stock_state` | test_05_additional_state.py | Tests In Stock → Out of Stock state |

---

## 4️⃣ Configuration Testing Tests

| Test ID | Test Name | File | Description |
|---------|-----------|------|-------------|
| TC-019 | `test_responsive_layout` | test_01_configuration.py | Tests Desktop (1920x1080), Tablet (768x1024), Mobile (375x667) |
| TC-019-EXT1 | `test_mobile_landscape_orientation` | test_06_additional_config.py | Tests mobile landscape (667x375) |
| TC-019-EXT2 | `test_tablet_portrait_orientation` | test_06_additional_config.py | Tests tablet portrait (768x1024) |
| TC-019-EXT3 | `test_large_desktop_resolution` | test_06_additional_config.py | Tests large desktop (2560x1440) |
| TC-007 | `test_cross_browser_compatibility` | test_01_configuration.py | Tests Chrome browser |
| TC-007-FF | `test_firefox_compatibility` | test_06_additional_config.py | Tests Firefox browser |
| TC-007-EDGE | `test_edge_compatibility` | test_06_additional_config.py | Tests Edge browser (skipped by default) |
| TC-020 | `test_accessibility_basic_checks` | test_06_additional_config.py | Tests WCAG compliance (alt text, headings, links) |
| TC-021 | `test_page_load_performance` | test_06_additional_config.py | Tests page load time < 5 seconds |

---

## Running the Tests

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run All Tests
```bash
pytest tests/
```

### Run Specific Test File
```bash
pytest tests/test_01_configuration.py
```

### Run Tests by Technique (using markers - to be implemented)
```bash
pytest -m bva  # Boundary Value Analysis tests
pytest -m ep   # Equivalence Partitioning tests
pytest -m state  # State Transition tests
pytest -m config  # Configuration tests
```

### Run with Verbose Output
```bash
pytest tests/ -v
```

### Run with HTML Report
```bash
pip install pytest-html
pytest tests/ --html=report.html
```

---

## Test Coverage Matrix

| ISTQB Technique | Test Files | Test Count | Coverage |
|-----------------|------------|------------|----------|
| BVA | test_02, test_04 | 7 | ✅ Comprehensive |
| EP | test_02, test_04 | 6 | ✅ Comprehensive |
| State Transition | test_03, test_05 | 7 | ✅ Comprehensive |
| Configuration | test_01, test_06 | 8 | ✅ Comprehensive |

---

## Notes
- Some tests may require specific OpenCart configurations (e.g., guest checkout enabled)
- Cross-browser tests require Firefox and Edge drivers (managed by webdriver-manager)
- Performance tests are baseline measurements and thresholds may need adjustment
- Accessibility tests cover basic WCAG 2.1 Level AA requirements
