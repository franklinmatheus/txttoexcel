from pandas import read_csv
from tkinter import Tk, Canvas, Button, StringVar, Label, Button
from tkinter.filedialog import askopenfilenames, asksaveasfile

import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

class TxtToExcel():
    def selectfiles(self):
        self.files = askopenfilenames(parent=self.root,
                                    title='Escolha o(s) arquivo(s) txt',
                                    filetypes=(('Arquivo(s) de texto', 'txt'),))

        self.text.set(str(len(self.files)) + " arquivos selecionados")

        if (len(self.files) > 0): self.buttonsave["state"] = "active"

    def savexcel(self):
        merge = ""
        for file in self.files:
            temp = open(file, 'r').read()
            merge += temp + '\n'

        self.directory = asksaveasfile(parent=self.root,
                        title='Salvar arquivo',
                        defaultextension='.xlsx',
                        initialfile='txttoexcel')
        if self.directory is None:
            return

        data = StringIO(merge)
        self.df = read_csv(data,sep='\t')
        self.df.to_excel(self.directory.name,index=False)
        
        self.text.set("Arquivo salvo!")
        self.buttonsave["state"] = "disabled"
        self.files = []
        self.directory = None
        self.df = None

    def __init__(self):
        self.files = []
        self.directory = None
        self.df = None
        
        self.root = Tk()
        self.root.title("Txt to Excel")
        self.root.resizable(False, False)
        
        self.canvas = Canvas(self.root, width=250, height=250)
        self.canvas.pack()

        self.buttonadd = Button(self.root,text='Escolher arquivos txt',command=self.selectfiles,)
        self.canvas.create_window(125, 80, window=self.buttonadd)

        self.text = StringVar()
        self.text.set(str(len(self.files)) + " arquivos selecionados")

        self.label = Label(self.root, textvariable=self.text)
        self.canvas.create_window(125, 120, window=self.label)

        self.buttonsave = Button(self.root,text='Exportar excel',command=self.savexcel,bg='lightgreen')
        self.buttonsave["state"] = "disabled"
        self.canvas.create_window(125, 160, window=self.buttonsave)

        self.root.mainloop()

app=TxtToExcel()