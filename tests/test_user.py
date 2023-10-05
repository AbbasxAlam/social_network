from lib.user import *

"""
Artist constructs with an id, name and genre
"""
def test_user_initialised():
    user = User(1, "Test username", "Test email")
    assert user.id == 1
    assert user.username == "Test username"
    assert user.email == "Test email"

"""
We can format artists to strings nicely
"""
def test_user_format_nicely():
    user = User(1, "Test username", "Test email")
    assert str(user) == "User(1, Test username, Test email)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_user_are_equal():
    user1 = User(1, "Test username", "Test email")
    user2 = User(1, "Test username", "Test email")
    assert user1 == user2 
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.