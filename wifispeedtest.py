from tkinter import * 
import speedtest

root=Tk()
root.title (" SpeedTest")
root.geometry("360x600")
root.resizable(False, False)
root.configure(bg="#1a212d")

#def
def speed_check ():
    test=speedtest.Speedtest()
    uploading=round(test.upload()/ (1024*1024), 2 )
    upload.config(text=uploading)
    
    downloading=round(test.download()/ (1024*1024), 2 )     
    download.config(text=downloading)
    Download.config(text=downloading)
    
    
    servernames=[]
    test.get_servers(servernames)
    ping.config(text=test.results.ping)
    
    
#icon 
image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)


#images 

Top=PhotoImage(file="top.png")
Label(root, image=Top, bg="#1a212d").pack()


Main=PhotoImage(file="main.png")
Label(root, image=Main, bg="#1a212d").pack(pady=(40,0))

button=PhotoImage(file="button.png")
Button=Button(root, image=button, bg="#1a212d", bd=0, activebackground="#1a212d", command=speed_check  )
Button.pack(pady=10)

Label(root, text="PING", font="arial 10 bold", bg="#384056" ).place(x=50, y=0)
Label(root, text="DOWNLOAD", font="arial 10 bold", bg="#384056" ).place(x=140, y=0)
Label(root, text="UPLOAD", font="arial 10 bold", bg="#384056" ).place(x=260, y=0)

Label(root, text="MS", font="arial 7 bold", bg="#384056", fg="yellow").place(x=60, y=80)
Label(root, text="Mbps", font="arial 7 bold", bg="#384056", fg="yellow").place(x=165, y=80)
Label(root, text="Mbps", font="arial 7 bold", bg="#384056", fg="yellow").place(x=275, y=80)


Label(root, text="DOWNLOAD", font="arial 15 bold", bg="#384056" , fg="yellow").place(x=140, y=280)
Label(root, text="MBPS", font="arial 15 bold", bg="#384056" , fg="yellow").place(x=155, y=380)


ping=Label(root, text="00", font="arial 13 bold", bg="#384056", fg="yellow")
ping.place(x=70,y=60,anchor= 'center')

download=Label(root, text="00", font="arial 13 bold", bg="#384056", fg="yellow")
download.place(x=180,y=60,anchor= 'center')

upload=Label(root, text="00", font="arial 13 bold", bg="#384056", fg="yellow")
upload.place(x=290,y=60,anchor= 'center')

Download=Label(root, text="00", font="arial 13 bold", bg="#384056", fg="yellow")
Download.place(x=185,y=350,anchor= 'center')








root.mainloop()


