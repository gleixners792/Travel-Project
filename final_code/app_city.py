#Import necessary libraries
import numpy as np
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template, redirect, request, url_for
from Passwords import pgAdmin_pwd


#Create instance of Flask app
app = Flask(__name__, template_folder='template')



#Create route to render index.html template
@app.route("/")
def index(): 
        
    return render_template("index.html")


#Create route to query data and  display info based on selected city
@app.route("/city", methods=['GET', 'POST'])
def city():
    
    select = request.form.get('cityID')
    city_data = {}
    cs_value = select
    
    POSTGRES_ADDRESS = 'localhost'
    POSTGRES_PORT = '5432'
    POSTGRES_USERNAME = 'postgres' 
    POSTGRES_PASSWORD = pgAdmin_pwd
    POSTGRES_DBNAME = 'Project3_TravelData'
    
    postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'.format
                    (username=POSTGRES_USERNAME,
                     password=POSTGRES_PASSWORD,
                     ipaddress=POSTGRES_ADDRESS,
                     port=POSTGRES_PORT,
                     dbname=POSTGRES_DBNAME))
    
    #Create the connection
    engine = create_engine(postgres_str)

    
    #city data
    city_df = pd.read_sql_table('city',engine)
    
    #CityState Name
    cs_name = city_df.loc[city_df["city_state"] == cs_value, 'city_state'].item()
    city_data["name"] = cs_name
    
    
    #Image URL
    img_url = city_df.loc[city_df["city_state"] == cs_value, 'image_url'].item()
    city_data["image"] = img_url
    
    #Population
    cpop = city_df.loc[city_df["city_state"] == cs_value, 'population'].item()
    city_data["cpop"] = cpop
    
        
    #city facts data
    facts = pd.read_sql_table('city_facts',engine)
           
    #Named For
    nf = facts.loc[facts["city_state"] == cs_value, 'named_for'].item()
    city_data["nf"] = nf
        
    #Settled
    stl = facts.loc[facts["city_state"] == cs_value, 'settled'].item()
    city_data["stl"] = stl
        
    #Founded
    fnd = facts.loc[facts["city_state"] == cs_value, 'founded'].item()
    city_data["fnd"] = fnd
        
    #Incorporated
    inc = facts.loc[facts["city_state"] == cs_value, 'incorporated'].item()
    city_data["inc"] = inc
        
    #Mayor
    mayor = facts.loc[facts["city_state"] == cs_value, 'mayor'].item()
    city_data["mayor"] = mayor
    
    #Land Area
    land = facts.loc[facts["city_state"] == cs_value, 'land_area'].item()
    city_data["land"] = land
        
    #Water Area
    water = facts.loc[facts["city_state"] == cs_value, 'water_area'].item()
    city_data["water"] = water
        
    #Elevation
    elev = facts.loc[facts["city_state"] == cs_value, 'elevation'].item()
    city_data["elev"] = elev
        
    #Time Zone
    time = facts.loc[facts["city_state"] == cs_value, 'time_zone'].item()
    city_data["time"] = time


    #weather data
    weath = pd.read_sql_table('city_weather',engine)
    col_list = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
        
    #High Temps
    ht1 = weath.loc[(weath["city_state"] == cs_value) & (weath["measure"] == 'Average High')]
    ht2 = ht1[col_list].values
    highTemps = ht2.ravel()
    janHigh = highTemps[0]
    febHigh = highTemps[1]
    marHigh = highTemps[2]
    aprHigh = highTemps[3]
    mayHigh = highTemps[4]
    junHigh = highTemps[5]
    julHigh = highTemps[6]
    augHigh = highTemps[7]
    sepHigh = highTemps[8]
    octHigh = highTemps[9]
    novHigh = highTemps[10]
    decHigh = highTemps[11]
    #city_data["highTemps"] = ht
        
    #Low Temps
    lt1 = weath.loc[(weath["city_state"] == cs_value) & (weath["measure"] == 'Average Low')]
    lt2 = lt1[col_list].values
    lowTemps = lt2.ravel()
    janLow = lowTemps[0]
    febLow = lowTemps[1]
    marLow = lowTemps[2]
    aprLow = lowTemps[3]
    mayLow = lowTemps[4]
    junLow = lowTemps[5]
    julLow = lowTemps[6]
    augLow = lowTemps[7]
    sepLow = lowTemps[8]
    octLow = lowTemps[9]
    novLow = lowTemps[10]
    decLow = lowTemps[11]
    #city_data["lowTemps"] = lt
        
    #Avg Precip
    pr1 = weath.loc[(weath["city_state"] == cs_value) & (weath["measure"] == 'Average Precipitation')]
    pr2 = pr1[col_list].values
    avgPrecip = pr2.ravel()
    
    janPrecip = avgPrecip[0]
    febPrecip = avgPrecip[1]
    marPrecip = avgPrecip[2]
    aprPrecip = avgPrecip[3]
    mayPrecip = avgPrecip[4]
    junPrecip = avgPrecip[5]
    julPrecip = avgPrecip[6]
    augPrecip = avgPrecip[7]
    sepPrecip = avgPrecip[8]
    octPrecip = avgPrecip[9]
    novPrecip = avgPrecip[10]
    decPrecip = avgPrecip[11]
    #city_data["avgPrecip"] = pr

    
    return render_template("index_city.html", city_data=city_data, highTemps=highTemps, lowTemps=lowTemps, avgPrecip=avgPrecip,\
                           janPrecip=janPrecip, febPrecip=febPrecip, marPrecip=marPrecip, aprPrecip=aprPrecip, mayPrecip=mayPrecip,\
                           junPrecip=junPrecip, julPrecip=julPrecip, augPrecip=augPrecip, sepPrecip=sepPrecip, octPrecip=octPrecip,\
                           novPrecip=novPrecip, decPrecip=decPrecip,\
                           janHigh=janHigh, febHigh=febHigh, marHigh=marHigh, aprHigh=aprHigh, mayHigh=mayHigh,\
                           junHigh=junHigh, julHigh=julHigh, augHigh=augHigh, sepHigh=sepHigh, octHigh=octHigh,\
                           novHigh=novHigh, decHigh=decHigh,\
                           janLow=janLow, febLow=febLow, marLow=marLow, aprLow=aprLow, mayLow=mayLow,\
                           junLow=junLow, julLow=julLow, augLow=augLow, sepLow=sepLow, octLow=octLow,\
                           novLow=novLow, decLow=decLow)



if __name__ == "__main__":
    app.run(debug=True)

