from flask import Flask, render_template, redirect   
from flask_pymongo import PyMongo
import scrape_mars
import os

app = Flask(__name__)

#conn = 'mongodb://localhost:27017/Missions_to_Mars'
#app.config["MONGO_URI"] = os.environ.get(conn)
#mongo = PyMongo(app)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
# setup mongo connection
#conn = "mongodb://localhost:27017"
#client = pymongo.MongoClient(conn)
#mongo = PyMongo(app)
# connect to mongo db and collection
#b = client.store_inventory
#collection = db.produce

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)

# one def in scrape mars seems a bit
@app.route("/scrape")
# examples show one def executing others in python or one def here executing multiple defs, choosing former
# rewriting python, sigh

def scrape():
    mars = mongo.db.mars 
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful"
#   return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)