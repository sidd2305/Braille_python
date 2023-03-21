from tkinter import *
from tkinter import ttk
import cv2
import pyttsx3
import PyPDF2 as Py
import pytesseract
import speech_recognition as sr
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe" 

def openWindow1():
    expression = ""
    f1=open("file.txt","w")
    equation=StringVar()
    
    def clear():
        nonlocal expression
        expression = ""
        equation.set("")

    def stt(chara):
        speaker = pyttsx3.init()
        speaker.setProperty('rate',100)
        speaker.say(chara)
        speaker.runAndWait()
    
    def convert(exp):
     if('1' in exp and '3' in exp and '4' in exp and '5' in exp and '6' in exp):
        f1.write('y')
        stt('y')
     elif('1' in exp and '2' in exp and '3' in exp and '4'in exp and '5' in exp):
        f1.write('q')
        stt('q')
     elif('1' in exp and '2' in exp and '4' in exp and '5' in exp):
        f1.write('g')
        stt('g')
     elif('1' in exp and '3' in exp and '4' in exp and '5' in exp):
        f1.write('n')
        stt('n')
     elif('1'in exp and'2'in exp and'3'in exp and'4' in exp):
        f1.write('p')
        stt('p')
     elif('1'in exp and'2'in exp and'3'in exp and'5' in exp):
        f1.write('r')
        stt('r')
     elif('2'in exp and'3'in exp and'4'in exp and'5' in exp):
        f1.write('t')
        stt('t')
     elif('1'in exp and'2'in exp and'3'in exp and'6' in exp):
        f1.write('v')
        stt('v')
     elif('1'in exp and'3'in exp and'4'in exp and'6' in exp):
        f1.write('x')
        stt('x')
     elif('1'in exp and'3'in exp and'5'in exp and'6' in exp):
        f1.write('z')
        stt('z')
     elif('2'in exp and'4'in exp and'5'in exp and'6' in exp):
        f1.write('w')
        stt('w')
     elif('2'in exp and'5'in exp and'6' in exp):
        f1.write('. ')
        stt('full-stop')
     elif('1'in exp and'4'in exp and'5' in exp):
        f1.write('d')
        stt('d')
     elif('1'in exp and'2'in exp and'4' in exp):
        f1.write('f')
        stt('f')
     elif('1'in exp and'2'in exp and'5' in exp):
        f1.write('h')
        stt('h')
     elif('2'in exp and'4'in exp and'5' in exp):
        f1.write('j')
        stt('j')
     elif('1'in exp and'2'in exp and'3' in exp):
        f1.write('l')
        stt('l')
     elif('1'in exp and'3'in exp and'4' in exp):
        f1.write('m')
        stt('m')
     elif('1'in exp and'3'in exp and'5' in exp):
        f1.write('o')
        stt('o')
     elif('2'in exp and'3'in exp and'4' in exp):
        f1.write('s')
        stt('s')
     elif('1'in exp and'3'in exp and'6' in exp):
        f1.write('u')
        stt('u')
     elif('1'in exp and'2' in exp):
        f1.write('b')
        stt('b')
     elif('1'in exp and'2' in exp):
        f1.write('c')
        stt('c')
     elif('1'in exp and'5' in exp):
        f1.write('e')
        stt('e')
     elif('2'in exp and'4' in exp):
        f1.write('i')
        stt('i')
     elif('1'in exp and'3' in exp):
        f1.write('k')
        stt('k')
     elif('1'in exp and'4' in exp):
        f1.write('c')
        stt('c')
     elif('1' in exp):
        f1.write('a')
        stt('a')
     elif(exp==""):
        f1.write(' ')
        stt("space")

    def press(num):
        nonlocal expression
        expression = expression + str(num)
        equation.set(expression)

    def equalpress():
        nonlocal expression
        convert(expression)
        expression = ""
        equation.set("")

    new_window1=Toplevel(root)
    new_window1.geometry("174x320")
    new_window1.title("Braille Keypad")
    expression_field = Entry(new_window1, textvariable=equation)
    expression_field.grid(columnspan=10, ipadx=24, ipady=10)

    button1 = Button(new_window1, text=' ● ',command=lambda: press(1), height=4, width=11)
    button1.grid(row=1, column=0)

    button2 = Button(new_window1, text=' ● ',command=lambda: press(4), height=4, width=11)
    button2.grid(row=1, column=1)

    button3 = Button(new_window1, text=' ● ',command=lambda: press(2), height=4, width=11)
    button3.grid(row=2, column=0)

    button4 = Button(new_window1, text=' ● ', command=lambda: press(5), height=4, width=11)
    button4.grid(row=2, column=1)

    button5 = Button(new_window1, text=' ● ', command=lambda: press(3), height=4, width=11)
    button5.grid(row=3, column=0)

    button6 = Button(new_window1, text=' ● ', command=lambda: press(6), height=4, width=11)
    button6.grid(row=3, column=1)

    equal = Button(new_window1, text=' = ', command=equalpress, height=4, width=11)
    equal.grid(row=4, column=0)

    clear = Button(new_window1, text='Del', command=clear, height=4, width=11)
    clear.grid(row=4, column=1)

