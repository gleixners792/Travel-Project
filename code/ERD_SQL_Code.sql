-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "City" (
    "state_name" varchar(30)   NOT NULL,
    "city" varchar(50)   NOT NULL,
    "city_state" varchar(90)   NOT NULL,
    "population" varchar(15)   NOT NULL,
    "state_code" char(2)   NOT NULL,
    "lat" decimal(10,6)   NOT NULL,
    "long" decimal(10,6)   NOT NULL,
    "region_specific" varchar(30)   NOT NULL,
    "region_general" varchar(30)   NOT NULL,
    CONSTRAINT "pk_City" PRIMARY KEY (
        "city_state"
     )
);

CREATE TABLE "CityWeather" (
    "city" VARCHAR(50)   NOT NULL,
    "city_state" VARCHAR(90)   NOT NULL,
    "measure" VARCHAR(30)   NOT NULL,
    "jan" DECIMAL(10,2)   NOT NULL,
    "feb" DECIMAL(10,2)   NOT NULL,
    "mar" DECIMAL(10,2)   NOT NULL,
    "apr" DECIMAL(10,2)   NOT NULL,
    "may" DECIMAL(10,2)   NOT NULL,
    "jun" DECIMAL(10,2)   NOT NULL,
    "jul" DECIMAL(10,2)   NOT NULL,
    "aug" DECIMAL(10,2)   NOT NULL,
    "sep" DECIMAL(10,2)   NOT NULL,
    "oct" DECIMAL(10,2)   NOT NULL,
    "nov" DECIMAL(10,2)   NOT NULL,
    "dec" DECIMAL(10,2)   NOT NULL,
    "year" DECIMAL(10,2)   NOT NULL
);

CREATE TABLE "CityFacts" (
    "city" VARCHAR(30)   NOT NULL,
    "city_state" VARCHAR(90)   NOT NULL,
    "named_for" VARCHAR(100)   NOT NULL,
    "settled" VARCHAR(100)   NOT NULL,
    "founded" VARCHAR(100)   NOT NULL,
    "incorporated" VARCHAR(100)   NOT NULL,
    "mayor" VARCHAR(50)   NOT NULL,
    "land_area" VARCHAR(30)   NOT NULL,
    "water_area" VARCHAR(50)   NOT NULL,
    "elevation" VARCHAR(100)   NOT NULL,
    "time_zone" VARCHAR(50)   NOT NULL
);

CREATE TABLE "Tours" (
    "tour_id" Integer   NOT NULL,
    "facility_id" VARCHAR(200)   NOT NULL,
    "tour_name" VARCHAR(500)   NOT NULL,
    "tour_type" VARCHAR(30)   NOT NULL,
    "description" VARCHAR(5000)   NOT NULL,
    "duration" Integer   NOT NULL,
    "accessible" BOOLEAN   NOT NULL,
    "created_date" DATE   NOT NULL,
    "updated_date" DATE   NOT NULL
);

CREATE TABLE "Facilities" (
    "facility_id" VARCHAR(200)   NOT NULL,
    "legacy_id" VARCHAR(200)   NOT NULL,
    "org_id" VARCHAR(200)   NOT NULL,
    "parent_id" VARCHAR(200)   NOT NULL,
    "rec_id" VARCHAR(200)   NOT NULL,
    "facility_name" VARCHAR(500)   NOT NULL,
    "description" VARCHAR(100000)   NOT NULL,
    "facility_type" VARCHAR(1000)   NOT NULL,
    "use_fee" VARCHAR(2000)   NOT NULL,
    "directions" VARCHAR(100000)   NOT NULL,
    "phone" VARCHAR(1000)   NOT NULL,
    "email" VARCHAR(1000)   NOT NULL,
    "res_url" VARCHAR(300)   NOT NULL,
    "map_url" VARCHAR(300)   NOT NULL,
    "ada_access" VARCHAR(1000)   NOT NULL,
    "lat" DECIMAL(10,6)   NOT NULL,
    "long" DECIMAL(10,6)   NOT NULL,
    "keywords" VARCHAR(1000)   NOT NULL,
    "stay_limit" VARCHAR(1000)   NOT NULL,
    "reservable" BOOLEAN   NOT NULL,
    "enabled" BOOLEAN   NOT NULL,
    "updated_date" DATE   NOT NULL,
    CONSTRAINT "pk_Facilities" PRIMARY KEY (
        "facility_id"
     )
);

CREATE TABLE "Camp" (
    "campsite_id" bigint   NOT NULL,
    "facility_id" VARCHAR(200)   NOT NULL,
    "campsite" VARCHAR(100)   NOT NULL,
    "camp_type" VARCHAR(300)   NOT NULL,
    "stay" VARCHAR(200)   NOT NULL,
    "loops" VARCHAR(200)   NOT NULL,
    "accessible" BOOLEAN   NOT NULL,
    "lat" DECIMAL(10,6)   NOT NULL,
    "long" DECIMAL(10,6)   NOT NULL,
    "created" DATE   NOT NULL,
    "updated" DATE   NOT NULL,
    CONSTRAINT "pk_Camp" PRIMARY KEY (
        "campsite_id"
     )
);

CREATE TABLE "Museums" (
    "museum_id" VARCHAR(500)   NOT NULL,
    "museum_name" VARCHAR(1000)   NOT NULL,
    "legal_name" VARCHAR(1000)   NOT NULL,
    "alt_name" VARCHAR(100)   NOT NULL,
    "museum_type" VARCHAR(1000)   NOT NULL,
    "institution" VARCHAR(1000)   NOT NULL,
    "admin_address" VARCHAR(1000)   NOT NULL,
    "admin_city" VARCHAR(50)   NOT NULL,
    "admin_state" CHAR(2)   NOT NULL,
    "admin_zip" VARCHAR(30)   NOT NULL,
    "museum_address" VARCHAR(1000)   NOT NULL,
    "museum_city" VARCHAR(1000)   NOT NULL,
    "museum_state" CHAR(2)   NOT NULL,
    "museum_zip" Integer   NOT NULL,
    "phone" VARCHAR(50)   NOT NULL,
    "lat" DECIMAL(10,6)   NOT NULL,
    "long" DECIMAL(10,6)   NOT NULL,
    "locale_code" Integer   NOT NULL,
    "county_code" Integer   NOT NULL,
    "state_code" Integer   NOT NULL,
    "region_code" Integer   NOT NULL,
    "employee_id" VARCHAR(50)   NOT NULL,
    "tax_period" bigint   NOT NULL,
    "income" bigint   NOT NULL,
    "revenue" bigint   NOT NULL,
    CONSTRAINT "pk_Museums" PRIMARY KEY (
        "museum_id"
     )
);

ALTER TABLE "CityWeather" ADD CONSTRAINT "fk_CityWeather_city_state" FOREIGN KEY("city_state")
REFERENCES "City" ("city_state");

ALTER TABLE "CityFacts" ADD CONSTRAINT "fk_CityFacts_city_state" FOREIGN KEY("city_state")
REFERENCES "City" ("city_state");

ALTER TABLE "Tours" ADD CONSTRAINT "fk_Tours_facility_id" FOREIGN KEY("facility_id")
REFERENCES "Facilities" ("facility_id");

ALTER TABLE "Camp" ADD CONSTRAINT "fk_Camp_facility_id" FOREIGN KEY("facility_id")
REFERENCES "Facilities" ("facility_id");

