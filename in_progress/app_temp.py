#Import necessary libraries
from flask import Flask, jsonify, render_template, redirect, request, url_for
import psycopg2
from Passwords import pgAdmin_pwd

#Create instance of Flask app
app = Flask(__name__, template_folder='template')


#Create route to render index.html template
@app.route("/")
def index(): 
    
    return render_template("index_new.html")


#Create route to query data and  display info based on selected city
@app.route("/city", methods=['GET', 'POST'])
def city():
    
    select = request.form.get('cityID')
    
    return render_template("index_city2.html")
        
    
    #run queries    
    cs_value = "1"
    
    connection = psycopg2.connect(user = "postgres",
                                      password = pgAdmin_pwd,
                                      host = "localhost",
                                      port = "5432",
                                      database = "Project3_TravelData")
    
    cursor = connection.cursor()
        
    Query1 = "SELECT city FROM city WHERE cs_id = (%s)"
    cursor.execute(Query1, cs_value)
    cy_query = cursor.fetchall()    
        
    
    if(connection):
        cursor.close()
        connection.close()

    return redirect("/city", city_name=jsonify(cy_query))


if __name__ == "__main__":
    app.run(debug=True)

