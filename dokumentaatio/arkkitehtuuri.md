# Ohjelman arkkitehtuuri

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


Toiminnallisuudesta vastaa luokka [AppService](https://github.com/paulikarels/ot-harjoitustyo/blob/main/verkkokurssi-app/src/services/app_service.py) (työn alla, tällä hetkellä UI luokka vastaa kyseistä).

AppService pääsee seuraaviin luokkiin; User, Course ja Exercise  [CourseRepository](https://github.com/paulikarels/ot-harjoitustyo/blob/main/verkkokurssi-app/src/repositories/course_repository.py), [UserRepository](https://github.com/paulikarels/ot-harjoitustyo/blob/main/verkkokurssi-app/src/repositories/user_repository.py) ja [ExerciseRepository](https://github.com/paulikarels/ot-harjoitustyo/blob/main/verkkokurssi-app/src/repositories/exercise_repository.py) kautta.

```mermaid
 classDiagram
      AppService ..> UserRepository
      UserRepository ..> User
      AppService "0..1" -- "0..1" User
      AppService ..> CourseRepository 
      CourseRepository ..> Course
      AppService "0..1" -- "0..1" Course
      AppService ..> ExerciseRepository
      ExerciseRepository ..> Exercise
      AppService "0..1" -- "0..1" Exercise
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
