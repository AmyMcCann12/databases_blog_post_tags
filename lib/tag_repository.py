from lib.tag import Tag

class TagRepository():
    def __init__(self,connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM tags')
        tags = []
        for row in rows:
            tag = Tag(row['id'], row['name'])
            tags.append(tag)
        return tags
    
    def find(self, tag_id):
        rows = self.connection.execute('SELECT * FROM tags WHERE id = %s', [tag_id])
        return Tag(rows[0]['id'], rows[0]['name'])
    
    def find_by_post(self,post_id):
        rows = self.connection.execute(
            """ SELECT tags.id, tags.name 
            FROM tags
            JOIN posts_tags ON posts_tags.tag_id = tags.id
            JOIN posts ON posts_tags.post_id = posts.id
            WHERE posts.id = %s
            """, [post_id])
        tags = []
        for row in rows:
            tag = Tag(row['id'], row['name'])
            tags.append(tag)
        return tags
    
    def create(self, tag):
        self.connection.execute('INSERT INTO tags (name) VALUES (%s)', [tag.name])
        return None
    
    def delete(self, tag_id):
        self.connection.execute('DELETE FROM tags WHERE id = %s', [tag_id])
        return None