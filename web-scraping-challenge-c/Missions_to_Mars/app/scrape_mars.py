# start here
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver 
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("http://www.google.com/")
print (driver.title)
driver.quit() 
# Choose the executable path to driver 
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

def marsNewst():
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("div", class_='list_text')
    news_title = article.find("div", class_="content_title").text
    return news_title

def marsNewsp():
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("div", class_='list_text')
    news_para = article.find("div", class_ ="article_teaser_body").text
    return news_para

def marsImage(browser):
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    # Find and click the full image button
    full_image_elem = browser.find_by_id("full_image")
    full_image_elem.click()
    browser.is_element_present_by_text("more info", wait_time=0.5)
    more_info_elem = browser.find_link_by_partial_text("more info")
    more_info_elem.click()
    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, "html.parser")
    # Find the relative image url
    img = img_soup.select_one("figure.lede a img")
    try:
        img_url_rel = img.get("src")
    except AttributeError:
        return None
    # Use the base url to create an absolute url
    img_url = f"https://www.jpl.nasa.gov{img_url_rel}"
    return img_url





#def marzzzsImage():
 #   url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
  #  browser.visit(url)
   # time.sleep(2)
# HTML Object 
    #html_image = browser.html
# Parse HTML with Beautiful Soup
    #soup = BeautifulSoup(html_image, 'html.parser')
# Retrieve background-image url from style tag 
    #featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
# Website Url 
#main_url = 'https://www.jpl.nasa.gov'
    #main_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
# Concatenate website url with scrapped route
    #featured_image_url = main_url + featured_image_url
# Display full link to featured image
    #return featured_image_url

def marsFacts():
    mars_facts_url = 'https://space-facts.com/mars'
    browser.visit(mars_facts_url)
    time.sleep(2)
# Use Panda's `read_html` to parse the url
    mars_facts = pd.read_html(mars_facts_url)

# need to find that note............datadict
# Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`
    mars_df = mars_facts[0]
    mars_df
    mars_df = mars_df.to_html()
    return mars_df


def marsWeather():
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(2)
    html = browser.html
    tweet_soup = BeautifulSoup(html, 'html.parser')
    
    # Scrape the tweet info and return
    first_tweet = tweet_soup.find('p', class_='TweetTextSize').text
    return first_tweet

def marsHemi():
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    mars_hemisphere = []

    products = soup.find("div", class_ = "result-list" )
    hemispheres = products.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        time.sleep(1)
        html = browser.html
        soup=BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        mars_hemisphere.append({"title": title, "img_url": image_url})
    return mars_hemisphere
marsHemi()

# Defining scrape & dictionary
def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    final_app = {
#   output = marsNews()
    "mars_news": marsNewst(),
    "mars_paragraph":marsNewsp(),
    "mars_image":marsImage(browser),
    "mars_facts": marsFacts(),
    "mars_hemisphere": marsHemi(),
    "mars_weather":marsWeather()
    }
    return final_app
#scrape()