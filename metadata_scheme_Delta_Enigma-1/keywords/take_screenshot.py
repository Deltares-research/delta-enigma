"""
Script to take a screenshot of the keyword hierarchy visualization.
Requires selenium and a webdriver (e.g., chromedriver).
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def take_screenshot(html_file, output_file, width=1200, height=800):
    """Take a screenshot of an HTML file using Selenium."""
    # Get the absolute path of the HTML file
    html_path = os.path.abspath(html_file)
    
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument(f"--window-size={width},{height}")
    
    # Initialize the driver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Load the HTML file
    driver.get(f"file://{html_path}")
    
    # Wait for the page to load
    time.sleep(2)
    
    # Expand the first few categories
    driver.execute_script("""
        const initialCategories = document.querySelectorAll('.category');
        for (let i = 0; i < Math.min(3, initialCategories.length); i++) {
            initialCategories[i].querySelector('.category-content').classList.add('active');
        }
    """)
    
    # Wait for the categories to expand
    time.sleep(1)
    
    # Take the screenshot
    driver.save_screenshot(output_file)
    
    # Close the driver
    driver.quit()
    
    print(f"Screenshot saved to {output_file}")

if __name__ == "__main__":
    # Path to the HTML file
    html_file = "keyword_hierarchy.html"
    
    # Path to the output file
    output_file = "keyword_hierarchy_screenshot.png"
    
    # Take the screenshot
    take_screenshot(html_file, output_file) 