def openWindow2():
   win= Toplevel()
   win.geometry("300x200")
   def convert():
      text=entry.get()
      f2=open(text,'r')
      read=f2.read()
      speaker = pyttsx3.init()
      speaker.say(read)
      speaker.runAndWait()
      f2.close()
   entry= Entry(win, width= 40)
   entry.focus_set()

   entry.pack(pady=20)
#Create a Button to validate Entry Widget
   ttk.Button(win, text= "Convert",width= 20, command= convert).pack(pady=20)

def openWindow3():
   we=Toplevel()
   we.geometry("300x200")
   f1=open('Speech.txt','w')
   def stt():
      r = sr.Recognizer()
      with sr.Microphone() as source:     #install pyaudio module for microphone access
         r.adjust_for_ambient_noise(source)
         r.energy_threshold=400
         print("Say something:")
         audio=r.listen(source)
         try:
            text= r.recognize_google(audio)
        #print("You said : {}".format(text))
            f1.write(text)
            print("You said : "+text)
            f1.close()
         except: 
            l1=Label(we,text="Couldn't recognise properly")
            l1.pack(pady=20)
            print("Couldn't recognize properly")
   bt1=Button(we, width=30,text="Start",command=stt)
   bt1.pack(pady=60)

def openWindow4():
   win= Toplevel()
   win.geometry("300x200")
   def convert():
      f2=open('speech.txt','w')
      text=entry.get()
      img=cv2.imread(text)
      #gray=cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
      #r,t=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
      text=pytesseract.image_to_string(img)
      f2.write(text)
      speaker = pyttsx3.init()
      speaker.say(text)
      speaker.runAndWait()

   entry= Entry(win, width= 40)
   entry.focus_set()
   entry.pack(pady=20)

#Create a Button to validate Entry Widget
   ttk.Button(win, text= "Convert",width= 20, command= convert).pack(pady=20)

def openWindow5():
    def ttb(f):
        array1=[' ','!','"','#','$','%','&','','(',')','*','+',',','-','.','/',
    '0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
    'r','s','t','u','v','w','x','y','z','[','\\',']','^','_','\n']
        array2=[' ','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
        '⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
        '⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠪','⠳','⠻','⠘','⠸','\n']
        f1=open("braille.txt","w",encoding='utf8')
        arr=[]
        a=f.read()
        for i in a:
            arr.append(i)
        for i in arr:
            for j in range(0,len(array1)):
                if array1[j]==i:
                    f1.write(array2[j])
                j=j+1        
        f.close()
        f1.close()
    win=Toplevel()
    win.geometry("300x200")
    entry1=Entry(win,width=40)
    def convert():
        text=entry1.get()
        f=open(text,'r')
        ttb(f)
    
    entry1.pack(pady=20)
    b1=Button(win, text='Enter',width=10,command=convert)
    b1.pack(pady=20)

def openWindow6():
   win=Tk()
   win.geometry("300x200")
   def funct(a):
    if(a.endswith('.html') or a.endswith('.doc')):
        if a.endswith(".html"):
            f=open(a,"r")
        elif a.endswith(".doc"):
            f=open(a,"r")
        a=f.read()
        speaker=pyttsx3.init()
        speaker.say(a)
        speaker.runAndWait()
        f.close()
    elif(a.endswith('.pdf')):
        f=open(a,"rb")
        pdfreader= Py.PdfFileReader(f)
        pages=pdfreader.numPages
        speaker=pyttsx3.init()
        speaker.setProperty('rate',160)
        for num in range(0,pages):
            page=pdfreader.getPage(num)
            text=page.extractText()
            speaker.say(text)
            speaker.runAndWait()
   def func():
    fil=entry.get()
    funct(fil)
   entry=Entry(win,width=40)
   entry.pack(pady=20)
   b1=Button(win,text='Convert',command=func)
   b1.pack(pady=20)

if __name__=="__main__":
    root=Tk()
    btn1=Button(root, text="Braille Keypad", command=openWindow1)
    btn1.pack(padx=20, pady=20)
    btn2=Button(root, text="Text to Speech", command=openWindow2)
    btn2.pack(pady=20, padx=20)
    btn3=Button(root, text="Speech to Text", command=openWindow3)
    btn3.pack(pady=20, padx=20)
    btn4=Button(root, text="Image to Speech", command=openWindow4)
    btn4.pack(pady=20, padx=20)
    btn4=Button(root, text="Text to Braille", command=openWindow5)
    btn4.pack(pady=20, padx=20)
    btn5=Button(root, text="File to Speech", command=openWindow6)
    btn5.pack(pady=20, padx=20)
    root.geometry("300x450")
    root.title("Main Window")
    root.mainloop()