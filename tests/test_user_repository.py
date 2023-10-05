from lib.user_repository import *
from lib.user import *

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new ArtistRepository

    users = repository.all() # Get all artists

    # Assert on the results
    assert users == [
        User(1, "kezzy1", "k1@email.com"),
        User(2, "kezzy2", "k2@email.com"),
        User(3, "kezzy3", "k3@email.com"),
        User(4, "kezzy4", "k4@email.com"),
    ]


"""
When we call ArtistRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    user = repository.find(3)
    assert user == User(3, 'kezzy3', 'k3@email.com')

"""
When we call ArtistRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, "kezzy5", "k5@email.com"))

    result = repository.all()
    assert result == [
        User(1, 'kezzy1', 'k1@email.com'),
        User(2, 'kezzy2', 'k2@email.com'),
        User(3, 'kezzy3', 'k3@email.com'),
        User(4, 'kezzy4', 'k4@email.com'),
        User(5, 'kezzy5', 'k5@email.com'),
    ]

"""
When we call ArtistRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.delete(3) # Apologies to Taylor Swift fans

    result = repository.all()
    assert result == [
        User(1, 'kezzy1', 'k1@email.com'),
        User(2, 'kezzy2', 'k2@email.com'),
        User(4, 'kezzy4', 'k4@email.com'),
    ]