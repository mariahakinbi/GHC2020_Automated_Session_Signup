from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def login():
    # website

    # opts = Options()
    # opts.set_headless()
    # assert opts.headless  # Operating in headless mode
    # browser = Firefox()
    # browser.get('https://duckduckgo.com')
    # read credentials file; if no credentials then ask for user input
    print('logging in')


def get_to_session_page():
    # click thru 3x (?)
    print('session list')

# fill in sessions.ini


def search_availability(session_name):
    # sarch for seimar page for availability
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


main()
