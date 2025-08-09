class Status:
    def uploadImage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is uploaded to ypur status")
class StatusV1(Status):
    def addCaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}"is added to your status')
class StatusV2(Status):
    def like(self):
        print(f'You can like status')
class StatusV3(StatusV1,StatusV2):
    def addMusic(self,music):
        self.music=music
        print(f'{self.music}')
class StatusV4(StatusV3):
    def VedioLength(self,vedio):
        self.vedio=vedio
        print(f'{self.vedio} is uploaded to your status')


sravani=Status()
sravani.uploadImage('selfie.png')
hema = StatusV1()
hema.uploadImage('GoodMrng.png')
hema.addCaption("Morning Friends!!!")

vaishnavi = StatusV2()
vaishnavi.uploadImage("coffee.png")
vaishnavi.like()

deepika = StatusV3()
deepika.uploadImage("Mountains_and_Trees.png")
deepika.addCaption("no wifi")
deepika.like()
deepika.addMusic("Nature.mp3")

nikitha=StatusV4()
nikitha.uploadImage("Mountains_and_Trees.png")
nikitha.addCaption("no wifi")
nikitha.like()
nikitha.addMusic("Nature.mp3")
nikitha.VedioLength("Somevedio.mp4")