# Käyttöohje

### Sovelluksen toiminta
Sovellus on kenen vain tarkasteltavana etusivun, julkisten saalismerkintöjen ja kalalaji-infon osalta. Etusivulla toivotetaan tervetulleeksi käyttämään sovellusta sekä luetellaan kalalajeittain raportoidut saalismerkintöjen määrät.

Saalismerkintöjen listauksessa näkyy julkiset saalismerkinnät ja kalalaji-infosta löytyy tietoja kalalajien rauhoitukseen liittyen.

Kirjauduttuaan sisään käyttäjällä on lisäksi mahdollisuus lisätä oma saalismerkintä. Saalismerkinnän lisäyksen yhteydessä käyttäjä täyttää lomakkeen oleellisista tiedoista. Lisäksi käyttäjä voi päättää haluuko saalismerkinnän olevan julkinen (näkyy muille kirjautuneille että kirjautumattomille) vai yksityinen, jolloin saalismerkinnän näkee vain itse. Vain saalismerkinnän lisännyt tai ylläpitäjä voi poistaa/muokata saalismerkintää.

Kirjautuneena käyttäjä voi myös lisätä uuden kalalajin ja siihen liittyvät tiedot, jos kalalajia ei vielä ole. Jokainen kirjautunut käyttäjä voi muokata kalalajien tietoja tai poistaa kalalajin.

Kirjautuneille käyttäjille on myös saalismerkintöjen hakuominaisuus. Saalismerkintöjen listaamisen lisäksi hakua on mahdollisuus filteröidä.

### Kirjautuminen sekä rekisteröityminen
Kirjautuminen tapahtuu sovelluksen oikeasta yläkulmasta painamalla *Login*-nappia. Toisaalta jos sovellusta käyttää kirjautumaton käyttäjä, joka aikoo tehdä jotain kirjautumisen vaativaa, sovellus ohjaa kirjautumissivulle.

Rekisteröityminen tapahtuu myös oikeasta yläkulmasta painamalla *Sign up*-nappia. Käyttäjältä pyydetään nimeä, käyttäjänimeä sekä salasanaa (kahdesti). Nimi ei saa olla tyhjä ja sen pitää olla uniikki, käyttäjänimen on oltava uniikki sekä sisältää 8-20 merkkiä. Salasanan on oltava vähintään 10 merkkiä ja täsmätä kahdesti kirjoittaessa.

### Perustoiminnot

Sovelluksen ylälaidassa on erilaisia toimintoihin vieviä otsikoita. Käydään nämä lävitse.

__Front page__ - ohjaa etusivulle, jossa tervetulotoivotus ja listattuna sovellukseen raportoitujen saaliideen määrä kalalajeittain (esimerkiksi *taimen: 43*) ja suuruusjärjestyksessä (eniten napatut ensin).

__List catches__ - listaa omat sekä julkiset saalismerkinnät. Saalismerkinnöistä näytetään *kalalaji, viehe vai perho, pituus (cm), paino (kg), paikka, kuvaus, lisätty, kalastaja (julkisissa). Kirjautuneelle käyttäjällä näkyy omien saalismerkintöjen yhteydessä *Change or delete*-nappi, josta voi muokata tai poistaa saalismerkinnän.

__Add a new catch__ - on uuden saalismerkinnän lisäyslomake. Saalismerkintä on muotoa *kalalaji, viehe vai perho, pituus (cm), paino (kg), kalapaikka, kuvaus, yksityinen vai julkinen* Lomakkeen lähettämiseksi vaaditaan, että kalalajin on oltava lisätty sovellukseen, pituuden on oltava arvo välillä 0.1-500.0, painon on oltava arvo välillä 0.1-50.0 ja kuvauksen 3-100 merkkiä. Lisäksi vaihtoehto valinnoissa on valittava jokin vaihtoehdoista.

__Details about species__ - listaa sovellukseen lisätyt kalalajit ja niihin liittyvät tiedot muodossa *kalalaji, alamitta, rauhoitusaika alkaa, rauhoitusaika päättyy*. Kirjautuneille näkyy lisäksi *Change or delete*-nappi josta voi muokata tietoja tai poistaa kalalajin.

__Add a new species__ - on uuden kalalajin lisäyslomake. Kalalajin on oltava uniikki, alamitan arvo väliltä 0.0-150.0 ja päivämäärät oikeaa muotoa (päivät 1-31 ja kuukaudet 1-12).

__Search__ - on hakutoiminto, jossa voi _List catches_ kohdan mukaisesti listata saalismerkintöjä. Täällä kuitenkin voi listauksen (uusimmat ensin) lisäksi filteröidä tuloksia esimerkiksi kalalajin ja/tai kalapaikan perusteella. Lisäksi kaikki haut voi muuttaa järjestetyiksi kalan koon perusteella (ensin painon sitten pituuden).
