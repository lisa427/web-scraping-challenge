# web-scraping-challenge

A Python app (app.py) was developed to create a web page that displays data about Mars that was scraped from multiple websites.  It uses Flask to render the web page and MongoDB to store the scraped data.  A Jupyter notebook was used to initially develop the code used for scraping.  The scraping code was then used in a Python function that scraped the various websites using Splinter and returned all the needed data in a dictionary.  The html template uses Bootstrap to structure and style the page.  Jinja is used to insert the scraped data into the html.

*See the images folder for a screenshot of the finished web page after clicking the "Scrape New Data" button.*

## Sites scraped:

* https://mars.nasa.gov/news
    * title of latest news story on Mars
    * paragraph of lastest news story on Mars

* https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
    * latest featured Mars image

* https://space-facts.com/mars/
    * table of facts about Mars

* https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
    * images of Mars' hemispheres
    * names of Mars' hemispheres
