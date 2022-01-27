from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter.font import Font
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x750+0+0")
        self.root.title("MyAttendence")

        #Background Image
        img=Image.open(r"C:\Users\sheto\Desktop\MyAttendence\images\bg4.jpg")
        img=img.resize((1366,750),Image.ANTIALIAS)
        self.bgimage=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.bgimage)
        f_lbl.place(x=0,y=0,width=1366,height=750)

        #Title Label
        title_lbl=Label(f_lbl,text="MY ATTENDENCE",font=("times new roman", 35, "bold"),bg="white",fg="black")
        title_lbl.place(x=440,y=80,width=500,height=60)


        #Student Details Button 1
        btnimg1=Image.open(r"C:\Users\sheto\Desktop\MyAttendence\images\StudentDetails.png")
        btnimg1=btnimg1.resize((150,100),Image.ANTIALIAS)
        self.button1=ImageTk.PhotoImage(btnimg1)

        b1=Button(f_lbl,image=self.button1,cursor="hand2")
        b1.place(x=233,y=200,width=150, height=150)
        b1_1=Button(f_lbl,text="Student Details",font=("times new roman", 12, "bold"),bg="darkblue",fg="white",cursor="hand2")
        b1_1.place(x=233,y=350,width=150, height=30)

        #Face Recognition Button 2
        btnimg2=Image.open(r"C:\Users\sheto\Desktop\MyAttendence\images\FaceRecog.png")
        btnimg2=btnimg2.resize((150,150),Image.ANTIALIAS)
        self.button2=ImageTk.PhotoImage(btnimg2)

        b2=Button(f_lbl,image=self.button2,cursor="hand2")
        b2.place(x=483,y=200,width=150, height=150)
        b2_1=Button(f_lbl,text="Face Recognition",font=("times new roman", 12, "bold"),bg="darkblue",fg="white",cursor="hand2")
        b2_1.place(x=483,y=350,width=150, height=30)


        #Attendence Button 3
        btnimg3=Image.open(r"C:\Users\sheto\Desktop\MyAttendence\images\Attendence.png")
        btnimg3=btnimg3.resize((100,100),Image.ANTIALIAS)
        self.button3=ImageTk.PhotoImage(btnimg3)

        b3=Button(f_lbl,image=self.button3,cursor="hand2")
        b3.place(x=733,y=200,width=150, height=150)
        b3_1=Button(f_lbl,text="Attendence",font=("times new roman", 12, "bold"),bg="darkblue",fg="white",cursor="hand2")
        b3_1.place(x=733,y=350,width=150, height=30)


        #ChatBot Button 4
        btnimg4=Image.open(r"C:\Users\sheto\Desktop\MyAttendence\images\ChatBot.png")
        btnimg4=btnimg4.resize((140,140),Image.ANTIALIAS)
        self.button4=ImageTk.PhotoImage(btnimg4)

        b4=Button(f_lbl,image=self.button4,cursor="hand2")
        b4.place(x=983,y=200,width=150, height=150)
        b4_1=Button(f_lbl,text="ChatBot",font=("times new roman", 12, "bold"),bg="darkblue",fg="white",cursor="hand2")
        b4_1.place(x=983,y=350,width=150, height=30)


        #Train Button 5
        btnimg5=Image.open(r"C:\Users\sheto\Desktop\MyAttendence\images\FaceTrain.png")
        btnimg5=btnimg5.resize((130,130),Image.ANTIALIAS)
        self.button5=ImageTk.PhotoImage(btnimg5)

        b5=Button(f_lbl,image=self.button5,cursor="hand2")
        b5.place(x=233,y=450,width=150, height=150)
        b5_1=Button(f_lbl,text="Train Face",font=("times new roman", 12, "bold"),bg="darkblue",fg="white",cursor="hand2")
        b5_1.place(x=233,y=600,width=150, height=30)


        #Gallery Button 6
        btnimg6=Image.open(r"C:\Users\sheto\Desktop\MyAttendence\images\Gallery.png")
        btnimg6=btnimg6.resize((140,140),Image.ANTIALIAS)
        self.button6=ImageTk.PhotoImage(btnimg6)

        b6=Button(f_lbl,image=self.button6,cursor="hand2")
        b6.place(x=483,y=450,width=150, height=150)
        b6_1=Button(f_lbl,text="Gallery",font=("times new roman", 12, "bold"),bg="darkblue",fg="white",cursor="hand2")
        b6_1.place(x=483,y=600,width=150, height=30)


        #Developer Button 7
        btnimg7=Image.open(r"C:\Users\sheto\Desktop\MyAttendence\images\Developer.png")
        btnimg7=btnimg7.resize((150,150),Image.ANTIALIAS)
        self.button7=ImageTk.PhotoImage(btnimg7)

        b7=Button(f_lbl,image=self.button7,cursor="hand2")
        b7.place(x=733,y=450,width=150, height=150)
        b7_1=Button(f_lbl,text="Developer",font=("times new roman", 12, "bold"),bg="darkblue",fg="white",cursor="hand2")
        b7_1.place(x=733,y=600,width=150, height=30)


        #Exit Button 8
        btnimg8=Image.open(r"C:\Users\sheto\Desktop\MyAttendence\images\Exit.png")
        btnimg8=btnimg8.resize((100,100),Image.ANTIALIAS)
        self.button8=ImageTk.PhotoImage(btnimg8)

        b8=Button(f_lbl,image=self.button8,cursor="hand2")
        b8.place(x=983,y=450,width=150, height=150)
        b8_1=Button(f_lbl,text="Exit",font=("times new roman", 12, "bold"),bg="darkblue",fg="white",cursor="hand2")
        b8_1.place(x=983,y=600,width=150, height=30)


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()