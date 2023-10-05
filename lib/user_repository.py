from lib.user import *

class UserRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["email"])
            users.append(item)
        return users

    # Find a single artist by their id
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [id])
        row = rows[0]
        return User(row["id"], row["username"], row["email"])

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, user):
        self._connection.execute('INSERT INTO users (username, email) VALUES (%s, %s)', [
                                 user.username, user.email])
        return None

    # Delete an artist by their id
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM users WHERE id = %s', [id])
        return None