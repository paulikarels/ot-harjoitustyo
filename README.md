# Ohjelmistotekniikka, harjoitustyö
Oppimassa **ohjelmistotuotantoprosessin** *suunnittelusta* ja sen muista vaiheista!
##  Tehtävät

- [laskarit](https://github.com/paulikarels/ot-harjoitustyo/tree/main/laskarit)

##  Dokumentaatio

- [dokumentaatiot](https://github.com/paulikarels/ot-harjoitustyo/tree/main/dokumentaatio)
  - [vaatimusmäärittely](https://github.com/paulikarels/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
  - [tuntikirjanpito](https://github.com/paulikarels/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)
    - [tuntikirjanpito](https://github.com/paulikarels/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)



## Asennus

1. Asenna riippuvuudet verkkokurssi-app polusta komennolla

```bash
poetry install
```

3. Käynnistä sovellus komennolla

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