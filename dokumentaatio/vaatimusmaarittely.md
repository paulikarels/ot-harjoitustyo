# Vaatimusmäärittely

## Sovelluksen käyttötarkoitus
Sovellus toimii **verkkokurssialustana**, jonka pää ideana on mahdollistaa luoda kursseja ja niihin tehtäviä joita käyttäjä voi merkata tehdyksi, niin kuin "todo-list" tyylisesti.

Käyttäjä  voi graafisesti luoda ja poistaa kursseja, sekä seurata ja merkata tehdyksi omia tehtäviään. 
Käyttäjät  voivat vapaasti liittyä haluamiinsa tehtyihin kursseihin ja tarkastella omien vastauksien tuloksia ja niiden teko/suoritus päiviä kaaviolla.


## Rekisteröinti ja kirjautuminen
Käyttäjiä voidaan rekisteröidä ja sovellus tarkistaa käyttäjän olemassaolon ja hyväksyy tai hylkää sen käyttäjän olemassaolon mukaan.
- Käyttäjätunnuksen tulee olla uniikki ja pituudeltaan vähintään 4 merkkiä

Luoduilla käyttäjillä voi kirjautua luoduillaan tunnuksilla
- Jos käyttäjätunnusta ei ole olemassa tai salasana on väärä annetaan virheilmoitus


## Päänäkymä 
Näkymässsä käyttäjät voivat luoda kirjatumisen jälkeen uusia kursseja
- Kurssin nimi kentässä tulee olla arvo, muuten annetaan virheilmoitus
- Kurssin pistearvo tulee olla positiviinen numero, muuten annetaan virheilmoitus

 Käyttäjät voivat liittyä olemassa oleviin kursseihin graafista näkymää hyödyntäen tuplaklikkaamalla kurssia. 
   -  Käyttäjät voivat poistaa omia tehtyjä kursseja graafista näkymää hyödyntäen.

- Käyttäjät kykenevät vain liittymään olemassa oleviin kursseihin ja seurata omaa edistymistään.
    - Jos kursseja ei ole luotu selain popup taulu on tyhjä

 Käyttäjä voi kirjautua ulos


## Kurssin tehtävä näkymä

Käyttäjä kykenee luoda kurssille tehtäviä
- Ilmoitetaan jos tehtävä on jo olemassa tai tyhjä

Tehtävät voi merkata tehdyiksi graafista käyttöliittymää hyödyntäen
- Ilmoitetaan jos ei ole valittu merkattavaa tehtävää

## Jatkokehitysideoita

Antaa erikoisoikeuksia pääkäyttäjille (admin) esimerkiksi.