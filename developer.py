from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #TITLE
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"D:\project\Images\dev.jpg")
        img_top=img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_dvlpr=Image.open(r"D:\project\Images\1568579834677.jpg")
        img_dvlpr=img_dvlpr.resize((200,200),Image.LANCZOS)
        self.photoimg_dvlpr=ImageTk.PhotoImage(img_dvlpr)

        f_lbl=Label(main_frame,image=self.photoimg_dvlpr)
        f_lbl.place(x=300,y=0,width=200,height=200)
        
        #developer info
        dlpr_label=Label(main_frame,text="SHUBHAM PANDEY",font=("times new roman",20,"bold"),bg="white")
        dlpr_label.place(x=0,y=5)

        dlpr_label=Label(main_frame,text="17BTCSE027",font=("times new roman",20,"bold"),bg="white")
        dlpr_label.place(x=0,y=40)

        img2=Image.open(r"D:\project\Images\developer.jfif")
        img2=img2.resize((500,390),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=390)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()