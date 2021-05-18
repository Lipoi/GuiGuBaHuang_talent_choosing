import win32api
import win32con
import random
import time
from PIL import Image
from PIL import ImageGrab
pos1 = (116, 35)
pos2 = (305, 35)
pos3 = (495, 35)

pos4 = (116, 102)
pos5 = (305, 102)
pos6 = (495, 102)

need_num_red = 1  #需要一个红色天赋

def move_click(x, y, t=0):  # 移动鼠标并点击左键
    win32api.SetCursorPos((x, y))  # 设置鼠标位置(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                         win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键
    if t == 0:
        time.sleep(random.random()*2+1)  # sleep一下
    else:
        time.sleep(t)
    return 0

def crop_screenshot(img_file, pos_x, pos_y, width, height, out_file):
    img = Image.open(img_file)
    region = (pos_x, pos_y, pos_x + width, pos_y + height)
    cropImg = img.crop(region)
    cropImg.save(out_file)
    print("exported:", out_file)

def isred(pos):
    rgb = pix[pos]
    return (152<=rgb[0]<=154 and 48<=rgb[1]<=50 and 48<=rgb[2]<=50)

if __name__ == "__main__":
    time.sleep(5)

    while(True):
        move_click(800, 225)
        time.sleep(2.5)
        img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
        img.save('tmp.png')
        crop_screenshot("tmp.png", 1100, 400, 550, 125, "test_id.png")
        image = Image.open('test_id.png')
        pix = image.load()
        num_red = isred(pos1) + isred(pos2) + isred(pos3) + isred(pos4) + isred(pos5) + isred(pos6)
        print(num_red)
        if(num_red >= need_num_red): break


