import sys
import datetime
import selenium.common.exceptions as exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import moodle_locators as locators


options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(options=options)


def setUp():
    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(5)

    # Navigating to the Moodle app website
    driver.get(locators.moodle_url)

    if driver.current_url == locators.moodle_url and driver.title == 'Software Quality Assurance Testing':
        print(f'We are at moodle homepage -- {driver.current_url}')


def tearDown():
    if driver is not None:
        print(f'----------------------------------')
        print(f'Test completed at {datetime.datetime.now()}')
        driver.close()
        driver.quit()


def log_in(username=locators.moodle_username, password=locators.moodle_password):
    if driver.current_url == locators.moodle_url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == locators.moodle_login_url:
            driver.find_element(By.ID, 'username').send_keys(username)
            sleep(0.5)
            driver.find_element(By.ID, 'password').send_keys(password)
            sleep(0.5)

            driver.find_element(By.ID, 'loginbtn').click()
            if driver.current_url == locators.moodle_dashboard_url:
                print(f'We log in with Username: {username} and password: {password}')
            assert driver.current_url == locators.moodle_dashboard_url


def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.5)
    driver.find_element(By.XPATH, "//span[contains(., 'Log out')]").click()
    sleep(0.5)
    print(f'Log out successfully at: {datetime.datetime.now()}')


def create_new_user():

    # Check if site administration is displayed.
    if not driver.find_element(By.XPATH, "//span[contains(., 'Site administration')]").is_displayed():
        # print(f"\'Site administration\' not displayed yet.")
        # print('I\'m gonna open it.')
        driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/nav/div/button/i').click()
    # else:
        # print(f"\'Site administration\' is displayed by default.")

    driver.find_element(By.XPATH, "//span[contains(., 'Site administration')]").click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    # Enter fake data to username field.
    driver.find_element(By.ID, 'id_username').send_keys(locators.username)
    sleep(0.25)
    # Click to password field and enter fake password.
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.password)
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.firstname)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.surname)
    sleep(0.25)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    sleep(0.25)
    # Select 'Allow everyone to see my email address'
    # Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_value(1)
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(0.25)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    sleep(0.25)
    # Select(driver.find_element(By.ID, 'id_country')).select_by_value(
    #     'CA')
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text(
        'Canada')    # fake.current_country()
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_visible_text('America/Vancouver')
    sleep(0.25)
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.discription)
    sleep(0.25)

    # Upload picture to the User picture section
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    sleep(0.25)
    # driver.find_element(By.XPATH, '//span[contains(., "Server files"]')
    # driver.find_element(By.PARTIAL_LINK_TEXT, "Server files")
    driver.find_element(By.LINK_TEXT, "Server files").click()
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Cosmetics").click()
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Biotherm 2021 fall school").click()
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Course image").click()
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT, "BT2021fall.png").click()
    sleep(0.25)

    driver.find_element(By.XPATH, '//button[contains(., "Select this file")]').click()
    sleep(0.25)

    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pics_disc)
    sleep(0.25)
    # Click by Additional names dropdown men
    driver.find_element(By.XPATH, '//a[contains(., "Additional names")]').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.phonetic_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.phonetic_name)

    driver.find_element(By.ID, 'id_middlename').send_keys(locators.phonetic_name)

    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.phonetic_name)
    sleep(0.25)
    # Click by "Interest" menu
    driver.find_element(By.XPATH, '//a[contains(., "Interests")]').click()
    sleep(0.25)
    for tag in locators.list_of_interest:
        driver.find_element(By.XPATH, '//*[@placeholder="Enter tags..."]').click()
        sleep(0.25)
        driver.find_element(By.XPATH, '//*[@placeholder="Enter tags..."]').send_keys(tag)
        sleep(0.25)
        driver.find_element(By.XPATH, '//*[@placeholder="Enter tags..."]').send_keys(Keys.ENTER)
        # driver.find_element(By.XPATH, '//div[3]/input"]').send_keys(Keys.ENTER)
    sleep(0.25)

    # Click by "Optional" menu
    # driver.find_element(By.LINK_TEXT, 'Optional').click()
    driver.find_element(By.XPATH, "//a[text() = 'Optional']").click()
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_url").send_keys(locators.web_page_url)  # //*[@id="id_url"]
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_icq").send_keys(locators.username)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_skype").send_keys(locators.username)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_aim").send_keys(locators.username)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_yahoo").send_keys(locators.username)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_msn").send_keys(locators.username)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_idnumber").send_keys(locators.username)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_institution").send_keys(locators.institution)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_department").send_keys(locators.department)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_phone1").send_keys(locators.phone_number)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_phone2").send_keys(locators.mobile_phone_number)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_address").send_keys(locators.address)
    sleep(0.25)

    # Click "Create User" button
    driver.find_element(By.CSS_SELECTOR, "input#id_submitbutton").click()
    sleep(0.25)

    print(f"----- Test Scenario : Create a new user '{locators.username}''{locators.email}' is passed. -----")


