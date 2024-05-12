# Verkkokurssisovellus
Verkkokurssisovellus, jossa käyttäjät voivat luoda kursseja ja niihin tehtäviä, jota voidaan tehdä!


Löydät ladattavat releasit versioineen [täältä](https://github.com/paulikarels/ot-harjoitustyo/releases) tai alhaalta Dokumentaatio osiosta.

##  Dokumentaatio

- [dokumentaatiot](https://github.com/paulikarels/ot-harjoitustyo/tree/main/dokumentaatio)
  - [vaatimusmäärittely](https://github.com/paulikarels/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
  - [tuntikirjanpito](https://github.com/paulikarels/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)
  - [changelog](https://github.com/paulikarels/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
  - [arkkitehtuuri](https://github.com/paulikarels/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
  - [kayttöohje](https://github.com/paulikarels/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)
  - [testausdokumentti](https://github.com/paulikarels/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md)
  - [ensimmäinen release](https://github.com/paulikarels/ot-harjoitustyo/releases/tag/viikko5)
  - [toinen release](https://github.com/paulikarels/ot-harjoitustyo/releases/tag/viikko6)
  - [Loppupalautus release (uusin)](https://github.com/paulikarels/ot-harjoitustyo/releases/tag/viikko7)



## Asennus
Ensikisi, sinulla tulee olla *poetry* sekä *python* versio >= **^3.8** asennettuna.

Pura asenettu sovellus ja jatka ohjeiden mukaan:

1. Asenna riippuvuudet verkkokurssi-app polusta komennolla

```bash
poetry install
```

2. Vaadittavat alustustoimipiteet suoritetaan komennolla

```bash
poetry run invoke build
```
3. Aktivoi virtuaaliympäristö (Suositeltavaa)

```bash
poetry shell
```


4. Käynnistä sovellus komennolla

```bash
poetry run invoke start
```

## Komentorivitoiminnot
Komennot suoritettettava alussa~ verkkokurssi-app hakemistopolussa
### Ohjelman suorittaminen

Käynnistä ohjelma:

```bash
poetry run invoke start
```

### Testaus

Suorita testit:

```bash
poetry run invoke test
```

### Testikattavuus

Luo testikattavuusraportti:

```bash
poetry run invoke coverage-report
```

Raportti löytyy htmlcov-hakemistosta.

