from entities.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (username, password, admin) VALUES (?, ?, ?)", (user.username, user.password, user.admin))

        user_id = cursor.lastrowid
        user.id = user_id

        self._connection.commit()

        return user

    def get_user_by_username_and_password(self, username, password):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user_data = cursor.fetchone()

        if user_data:
            return User(user_data["username"], user_data["password"], user_data["admin"])
        else:
            return None

    def get_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        return [User(row["username"], row["password"]) if row else None for row in users]

    def delete_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")

        self._connection.commit()
