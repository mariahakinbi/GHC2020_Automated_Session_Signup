from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions

import time

home_page = 'https://web.cvent.com/event/84f26b13-25ef-458c-9d38-38432d71be09/summary?rp=00000000-0000-0000-0000-000000000000#'
# website
# opts = Options()
# opts.set_headless()
# assert opts.headless  # Operating in headless mode
driver = Firefox()
driver.get(home_page)


def login():
    # click "already registered?"
    already_registered_elem = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "Button__inlineBlock___2Yr-P")))
    already_registered_elem.click()
    # enter credentials; read credentials file; if no credentials then ask for user input
    email_addr_elem = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "emailAddress")))
    email_addr_elem.send_keys(input('ENTER EMAIL: '))

    confirm_nbr_elem = driver.find_element_by_id('confirmationNumber')
    confirm_nbr_elem.send_keys(input('ENTER CONFIRMATION NUMBER: '))
    # driver.find_element_by_xpath('/html/body/div/div/div[2]/span/div/div/div/div[2]/div/div/div/div[2]/span/div/div/div/button')
    submit_btn_elem = driver.find_element_by_css_selector(
        '.AlreadyRegisteredDialog__panel___3JH8a > div:nth-child(1) > div:nth-child(1) > button:nth-child(5)')
    submit_btn_elem.click()
    # driver.find_element_by_link_text('Submit')
    print('LOGGED IN!')


def get_to_session_page():
    # click modify registration
    modify_reg_elem = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[.='Modify Registration']")))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    modify_reg_elem.click()
    

    # personal info
    time.sleep(5)
    next_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "forward")))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    next_btn.click()
    
    # registration items
    time.sleep(5)
    # wait.until(EC.refreshed(EC.stalenessOf("forward")));
    next_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "forward")))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    next_btn.click()

    time.sleep(5)
    next_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "forward")))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    next_btn.click()

    print('SESSIONS LISTED')

# fill in sessions.ini


def search_availability(session_name):
    # sarch for seimar page for availability

    # generator for name and availability
    session_names = ['']
    session_availability = ''
    # search by button text

    # search by div attribute

    # add results to df
    print('searching for sessions')


def send_email():
    # send ( p r e t t y ) email if session available/not available
    print('sending email')

# lint code


def main():
    login()
    get_to_session_page()
    search_availability('INSERT_SESSION_NAME')
    send_email()
    # driver.close()


main()
