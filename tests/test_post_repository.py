from lib.post_repository import *
from lib.post import *

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new ArtistRepository

    posts = repository.all() # Get all artists

    # Assert on the results
    assert posts == [
        Post(1, 'New job1','WOOO I have a new job1!', 0, 1),
        Post(2, 'New job2','WOOO I have a new job2!', 10, 2),
        Post(3, 'New job3','WOOO I have a new job3!', 20, 3),
        Post(4, 'New job4','WOOO I have a new job4!', 30, 4),
    ]


"""
When we call ArtistRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post = repository.find(3)
    assert post == Post(3, 'New job3','WOOO I have a new job3!', 20, 3)

"""
When we call ArtistRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    repository.create(Post(None, 'New job5','WOOO I have a new job5!', 40, 1))

    result = repository.all()
    assert result == [
        Post(1, 'New job1','WOOO I have a new job1!', 0, 1),
        Post(2, 'New job2','WOOO I have a new job2!', 10, 2),
        Post(3, 'New job3','WOOO I have a new job3!', 20, 3),
        Post(4, 'New job4','WOOO I have a new job4!', 30, 4),
        Post(5, 'New job5','WOOO I have a new job5!', 40, 1)
    ]

"""
When we call ArtistRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.delete(3) # Apologies to Taylor Swift fans

    result = repository.all()
    assert result == [
        Post(1, 'New job1','WOOO I have a new job1!', 0, 1),
        Post(2, 'New job2','WOOO I have a new job2!', 10, 2),
        Post(4, 'New job4','WOOO I have a new job4!', 30, 4),
    ]