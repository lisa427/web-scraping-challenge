# web-scraping-challenge

A Python app (app.py) was developed to create a web page that displays data about Mars that was scraped from multiple websites.  A Jupyter notebook was used to initially devlop the code used for scraping.  The scraping code was then used in a Python function that scraped the various websites using Splinter and returned all the needed data in a dictionary.  The html template uses Bootstrap to structure and style the page.  Jinja is used to insert the scraped data into the html.

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
