from lib.post import *

"""
Artist constructs with an id, name and genre
"""
def test_post_initialised():
    post = Post(1, "Test title", "Test content", "Test views", "Test user_id")
    assert post.id == 1
    assert post.title== "Test title"
    assert post.content == "Test content"
    assert post.views == "Test views"
    assert post.user_id == "Test user_id"

"""
We can format artists to strings nicely
"""
def test_post_format_nicely():
    post = Post(1, "Test title", "Test content", "Test views", "Test user_id")
    assert str(post) == "Post(1, Test title, Test content, Test views, Test user_id)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_post_are_equal():
    post1 = Post(1, "Test title", "Test content", "Test views", "Test user_id")
    post2 = Post(1, "Test title", "Test content", "Test views", "Test user_id")
    assert post1 == post2 
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.