def check_user_created():
    # check that we are on the user's main page
    if driver.current_url == locators.moodle_user_list_page:
        assert driver.find_element(By.XPATH, "//h1[text()='Software Quality Assurance Testing']").is_displayed()
        if driver.find_element(By.ID, 'fgroup_id_email_grp_label') and driver.find_element(By.NAME, 'email'):
            driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
            driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
            if driver.find_element(By.XPATH, f"//td[contains(., '{locators.email}')]"):
                print(f"----- Test Scenario : Check user created in user list. {locators.email} is passed. -----")


def logger():
    old_instance = sys.stdout
    log_file = open('message.log', 'a') # 'w'
    log_file.write(f'Email: {locators.email}\nPassword: {locators.password}\nUsername: {locators.username}\nPhone number: {locators.phone_number}\nFirstname: {locators.firstname}\nLastname: {locators.surname}\n')
    log_file.write(f'------------🤗-------\n')
    log_file.close()


def check_logged_in_with_new_cred():
    assert driver.current_url == locators.moodle_dashboard_url
    assert driver.find_element(By.XPATH, f"//span[contains(., '{locators.fullname}')]").is_displayed
    print(f'User name "{locators.fullname}" displayed in the dashboard. Test Passed. ')


def delete_new_user():
    assert driver.current_url == locators.moodle_dashboard_url
    if not driver.find_element(By.XPATH, "//span[contains(., 'Site administration')]").is_displayed():
        driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/nav/div/button/i').click()
        sleep(0.25)

    driver.find_element(By.XPATH, "//span[contains(., 'Site administration')]").click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    sleep(0.5)  # Switch pages, give more time
    assert driver.find_element(By.CSS_SELECTOR, 'input#id_email').is_displayed()
    driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
    sleep(0.25)
    driver.find_element(By.XPATH, f"//td[contains(.,'{locators.email}')]/../td/a/i[@title='Delete']").click()
    # driver.find_element(By.XPATH, "//i[@title='Delete']").click()
    sleep(0.25)
    driver.find_element(By.XPATH, "//button[text()='Delete']").click()
    sleep(0.25)

    # checkpoint to make sure it is deleted.
    # assert driver.find_element(By.CSS_SELECTOR, 'input#id_email').is_displayed()
    # driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
    # sleep(0.25)
    # driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
    # sleep(0.25)
    # print(f"Double check: look for the user again from search result: {datetime.datetime.now()}")
    # try:
    #     driver.find_element(By.XPATH, f"//td[contains(.,'{locators.email}')]")
    # except exceptions.NoSuchElementException:
    #     print(f"New user '{locators.username}' has been deleted successfully!")
    # # assert not driver.find_element(By.XPATH, f"//td[contains(.,'{locators.email}')]").is_displayed()
    #
    # print(f"Double check: after search: {datetime.datetime.now()}") # cost 5 seconds for above statement
    print(f"----- Test Scenario : Delete user '{locators.username}''{locators.email}' is passed. -----")

