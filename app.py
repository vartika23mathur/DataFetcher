from flask import Flask, render_template, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    case_type = data['case_type']
    case_no = data['case_no']
    case_year = data['case_year']

    options = Options()
    options.add_argument('--headless=new')  # Use new headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://delhihighcourt.nic.in/app/get-case-type-status")
        time.sleep(2)

        # Fill form
        dropdown = driver.find_element(By.ID, "case_type")
        for option in dropdown.find_elements(By.TAG_NAME, "option"):
            if option.get_attribute("value").strip() == case_type.strip():
                option.click()
                break

        driver.find_element(By.ID, "case_number").send_keys(case_no)

        year_dropdown = driver.find_element(By.ID, "case_year")
        for option in year_dropdown.find_elements(By.TAG_NAME, "option"):
            if option.get_attribute("value").strip() == case_year.strip():
                option.click()
                break

        # Read CAPTCHA text from visible span
        captcha_text = driver.find_element(By.ID, "captcha-code").text
        driver.find_element(By.ID, "captchaInput").send_keys(captcha_text)

        # Click submit using JS to avoid interception error
        wait = WebDriverWait(driver, 10)
        submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Submit"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", submit_btn)

        # Wait for result table to load
        time.sleep(5)
        case_rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

        if not case_rows:
            return jsonify({"error": "No case data found."})

        header = [col.text for col in case_rows[0].find_elements(By.TAG_NAME, "th")]
        if not header:
            header = [col.text for col in driver.find_elements(By.CSS_SELECTOR, "table thead th")]

        rows = []
        for row in case_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells:
                rows.append([cell.text.strip() for cell in cells])

        return jsonify({"header": header, "rows": rows})

    except Exception as e:
        return jsonify({"error": str(e)})

    finally:
        driver.quit()

if __name__ == "__main__":
    app.run(debug=True)
