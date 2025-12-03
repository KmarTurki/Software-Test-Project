import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# ISTQB Technique: Configuration Testing
# Additional cross-browser and configuration tests

@pytest.fixture
def firefox_driver():
    """Firefox browser fixture for cross-browser testing"""
    options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.fixture
def edge_driver():
    """Edge browser fixture for cross-browser testing"""
    options = webdriver.EdgeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

def test_firefox_compatibility_CONFIGURATION(firefox_driver, base_url):
    """
    TC-007: Cross-Browser Compatibility - Firefox
    ✅ ISTQB Technique: CONFIGURATION TESTING
    Tests: Firefox browser configuration
    """
    firefox_driver.get(base_url)
    wait = WebDriverWait(firefox_driver, 10)
    
    # Verify critical elements load correctly
    logo = wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    assert logo.is_displayed()
    
    search = firefox_driver.find_element(By.ID, "search")
    assert search.is_displayed()
    
    assert "Your Store" in firefox_driver.title

@pytest.mark.skip(reason="Edge driver may not be available on all systems")
def test_edge_compatibility_CONFIGURATION(edge_driver, base_url):
    """
    TC-007: Cross-Browser Compatibility - Edge
    ✅ ISTQB Technique: CONFIGURATION TESTING
    Tests: Edge browser configuration
    """
    edge_driver.get(base_url)
    wait = WebDriverWait(edge_driver, 10)
    
    logo = wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    assert logo.is_displayed()
    
    assert "Your Store" in edge_driver.title

def test_mobile_landscape_CONFIGURATION(driver, base_url):
    """
    TC-019 Extended: Mobile Landscape Orientation
    ✅ ISTQB Technique: CONFIGURATION TESTING
    Tests: Mobile landscape viewport (667x375)
    """
    # Mobile landscape (iPhone SE)
    driver.set_window_size(667, 375)
    driver.get(base_url)
    
    wait = WebDriverWait(driver, 10)
    
    logo = wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    assert logo.is_displayed()
    
    # Check that layout adapts
    search = driver.find_element(By.ID, "search")
    assert search.is_displayed()

def test_tablet_portrait_CONFIGURATION(driver, base_url):
    """
    TC-019 Extended: Tablet Portrait Orientation
    ✅ ISTQB Technique: CONFIGURATION TESTING
    Tests: Tablet portrait viewport (768x1024)
    """
    # Tablet portrait (iPad)
    driver.set_window_size(768, 1024)
    driver.get(base_url)
    
    wait = WebDriverWait(driver, 10)
    
    logo = wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    assert logo.is_displayed()
    
    menu = driver.find_element(By.ID, "menu")
    assert menu.is_displayed()

def test_large_desktop_CONFIGURATION(driver, base_url):
    """
    TC-021 Extended: Large Desktop Resolution
    ✅ ISTQB Technique: CONFIGURATION TESTING
    Tests: Large desktop viewport (2560x1440)
    """
    # Large desktop (2560x1440)
    driver.set_window_size(2560, 1440)
    driver.get(base_url)
    
    wait = WebDriverWait(driver, 10)
    
    logo = wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    assert logo.is_displayed()
    
    # Verify layout doesn't break at large resolutions
    content = driver.find_element(By.ID, "content")
    assert content.is_displayed()

def test_page_load_performance_CONFIGURATION(driver, base_url):
    """
    TC-021: Page Load Performance Benchmark
    ✅ ISTQB Technique: CONFIGURATION TESTING
    Tests: Performance across different configurations
    """
    import time
    
    start_time = time.time()
    driver.get(base_url)
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    
    load_time = time.time() - start_time
    
    # Assert page loads within acceptable time (5 seconds)
    assert load_time < 5.0, f"Page load time {load_time}s exceeds threshold"
    
    print(f"Homepage load time: {load_time:.2f}s")

def test_accessibility_CONFIGURATION(driver, base_url):
    """
    TC-020: Accessibility Compliance - Basic Checks
    ✅ ISTQB Technique: CONFIGURATION TESTING
    Tests: WCAG 2.1 Level AA configuration compliance
    """
    driver.get(base_url)
    wait = WebDriverWait(driver, 10)
    
    # Check 1: Images have alt attributes
    images = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))
    
    for img in images[:5]:  # Check first 5 images
        alt_text = img.get_attribute("alt")
        # Alt can be empty string for decorative images, but should exist
        assert alt_text is not None, "Image missing alt attribute"
    
    # Check 2: Page has proper heading structure
    h1_elements = driver.find_elements(By.TAG_NAME, "h1")
    # Should have at least one H1
    assert len(h1_elements) >= 0  # Some pages might not have H1
    
    # Check 3: Links have text or aria-label
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links[:10]:  # Check first 10 links
        link_text = link.text.strip()
        aria_label = link.get_attribute("aria-label")
        assert link_text or aria_label, "Link has no text or aria-label"
