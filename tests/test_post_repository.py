from lib.post_repository import PostRepository
from lib.post import Post
from lib.tag import Tag

"""
When we call PostsRepository#all
We get a list of Post objects reflecting the seed data.
"""

def test_get_all_records(db_connection):
    db_connection.seed('seeds/blog_posts_tags.sql')
    repository = PostRepository(db_connection)
    posts = repository.all()

    assert posts == [
        Post(1,'How to use Git'),
        Post(2,'Fun classes'),
        Post(3,'Using a REPL'),
        Post(4,'My weekend in Edinburgh'),
        Post(5,'The best chocolate cake EVER'),
        Post(6,'A foodie week in Spain'),
        Post(7,'SQL basics')
    ]

"""
When we call PostRepository#find
We get a single Post object reflecting the seed data.
"""

def test_find_a_record(db_connection):
    db_connection.seed('seeds/blog_posts_tags.sql')
    repository = PostRepository(db_connection)

    result = repository.find(3)
    assert result == Post(3,'Using a REPL')

"""
When I call #find_by_tags with a tag name
Then I get the posts which are linked to that tag
"""

def test_find_by_tag(db_connection):
    db_connection.seed('seeds/blog_posts_tags.sql')
    repository = PostRepository(db_connection)
    result = repository.find_by_tag('coding')
    assert result == [
        Post(1,'How to use Git'),
        Post(2,'Fun classes'),
        Post(3,'Using a REPL'),
        Post(7,'SQL basics')
    ]

"""
When we call PostRepository#create
We get a new record in the database.
"""

def test_create_a_post(db_connection):
    db_connection.seed('seeds/blog_posts_tags.sql')
    repository = PostRepository(db_connection)

    repository.create(Post(8, "Making a Cake"))
    result = repository.all()
    assert result == [
        Post(1,'How to use Git'),
        Post(2,'Fun classes'),
        Post(3,'Using a REPL'),
        Post(4,'My weekend in Edinburgh'),
        Post(5,'The best chocolate cake EVER'),
        Post(6,'A foodie week in Spain'),
        Post(7,'SQL basics'),
        Post(8, "Making a Cake")
    ]


"""
When we call PostRepository#delete
We remove a record from the database.
"""

def test_delete_a_post(db_connection):
    db_connection.seed('seeds/blog_posts_tags.sql')
    repository = PostRepository(db_connection)
    repository.delete(4)
    result = repository.all()
    assert result == [
        Post(1,'How to use Git'),
        Post(2,'Fun classes'),
        Post(3,'Using a REPL'),
        Post(5,'The best chocolate cake EVER'),
        Post(6,'A foodie week in Spain'),
        Post(7,'SQL basics'),
    ]
