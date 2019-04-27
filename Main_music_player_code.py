from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tinytag import TinyTag
from mutagen.mp3 import MP3
import pygame
import random
import os,time
pygame.init()
pygame.mixer.pre_init(44100,-16,2,2048)
from PIL import Image,ImageTk
root=Tk()


root.title("ZEROMI")
root.minsize(width=300,height=350)
root.configure(bg="gray40")
root.resizable(0,0)
canvas11=Canvas(root,width=300,height=-20)
canvas11.place(x=0,y=270)
canvas12=Canvas(root,width=300,height=200,bg="gray")
canvas12.place(x=-2,y=270)
imagelist=["love1.gif","love2.gif","love3.gif","love4.gif","love5.gif","love6.gif","love7.gif","love8.gif","love9.gif","love10.gif","love11.gif","love12.gif","love13.gif","love14.gif","love15.gif","love16.gif"]

name=sys.argv[1]
#================================================================================

def format_duration(ms):
    total_s = ms / 1000
    total_min = total_s / 60
    remain_s = total_s % 60
    return "%0d:%02d" % (total_min, remain_s)



#===========================================================
pygame.mixer_music.load(name)
pygame.mixer_music.play(0)
path=name.split("/")
suffix=len(path)
a=""
for j in range(0,suffix-1):  
   a=a+"/"+path[j]
music_value=path[suffix-1]
print(music_value)
a=a.replace("/","",1)
a=a+"/"
#print(a)
list=[]
for name in os.listdir(a):
    if name.endswith(".mp3"):
       list.append(name) 
def transform(photo,x,y):
    icon=Image.open(photo)
    icon=icon.resize((x,y),Image.ANTIALIAS)
    icon=ImageTk.PhotoImage(icon)
    return icon
    

icon=transform("icon6.png",30,30)
root.iconphoto(True,icon)
img1=transform("white3.png",28,30)
img2=transform("white4.png",35,30)
img3=transform("white1.png",23,20)
img4=transform("white2.png",23,20)
repeat=transform("repeat_1.png",25,25)
repeat_play=transform("repeat.png",25,25)
shuffle=transform("shuffle_play.png",30,30)
shuffle_play=transform("shuffle2.png",25,25)
stop=transform("stop_main.png",30,30)
logo=transform("logo.png",250,250)
volume=transform("w3.png",30,45)
volume1=transform("w12.png",27,27)
mute=transform("mute2.png",27,27)
option=transform("option.png",25,25)
photo_back=transform("pppppp.jpg",556,270)
artist=""



giflist=[] 
canvas0=Canvas(root,width=250,height=250,bg="black",highlightthickness=0)
#canvas0.place(x=0,y=0)
for i in range(len(imagelist)):
    icon=transform(imagelist[i],210,210)
    giflist.append(icon)
m=0 
play_id=1
shuffling=1
gif_value=0
##print(giflist)
def gif():
    h=pygame.mixer.music.get_pos()
    for gif_value in giflist:
        canvas13.create_image(100,120,image=gif_value)
        canvas13.update()  
        time.sleep(0.1)
    
    
    root.after(100,gif)
 
   
def method(n,play):
   global m,play_id,music_value,a,blick_value,blick_call;
   m=n
   play_id=play
  
   if m==1:
       if play_id==1:
           pygame.mixer_music.unpause() 
       else:
           print("hii")
           pygame.mixer_music.load(a+music_value)
           pygame.mixer_music.play()  
           #call()
           play_id=1
       unpause_button["image"]=img2
       m=0
       blick_value=0
       root.after_cancel(blick_call)
   else:  
       pygame.mixer_music.pause()
       blick_value=1
       unpause_button["image"]=img1
       blick()
       m=1
