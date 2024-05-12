class Course:
    """Luokka, joka kuvaa kursseja.

        Attributes:
            ids: Numero, joka kuvaa kurssin ID:tä
            title: Merkkijono, joka kuvaa kurssin nimeä.
            credits: Numero, joka kuvaa kurssin piste arvoa.
            user: User-olio, joka kuvaa kurssin linkitettyä omistajaa.
    """
    def __init__(self, ids, title , creditss, user=None):
        """Luokan konstruktori, joka luo uuden kurssin.

        Attributes:
            ids: Numero, joka kuvaa kurssin ID:tä
            title: Merkkijono, joka kuvaa kurssin nimeä.
            credits: Numero, joka kuvaa kurssin piste arvoa.
            user: User-olio, joka kuvaa kurssin linkitettyä omistajaa.
        """
        self.id = ids
        self.title = title
        self.credits = creditss
        self.user = user
