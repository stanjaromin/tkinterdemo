try:
    import tkinter
except ImportError:
    import TKinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()
mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480')
mainWindow.mainloop()



