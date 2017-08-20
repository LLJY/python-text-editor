from tkinter import *
import tkinter, tkinter.filedialog
root=Tk("PyEdit");
text=Text(root);
text.grid();
hasopened = False;
def fileopen():
    global hasopened
    global file
    hasopened = True;
    file = tkinter.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")));
    f = open(file,'r+');
    dlg = f.read();
    text.insert(INSERT, dlg);
    f.close();
    return file
def saveas():
    try:
        t = text.get("1.0", "end-1c");
        f = open(save, "w+");
        f.write(t);
        f.close();
    except:
        save = tkinter.filedialog.asksaveasfilename();
        t = text.get("1.0", "end-1c");
        f = open(file,'w');
        f.write(t);
        f.close();
button=Button(root, text="Save", command=saveas);
button.grid(row=10, column=0);
button1=Button(root, text="Open", command=fileopen);
button1.grid(row=10, column=1);
if (hasopened == True):
    button2=Button(root, text="Save", command=save);
    button2.grid(row=10, column=2);
root.mainloop();
