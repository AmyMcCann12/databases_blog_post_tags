from lib.post import Post

class PostRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Post(row['id'], row['title'])
            posts.append(item)
        return posts
    
    def find(self, post_id):
        rows = self.connection.execute('SELECT * FROM posts where id = %s', [post_id])
        return Post(rows[0]['id'], rows[0]['title'])
    
    def find_by_tag(self,tag):
        rows = self.connection.execute(
            """SELECT posts.id, posts.title 
            FROM posts
            JOIN posts_tags ON posts_tags.post_id = posts.id
            JOIN tags ON posts_tags.tag_id = tags.id
            WHERE tags.name = %s """, [tag]
        )
        posts_by_tag = []
        for row in rows:
            post = Post(row['id'], row['title'])
            posts_by_tag.append(post)
        return posts_by_tag
    
    def create(self, post):
        self.connection.execute('INSERT INTO posts (title) VALUES (%s)', [post.title])
        return None
    
    def delete(self, post_id):
        self.connection.execute('DELETE FROM posts WHERE id = %s', [post_id])
        return None