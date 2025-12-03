import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ISTQB Technique: State Transition Testing

def test_cart_STATE_TRANSITION(driver, base_url):
    """
    TC-005: Update Cart Quantity - State Transition
    ✅ ISTQB Technique: STATE TRANSITION TESTING
    States: Empty Cart → Item Added → Quantity Updated → Item Removed
    """
    driver.get(base_url)
    wait = WebDriverWait(driver, 10)
    
    # State 1: Empty Cart (Initial) - Assumed

    # Transition -> State 2: Add Item
    driver.get(f"{base_url}/index.php?route=product/product&product_id=43") # MacBook
    
    add_btn = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    add_btn.click()
    
    success_alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
    assert success_alert.is_displayed()
    
    # Go to Cart
    driver.get(f"{base_url}/index.php?route=checkout/cart")
    
    cart_item = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "MacBook")))
    assert cart_item.is_displayed()

    # Transition -> State 3: Update Quantity
    qty_input = driver.find_element(By.CSS_SELECTOR, "input[name^='quantity']")
    qty_input.clear()
    qty_input.send_keys("2")
    
    update_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    update_btn.click()
    
    # Verify update (State 3)
    success_alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
    assert success_alert.is_displayed()
    
    # Transition -> State 4: Remove Item
    # Note: The remove button might be inside a form or table cell
    remove_btn = driver.find_element(By.CSS_SELECTOR, "button.btn-danger")
    remove_btn.click()
    
    # Verify Empty (State 4)
    # Wait for the empty message
    empty_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Your shopping cart is empty!')]")))
    assert empty_msg.is_displayed()

def test_login_STATE_TRANSITION(driver, base_url):
    """
    TC-012: Login Functionality - State Transition
    ✅ ISTQB Technique: STATE TRANSITION TESTING
    States: Logged Out → Login Failed → (Logged In)
    """
    driver.get(f"{base_url}/index.php?route=account/login")
    wait = WebDriverWait(driver, 10)
    
    # State: Logged Out
    
    # Transition -> Login Failed
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "input-email")))
    email_input.send_keys("wrong@email.com")
    
    pass_input = driver.find_element(By.ID, "input-password")
    pass_input.send_keys("wrongpass")
    
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()
    
    error_alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
    assert error_alert.is_displayed()
    
    # Transition -> Logged In (Skipped as per previous plan to avoid dependency)
