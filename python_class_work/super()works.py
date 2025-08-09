class Instagram:
    def __init__(self,username):
        self.username=username
        self.post=[]
        print(f"{self.username.center(40,'-')}")
    def uploadPost(self,image):
        self.post.append(image)
        print(f"{image} is posted")

class InstagramV1(Instagram):
    def __init__(self,username,bio):
        super().__init__(username)
        self.bio=bio
        print(f'{self.bio}')
    def uploadpost(self,post,music):
        super().uploadPost(post)
        self.music=music
        print(f"{self.music} is added")

dinesh=Instagram('dinesh123')
dinesh.uploadPost("GoodMorning.png")
sanjay=InstagramV1("sanjay","Coder")
sanjay.uploadPost("GoodEvening.png,someMusic.mp3")

