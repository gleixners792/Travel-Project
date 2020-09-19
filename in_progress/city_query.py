# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:12:51 2020

@author: betsy_k
"""

import psycopg2
from Passwords import pgAdmin_pwd

#cs_value = ("Cleveland, Ohio",)

def stats_city(cs_value):
    
    city_data = {}
    #DATA QUERIES
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = pgAdmin_pwd,
                                      host = "localhost",
                                      port = "5432",
                                      database = "Project3_TravelData")
    
        cursor = connection.cursor()
        
        Query1 = "SELECT city FROM city WHERE city_state = (%s)"
        cursor.execute(Query1, cs_value)
        cy_query = cursor.fetchall()
        #print(cy_query)
        
                    
        Query2 = "SELECT image_url FROM city WHERE city_state = (%s)"  
        cursor.execute(Query2, cs_value)
        im_query = cursor.fetchall()
        #print(im_query)
        
        
        Query3 = "SELECT cf.named_for, cf.settled, cf.founded, cf.incorporated, cf. mayor, city.population,\
                                    cf.land_area, cf.water_area, cf.elevation, cf.time_zone\
                                    FROM city \
                                    INNER JOIN city_facts AS cf\
                                    ON city.city_state = cf.city_state\
                                    WHERE city.city_state = (%s)"
        cursor.execute(Query3, cs_value)
        cf_query = cursor.fetchall()
        #print(cf_query)
        
        
        Query4 = "SELECT jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec\
                    FROM city_weather\
                    WHERE city_state = (%s) AND measure = 'Average High'"  
        cursor.execute(Query4, cs_value)
        ht_query = cursor.fetchall()
        #print(ht_query)
        
            
        Query5 = "SELECT jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec\
                    FROM city_weather\
                    WHERE city_state = (%s) AND measure = 'Average Low'"  
        cursor.execute(Query5, cs_value)
        lt_query = cursor.fetchall()
        #print(lt_query)
        
            
        Query6 = "SELECT jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec\
                    FROM city_weather\
                    WHERE city_state = (%s) AND measure = 'Average Precipitation'"  
        cursor.execute(Query6, cs_value)
        pr_query = cursor.fetchall()
        #print(pr_query)
        
    
    except (Exception, psycopg2.Error) as error :
        return ("Error getting data", error)

    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                #print("PostgreSQL connection is closed")
    
    
    
    
    for row in cy_query:
        #cn_dict = {}
        #cn_dict["City_Name"] = row[0]
        cname = row[0]
        #city_data.append(cn_dict)
    city_data["cityName"] = cname
    
    city_data["imageUrl"] = im_query
    
    #for row in im_query:
        #im_dict = {}
        #im_dict["Image_Url"] = row[0]
        #city_data.append(im_dict)
    
    for row in cf_query:
        cf_dict = {}
        cf_dict["Named_For"] = row[0]
        cf_dict["Settled"] = row[1]
        cf_dict["Founded"] = row[2]
        cf_dict["Incorporated"] = row[3]
        cf_dict["Mayor"] = row[4]
        cf_dict["Population"] = row[5]
        cf_dict["Land_Area"] = row[6]
        cf_dict["Water_Area"] = row[7]
        cf_dict["Elevation"] = row[8]
        cf_dict["Time_Zone"] = row[9]
        city_data["cityFacts"] = cf_dict
        
    for row in ht_query:
        ht_dict = {}
        ht_dict["janHigh"] = row[0]
        ht_dict["febHigh"] = row[1]
        ht_dict["marHigh"] = row[2]
        ht_dict["aprHigh"] = row[3]
        ht_dict["mayHigh"] = row[4]
        ht_dict["junHigh"] = row[5]
        ht_dict["julHigh"] = row[6]
        ht_dict["augHigh"] = row[7]
        ht_dict["sepHigh"] = row[8]
        ht_dict["octHigh"] = row[9]
        ht_dict["novHigh"] = row[10]
        ht_dict["decHigh"] = row[11]
        #city_data["highTemps"] = ht_dict
        
             
    for row in lt_query:
        lt_dict = {}
        lt_dict["janLow"] = row[0]
        lt_dict["febLow"] = row[1]
        lt_dict["marLow"] = row[2]
        lt_dict["aprLow"] = row[3]
        lt_dict["mayLow"] = row[4]
        lt_dict["junLow"] = row[5]
        lt_dict["julLow"] = row[6]
        lt_dict["augLow"] = row[7]
        lt_dict["sepLow"] = row[8]
        lt_dict["octLow"] = row[9]
        lt_dict["novLow"] = row[10]
        lt_dict["decLow"] = row[11]
        #city_data.append(lt_dict)
        #city_data["lowTemps"] = lt_dict
                  
    for row in pr_query:
        pr_dict = {}
        pr_dict["janPre"] = row[0]
        pr_dict["febPre"] = row[1]
        pr_dict["marPre"] = row[2]
        pr_dict["aprPre"] = row[3]
        pr_dict["mayPre"] = row[4]
        pr_dict["junPre"] = row[5]
        pr_dict["julPre"] = row[6]
        pr_dict["augPre"] = row[7]
        pr_dict["sepPre"] = row[8]
        pr_dict["octPre"] = row[9]
        pr_dict["novPre"] = row[10]
        pr_dict["decPre"] = row[11]
        #city_data.append(pr_dict)
        #city_data["Precip"] = pr_dict
        
    return city_data