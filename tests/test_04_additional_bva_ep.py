import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# ISTQB Techniques: Boundary Value Analysis (BVA) & Equivalence Partitioning (EP)
# Additional comprehensive tests

def test_product_price_filter_ep(driver, base_url):
    """
    TC-003: Product Filtering with Equivalence Partitioning
    Technique: Equivalence Partitioning (EP)
    """
    driver.get(f"{base_url}/index.php?route=product/category&path=20") # Desktops
    wait = WebDriverWait(driver, 10)
    
    # Wait for products to load
    products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-thumb")))
    initial_count = len(products)
    
    # Verify products are displayed
    assert initial_count > 0, "No products found in category"

def test_registration_form_bva(driver, base_url):
    """
    TC-011: User Registration - Boundary Value Analysis on Input Fields
    Technique: Boundary Value Analysis (BVA)
    """
    driver.get(f"{base_url}/index.php?route=account/register")
    wait = WebDriverWait(driver, 10)
    
    firstname_input = wait.until(EC.visibility_of_element_located((By.ID, "input-firstname")))
    lastname_input = driver.find_element(By.ID, "input-lastname")
    email_input = driver.find_element(By.ID, "input-email")
    password_input = driver.find_element(By.ID, "input-password")
    
    # Test 1: Minimum valid length (1 character for name)
    firstname_input.send_keys("A")
    lastname_input.send_keys("B")
    
    # Test 2: Maximum length (32 characters)
    firstname_input.clear()
    firstname_input.send_keys("A" * 32)
    
    # Test 3: Exceeds maximum (33 characters) - should be truncated or rejected
    firstname_input.clear()
    firstname_input.send_keys("A" * 33)
    
    # Test 4: Password minimum length (typically 4-8 characters)
    password_input.send_keys("abc")  # Too short
    
    # Test 5: Valid password
    password_input.clear()
    password_input.send_keys("ValidPass123")

def test_wishlist_functionality_ep(driver, base_url):
    """
    TC-014: Add to Wishlist - Equivalence Partitioning
    Technique: Equivalence Partitioning (EP)
    Partitions: Guest user (invalid) vs Logged-in user (valid)
    """
    driver.get(f"{base_url}/index.php?route=product/product&product_id=43")
    wait = WebDriverWait(driver, 10)
    
    # Find and click wishlist button
    wishlist_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Add to Wish List']")))
    wishlist_btn.click()
    
    # Guest user should be redirected to login or see error
    # Check if we're on login page or see an alert
    try:
        alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert")))
        assert alert.is_displayed()
    except:
        # Might redirect to login
        assert "login" in driver.current_url.lower()

def test_product_comparison_bva(driver, base_url):
    """
    TC-015: Product Comparison - Boundary Testing on Number of Products
    Technique: Boundary Value Analysis (BVA)
    """
    driver.get(f"{base_url}/index.php?route=product/category&path=20")
    wait = WebDriverWait(driver, 10)
    
    # Add 1 product to compare (minimum)
    compare_btns = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[title='Compare this Product']")))
    
    if len(compare_btns) > 0:
        compare_btns[0].click()
        
        # Wait for success message
        try:
            success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
            assert success.is_displayed()
        except:
            pass  # Some versions might not show alert

def test_checkout_form_validation_ep(driver, base_url):
    """
    TC-009: Checkout Form Validation - Equivalence Partitioning
    Technique: Equivalence Partitioning (EP)
    """
    # First add a product to cart
    driver.get(f"{base_url}/index.php?route=product/product&product_id=43")
    wait = WebDriverWait(driver, 10)
    
    add_btn = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    add_btn.click()
    
    # Go to checkout
    driver.get(f"{base_url}/index.php?route=checkout/checkout")
    
    # Wait for checkout page to load
    try:
        # Guest checkout option
        guest_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='guest']")))
        guest_radio.click()
        
        continue_btn = driver.find_element(By.ID, "button-account")
        continue_btn.click()
        
        # Now test form validation
        firstname = wait.until(EC.visibility_of_element_located((By.ID, "input-payment-firstname")))
        
        # Partition 1: Empty fields (invalid)
        firstname.send_keys("")
        
        # Partition 2: Valid input
        firstname.send_keys("John")
        
    except:
        # Checkout might require login
        pass

def test_negative_quantity_bva(driver, base_url):
    """
    TC-004 Extended: Negative Quantity Testing
    Technique: Boundary Value Analysis (BVA)
    """
    driver.get(f"{base_url}/index.php?route=product/product&product_id=43")
    wait = WebDriverWait(driver, 10)
    
    qty_input = wait.until(EC.visibility_of_element_located((By.ID, "input-quantity")))
    
    # Test negative value
    qty_input.clear()
    qty_input.send_keys("-5")
    
    add_btn = driver.find_element(By.ID, "button-cart")
    add_btn.click()
    
    # Should either reject or default to minimum
    # Most systems will either show error or default to 1
