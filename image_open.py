import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
from time import sleep
import os
import speech_recognition as sr
import pyttsx3 as pt

Img_1 =r"C:\Users\NAZBEEN_MULTIMEDIA\Pictures\future_wife\love (1).png"
Img_2 =r"C:\Users\NAZBEEN_MULTIMEDIA\Pictures\future_wife\love (2).png"
Img_3 =r"C:\Users\NAZBEEN_MULTIMEDIA\Pictures\future_wife\love (3).png"
Img_4 =r"C:\Users\NAZBEEN_MULTIMEDIA\Pictures\future_wife\love (4).png"
Img_5 =r"C:\Users\NAZBEEN_MULTIMEDIA\Pictures\future_wife\love (5).png"
Img_6 =r"C:\Users\NAZBEEN_MULTIMEDIA\Pictures\future_wife\love (6).png"
Img_7 =r"C:\Users\NAZBEEN_MULTIMEDIA\Pictures\future_wife\love (7).png"
Img_8 =r"C:\Users\NAZBEEN_MULTIMEDIA\Pictures\future_wife\love (8).png"
Img_9 =r"C:\Users\NAZBEEN_MULTIMEDIA\Pictures\future_wife\love (9).png"
Img_10 =r"C:\Users\NAZBEEN_MULTIMEDIA\Pictures\future_wife\love (10).png"
Img_11 =r"C:\Users\NAZBEEN_MULTIMEDIA\Pictures\future_wife\love (11).png"
Img_12=r"C:\Users\NAZBEEN_MULTIMEDIA\Pictures\future_wife\love (12).png"


pdf_1 = r"G:\videos\pdf\LearnJava.pdf"
pdf_2 = r"G:\videos\pdf\python CookBook.pdf"
pdf_3 = r"G:\videos\pdf\PythonDataVisualizationCookBook.pdf"
pdf_4 = r"G:\videos\pdf\LearnJava.pdf"
pdf_5 = r"G:\videos\pdf\LearnJava.pdf"
pdf_6 = r"G:\videos\pdf\LearnJava.pdf"
pdf_7 = r"G:\videos\pdf\LearnJava.pdf"
pdf_8 = r"G:\videos\pdf\LearnJava.pdf"
pdf_9 = r"G:\videos\pdf\LearnJava.pdf"
pdf_10 = r"G:\videos\pdf\LearnJava.pdf"
pdf_11 = r"G:\videos\pdf\LearnJava.pdf"
pdf_12 = r"G:\videos\pdf\LearnJava.pdf"


def pdf_read():
    return [pdf_1, pdf_2, pdf_3, pdf_4, pdf_5, pdf_6,pdf_7,pdf_8, pdf_9,pdf_10,pdf_11,pdf_12]



def close_pictures():
    browserExe = "Microsoft.Photos.exe" 
    return  os.system("taskkill /f /im "+browserExe) 

def my_pics_list_():
     return [Img_1, Img_2, Img_3, Img_4, Img_5, Img_6,Img_7, Img_8, Img_9, Img_10, Img_11, Img_12]
  





# def open_location():
#         path =r'C:\Users\NAZBEEN_MULTIMEDIA\Pictures\future_wife'
#         webbrowser.open(pdf_1)     
     
# open_location()



