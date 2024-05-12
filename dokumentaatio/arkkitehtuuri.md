# Arkkitehtuurikuvaus

## Rakenne

Koodin pakkausrakenne on seuraava:

```mermaid
classDiagram

    ui..>repositories
    services..>ui
    repositories..>entities
```
 Pakkaus **services**, joka sisältää käyttöliittymästä vastaavan pakkauksen ja koodin (**UI**). UI on  riippuvainen pakkauksesta  **repositories**, jonka avulla poimitaan näyttettäviä tietoja.  **repositories** sisältää  tallennuksesta vastaavaa koodia ja pakkaus **entities** sisältää luokkia, jotka kuvastavat sovelluksen oloita. 


## Käyttöliittymä

Käyttöliittymä sisältää seuraavat näkymät:
- Kirjautuminen (aloitussivu)
- käyttäjän rekisteröintisivu
- Kurssinäkymä
- Tehtävänäkymä

 UI luokka vastaa kaikista näkymistä. Vain yksi näkymä on näkyvillä ja jokainen on toteutettu omana luokkana.
 
## Sovelluslogiikka

Sovellus muodostuu seuraavista luokista:

- [User](https://github.com/paulikarels/ot-harjoitustyo/blob/main/verkkokurssi-app/src/entities/user.py)
- [Course](https://github.com/paulikarels/ot-harjoitustyo/blob/main/verkkokurssi-app/src/entities/course.py)
- [Exercise](https://github.com/paulikarels/ot-harjoitustyo/blob/main/verkkokurssi-app/src/entities/exercise.py)

```mermaid
 classDiagram
      User "1" --> "*" Course 
      Course "1" --> "*" Exercise
      class User{
          username
          password
          admin
      }
      class Course{
          title
          credits
          user
      }
      class Exercise{
          description
          done
          courseID
      }
```

Toiminallisuus alkaa User luokasta, joka voi luoda kursseja ja siihen tehtäviä.
Metodit käyttäjien ja kurssien luomiseen ovat esimerkiksi:
- `create_user(self, user)`
- `create_course(self, course, user_id)`


Toiminnallisuudesta vastaa luokka [AppService](https://github.com/paulikarels/ot-harjoitustyo/blob/main/verkkokurssi-app/src/services/app_service.py) , mikä viittaa UI luokkaan, joka hoitaa näkymät ja niiden poimittavat datat.

AppService pääsee seuraaviin luokkiin UI:n kautta; User, Course ja Exercise  [CourseRepository](https://github.com/paulikarels/ot-harjoitustyo/blob/main/verkkokurssi-app/src/repositories/course_repository.py), [UserRepository](https://github.com/paulikarels/ot-harjoitustyo/blob/main/verkkokurssi-app/src/repositories/user_repository.py) ja [ExerciseRepository](https://github.com/paulikarels/ot-harjoitustyo/blob/main/verkkokurssi-app/src/repositories/exercise_repository.py) kautta.

```mermaid
 classDiagram
      AppService ..> UI
      UI ..> UserRepository
      UserRepository ..> User
      UI "0..1" -- "0..1" User
      UI ..> CourseRepository 
      CourseRepository ..> Course
      UI "0..1" -- "0..1" Course
      UI ..> ExerciseRepository
      ExerciseRepository ..> Exercise
      UI "0..1" -- "0..1" Exercise
      Course "*" -- "1" User
      Course "1" -- "*" Exercise
```


## Päätoiminnallisuudet

Sovelluksemme ja sen toimintalogiikka voidaan kuvata  sekvenssikaaviona.

### Käyttäjän luominen

Uuden käyttäjän luomista varten tarvitaan käyttäjätunnus (uniikki), salasana ja ylläpitäjätieto. Käyttäjän luonti eteenee "Create User" painikkea painaen.

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant AppService
    participant UserRepository
    participant testUser
    User->>UI: click "Create User" button
    UI->>AppService: create_user("testUser", "test", true)
    AppService->>UserRepository: get_user_by_username_and_password("testUser", "test")
    UserRepository-->>AppService: None
    AppService->>testUser: User("testUser", "test", true)
    AppService->>UserRepository: create_user(testUser)
    UserRepository-->>AppService: user
    AppService-->>UI: user
    UI->>UI: _show_online_course_view()
```

Logiikkaamme alkaa painamisenjälkeen Appservicestä, jossa hoidamme käyttäjätunnuksen ja UserRepository:n avulla varmistemme sen olemassa olon.
Tämän jälkeen tallennamme uuden luodun Userin create_user metodilla. Käyttäjä luonnin jälkeen voidaan UI:n avulla jatkaa/kirjautua Kurssinäkymään.

### Sisäänkirjautuminen

Käyttäjä voi kirjautua luodun käyttäjän jälkeen tunkemalla käyttäjätunnuksen ja salasanan syötekenttiin ja klikkaamalla painiketta "Log in".

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant AppService
    participant UserRepository
    User->>UI: click "Log in" button
    UI->>AppService: _handle_login("testUser", "test")
    AppService->>UserRepository: get_user_by_username_and_password("testUser", "test")
    UserRepository-->>AppService: user
    AppService-->>UI: user
    UI->UI: _show_online_course_view()
```

Yhtälailla kuin luomisessa, "Log in" painamisen jälkeen `AppService` etsii metodillaa onko käyttäjä olemassa sen käyttäjätunnuksella ja salasanalla
`UserRepository`:n avulla. Tämän jälkeen `UserRepository` selvittää ovatko tunnukset olemassa ja täsmäävätkö tunnukset tietokannassa olevien kanssa. Nyt näiden jälkeen käyttäjä pääsee Kurssinäkymään kirjautuneella käyttäjällä.
