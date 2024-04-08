from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS courses;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS exercises;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            admin BOOLEAN,
            username TEXT UNIQUE,
            password TEXT 
        );
    ''')

    cursor.execute('''
        CREATE TABLE  courses (
            id SERIAL PRIMARY KEY,
            userID INTEGER REFERENCES users ON DELETE CASCADE,
            title TEXT UNIQUE,
            credits INTEGER
        );
    ''')

    cursor.execute('''
        CREATE TABLE exercises (
            id SERIAL PRIMARY KEY,
            courseID INTEGER REFERENCES courses ON DELETE CASCADE,
            description TEXT,
            done BOOLEAN DEFAULT false
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()