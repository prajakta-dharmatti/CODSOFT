import tkinter
from tkinter import *

module=Tk()
module.title("To Do List By Prajakta Dharmatti")
module.geometry("400x650+400+100")
module.resizable(False,False)

task_list= []

def AddTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("taskList.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
            task_list.append(task)
            listbox.insert(END, task)

def DeleteTask():
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete( ANCHOR)


Image_icon=PhotoImage(file="Images/iconimage.png")
module.iconphoto(False,Image_icon)


TopbarImage=PhotoImage(file="Images/topbar.png")
Label(module,image=TopbarImage).pack()



menuImage=PhotoImage(file="Images/dock.png")
Label(module,image=menuImage,bg="#32405b").place(x=30,y=25)



heading=Label(module,text="All TASKS",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=130,y=20)


frame= Frame(module,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0, command=AddTask)
button.place(x=300,y=0)


frame1= Frame(module,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox= Listbox(frame1,font=("arial",12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar= Scrollbar(frame1)
scrollbar.pack(side= RIGHT, fill= BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


Delete_icon=PhotoImage(file="Images/delete.png")
Button(module,image=Delete_icon,bd=0, command=DeleteTask).pack(side=BOTTOM,pady=13)



module.mainloop()
