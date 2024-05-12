# Testausdokumentti

Ohjelmaa on testattu automatisoitujen yksikkö- ja integraatiotestien avulla unittestilla sekä manuaalisilla järjestelmätason testeillä.

## Yksikkö- ja integraatiotestaus

### Repository-luokat

Luokkia testataan testeissä käytössä olevilla repository tiedostoilla. _UserRepository_-luokkaa testataan [TestUserRepository](https://github.com/paulikarels/ot-harjoitustyo/blob/main/verkkokurssi-app/src/tests/repositories/user_repository_test.py)-luokalla, _CourseRepository_-luokkaa testataan [TestCourseRepository](https://github.com/paulikarels/ot-harjoitustyo/blob/main/verkkokurssi-app/src/tests/repositories/course_repository_test.py)-luokalla ja _ExerciseRepository_-luokkaa testataan [TestExerciseRepository](https://github.com/paulikarels/ot-harjoitustyo/blob/main/verkkokurssi-app/src/tests/repositories/exercise_repository_test.py)-luokalla.

### Sovelluslogiikka

_AppService_-luokkaa testataan [TestAppService](https://github.com/paulikarels/ot-harjoitustyo/blob/main/verkkokurssi-app/src/tests/services/appservice_test.py)-luokalla.

### Testikattavuus

Testikattavuuden haarautumakattavuus on sovelluksessa 93%. 
Testaamatta on jättetty _config.py_ ja _databaselogic_ kansiossa olevat tietokantaa laativat tiedostot.

## Järjestelmätestaus

Järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellusta on testattu [käyttöohjeen](https://github.com/paulikarels/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md) kuvaamalla tavalla käyttöliittymää noudattaen.

Sovelluksen testaus on replikoitu tilanteessa, jossa ei ole ja on ennakko dataa tietokannassa. 

### Toiminnallisuudet

Kaikki [määrittelydokumentin](https://github.com/paulikarels/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md) ja käyttöohjeen toiminnallisuudet on testattu ja käyty läpi myös mahdollisilla virheellisillä arvoilla. 

## Sovelluksen laatuongelmat

Sovellus ei anna virheilmoitusta, jos buildattua SQLite tietokantaa ei ole alustettu, vaikka se ei ole pakollinen.