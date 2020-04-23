# User stories / Käyttäjätarinat

Oli käyttäjä sitten vapaa-ajan kalastaja, kalastuskilpailun järjestäjä, kalastuksenvalvoja tms. Voi käyttäjä...

- ... luoda uuden käyttäjätilin. :heavy_check_mark:

INSERT INTO account (date_created, date_modified, name, username, password, role) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)

- ... muokata käyttäjätiliään. :heavy_check_mark:

UPDATE account SET date_modified=CURRENT_TIMESTAMP, password=? WHERE account.id = ?

- ... poistaa käyttäjätilinsä. :heavy_check_mark:

DELETE FROM account WHERE account.id = ?

- ... lisätä saalismerkinnän. :heavy_check_mark:

INSERT INTO catch (date_created, date_modified, lure_or_fly, length, weight, spot, description, private_or_public, account_id, species_id, fisher) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?, ?, ?, ?)

- ... muokata saalismerkintäänsä. :heavy_check_mark:

UPDATE catch SET date_modified=CURRENT_TIMESTAMP, length=?, weight=?, spot=?, description=? WHERE catch.id = ?

- ... poistaa saalismerkintänsä. :heavy_check_mark:

DELETE FROM catch WHERE catch.id = ?

- ... voi listata kaikki omat saaliit. :heavy_check_mark:

SELECT catch.id AS catch_id, catch.date_created AS catch_date_created, catch.date_modified AS catch_date_modified, catch.lure_or_fly AS catch_lure_or_fly, catch.length AS catch_length, catch.weight AS catch_weight, catch.spot AS catch_spot, catch.description AS catch_description, catch.private_or_public AS catch_private_or_public, catch.account_id AS catch_account_id, catch.species_id AS catch_species_id, catch.fisher AS catch_fisher 
FROM catch 
WHERE catch.account_id = ?

- ... voi listata kaikki julkiset saaliit. :heavy_check_mark:

SELECT catch.id AS catch_id, catch.date_created AS catch_date_created, catch.date_modified AS catch_date_modified, catch.lure_or_fly AS catch_lure_or_fly, catch.length AS catch_length, catch.weight AS catch_weight, catch.spot AS catch_spot, catch.description AS catch_description, catch.private_or_public AS catch_private_or_public, catch.account_id AS catch_account_id, catch.species_id AS catch_species_id, catch.fisher AS catch_fisher 
FROM catch 
WHERE catch.private_or_public = ?

- ... tarkistaa listasta kalalajikohtaiset tiedot. :heavy_check_mark:

SELECT fish.id AS fish_id, fish.date_created AS fish_date_created, fish.date_modified AS fish_date_modified, fish.name AS fish_name, fish.minimum_catch_size AS fish_minimum_catch_size, fish.closed_season_starts AS fish_closed_season_starts, fish.closed_season_ends AS fish_closed_season_ends 
FROM fish

- ... voi lisätä uuden kalalajin, jos sitä ei vielä ole. :heavy_check_mark:

INSERT INTO fish (date_created, date_modified, name, minimum_catch_size, closed_season_starts, closed_season_ends) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)

- ... voi muokata kalalajia, jos tieto virheellistä. :heavy_check_mark:

UPDATE fish SET date_modified=CURRENT_TIMESTAMP, name=?, minimum_catch_size=? WHERE fish.id = ?

- ... voi poistaa kalalajin. :heavy_check_mark:

DELETE FROM fish WHERE fish.id = ?

- ... voi katsella, mistä on saatu tiettyjä kaloja.
- ... voi katsella, milloin on saatu kalaa.
- ... voi etsiä ennätyksiä.