artist=0;
title=0
blick_call=0
blick_value=0
blick_value1=0
def blick():
    global artist,title,blick_call,blick_value1,pos_ms
    #print("hii")
    if pos_ms==-1:
         position="0.00"
         label_move['text']=position
    if blick_value1==0:
        label_move["text"]=" "
        blick_value1=1
        #time.sleep(0.1)
    else:
        label_move["text"]=format_duration(pos_ms) 
        blick_value1=0
    blick_call=root.after(300,blick)
    
       
def method1(event):
   global music_value,shuffle_random,x1;
   x1=20
   canvas12.itemconfig(seek_rect, outline='gray70')
   canvas12.itemconfig(rect_move, outline='gray70')
   method(1,1)
   for i in range(len(list)):
       if list[i]==music_value:
          j=i
          break;
   j=j-1
   if j<0:
       j=len(list)-1
   music_value=list[j]
   #print("pre::::",music_value)
   name1=a+list[j] 
   pygame.mixer_music.load(name1) 
   pygame.mixer_music.play() 

def method2(event):
   global music_value,shuffle_random,x1;
   x1=20
   canvas12.itemconfig(seek_rect, outline='gray70')
   canvas12.itemconfig(rect_move, outline='gray70')
   method(1,1)
   if shuffle_random==1:
       #print("next")
       random.shuffle(list)
   for i in range(len(list)):
       if list[i]==music_value:
           j=i 
           break
   j=j+1

   if j>len(list)-1:
       j=0
   music_value=list[j]
   ##print("next::::",music_value)
   name1=a+list[j] 
   pygame.mixer_music.load(name1) 
   pygame.mixer_music.play()
solve=1
def method3(button_id):
    global music_value,solve,solve1
    y=pygame.mixer_music.get_busy()
    h=pygame.mixer_music.get_pos()
    #print("shuffle",h)
    if button_id==1:
        if int(h)==-1:
          print("hiii")
          pygame.mixer_music.load(a+music_value)
          pygame.mixer_music.play()
        solve=root.after(100,lambda:method3(button_id))
    elif button_id==2:
        ##root.after_cancel(solve)
        #print("shuffle")
        if int(h)==-1:
            music_value=random.choice(list)
            pygame.mixer_music.load(a+music_value)
            pygame.mixer_music.play()
        solve=root.after(100,lambda:method3(button_id))

    else:
         root.after_cancel(solve) 
        
     


def method4():
    global play_id
    pygame.mixer_music.stop() 
    method(2,2)
    root.after_cancel(repeat_repeat)
    root.after_cancel(shuffle_repeat)
    ##method3(3)
    
    
  
t=pygame.mixer_music.get_volume()  
d=1  
sound_value=0
def method5(d1):
    global d,button4,volume_value,cut
    d=d1

    if d==1:
        pygame.mixer_music.set_volume(0.0)
        button4['image']=mute
        ##mute_sound(1)
        sound_value=0
        cut=mute
        d=0
    else:
        pygame.mixer_music.set_volume(t)
        button4['image']=volume1
        cut=volume1
        d=1

color=0
def method6(event):
    global xpos,ypos,x_value,yvalue,t,sound_value,button3,canvas3,rect,color_value,color
    ra=range(50,170)
    r=range(50,56)
    r1=range(57,70)

   
    r2=range(71,80);r3=range(81,90);r4=range(91,100);r5=range(101,120);r6=range(121,140);r7=range(150,155)
    r8=range(155,160);r9=range(160,165);r10=range(165,174)
    ##if sound_value==0:
    method5(0)

    
    
   # canvas3.delete(rect)
    color_value=1
    
  
    if xpos in ra:
        x_value,yvalue=xpos,14.65
        #print("move",xpos)
        color=xpos
        button3.place(x=xpos,y=14.65)
        #canvas3.delete(rect)
        rect=canvas3.create_rectangle(50,20,170,20,fill="gray70",outline="gray70")
        rect1=canvas3.create_rectangle(50,20,color,20,fill="gray70",outline="blue")
        
        if xpos in r:
            t=0.0
            pygame.mixer_music.set_volume(t)
        if xpos in r1:
            t=0.1
            pygame.mixer_music.set_volume(t)
        if xpos in r2:
            t=0.2
            pygame.mixer_music.set_volume(t)
        if xpos in r3:
            t=0.3
            pygame.mixer_music.set_volume(t)
        if xpos in r4:
            t=0.4
            pygame.mixer_music.set_volume(t)
        if xpos in r5:
            t=0.5
            pygame.mixer_music.set_volume(t)
        if xpos in r6:
            t=0.6
            pygame.mixer_music.set_volume(t)
        if xpos in r7:
            t=0.7
            pygame.mixer_music.set_volume(t)
        if xpos in r8:
            t=0.8
            pygame.mixer_music.set_volume(t)
        if xpos in r9:
            t=0.9
            pygame.mixer_music.set_volume(t)
        if xpos in r10:
            t=1.0
            pygame.mixer_music.set_volume(t)
        ##canvas1.delete(myrectangle1)
        ##canvas1.move(myrectangle1,1,0)


