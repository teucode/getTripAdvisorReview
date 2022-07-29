import sys
import csv
from selenium import webdriver
import time

# path to file to store data
path_to_file = "D:/Kuliah/S2/Thesis/scrapemine/Scraping-TripAdvisor-with-Python-2020-master/hasil/revmcd12ags.csv"

# number of scraped pages
num_page = 10

# default tripadvisor website of restaurant
url = "https://www.tripadvisor.co.id/Restaurant_Review-g297715-d5020146-Reviews-McDonald_s-Surabaya_East_Java_Java.html"

# Import the webdriver
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

# Save the review
csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)

for i in range(0, num_page):
    
    time.sleep(2)
    driver.find_element_by_xpath("//span[@class='taLnk ulBlueLinks']").click()

    container = driver.find_elements_by_xpath(".//div[@class='review-container']")

    for j in range(len(container)):

        title = container[j].find_element_by_xpath(".//span[@class='noQuotes']").text
        date = container[j].find_element_by_xpath(".//span[contains(@class, 'ratingDate')]").get_attribute("title")
        rating = container[j].find_element_by_xpath(".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
        review = container[j].find_element_by_xpath(".//p[@class='partial_entry']").text.replace(" ", " ")

        csvWriter.writerow([date, rating, title, review]) 

    # change the page
    driver.find_element_by_xpath('.//a[@class="nav next ui_button primary"]').click()

driver.close()
