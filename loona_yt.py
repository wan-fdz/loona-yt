"""
    program to manually stream and take screenshots as streaming proofs
    made by wan
"""

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from datetime import datetime, timezone
import numpy as np
import webbrowser
import pyautogui
import platform
import random
import pytz
import time
import cv2

from bs4 import BeautifulSoup
import requests

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_change(entry_1, entry_2, entry_3, entry_4):
    user_id, youtube_url, video_duration, videos_inbetween = retrieve_user_data(entry_1, entry_2, entry_3, entry_4)
    main(user_id, youtube_url, video_duration, videos_inbetween)

def retrieve_user_data(entry_1, entry_2, entry_3, entry_4):
    user_id = entry_1.get()
    youtube_url = entry_2.get()
    video_duration = entry_3.get()
    videos_inbetween = entry_4.get()
    return user_id, youtube_url, video_duration, videos_inbetween

def create_gui():
    window = Tk()
    window.title('jinsoulbby')

    window.geometry("862x520")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 520,
        width = 862,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        432.0,
        519.0,
        fill="#5D5FEF",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        649.5,
        121.49999999999989,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#F0EFEF",
        highlightthickness=0
    )
    entry_1.place(
        x=471.0,
        y=95.99999999999989 + 27,
        width=357.0,
        height=20.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        649.5,
        186.4999999999999,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#F0EFEF",
        highlightthickness=0
    )
    entry_2.place(
        x=471.0,
        y=160.9999999999999 + 27,
        width=357.0,
        height=20.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        649.5,
        251.4999999999999,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#F0EFEF",
        highlightthickness=0
    )
    entry_3.place(
        x=471.0,
        y=225.9999999999999 + 27,
        width=357.0,
        height=20.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        649.5,
        316.4999999999999,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#F0EFEF",
        highlightthickness=0
    )
    entry_4.place(
        x=471.0,
        y=290.9999999999999 + 27,
        width=357.0,
        height=20.0
    )

    canvas.create_text(
        458.0,
        45.999999999999886,
        anchor="nw",
        text="Enter the details.",
        fill="#000000",
        font=("Inter SemiBold", 25 * -1)
    )

    canvas.create_text(
        469.0,
        166.9999999999999,
        anchor="nw",
        text="YouTube URL",
        fill="#000000",
        font=("Inter", 10 * -1)
    )

    canvas.create_text(
        469.0,
        231.9999999999999,
        anchor="nw",
        text="Video Duration",
        fill="#000000",
        font=("Inter", 10 * -1)
    )

    canvas.create_text(
        469.0,
        296.9999999999999,
        anchor="nw",
        text="Number of videos in between",
        fill="#000000",
        font=("Inter", 10 * -1)
    )

    canvas.create_text(
        469.0,
        101.99999999999989,
        anchor="nw",
        text="ID (Twitter handle)",
        fill="#000000",
        font=("Inter", 10 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_change(entry_1, entry_2, entry_3, entry_4),
        relief="flat"
    )
    button_1.place(
        x=547.0,
        y=420.9999999999999,
        width=188.0,
        height=56.0
    )

    canvas.create_text(
        37.0,
        100.99999999999989,
        anchor="nw",
        text="LOONA TAKE THE CROWN",
        fill="#FFFFFF",
        font=("Inter", 25 * -1)
    )

    canvas.create_rectangle(
        38.0,
        141.9999999999999,
        251.0,
        144.9999999999999,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        32.0,
        177.9999999999999,
        anchor="nw",
        text="Fill up the details and save time\ntaking the streaming proofs.",
        fill="#FFFFFF",
        font=("Inter", 16 * -1)
    )

    canvas.create_text(
        32.0,
        226.9999999999999,
        anchor="nw",
        text="It also helps to make manually streaming easier!!",
        fill="#FFFFFF",
        font=("Inter", 16 * -1)
    )

    canvas.create_text(
        32.0,
        297.9999999999999,
        anchor="nw",
        text="Important:",
        fill="#FFFFFF",
        font=("Inter", 16 * -1)
    )

    canvas.create_text(
        32.0,
        331.9999999999999,
        anchor="nw",
        text="Autoplay must be enabled on YouTube.",
        fill="#FFFFFF",
        font=("Inter", 16 * -1)
    )

    canvas.create_text(
        32.0,
        365.9999999999999,
        anchor="nw",
        text="Single display computer only.",
        fill="#FFFFFF",
        font=("Inter", 16 * -1)
    )

    canvas.create_text(
        138.0,
        427.9999999999999,
        anchor="nw",
        text="STAN LOONA",
        fill="#FFFFFF",
        font=("Inter", 16 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def play_video(url):
    client = webbrowser.get("firefox")
    client.open(url)

def text_on_image(user_id, filename):
    img = Image.open(filename)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 80)

    dt_utc = datetime.now(timezone.utc)
    dt_korea = dt_utc.astimezone(tz=pytz.timezone("Asia/Seoul"))
    text = user_id + "\n" + str(dt_korea) + " KST"

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

def get_meta(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="html.parser")

    meta = soup.find_all('meta')

    keep_going = False

    for tag in meta:
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['keywords']:
            #print ('CONTENT :',tag.attrs['content'])
            if "LOONA" in tag.attrs['content'] or "이달의소녀" in tag.attrs['content']:
                    keep_going = True
                    break

    return keep_going

    
def main(user_id, youtube_url, video_duration, videos_inbetween):

    while True:
        try:
            if youtube_url == "":
                youtube_url = "https://www.youtube.com/watch?v=ytuMObZlqOE" # default url

            if videos_inbetween == "":
                videos_inbetween = 3 # default number of videos inbetween

            if video_duration == "":
                video_duration = "00:05:12"

            if user_id == "":
                user_id = "loonatheworld"

            keep_going = get_meta(youtube_url) # check if its a loona video

            if keep_going == False:
                exit()

            if platform.system() == "Windows":
                webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))

            play_video(youtube_url)
            time.sleep(10) # give it a couple seconds to load

            if platform.system() == "Windows":
                pyautogui.click()
                time.sleep(3)
            pyautogui.press('space')

            time_to_sleep = random.randrange(10, 30)
            time.sleep(time_to_sleep)
            image = pyautogui.screenshot() # take first screenshot

            image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)

            # writing it to the disk using opencv
            filename = 'loonastream1.png'
            cv2.imwrite(filename, image)
            text_on_image(user_id, filename)

            total_duration = get_sec(video_duration)
            total_duration = total_duration - 40 # substract time taken to take first screenshot
            time.sleep(total_duration)  # sleep throughout video
            image = pyautogui.screenshot() # take screenshot at the end of it

            image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)

            # writing it to the disk using opencv
            filename = 'loonastream2.png'
            cv2.imwrite(filename, image)
            text_on_image(user_id, filename)


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

            waiting_time = int(videos_inbetween) * 200

            time.sleep(waiting_time)
            pyautogui.hotkey('ctrl', 'w') #close window
            time.sleep(10)

        except webbrowser.Error as e:
            print(e)
            break


if __name__ == "__main__":
    create_gui()