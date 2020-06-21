from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def openTheBrowser(url):

    chop = webdriver.ChromeOptions()
    chop.add_extension('e.crx')
    browser = webdriver.Chrome(r'path to the chrome browser here', chrome_options=chop)
    browser.get(url)
    target = browser.find_element_by_tag_name('body')
    print(browser.page_source)
    i = 0
    while i<5:
        time.sleep(.500)
        if browser.find_element_by_css_selector('body > div > div.game-container > div.game-message > p').text == 'Game over!':
            break
        target.send_keys(Keys.RIGHT)

        if browser.find_element_by_css_selector('body > div > div.game-container > div.game-message > p').text == 'Game over!':
            break
        target.send_keys(Keys.DOWN)

        if browser.find_element_by_css_selector('body > div > div.game-container > div.game-message > p').text == 'Game over!':
            break
        target.send_keys(Keys.UP)

        if browser.find_element_by_css_selector('body > div > div.game-container > div.game-message > p').text == 'Game over!':
            break
        target.send_keys(Keys.LEFT)
        i += 1
    time.sleep(3)
    print('Game Over!')
    browser.execute_script("window.open('');")
    time.sleep(1)
    # Switch to the new window
    browser.switch_to.window(browser.window_handles[1])
    browser.get("http://stackoverflow.com")
    time.sleep(3)
    # close the active tab
    browser.close()
    time.sleep(1)
    # Switch back to the first tab
    browser.switch_to.window(browser.window_handles[0])
    browser.get("http://google.se")
    time.sleep(3)
    # Close the only tab, will also close the browser.
    browser.close()


if __name__ == '__main__':
    url = 'http://gabrielecirulli.github.io/2048/'
    openTheBrowser(url)
