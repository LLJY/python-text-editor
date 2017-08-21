from tkinter import *
import tkinter, tkinter.filedialog
class m:
    def __init__(self, file, f, t, hasopened, dlg, save):
        self.file = file;
        self.f = f;
        self.t = t;
        self.hasopened = hasopened;
        self.dlg = dlg;
        self.save = save;
        self.hasopened = False;
    def fileopen():
        hasopened = True;
        file = tkinter.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")));
        f = open(file,'r+');
        dlg = f.read();
        text.insert(INSERT, dlg);
        f.close();
        button2=Button(root, text="Save", command=m.saveas);
        button2.grid(row=10, column=2);
        return file
    def saveas():
        save = tkinter.filedialog.asksaveasfilename();
        t = text.get("1.0", "end-1c");
        f = open(save,'w');
        f.write(t);
        f.close();
    def new():
        save = tkinter.filedialog.asksaveasfilename();
        t = text.get("1.0", "end-1c");
        f = open(file,'w');
        f.write(t);
        f.close();
    def save():
       t = text.get("1.0", "end-1c");
       f = open(self.file,'w');
       f.write(t);
       f.close();


root=Tk("PyEdit");
text=Text(root);
text.grid();
hasopened = False;
button=Button(root, text="Save as", command=m.saveas);
button.grid(row=10, column=0);
button1=Button(root, text="Open", command=m.fileopen);
button1.grid(row=10, column=1);
button2=Button(root, text="Save", command=m.save, state=DISABLED);
button2.grid(row=10, column=2);
root.mainloop();
