# KalastajanKaveri

KalastajanKaveri-sovelluksella jokainen kalastaja voi pitää kirjaa omista saaleistaan
sekä nähdä muiden jakamia saalismerkintöjä - jos he suinkaan haluavat paljastaa niitä!
Toisaalta omien vonkaleiden esittely on varmasti jokaisen kalastajan mielessä.

[Sovellus Herokussa](https://quiet-stream-39899.herokuapp.com/)

## Toiminnot

- saalismerkinnän lisäys (mm. kalalaji, pituus, paino, kalapaikka, päivämäärä sekä ajankohta,
kuvaus sekä tieto siitä, että onko saalismerkintä julkinen vai yksityinen)

- saalismerkintöjen haku (omat ja julkiset):

  - kaiken kaikkiaan (kahden vuoden ajalta)
  - kalapaikan perusteella (kahden vuoden ajalta)
  - päivämäärän perusteella
  - kalapaikan sekä päivämäärän perusteella
  - kalalajin perusteella (kahden vuoden ajalta)
  - kalalajin ja kalapaikan perusteella (kahden vuoden ajalta)
  - kalalajin ja päivämäärän perusteella
  - painavin saalis
  - pisin saalis

- kalalajien rauhoitusaikojen ja alamittojen lisäys paikkakohtaisesti

- kalalajien rauhoitusaikojen ja alamittojen haku (esim. paikkakohtaisesti) 

## Dokumentaatio

[Tietokantakaavio](https://github.com/matiastamsi/KalastajanKaveri/blob/master/images/database_diagram.png)

[User stories](https://github.com/matiastamsi/KalastajanKaveri/blob/master/documentation/User_stories.md)

[Käyttöohje](https://github.com/matiastamsi/KalastajanKaveri/blob/master/documentation/kayttoohje.md)

[Asennusohje](https://github.com/matiastamsi/KalastajanKaveri/blob/master/documentation/asennusohje.md)


## Rekisteröinti ja kirjautuminen

Tällä hetkellä validoidaan seuraavat asiat:
  - Käyttäjän nimen on oltava vähintään kaksi merkkiä pitkä
  - Käyttäjätunnuksen on oltava uniikki (tietokannassa ei toista) sekä vähintään 8 merkkiä pitkä.
  - Salasanan on oltava vähintään 10 merkkiä pitkä sekä täsmätä kahdesti kirjoittaessa.
