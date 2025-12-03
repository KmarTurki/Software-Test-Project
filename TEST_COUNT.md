# Test Count Quick Reference

## Test Files and Test Counts

| File | Test Functions | Notes |
|------|----------------|-------|
| `test_01_configuration.py` | 2 | `test_responsive_layout` is parametrized (runs 3x) |
| `test_02_bva_ep.py` | 3 | BVA and EP tests |
| `test_03_state_transition.py` | 2 | State transition tests |
| `test_04_additional_bva_ep.py` | 6 | Additional BVA/EP tests |
| `test_05_additional_state.py` | 5 | Additional state tests |
| `test_06_additional_config.py` | 7 | Additional config tests |

**Total Test Functions**: 25
**Total Test Executions**: 27 (due to parametrization)

## List of All Test Functions

### test_01_configuration.py (2 functions, 4 executions)
1. `test_responsive_layout` - Parametrized with 3 viewports (Desktop, Tablet, Mobile)
2. `test_cross_browser_compatibility`

### test_02_bva_ep.py (3 functions)
3. `test_search_bva`
4. `test_cart_quantity_bva`
5. `test_contact_form_ep`

### test_03_state_transition.py (2 functions)
6. `test_cart_state_transition`
7. `test_login_state_transition`

### test_04_additional_bva_ep.py (6 functions)
8. `test_product_price_filter_ep`
9. `test_registration_form_bva`
10. `test_wishlist_functionality_ep`
11. `test_product_comparison_bva`
12. `test_checkout_form_validation_ep`
13. `test_negative_quantity_bva`

### test_05_additional_state.py (5 functions)
14. `test_product_category_navigation_state`
15. `test_account_dashboard_navigation_state`
16. `test_guest_checkout_flow_state`
17. `test_session_timeout_state`
18. `test_out_of_stock_state`

### test_06_additional_config.py (7 functions)
19. `test_firefox_compatibility`
20. `test_edge_compatibility` (skipped by default)
21. `test_mobile_landscape_orientation`
22. `test_tablet_portrait_orientation`
23. `test_large_desktop_resolution`
24. `test_page_load_performance`
25. `test_accessibility_basic_checks`

## Running the Tests

To see all collected tests:
```bash
python -m pytest --collect-only tests/
```

To run all tests:
```bash
python -m pytest tests/ -v
```
