from entities.user import User

class UserRepository:
    """
    Luokka, joka vastaa käyttäjiin liittyvistä tietokanta toiminnoista.
    """
    def __init__(self, connection):
        """
        Luokan konstruktori.

        Args:
            connection: Tietokantayhteysobjekti, joka vastaa tietokantayhteydestä.
        """
        self._connection = connection

    def create_user(self, user):
        """
        Tallentaa luodun käyttäjän tietokantaan.

        Args:
            user: Tallennettava käyttäjä-olio.

        Returns:
            Palauttaa tallennetun luodun käyttäjän.

        """
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (id, username, password, admin) VALUES (?, ?, ?, ?)",
                       (user.id, user.username, user.password, user.admin))

        user_id = cursor.lastrowid
        user.id = user_id

        self._connection.commit()

        return user

    def get_user_by_username_and_password(self, username, password):
        """
        Etsii ja palauttaa käyttäjän, käyttäjätunnuksen ja salasanan perusteella

        Args:
            username: Käyttäjän käyttäjätunnus.
            password: Käyttäjän salasana.

        Returns:
            Käyttäjäobjekti, jos käyttäjä löytyy, muuten ei mitään

        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                       (username, password))

        user_data = cursor.fetchone()

        if user_data:
            return (User(user_data["id"], user_data["username"],
                user_data["password"], user_data["admin"])
)
        return None

    def get_all_users(self):
        """
        Löytää ja palauttaa kaikki käyttäjät.

        Returns:
            Palauttaa listan käyttäjä olioita.

        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        return ([User(row["id"], row["username"], row["password"],
            row["admin"]) if row else None for row in users])

    def delete_all_users(self):
        """
        Poistaa kaikki käyttäjät.

        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")

        self._connection.commit()
