class Comment():
    def __init__(self, id, content, author_name, post_id):
        self.id = id
        self.content = content
        self.author = author_name
        self.post_id = post_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Comment ID: {self.id}, Content: {self.content}, Author: {self.author}, Post ID: {self.post_id}"