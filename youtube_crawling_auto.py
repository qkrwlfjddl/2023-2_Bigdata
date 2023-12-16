from selenium import webdriver
import time
from openpyxl import Workbook
import pandas as pd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
import re
import csv

warnings.filterwarnings('ignore')

wb = Workbook(write_only=True)
ws = wb.create_sheet()

# 'url.txt' 파일 읽어오기
with open('url_21_2.txt', 'r') as file:
    urls = file.readlines()

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

for url in urls:
    url = url.strip()  # Remove leading/trailing whitespaces
    
    print("Before getting URL")
    driver.get(url)
    print("After getting URL")
    print(url)
    
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comment-thread-renderer")))
    except Exception as e:
        print(f"Error: {e}")
        continue  # Skip to the next URL in case of an error
    """

    driver.get(url)
    
    driver.implicitly_wait(10)

    time.sleep(5)
    """
    # Function to check if comments are loaded
    def check_comments_loaded(driver):
        try:
            WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comment-thread-renderer")))
            return True
        except:
            return False
        

    # Scroll down in increments until comments are loaded
    while not check_comments_loaded(driver):
        driver.execute_script("window.scrollBy(0, 100);")  # Scroll down
        time.sleep(8)  # Wait for the page to load

    driver.execute_script("window.scrollTo(0, 800)")
    time.sleep(8)

    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(8)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    time.sleep(8)

    # 유튜브 프리미엄 팝업 닫기
    """
    try:
        driver.find_element_by_css_selector("#dismiss-button > a").click()
    except:
        pass
    """

    #제목 가져오기
    main_title = driver.find_element(By.CSS_SELECTOR, "h1.style-scope.ytd-watch-metadata yt-formatted-string").text
    main_title = re.sub(r'[\/:*?"<>|]', '_', main_title)
    print(main_title)
  
    
    buttons = driver.find_elements(By.CSS_SELECTOR, "#more-replies > button")

    time.sleep(2)

    for button in buttons:
        button.send_keys(Keys.ENTER)
        time.sleep(2)
        button.click()

    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    id_list = soup.select("a#author-text")
    comment_list = soup.select("yt-formatted-string#content-text")
    likeCount_list = [like.text.strip() for like in soup.select("span#vote-count-middle")]

    id_final = []
    comment_final = []
    likeCount_final = []

    min_length = min(len(comment_list), len(id_list),len(likeCount_list))
    for i in range(min_length):
        temp_id = id_list[i].text
        temp_id = temp_id.replace('\n', '')
        temp_id = temp_id.replace('\t', '')
        temp_id = temp_id.replace('    ', '')
        id_final.append(temp_id) # 댓글 작성자

        temp_comment = comment_list[i].text
        temp_comment = temp_comment.replace('\n', '')
        temp_comment = temp_comment.replace('\t', '')
        temp_comment = temp_comment.replace('    ', '')
        comment_final.append(temp_comment) # 댓글 내용

        temp_likeCount = likeCount_list[i] if i < len(likeCount_list) else "N/A"
        temp_likeCount = temp_likeCount.replace('\n', '')
        temp_likeCount = temp_likeCount.replace('    ', '')
        temp_likeCount = temp_likeCount.replace('  ', '')
        likeCount_final.append(int(temp_likeCount)) #좋아요 수

    pd_data = {"제목" : main_title, "아이디" : id_final , "댓글 내용" : comment_final,  "좋아요 수" : likeCount_final}
    youtube_pd = pd.DataFrame(pd_data)
    print(youtube_pd.head())  # Print the first 5 rows for debugging purposes

    try:
        youtube_pd.to_csv(f'C:/Users/hyeee/Desktop/빅데이터/youtube_21/{main_title}.csv', index=False, encoding='utf-8-sig')
    except Exception as e:
        print(f"Error during CSV export: {e}")
    # Quit the WebDriver after processing each URL
    driver.quit()
    # Re-initialize the WebDriver for the next URL
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Close the WebDriver
driver.quit()