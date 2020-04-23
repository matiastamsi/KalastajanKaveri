# Tietokantarakenne

## Tietokantakaavio

![tietokantakaavio](https://github.com/matiastamsi/KalastajanKaveri/blob/master/documentation/images/database_diagram.png)

## Tietokannanluomiskomennot

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password TEXT NOT NULL, 
	role INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	UNIQUE (username)
)

CREATE TABLE fish (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	minimum_catch_size INTEGER, 
	closed_season_starts VARCHAR, 
	closed_season_ends VARCHAR, 
	PRIMARY KEY (id), 
	UNIQUE (name)
)

CREATE TABLE catch (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	lure_or_fly VARCHAR(144) NOT NULL, 
	length FLOAT NOT NULL, 
	weight FLOAT NOT NULL, 
	spot VARCHAR(144) NOT NULL, 
	description VARCHAR(144) NOT NULL, 
	private_or_public VARCHAR(144) NOT NULL, 
	account_id INTEGER, 
	species_id INTEGER, 
	fisher VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(species_id) REFERENCES fish (id)
)
