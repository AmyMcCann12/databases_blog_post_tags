from lib.post import Post
from lib.comment import Comment

class PostRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows: 
            item = Post(row['id'], row['title'], row['content'])
            posts.append(item)
        return posts
    
    def find(self, post_id):
        rows = self.connection.execute('SELECT * FROM posts WHERE id = %s', [post_id])
        post = Post(rows[0]['id'], rows[0]['title'], rows[0]['content'])
        return post
    
    def find_with_comments(self, post_id):
        rows = self.connection.execute(
            """SELECT posts.id AS post_id, 
            posts.title, 
            posts.content AS post_content,
            comments.id AS comment_id,
            comments.content AS comment_content,
            comments.author,
            comments.post_id
            FROM posts 
            JOIN comments 
            ON posts.id = comments.post_id 
            WHERE posts.id = %s""", 
            [post_id]
        )
        comments = []
        for row in rows:
            comment = Comment(row['comment_id'], row['comment_content'], row['author'], row['post_id'])
            comments.append(comment)
        post = Post(rows[0]['post_id'], rows[0]['title'], rows[0]['post_content'], comments)
        return post

    def create(self, post):
        self.connection.execute(
            'INSERT INTO posts (title, content) VALUES (%s, %s)', [post.title, post.content]
        )
        return None
    
    def delete(self, post_id):
        self.connection.execute(
            'DELETE FROM posts WHERE id = %s', [post_id]
        )
        return None