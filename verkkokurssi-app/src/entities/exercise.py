class Exercise:
    """Luokka, joka kuvaa tehtäviä.

        Attributes:
            ids: Numero, joka kuvaa tehtävän ID:tä
            description: Merkkijono, joka kuvaa tehtävän sisältöä/nimeä.
            done: Totuusarvo, joka kuvaa onko tehtävä tehty.
            course: Course-olio, joka kuvaa tehtävän linkitettyä kurssia.
    """
    def __init__(self, ids, description, done, course):
        """Luokan konstruktori, joka luo uuden tehtävän.

            Args:
                ids: Numero, joka kuvaa tehtävän ID:tä
                description: Merkkijono, joka kuvaa tehtävän sisältöä/nimeä.
                done: Totuusarvo, joka kuvaa onko tehtävä tehty.
                course: Course-olio, joka kuvaa tehtävän linkitettyä omistajaa.
        """
        self.id = ids
        self.description = description
        self.done = done
        self.course = course