shuffle_list=list[:]
shuffle_value=1
shuffle_random=7
def method7():
    global shuffle_value,shuffle_repeat,list,shuffle_random,shuffle_list
    if shuffle_value==1:
        random.shuffle(list)
        shuffle_button['image']=shuffle_play
        shuffle_method()
        shuffle_random=1
        method(1,1)
        shuffle_value=0
    else:
        shuffle_value=1
        list=shuffle_list
        shuffle_random=0
        shuffle_button['image']=shuffle
        root.after_cancel(shuffle_repeat)

shuffle_repeat=1
def shuffle_method():
    h=pygame.mixer_music.get_pos()
    global shuffle_repeat,music_value,x1
    if int(h)==-1:
            x1=20
            music_value=random.choice(list)
            pygame.mixer_music.load(a+music_value)
            pygame.mixer_music.play()
            canvas12.itemconfig(seek_rect, outline='gray70')
            canvas12.itemconfig(rect_move, outline='gray70')
    shuffle_repeat=root.after(100,shuffle_method)

repeat_repeat=1
repeat_value=1
def method8():                
    global repeat_value,repeat_repeat,a
    if repeat_value==1:
        repeat_button['image']=repeat_play
        method(1,1)
        repeat_method()
        repeat_value=0
    else:
        repeat_value=1
        repeat_button['image']=repeat
        root.after_cancel(repeat_repeat)
def repeat_method():
    
    global repeat_repeat,music_value,a,x1
    h=pygame.mixer_music.get_pos()
    if int(h)==-1:
        x1=20
        #print("hiii")
        pygame.mixer_music.load(a+music_value)
        pygame.mixer_music.play()
        canvas12.itemconfig(seek_rect, outline='gray70')
        canvas12.itemconfig(rect_move, outline='gray70')
    repeat_repeat=root.after(100,repeat_method)
def motion(event):
    global xpos,ypos
    xpos, ypos = event.x, event.y
    #print(xpos,ypos)
def method9():
    global music_value,a,x1,rect_move;
    try:
        file_path = filedialog.askopenfilename()
    except:
        pass
    try:
        file_index=file_path.rindex("/")
    except ValueError:
        pass
    try:
        music_value=file_path[file_index+1:100]
        a=file_path[0:file_index+1]
        pygame.mixer_music.load(a+music_value)
        x1=20
        canvas12.itemconfig(seek_rect, outline='gray70')
        canvas12.itemconfig(rect_move, outline='gray70')
        pygame.mixer_music.play()
        method(1,1)
        list.clear()
        for name in os.listdir(a):
            if name.endswith(".mp3"):
               list.append(name) 
               ##print(name)
    except:
        pass
        
