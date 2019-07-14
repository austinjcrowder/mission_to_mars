from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser ("chrome", **executable_path, headless=False)
print("error message")
## Step 1 - Scraping
def scrape_info():
    browser = init_browser()

    #visit URL
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    #scrape page to soup 
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    #get titles 
    news_title = soup.find("div",class_="content_title").text
    news_p = soup.find('div', class_="article_teaser_body").text

    #Get the featured image
    url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit"
    browser.visit(url_image)
    # from IPython.display import Image
    # from IPython.core.display import HTML

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.find("img", class_="thumb")["src"]
    image_url = "https://jpl.nasa.gov"+image
    # featured_image_url = img_url
    #image_print = Image(featured_image_url)
#i just added image print
    #TweetlydeeeTwittleDumb
    #Pirate NSA's Twitter and scrape the thing 
    #lol i already did this to my girlfriends twitter before this assignment
    url_weather = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_weather)

    html_weather = browser.html
    soup2 = BeautifulSoup(html_weather, "html.parser")
    mars_weather = soup2.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    ##print(f"The latest Weather Tweet from our good friends NSA is: {mars_weather}")

    url_facts = "https://space-facts.com/mars/"
    tables_mars = pd.read_html(url_facts)[1]
    df = tables_mars
    df.columns = ['Mars', '']
    df.set_index('Mars')
    html_table = df.to_html()
    html_table.replace('\n', '')
    facts_df = df.to_html('table.html')


    scrape_stuff = {
        "news_title": news_title,
        "news_p": news_p,
        "mars_weather": mars_weather,
        "image_url": image_url,
        "facts_df": facts_df,

    }
    browser.quit()
    return scrape_stuff