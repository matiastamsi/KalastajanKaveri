# User stories / Käyttäjätarinat

Oli käyttäjä sitten vapaa-ajan kalastaja, kalastuskilpailun järjestäjä, kalastuksenvalvoja tms. Voi käyttäjä...

- ... tarkastella etusivulla sivustolle raportoitujen napattujen kalojen määrää (kalalaji kohtaisesti ja järjestetty suurimmasta pienimpään). __Raaka SQL-kysely__.

      SELECT Fish.name, COUNT(Catch.species_id) as count FROM Fish LEFT JOIN Catch ON Fish.id = Catch.species_id GROUP BY Fish.name ORDER BY count DESC

- ... luoda uuden käyttäjätilin.

      INSERT INTO account (date_created, date_modified, name, username, password, role) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)

- ... muokata käyttäjätiliään.

      UPDATE account SET date_modified=CURRENT_TIMESTAMP, password=? WHERE account.id = ?

- ... poistaa käyttäjätilinsä.

      DELETE FROM account WHERE account.id = ?

- ... lisätä saalismerkinnän.

      INSERT INTO catch (date_created, date_modified, lure_or_fly, length, weight, spot, description, private_or_public, account_id, species_id, fisher) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?, ?, ?, ?)

- ... muokata saalismerkintäänsä.

      UPDATE catch SET date_modified=CURRENT_TIMESTAMP, length=?, weight=?, spot=?, description=? WHERE catch.id = ?

- ... poistaa saalismerkintänsä.

      DELETE FROM catch WHERE catch.id = ?

- ... voi listata kaikki omat saaliit (uusin ensin).

      SELECT catch.id AS catch_id, catch.date_created AS catch_date_created, catch.date_modified AS catch_date_modified, catch.lure_or_fly AS catch_lure_or_fly, catch.length AS catch_length, catch.weight AS catch_weight, catch.spot AS catch_spot, catch.description AS catch_description, catch.private_or_public AS catch_private_or_public, catch.account_id AS catch_account_id, catch.species_id AS catch_species_id, catch.fisher AS catch_fisher FROM catch WHERE catch.account_id = ? ORDER BY catch.date_created DESC

- ... voi listata kaikki julkiset saaliit (uusin ensin).

      SELECT catch.id AS catch_id, catch.date_created AS catch_date_created, catch.date_modified AS catch_date_modified, catch.lure_or_fly AS catch_lure_or_fly, catch.length AS catch_length, catch.weight AS catch_weight, catch.spot AS catch_spot, catch.description AS catch_description, catch.private_or_public AS catch_private_or_public, catch.account_id AS catch_account_id, catch.species_id AS catch_species_id, catch.fisher AS catch_fisher FROM catch WHERE catch.private_or_public = ? ORDER BY catch.date_created DESC

- ... tarkistaa listasta kalalajikohtaiset tiedot.

      SELECT fish.id AS fish_id, fish.date_created AS fish_date_created, fish.date_modified AS fish_date_modified, fish.name AS fish_name, fish.minimum_catch_size AS fish_minimum_catch_size, fish.closed_season_starts AS fish_closed_season_starts, fish.closed_season_ends AS fish_closed_season_ends FROM fish

- ... voi lisätä uuden kalalajin, jos sitä ei vielä ole.

      INSERT INTO fish (date_created, date_modified, name, minimum_catch_size, closed_season_starts, closed_season_ends) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)

- ... voi muokata kalalajia, jos esimerkiksi tieto virheellistä.

      UPDATE fish SET date_modified=CURRENT_TIMESTAMP, name=?, minimum_catch_size=? WHERE fish.id = ?

- ... voi poistaa kalalajin.

      DELETE FROM fish WHERE fish.id = ?

- ... voi hakea saalismerkintöjä kalalajin perusteella.

       //Etsii ensin kalalajin id:n nimen perusteella. 
       SELECT fish.id AS fish_id, fish.date_created AS fish_date_created, fish.date_modified AS fish_date_modified, fish.name AS fish_name, fish.minimum_catch_size AS fish_minimum_catch_size, fish.closed_season_starts AS fish_closed_season_starts, fish.closed_season_ends AS fish_closed_season_ends FROM fish WHERE fish.name = ?

      //Suorittaa seuraavan kyselyn kun kalalajin id on tiedossa.
      SELECT catch.id AS catch_id, catch.date_created AS catch_date_created, catch.date_modified AS catch_date_modified, catch.lure_or_fly AS catch_lure_or_fly, catch.length AS catch_length, catch.weight AS catch_weight, catch.spot AS catch_spot, catch.description AS catch_description, catch.private_or_public AS catch_private_or_public, catch.account_id AS catch_account_id, catch.species_id AS catch_species_id, catch.fisher AS catch_fisher FROM catch WHERE catch.species_id = ?
      
- ... voi hakea saalismerkintöjä kalapaikan perusteella.

      SELECT catch.id AS catch_id, catch.date_created AS catch_date_created, catch.date_modified AS catch_date_modified, catch.lure_or_fly AS catch_lure_or_fly, catch.length AS catch_length, catch.weight AS catch_weight, catch.spot AS catch_spot, catch.description AS catch_description, catch.private_or_public AS catch_private_or_public, catch.account_id AS catch_account_id, catch.species_id AS catch_species_id, catch.fisher AS catch_fisher FROM catch WHERE catch.spot = ?
      
- ... voi hakea saalismerkintöjä kalapaikan ja kalalajin perusteella.

      //Etsii ensin kalalajin id:n nimen perusteella.
      SELECT fish.id AS fish_id, fish.date_created AS fish_date_created, fish.date_modified AS fish_date_modified, fish.name AS fish_name, fish.minimum_catch_size AS fish_minimum_catch_size, fish.closed_season_starts AS fish_closed_season_starts, fish.closed_season_ends AS fish_closed_season_ends FROM fish WHERE fish.name = ?

      //Suorittaa seuraavan kyselyn kun kalalajin id on tiedossa.
      SELECT catch.id AS catch_id, catch.date_created AS catch_date_created, catch.date_modified AS catch_date_modified, catch.lure_or_fly AS catch_lure_or_fly, catch.length AS catch_length, catch.weight AS catch_weight, catch.spot AS catch_spot, catch.description AS catch_description, catch.private_or_public AS catch_private_or_public, catch.account_id AS catch_account_id, catch.species_id AS catch_species_id, catch.fisher AS catch_fisher FROM catch WHERE catch.species_id = ? AND catch.spot = ?

- ... voi hakea saalismerkintöjä kalan koon perusteella. 

      //Edellä mainittuihin saalismerkintöjen hakuihin lisätään perään vain:
      ... ORDER BY catch.weight DESC, catch.length DESC

Saalismerkintöjen listausoperaatioissa suoritetaan myös kysely kalalajin nimestä sekä julkisten saalismerkintöjen kohdalla kalastajan nimestä. Nämä ovat myös toteutettu __raakoina SQL-kyselyinä__.

      //Kalalajin nimi id:n perusteella
      SELECT Fish.name FROM Fish WHERE Fish.id = ?

      //Kalastajan nimi id:n perusteella
      SELECT name FROM account WHERE id = ?
