from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# set up Flask
app = Flask(__name__)

# connect to Mongo
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_mission")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function and save the results to a variable
    mars_data = scrape_mars.scrape_web()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)