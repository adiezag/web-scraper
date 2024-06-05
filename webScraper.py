from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# chromedriver_path = './chromedriver'
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service = Service(executable_path = './chromedriver')
driver = webdriver.Chrome(service = service, options = options)
driver.maximize_window()

website1 = 'https://www.reddit.com/r/Python'
website2 = 'https://www.reddit.com/r/javascript/'
driver.get(website1)



time.sleep(1)
# element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'shreddit-post')))
# driver.execute_script("arguments[0].scrollIntoView(true);", element)

scroll_pause = 2
counter = 0
last_heigth =driver.execute_script("return document.body.scrollHeight")
while counter < 1:
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
	time.sleep(2)
	new_height = driver.execute_script("return document.body.scrollHeight")
	last_heigth = new_height
	counter += 1

articles = driver.find_elements(By.TAG_NAME, 'article')


def get_id(article):
	article_id = (article.find_element(By.TAG_NAME, 'shreddit-post')).get_attribute('id')
	return article_id
# xpath = '//*[@id="t3_1d89b03"]//div/div/span/span/span/faceplate-number'
# xpath_1 = '/html/body/shreddit-app/div/div[1]/div[1]/section/div/div[1]/div[2]/h1'
# xpath_2 = '//*[@id="t3_1d5jt6n"]/a[1]'
# tag_id = 't3_1d89b03'
# xpath_3 = '//*[@id="t3_1d8mv0a"]//div[2]/span/span/span/faceplate-number'
# element = driver.find_element(By.XPATH, xpath_3)
# print(element.text)

# score_query = f"return (document.querySelector('shreddit-post[id={tag_id}]').shadowRoot.querySelector('div > div > span > span > span > faceplate-number')).innerText"
# score = driver.execute_script(score_query)
# print(score)

# shadow_root_wrapper = driver.find_element(By.CSS_SELECTOR, '#shadow-root (open)')
# shadow_root_wrapper = driver.find_element(By.CSS_SELECTOR, '#shadow-root-wrapper')

# shadow_root_script = "return document.querySelector('shreddit-post').shadowRoot"
# shadow_root = driver.execute_script(shadow_root_script)



# element_in_shadow_dom = shadow_root.find_element(By.CSS_SELECTOR, 'div > div > span > span > span > faceplate-number')
# print(element_in_shadow_dom.text)


# all_shadow_roots_script = """
#     let elements = document.querySelectorAll('shreddit-post');
#     return Array.from(elements).map(e => e.shadowRoot);
# """

# # Get all shadow roots
# shadow_roots = driver.execute_script(all_shadow_roots_script)

# # Iterate through each shadow root and find the desired element
# for shadow_root in shadow_roots:
#     try:
#         element_in_shadow_dom = shadow_root.find_element(By.CSS_SELECTOR, 'div > div > span > span > span > faceplate-number')
#         print(element_in_shadow_dom.text)
#     except Exception as e:
#         print(f"Element not found in shadow root: {e}")







print('Length of the list: ', len(articles))
# print(shadow_root)
iteration = 0;
for index, article in enumerate(articles):
	if iteration > 5:
		break
	iteration += 1
	print('********************* article ***********************')
	print(f'article # {index}')
	
	article_title = (article.find_element(By.TAG_NAME, 'a')).text
	article_description = (article.find_element(By.TAG_NAME, 'p')).text
	article_link = (article.find_element(By.TAG_NAME, 'a')).get_attribute('href')


	article_id = get_id(article)

	try:
		score_query_pinned = f"return (document.querySelector('shreddit-post[id={article_id}]').shadowRoot.querySelector('div > div > span > span > span > faceplate-number')).innerText"
		comments_query_pinned = f"return (document.querySelector('shreddit-post[id={article_id}]').shadowRoot.querySelector('div > div > a > span > span:nth-child(2) > faceplate-number')).innerText"
		score = driver.execute_script(score_query_pinned)
		comments = driver.execute_script(comments_query_pinned)
	except:
		score_query = f"return (document.querySelector('shreddit-post[id={article_id}]').shadowRoot.querySelector('div.flex.flex-row.items-center.flex-nowrap.overflow-hidden.justify-start > span > span > span > faceplate-number')).innerText"
		comments_query = f"return (document.querySelector('shreddit-post[id={article_id}]').shadowRoot.querySelector('div.flex.flex-row.items-center.flex-nowrap.overflow-hidden.justify-start > a > span > span:nth-child(2) > faceplate-number')).innerText"
		score = driver.execute_script(score_query)
		comments = driver.execute_script(comments_query)


	
	print('Title: ', article_title)
	print('Description: ', article_description)
	print('Link: ', article_link)
	print('ID: ', article_id)
	print('score: ', score)
	print('comments: ', comments)
	print('\n')
	time.sleep(2)



	


	

