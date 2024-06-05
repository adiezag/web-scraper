from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


# print('Length of the list: ', len(articles))
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
