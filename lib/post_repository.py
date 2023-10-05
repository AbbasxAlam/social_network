from lib.post import *

class PostRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"], row["content"], row["views"], row["user_id"])
            posts.append(item)
        return posts

    # Find a single artist by their id
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from posts WHERE id = %s', [id])
        row = rows[0]
        return Post(row["id"], row["title"], row["content"], row["views"], row["user_id"])

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, post):
        self._connection.execute('INSERT INTO posts (title, content, views, user_id) VALUES (%s, %s, %s, %s)', [
                                 post.title, post.content, post.views, post.user_id])
        return None

    # Delete an artist by their id
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM posts WHERE id = %s', [id])
        return None