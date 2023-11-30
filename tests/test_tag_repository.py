from lib.tag import Tag
from lib.tag_repository import TagRepository

"""
When we call TagRepository#all
We get a list of Post objects reflecting the seed data.
"""

def test_get_all_records(db_connection):
    db_connection.seed('seeds/blog_posts_tags.sql')
    repository = TagRepository(db_connection)
    result = repository.all()
    assert result == [
        Tag(1,'coding'),
        Tag(2,'travel'),
        Tag(3,'cooking'),
        Tag(4,'education')
    ]

"""
When we call TagRepository#find
We get a single Post object reflecting the seed data.
"""
def test_find_a_record(db_connection):
    db_connection.seed('seeds/blog_posts_tags.sql')
    repository = TagRepository(db_connection)
    result = repository.find(3) 
    assert result == Tag(3,'cooking')

"""
When I call #find_by_posts with a post id
Then I get the tags which are linked to that post
"""

def test_find_by_post(db_connection):
    db_connection.seed('seeds/blog_posts_tags.sql')
    repository = TagRepository(db_connection)
    result = repository.find_by_post(2)
    assert result == [
        Tag(1, 'coding'),
        Tag(4, 'education')
    ]

"""
When we call PostRepository#create
We get a new record in the database.
"""

def test_create_a_record(db_connection):
    db_connection.seed('seeds/blog_posts_tags.sql')
    repository = TagRepository(db_connection)
    repository.create(Tag(5, 'home'))
    assert repository.all() == [
        Tag(1,'coding'),
        Tag(2,'travel'),
        Tag(3,'cooking'),
        Tag(4,'education'),
        Tag(5, 'home')
    ]

"""
When we call PostRepository#delete
We remove a record from the database.
"""

def test_delete_a_record(db_connection):
    db_connection.seed('seeds/blog_posts_tags.sql')
    repository = TagRepository(db_connection)
    repository.delete(2)
    assert repository.all() == [
        Tag(1,'coding'),
        Tag(3,'cooking'),
        Tag(4,'education')
    ]