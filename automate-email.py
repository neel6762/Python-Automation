from selenium import webdriver
import time

print('Valid for Gmail Users ! Provide a valid ID and Password for it to work...')
email = input('Enter your Email Address:')
password = input('Enter your password:')
emailTo = input("Recipient's Email Address:")
emailSub = input('Enter the subject of the mail:')
emailBody = input("Type in the message you want to send:")
# Opening the WebBrowser
browser = webdriver.Chrome(r'path_to_the_web_driver')
url = 'https://www.google.com/gmail/'
browser.get(url)

# Writing the email to the input and clicking the next button -----
browser.find_element_by_css_selector('#identifierId').send_keys(email)
next = browser.find_element_by_css_selector('#identifierNext')
next.click()
time.sleep(2)

# The Password Section and clicking the next button, it is necessary to the the srcipt to sleep for some time-----
browser.find_element_by_name('password').send_keys(password)
time.sleep(2)
browser.find_element_by_css_selector('#passwordNext').click()
print('You are now Logged In !')
time.sleep(10)

# The compose button
browser.find_element_by_class_name('z0').click()
time.sleep(5)

# Send to -----
browser.find_element_by_name('to').send_keys(emailTo)
time.sleep(3)

# The Subject part -----
browser.find_element_by_name('subjectbox').send_keys(emailSub)
browser.implicitly_wait(10)

browser.find_element_by_class_name('editable').send_keys(emailBody)
time.sleep(5)
browser.find_element_by_class_name('gU').click()
print('Message Send ! Cheers')