x11_value=0
y11_value=0
button4=0
button3=0
volume_value=0
cut=volume1
x_value=166
canvas3=0
color_value=0
w,h=0,0
def method10():
   
    global x,w,h,top,x11_value,y11_value,winx,winy,button4,volume_value,cut,button3,x_value,canvas3,rect,color_value,xpos,color
    top.destroy()
    x11_value=winx + 25
    y11_value=winy+ 35
    w=200
    h=50
    top=Toplevel(root)
    top.geometry('%dx%d+%d+%d' % (w, h, x11_value, y11_value))
    canvas3=Canvas(top,width=200,height=50,bg="gray",highlightthickness=0)
    canvas3.bind("<Button-1>",method6)
    canvas3.pack()
    rect=canvas3.create_rectangle(50,20,170,20,fill="gray70")
    if color_value==0:
        canvas3.itemconfig(rect,outline="blue")
    else:
        #print("dish")
        #canvas3.delete(rect)
        canvas3.itemconfig(rect,outline="gray70")
        rect2=canvas3.create_rectangle(color,20,170,20,fill="gray70",outline="gray70")
        rect2=canvas3.create_rectangle(50,20,color,20,fill="gray70",outline="blue")
   
    photo1=transform("ball.png",20,20)
    button3=Button(canvas3,image=photo,bg="gray")
    button3['border']='0'
    button3.place(x=x_value,y=14.65)
    
    button4=Button(canvas3,image=cut,bg="gray",command=lambda:method5(d))
    button4['border']='0'
    button4.place(x=10,y=8)
    canvas3.bind('<Motion>', motion)
   
    top.wm_overrideredirect(True)
    x=0
    method12()

label_orignal=Label(canvas12,text="0.00",bg="gray",fg="gray91")
#label_orignal.config(font=("COOPBL", 9))
label_move=Label(canvas12,text="",bg="gray",fg="gray91")
label_move.place(x=13,y=34)
label_orignal.place(x=268,y=36)
top=Toplevel(root)
top.geometry("0x0")
top.wm_overrideredirect(True)
solve11=0
def method12():
    global x,solve11,top,winx,winy,w,h
    x=x+1
   
    #print(x)
    #top.geometry('%dx%d+%d+%d' % (w, h,winx1,winy1))
    if x==90:
       #print("hii")
       top.destroy()
       root.after_cancel(solve11)
         
    solve11=root.after(100,method12) 

x1=20
solve=1
value=-1
pos_ms=0
rect_move=0
def call():
    global x1,total_ms,value,solve11,top,artist,title,pos_ms,blick_value,blick_call,rect_move
    pos_ms = pygame.mixer_music.get_pos()
    audio=MP3(a+music_value)
    tag = TinyTag.get(a+music_value)
    artist=tag.artist
    title=tag.title
    year=tag.year
    
    if artist is None: 
        artist="audio"
    if year is None:
        year="Unknown"
    if year is "":
        year="Unknown"
    if title is None:
        length=len(music_value)
        title_length=length-3
        title=music_value[0:title_length]
        #title="Unkown"
   
    label_artist['text']=artist
    label_title['text']=title
    label_year['text']=year
    total_ms =audio.info.length
    total_ms=total_ms*1000
    
    progress_percent = pos_ms / float(total_ms) * 100
    if int(value) is int(progress_percent):   
        x1=x1
        #print("hii")
    else:
        if total_ms<7549.375:
           x1=x1+30.18
           print("hiiiiii")
           
        elif int(total_ms)<51854:
           print("heheheh")
           x1=x1+4.90
        else:
           x1=x1+2.45
    if x1>276:
        x1=276
    else:
        rect_move=canvas12.create_rectangle(22,59,x1,60,fill="gray90",outline="blue")
    if blick_value==0:
        position=format_duration(pos_ms) 
        label_move['text']=position
        #print("nope")
    else:
        label_move['text']=""
        if pos_ms==-1:
            position="0.00"
            label_move['text']=position
        #print("yup")
       
    label_orignal['text']=format_duration(total_ms) 
    if(pos_ms==-1):
        print(pos_ms)
        blick_value=0
        root.after_cancel(blick_call)
        canvas12.itemconfig(seek_rect, outline='gray70')
        canvas12.itemconfig(rect_move, outline='gray70')
        method(2,2)
        x1=20 
    value=progress_percent
    button1.place(x=x1,y=54)
    print(progress_percent,total_ms)
    solve11=root.after((1000) ,call)
