# Vaatimusmäärittely
## Sovelluksen tarkoitus
##### Sovellus on simppeli watchlist-sovellus, johon käyttäjä voi lisätä elokuvia, joita hän aikoo katsoa. Käyttäjä voi lisätä elokuvia ohjaajan, käsikirjoittajan ja kuvaajan mukaan, niin että kun käyttäjä hakee ohjaajan nimen, antaa sovellus kaikki ohjaajan elokuvat, jotka käyttäjä on lisännyt watchlistiinsa. Jokaisella käyttäjällä on yksilöity watchlist.
## Käyttäjät
##### Sovelluksessa on vain rekisteröityneet käyttäjät, mutta tarpeen mukaan sovelluksen kehittyessä voidaan siihen lisätä käyttäjiä, joilla on enemmän oikeuksia.
## Käyttöliittymäluonnos
##### Sovelluksessa on 3 näkymää: kirjaudu, luo käyttäjä ja itse sovellus josta löytyy kaikki sen toiminnallisuudet. Kirjaudu ja luo käyttäjä toimivat kaikille tutulla tavalla. Sovelluksessa itsessään on kolme kategoriaa: ohjaajat, käsikirjoittajat ja kuvaajat. Kun klikkaat vaikka ohjaajaa vie sovellus sinut ohjaajan sivulle, jossa on kaikki elokuvat, jotka olet lisännyt ohjaajan alle watchlistiin.
## Perusversio
### Ennen kirjautumista
* Käyttäjällä on mahdollisuus luoda käyttäjätunnus sovellukseen

	Käyttäjätunnuksen on oltava uniikki

* Käyttäjä voi kirjautua luomalleen tilille
	
	Käyttäjätunnuksen on oltava luotuna ja salasanan on mentävä oikein

### Kirjautumisen jälkeen
* Alku näkymässä on kategoriat ohjaajat, käsikirjoittajat ja kuvaajat.
	
	Käyttäjä voi klikata haluamaansa kategoriaa, joka vie kategorian sivulle

* Ohjaajat, käsikirjoittajat ja kuvaajat näkymät ovat identtisiä

	Käyttäjä voi klikata henkilön nimeä, joka vie henkilön alle lisättyihin elokuviin tai lisätä kategoriaan uuden henkilön nimen

* Nimen alla olevat näkymät ovat myös identtisiä

	Käyttäjä pääsee lisäämään uusia elokuvia ja merkkaamaan elokuvat katsotuiksi
## Jatkokehitys
Sovellusta voidaan perusrakenteen jälkeen kehittää seuraavalla lailla: 
* Käyttäjä pystyy arvostella katsomansa elokuvat, jolloin ne siirtyvät nimen alla katsotut kategoriaan. Tämän jälkeen sovellus näyttää nimen vieressä käyttäjän kyseiselle nimelle antamien elokuvien keskiarvon
* Sovellus voisi hakea netistä tietoa, jota voitaisiin käyttää mm. seuraaviin tarkoituksiin:
	
	Jos käyttäjä lisää elokuvan vaikkapa ohjaajan nimen alle ja myös elokuvan kuvaaja löytyy sovelluksesta, lisätään se automaattisesti myös kuvaajan watchlistiin
	
	Sovellus voi ehdottaa ohjaajan, kuvaajan tai käsikirjoittajan mukaan elokuvia käyttäjälle
	  
	  
