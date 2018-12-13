import Tkinter as tkinter
import psutil
import os

for processess in psutil.process_iter():
    myprocessname = processess.as_dict(attrs=['name', 'pid'])
    if 'myreminder' in myprocessname:
        print(processess.as_dict(attrs=['name','pid']))
        with open('/tmp/myreminder.log',mode='a') as log:
            # print(' reminder is already opened so exiting.',file=log)
		print("okay")        
	exit(0)
   # else:
        # print(myprocessname)


mainwindow = tkinter.Tk()
mainwindow.title("...............hourly myreminder...............")
mainwindow.geometry('380x180+400+60')
mainwindow['padx'] = 5

resultLabel= tkinter.Label(mainwindow, text='What have you done in this hour?')
resultLabel.grid(row=0, column=0, sticky='w')

emptyLabel= tkinter.Entry(mainwindow, text="sdf*")
emptyLabel.grid(row=1, column=0, sticky='w')

emptyLabel1= tkinter.Entry(mainwindow)
emptyLabel1.grid(row=2, column=0, sticky='w')

emptyLabel2= tkinter.Entry(mainwindow)
emptyLabel2.grid(row=3, column=0, sticky='w')

# button1.destroy()
mainwindow.mainloop()
