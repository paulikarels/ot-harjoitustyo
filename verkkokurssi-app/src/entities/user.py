class User:
    """Luokka, joka kuvaa käyttäjiä.

    Attributes:
        ids: Numero, joka kuvaa käyttäjän ID:tä
        username: Merkkijono, joka kuvaa käyttäjän käyttäjätunnusta.
        password: Merkkijono, joka kuvaa käyttäjän salasanaa.
        admin: Totuusarvo, joka kuvaa käyttäjän käyttäjä oikeutta.
    """
    def __init__(self, ids, username, password, admin=False):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            ids: Numero, joka kuvaa käyttäjän ID:tä
            username: Merkkijono, joka kuvaa käyttäjän käyttäjätunnusta.
            password: Merkkijono, joka kuvaa käyttäjän salasanaa.
            admin: Totuusarvo, joka kuvaa käyttäjän käyttäjä oikeutta.
        """
        self.id = ids
        self.username = username
        self.password = password
        self.admin    = admin
