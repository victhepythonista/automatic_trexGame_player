import pyautogui,time, numpy,os
from PIL import ImageGrab
from PIL import ImageOps,Image


# bot to play that t-rex game when
# you dont have internet


# the basic logic of thus bot is to capture an image
# of  specified area infront of the t-rex when the screen is white
#, grayscale the image and using numpy convert the colors of the pixels 
# into an array then get the sum
# the sum obtained will be the constant you will bw using
# to identify when a cactus enters the region infront if th t-rex

# due to different factors ... this code will not run on your computer as 
# expected..take 5min to locate the retry button , then also tweek your 'box'..
#and it should work properly

x =  700
y = 181
restart = x,y
dino_pos = 472,178
 
box = (511,199,511+100,199+27)

def load_retry_button():
        # load the retry button image we will try to detect
        # Ive pre loaded it
        im = Image.open("retry_button_org.jpg")
        im_gray = ImageOps.grayscale(im)
        im_colors = numpy.array(im_gray.getcolors()).sum()

        return   im_colors

class DinoRun:

    def __init__(self ):
        
        self.dino_pos = dino_pos
        self.box_w= 90
        self.box_h = 25                             
        self.box = (500,229,self.box_w, self.box_h)
        self.retry_id = load_retry_button()
        
    def check_for_retry(self):
        # check if the retry button appears      
                # current image
        retry_box =   700,181 , 700+27,181 +27   
        image = ImageGrab.grab(retry_box)
        image.save('retry2.jpg')
        gray_image = ImageOps.grayscale(Image.open('retry2.jpg'))
        colors = numpy.array(gray_image.getcolors()).sum()
        
        if colors == self.retry_id:
            pyautogui.click(719,194)

   

    def image_grab(self):
        x = 483
        y = 200
         
        image = ImageGrab.grab(box)
        gray_image = ImageOps.grayscale(image)
        colors = numpy.array(gray_image.getcolors())
        return colors.sum()
    def play(self):
        time.sleep(4)
        while True:
            self.check_for_retry()
            imagegrab = self.image_grab()
             
             
            if imagegrab != 2955:
                pyautogui.keyDown("space")
            
        
DinoRun().play()







