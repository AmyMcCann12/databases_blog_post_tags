from lib.post_repository import PostRepository
from lib.post import Post
from lib.comment import Comment
"""
When we call PostRepository#all
we get a list of the Post objects reflecting the seed data
"""

def test_get_all_records(db_connection):
    db_connection.seed('seeds/blog.sql')
    repository = PostRepository(db_connection)
    posts = repository.all()
    assert posts == [
        Post(1,'Title1', 'Contents1'),
        Post(2, 'Title2', 'Contents2'),
        Post(3, 'Title3', 'Contents3'),
        Post(4, 'Title4', 'Contents4'),
        Post(5, 'Title5', 'Contents5')
    ]

"""
When we call PostRepository#find
we get a single Post object reflecting the seed data
"""

def test_get_a_single_record(db_connection):
    db_connection.seed('seeds/blog.sql')
    repository = PostRepository(db_connection)
    post = repository.find(3)
    assert post == Post(3, 'Title3', 'Contents3')

"""
When we call PostRepository#create
we get a new record in the database
"""

def test_create_a_record(db_connection):
    db_connection.seed('seeds/blog.sql')
    repository = PostRepository(db_connection)
    repository.create(Post(6, "Title6", "Contents6"))
    result = repository.all()
    assert result == [
        Post(1,'Title1', 'Contents1'),
        Post(2, 'Title2', 'Contents2'),
        Post(3, 'Title3', 'Contents3'),
        Post(4, 'Title4', 'Contents4'),
        Post(5, 'Title5', 'Contents5'),
        Post(6, "Title6", "Contents6")
    ]

"""
When we call PostRepository#delete
we remove a record from the database
"""

def test_delete_record(db_connection):
    db_connection.seed('seeds/blog.sql')
    repository = PostRepository(db_connection)
    repository.delete(2)
    result = repository.all()
    assert result == [
        Post(1,'Title1', 'Contents1'),
        Post(3, 'Title3', 'Contents3'),
        Post(4, 'Title4', 'Contents4'),
        Post(5, 'Title5', 'Contents5')
    ]

"""
When I call #find_with_comments with a post id
Then I get the post with a list of comments, populated
"""

def test_find_with_comments(db_connection):
    db_connection.seed('seeds/blog.sql')
    repository = PostRepository(db_connection)
    result = repository.find_with_comments(3)
    assert result == Post(3, "Title3", 'Contents3', [
        Comment(4,'Comments content 4', 'Author4', 3),
        Comment(8,'Comments content 8', 'Author8', 3),
    ])