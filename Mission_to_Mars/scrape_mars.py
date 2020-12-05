from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

def Merge(dict1, dict2):
    result = {**dict1, **dict2}
    return result

def scrape():

    # get news title and text
    browser = init_browser()
    news_url = 'https://mars.nasa.gov/news'
    browser.visit(news_url)
    titles = browser.find_by_tag('div[class="content_title"]')
    news_titles = titles[1].text
    articles = browser.find_by_tag('div[class="article_teaser_body"]')
    news_p = articles[0].text 
    browser.quit()

    # get featured image
    browser = init_browser()
    img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(img_url)
    browser.find_by_tag('a[class="fancybox"]').click()
    browser.links.find_by_partial_text('more info').click()
    jpg_element = browser.links.find_by_partial_text('.jpg')
    featured_jpg_href = jpg_element['href']
    browser.quit()

    # get fact table
    table_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(table_url)
    facts_df = tables[0]
    table_html = facts_df.to_html(index=False, header=False)

    # get hemisphere titles and images
    browser = init_browser()
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)
    hemi_titles = browser.find_by_tag('a[class="itemLink product-item"]')
    hemi_titles_list = []

    for title in hemi_titles:
        hemi_titles_list.append(title.value)
    
    hemi_titles_list_clean = [x for x in hemi_titles_list if '' != x]

    links = browser.find_by_tag('a[class="itemLink product-item"]')
    links_list = []

    for link in links:
        links_list.append(link['href'])
    
    hemi_links = [] 
    [hemi_links.append(x) for x in links_list if x not in hemi_links] 
    browser.quit()

    jpg_list = []

    for hemi_link in hemi_links:
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)
        browser.visit(hemi_link)
        jpg = browser.links.find_by_partial_text('Sample')
        jpg_list.append(jpg['href'])
        browser.quit()
    
    title_dict_list = []

    for title in hemi_titles_list_clean:
        title_dict = {"title": title}
        title_dict_list.append(title_dict)
    
    jpg_dict_list = []

    for jpg in jpg_list:
        jpg_dict = {"img_url": jpg}
        jpg_dict_list.append(jpg_dict)
    
    title_jpg_dict = []
    counter = 0

    for item in title_dict_list:
        mini_dict = Merge(item, jpg_dict_list[counter])
        title_jpg_dict.append(mini_dict)
        counter = counter + 1
    
    # store the data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_img": featured_jpg_href,
        "table_html": table_html,
        "hemi_dict": title_jpg_dict
    }

    # return results
    return mars_data

