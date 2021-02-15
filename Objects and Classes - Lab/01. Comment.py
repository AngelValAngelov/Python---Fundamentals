class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes
        print(username)
        print(content)
        print(likes)


p = Comment("user1", "I like this book")
