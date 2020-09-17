-- Create city table
-- drop table city;
CREATE TABLE city (
	state_name VARCHAR(30),
	city VARCHAR(50),
	city_state VARCHAR(90) PRIMARY KEY,
	population VARCHAR(15),
	state_code CHAR(2),
	lat DECIMAL(10,6),
	long DECIMAL(10,6),
	region_specific VARCHAR(30),
	region_general VARCHAR(30)
);

-- city weather table
drop table city_weather;
CREATE TABLE city_weather (
	city VARCHAR(50),
	city_state VARCHAR(90),
	measure VARCHAR(30),
	jan DECIMAL(10,2),
	feb DECIMAL(10,2),
	mar DECIMAL(10,2),
	apr DECIMAL(10,2),
	may DECIMAL(10,2),
	jun DECIMAL(10,2),
	jul DECIMAL(10,2),
	aug DECIMAL(10,2),
	sep DECIMAL(10,2),
	oct DECIMAL(10,2),
	nov DECIMAL(10,2),
	dec DECIMAL(10,2),
	year DECIMAL(10,2),
	FOREIGN KEY (city_state) REFERENCES city(city_state)
);

ALTER TABLE city_weather 
ADD COLUMN id SERIAL PRIMARY KEY;
SELECT * FROM city_weather;

-- Create city facts table
drop table city_facts;
CREATE TABLE city_facts (
	city VARCHAR(30) NOT NULL,
	city_state VARCHAR(90),
	named_for VARCHAR(100),
	settled VARCHAR(100),
	founded VARCHAR(100),
	incorporated VARCHAR(100),
	mayor VARCHAR(50),
	land_area VARCHAR(30),
	water_area VARCHAR(50),
	elevation VARCHAR(100),
	time_zone VARCHAR(50),
	FOREIGN KEY (city_state) REFERENCES city(city_state)
);

ALTER TABLE city_facts 
ADD COLUMN id SERIAL PRIMARY KEY;
SELECT * FROM city_facts;

-- Create tours table
DROP TABLE tours;
CREATE TABLE tours (
	tour_id Integer NOT NULL,
	facility_id VARCHAR(200) NOT NULL,
	tour_name VARCHAR(500),
	tour_type VARCHAR(30),
	description VARCHAR(5000),
	duration Integer,
	accessible BOOLEAN DEFAULT false,
	created_date DATE,
	updated_date DATE
);

ALTER TABLE tours add constraint facility_id FOREIGN KEY(facility_id) REFERENCES facilities(facility_id);

-- Create facilities table
DROP TABLE facilities;
CREATE TABLE facilities (
	facility_id VARCHAR(200) NOT NULL PRIMARY KEY,
	legacy_id VARCHAR(200),
	org_id VARCHAR(200),
	parent_id VARCHAR(200),
	rec_id VARCHAR(200),
	facility_name VARCHAR(500),
	description VARCHAR(100000),
	facility_type VARCHAR(1000),
	use_fee VARCHAR(2000),
	directions VARCHAR(100000),
	phone VARCHAR(1000),
	email VARCHAR(1000),
	res_url VARCHAR(300),
	map_url VARCHAR(300),
	ada_access VARCHAR(1000),
	lat DECIMAL(10,6),
	long DECIMAL(10,6),
	keywords VARCHAR(1000),
	stay_limit VARCHAR(1000),
	reservable BOOLEAN DEFAULT false,
	enabled BOOLEAN DEFAULT false,
	updated_date DATE
);

-- Create campsite table
DROP TABLE camp;
CREATE TABLE camp (
	campsite_id bigint NOT NULL PRIMARY KEY,
	facility_id VARCHAR(200) NOT NULL,
	campsite VARCHAR(100),
	camp_type VARCHAR(300),
	stay VARCHAR(200),
	loops VARCHAR(200),
	accessible BOOLEAN DEFAULT false,
	lat DECIMAL(10,6),
	long DECIMAL(10,6),
	created DATE,
	updated DATE,
	FOREIGN KEY (facility_id) REFERENCES facilities(facility_id)
);

-- Create museums table
DROP TABLE museums;
CREATE TABLE museums (
	museum_id VARCHAR(500) NOT NULL PRIMARY KEY,
	museum_name VARCHAR(1000) NOT NULL,
	legal_name VARCHAR(1000),
	alt_name VARCHAR(100),
	museum_type VARCHAR(1000),
	institution VARCHAR(1000),
	admin_address VARCHAR(1000),
	admin_city VARCHAR(50),
	admin_state CHAR(2),
	admin_zip VARCHAR(30),
	museum_address VARCHAR(1000),
	museum_city VARCHAR(1000),
	museum_state CHAR(2),
	museum_zip Integer,	 
	phone VARCHAR(50), 
	lat DECIMAL(10,6),
	long DECIMAL(10,6),
	locale_code Integer,
	county_code Integer,
	state_code Integer,					
	region_code Integer,					
	employee_id VARCHAR(50),
	tax_period bigint,
	income bigint,
	revenue bigint					
);