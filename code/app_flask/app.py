#Import necessary libraries
from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
import city_query


#Create instance of Flask app
app = Flask(__name__, template_folder='template')

mongo = PyMongo(app, uri="mongodb://localhost:27017/city_app")


#Create route to render index.html template
@app.route("/")
def index(): 
        
    return render_template("index.html")


#Create route to query data and  display info based on selected city
@app.route("/city", methods=['GET', 'POST'])
def city():
    
    select = request.form.get('cityID')
    
    return render_template("index_city.html")
 
    #hold queries in mongo db       
    city_data = mongo.db.city_data
    
    #run queries    
    cs_value = select
    query_data = city_query.stats_city(cs_value)
    
    city_data.update({}, query_data, upsert=True)
        

    return redirect("/city", city_data=city_data)


if __name__ == "__main__":
    app.run(debug=True)

