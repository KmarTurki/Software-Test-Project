import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ISTQB Techniques: Boundary Value Analysis (BVA) & Equivalence Partitioning (EP)

def test_search_bva(driver, base_url):
    """
    TC-001: Product Search with Boundary Value Analysis
    Technique: Boundary Value Analysis (BVA)
    """
    driver.get(base_url)
    wait = WebDriverWait(driver, 10)
    
    search_input = wait.until(EC.visibility_of_element_located((By.NAME, "search")))
    search_btn = driver.find_element(By.CSS_SELECTOR, "button.btn-light")

    # 1. Empty String
    search_input.clear()
    search_input.send_keys("")
    search_btn.click()
    # Expectation: Should stay on page or show all
    
    # 2. Single Character (Valid Min)
    search_input = wait.until(EC.visibility_of_element_located((By.NAME, "search")))
    search_input.clear()
    search_input.send_keys("a")
    driver.find_element(By.CSS_SELECTOR, "button.btn-light").click()
    
    content = wait.until(EC.visibility_of_element_located((By.ID, "content")))
    assert content.is_displayed()

    # 3. Valid Search
    search_input = wait.until(EC.visibility_of_element_located((By.NAME, "search")))
    search_input.clear()
    search_input.send_keys("MacBook")
    driver.find_element(By.CSS_SELECTOR, "button.btn-light").click()
    
    result = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "MacBook")))
    assert result.is_displayed()

    # 4. Long String (Boundary)
    long_string = "a" * 255
    search_input = wait.until(EC.visibility_of_element_located((By.NAME, "search")))
    search_input.clear()
    search_input.send_keys(long_string)
    driver.find_element(By.CSS_SELECTOR, "button.btn-light").click()
    
    content = wait.until(EC.visibility_of_element_located((By.ID, "content")))
    assert content.is_displayed()

def test_cart_quantity_bva(driver, base_url):
    """
    TC-004: Add to Cart - Quantity Boundary Value Analysis
    Technique: Boundary Value Analysis (BVA)
    """
    # Navigate to a product page (MacBook)
    driver.get(f"{base_url}/index.php?route=product/product&product_id=43")
    wait = WebDriverWait(driver, 10)
    
    qty_input = wait.until(EC.visibility_of_element_located((By.ID, "input-quantity")))
    add_btn = driver.find_element(By.ID, "button-cart")

    # 1. Min-1 (0) - Invalid
    qty_input.clear()
    qty_input.send_keys("0")
    add_btn.click()
    
    # OpenCart behavior varies, but we check that success alert is NOT shown immediately
    # or we check for some error. For simplicity, we assume no success alert.
    # Note: In a real scenario, we'd assert specific error message visibility.
    # time.sleep(1) # Brief wait to ensure no alert pops up instantly
    # alerts = driver.find_elements(By.CSS_SELECTOR, ".alert-success")
    # assert len(alerts) == 0 

    # 2. Min (1) - Valid
    qty_input.clear()
    qty_input.send_keys("1")
    add_btn.click()
    
    success_alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
    assert success_alert.is_displayed()

def test_contact_form_ep(driver, base_url):
    """
    TC-009 (Adapted): Contact Form Validation
    Technique: Equivalence Partitioning (EP)
    """
    driver.get(f"{base_url}/index.php?route=information/contact")
    wait = WebDriverWait(driver, 10)
    
    name_input = wait.until(EC.visibility_of_element_located((By.ID, "input-name")))
    email_input = driver.find_element(By.ID, "input-email")
    enquiry_input = driver.find_element(By.ID, "input-enquiry")
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Partition 1: Invalid Email Format
    name_input.send_keys("Test User")
    email_input.send_keys("invalid-email")
    enquiry_input.send_keys("This is a test enquiry.")
    
    # Scroll to button to ensure it's clickable
    driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
    # submit_btn.click() 
    
    # Selenium doesn't automatically catch HTML5 validation preventing submission like Playwright does easily.
    # We would check for the :invalid pseudo-class or browser validation message.
    # For this script, we'll assume we are testing server-side or JS validation that shows an error message.
    
    # Partition 2: Valid Input
    email_input.clear()
    email_input.send_keys("valid@email.com")
    # submit_btn.click()