winx=0
winy=0
def click(event):
   global winx,winy
   winx,winy=root.winfo_x(), root.winfo_y()     



unpause_button=Button(canvas12,image=img2,bg="gray",command=lambda:method(m,play_id))
unpause_button['border']='0'
unpause_button.config(width=30,height=30)
unpause_button.place(x=134,y=18)
#================================================
prev_button=Button(canvas12,image=img3,bg="gray")
prev_button.config(width=30,height=30)
prev_button['border']='0'
prev_button.bind("<Button-1>",method1)
prev_button.place(x=98,y=19)
#================================================
next_button=Button(canvas12,image=img4,bg="gray")
next_button['border']='0'
next_button.bind("<Button-1>",method2)
next_button.place(x=180,y=24) 
#================================================
seek_rect=canvas12.create_rectangle(22,59,276,60,fill="gray90",outline="gray70")
#================================================
photo=transform("ball4.png",10,10)
#photo=transform("orange.png",10,10)
button1=Button(canvas12,image=photo,bg="gray",command=method1)
button1['border']='0'
button1.place(x=20,y=54)
#================================================

repeat_button=Button(root,image=repeat,command=method8,bg="gray40")
repeat_button['border']='0'
repeat_button.place(x=264,y=111)
#=================================================
shuffle_button=Button(root,image=shuffle,bg="gray40",command=method7)
shuffle_button.place(x=264,y=60)
shuffle_button['border']='0'
#=================================================
stop_button=Button(canvas12,image=stop,command=method4,bg="gray")
stop_button['border']='0'
#stop_button.place(x=55,y=19)
#=================================================
mute_button=Button(root,image=volume,bg="gray40",command=method10)
mute_button['border']='0'
mute_button.place(x=265,y=151)
#====================================================
arrow=transform("ulta.png",15,10)
arrow_button=Button(root,image=arrow,bg="gray40")
arrow_button['border']='0'
#arrow_button.place(x=272,y=160)
#=====================================================
option_button=Button(root,image=option,bg="gray40",command=method9)
option_button.place(x=265,y=15)
option_button['border']='0'
#====================================================
root.bind('<Motion>', motion)
root.bind("<Motion>",click)
#===========================================================
label_artist=Label(root,text="",bg="gray40",fg="gray91")
label_artist.config(font=("COOPBL", 10))
label_artist.place(x=43,y=190)
#==========================================================

artist_tag=transform("micro4.png",20,20)
label_tag=Label(root,image=artist_tag,bg="gray40")
label_tag.place(x=12,y=190)  
#===========================================================
artist_tag1=transform("album4.png",32,25)
label_tag1=Label(root,image=artist_tag1,bg="gray40")
label_tag1.place(x=6,y=220) 
#==========================================================
label_title=Label(root,text=" ",bg="gray40",fg="gray91")
label_title.config(font=("COOPBL", 10))
label_title.place(x=43,y=220)
#==========================================================
artist_tag2=transform("disc.png",15,15)
label_tag2=Label(root,image=artist_tag2,bg="gray40")
label_tag2.place(x=13.65,y=248) 
#==========================================================
label_year=Label(root,text=" ",bg="gray40",fg="gray91")
label_year.config(font=("COOPBL", 10))
label_year.place(x=43,y=247)
canvas13=Canvas(root,width=224,height=170,bg="gray2",highlightthickness=0)
canvas13.place(y=-1,x=-1)
call()
gif()
#root.lift()
#root.attributes('-topmost',True)
#root.after_idle(root.attributes,'-topmost',False)  
root.mainloop()

