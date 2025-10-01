class Media:
    def play(self):
        pass

class Audio(Media):
    def play(self):
        print("Playing audio...")

class Video(Media):
    def play(self):
        print("Playing video...")

media_files = [Audio(), Video()]
for media in media_files:
    media.play()