
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from datetime import datetime, timezone
import pytz
import numpy as np
import webbrowser
import pyautogui
import random
import time
import cv2

def play_video(url):
    client = webbrowser.get("firefox")
    client.open(url)

def text_on_image(filename):
    img = Image.open(filename)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 80)

    dt_utc = datetime.now(timezone.utc)
    dt_korea = dt_utc.astimezone(tz=pytz.timezone("Asia/Seoul"))
    text = "@so_wane \n" + str(dt_korea) + " KST"

    x, y = 150, 500
    fillcolor = "white"
    shadowcolor = "black"
    
    # thin border
    draw.text((x-1, y), text, font=font, align="center", fill=shadowcolor)
    draw.text((x+1, y), text, font=font, align="center", fill=shadowcolor)
    draw.text((x, y-1), text, font=font, align="center", fill=shadowcolor)
    draw.text((x, y+1), text, font=font, align="center", fill=shadowcolor)

    # now draw the text over it
    draw.text((x, y), text, font=font, align="center", fill=fillcolor)
    img.save(filename)

def main():

    while True:
        try:
            url = "https://www.youtube.com/watch?v=87fKv045u5U"

            play_video(url) #294 secs
            time.sleep(10) #give it a couple seconds to load
            pyautogui.press('space')

            time_to_sleep = random.randrange(10, 30)
            time.sleep(time_to_sleep)
            image = pyautogui.screenshot()

            image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)

            # writing it to the disk using opencv
            filename = 'loonastream1.png'
            cv2.imwrite(filename, image)
            text_on_image(filename)

            time.sleep(240)
            image = pyautogui.screenshot()

            image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)

            # writing it to the disk using opencv
            filename = 'loonastream2.png'
            cv2.imwrite(filename, image)
            text_on_image(filename)


            images = [Image.open(x) for x in ['loonastream1.png', 'loonastream2.png']]
            widths, heights = zip(*(i.size for i in images))

            total_width = sum(widths)
            max_height = max(heights)

            new_im = Image.new('RGB', (total_width, max_height))

            x_offset = 0
            for im in images:
                new_im.paste(im, (x_offset,0))
                x_offset += im.size[0]

            filename = "loonastream" + time.strftime('%Y%m%d-%H%M%S') + ".png"
            new_im.save(filename)

            time.sleep(720)

        except webbrowser.Error as e:
            print(e)
            break


if __name__ == "__main__":
    main()