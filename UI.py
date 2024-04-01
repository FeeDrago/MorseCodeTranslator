import tkinter as tk




class Ui(tk.Tk):

    def __init__(self, translate_func):
        super().__init__()
        self.translate = translate_func
        self.geometry("600x300")
        self.resizable(False, False)
        self.title("MorseCodeTranslator")
        self.center_window()
        
        # Entry
        self.word = tk.StringVar()
        self.entry = tk.Entry(textvariable=self.word,width=30, font=('Arial', 20))
        self.entry.insert(0, 'Enter text to translate.')
        self.entry.bind("<FocusIn>", self.entryFocusIn)
        self.entry.bind("<FocusOut>", self.entryFocusOut)

        self.entry.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

        # Submit Button
        self.button = tk.Button(text='Translate', command=lambda: self.translate(self.entry.get()), state='normal')
        self.button.grid(row=0, column=2, padx=20)


        #Output
        self.out = tk.Text()
        self.out.insert(tk.END, 'Your translated message.')

        self.out.grid(row=1, column=0, columnspan=3, pady=20)
        self.mainloop()


    def entryFocusIn(self, event):
        if self.entry.get() == 'Enter text to translate.':
            self.entry.delete(0, tk.END)
        else:
            return
        
    def entryFocusOut(self, event):
        if self.entry.get() == 'Enter text to translate.':
            pass
        else:
            self.translate(self.entry.get())
    
    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - self.winfo_reqwidth() - 300) / 2
        y = (screen_height - self.winfo_reqheight() -150) / 2

        self.geometry(f"+{int(x)}+{int(y)}")

if __name__ == '__main__':
    window = Ui()