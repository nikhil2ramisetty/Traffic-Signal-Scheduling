from tkinter import *
from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import random
import numpy as np
import time
from cvlib.object_detection import draw_bbox
def count(im):
    lo = cv2.imread(im)
    bbox, label, conf = cv.detect_common_objects(lo)
    output_image = draw_bbox(lo, bbox, label, conf)
    num = str(label.count('car')+label.count('person')+label.count('truck')+label.count('motorcycle'))
    return num
class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        no = 250
        width, height = root.winfo_screenwidth(), root.winfo_screenheight()
        pos =  [[no+30,(height//2)-no/2+ 100],[(width//2)-no/2+ 125,no+30],[width-no-100,(height//2)-no/2+ 100],[(width//2)-no/2+ 125, height-no-80]]
        index = res_list.index(max(res_list))
        self.master.title("Absolute Positioning")
        self.pack(fill=BOTH, expand=1)
        Style().configure("TFrame", background="#333")

        bard = Image.open(image_path+"Lights\\red.jpg")
        no = 250
        bard = bard.resize((50,50))
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x = pos[0][0],y = pos[0][1])

        bard = Image.open(image_path+"Lights\\red.jpg")
        no = 250
        bard = bard.resize((50,50))
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x = pos[1][0],y = pos[1][1])

        bard = Image.open(image_path+"Lights\\red.jpg")
        no = 250
        bard = bard.resize((50,50))
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x = pos[2][0],y = pos[2][1])

        bard = Image.open(image_path+"Lights\\red.jpg")
        no = 250
        bard = bard.resize((50,50))
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x = pos[3][0],y = pos[3][1])

        bard = Image.open(image_path+"Lights\\Green.jpg")
        no = 250
        bard = bard.resize((50,50))
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x = pos[index][0],y = pos[index][1])

        bard = Image.open(images[0])
        no = 250
        bard = bard.resize((no,no))
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=0, y=(height//2)-no/2)

        bard = Image.open(images[1])
        bard = bard.resize((no,no))
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=(width//2)-no/2, y=0)

        bard = Image.open(images[2])
        bard = bard.resize((no,no))
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=width-no, y=(height//2)-no/2)

        bard = Image.open(images[3])
        bard = bard.resize((no,no))
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=(width//2)-no/2, y=height-no)

        text = Label(self, text="West: \nVehicle Count: {} \nWaiting Time: {} \nProduct: {}".format(vehicle_count[0],starvation[0],res_list[0]),font=("Arial", 25))
        text.place(x=0,y=130)

        text = Label(self, text="North: \nVehicle Count: {} \nWaiting Time: {} \nProduct: {}".format(vehicle_count[1],starvation[1],res_list[1]),font=("Arial", 25))
        text.place(x=880,y=0)

        text = Label(self, text="East: \nVehicle Count: {} \nWaiting Time: {} \nProduct: {}".format(vehicle_count[2],starvation[2],res_list[2]),font=("Arial", 25))
        text.place(x=width-no-20,y=560)

        text = Label(self, text="South: \nVehicle Count: {} \nWaiting Time: {} \nProduct: {}".format(vehicle_count[3],starvation[3],res_list[3]),font=("Arial", 25))
        text.place(x=width//2 - no/2 - 270,y=height-no)

image_path = "C:\\Users\\Nikhil\\Desktop\\Trial1\\"
starvation = [0,10,20,30]
vehicle_count = [0,0,0,0]
images = [image_path,image_path,image_path,image_path]
"""root = Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
app = Example()
root.mainloop()"""
while(True):
    randnums= np.random.randint(1,20,4)
    images[0] = image_path+"{}".format(randnums[0])+".jpg"
    images[1] = image_path+"{}".format(randnums[1])+".jpg"
    images[2] = image_path+"{}".format(randnums[2])+".jpg"
    images[3] = image_path+"{}".format(randnums[3])+".jpg"
    vehicle_count[0] = count(images[0])
    vehicle_count[1] = count(images[1])
    vehicle_count[2] = count(images[2])
    vehicle_count[3] = count(images[3])
    res_list = []
    for i in range(0, len(vehicle_count)):
        res_list.append((int(vehicle_count[i])) * (starvation[i]))
    maxi = res_list.index(max(res_list))
    root = Tk()
    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry('%dx%d+0+0' % (width,height))
    app = Example()
    root.after(16000, root.destroy)
    root.mainloop()
    starvation = np.array(starvation)+10
    starvation[maxi] = 0