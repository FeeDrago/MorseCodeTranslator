import tkinter as tk
import json



class Ui(tk.Tk):

    @staticmethod
    def get_morse_code() -> dict:
        """Returns a dictionary with keys the characters and values their morse translation"""
        with open("./morsecode.json", 'r') as file:
            d = json.load(file)
        return d



    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.resizable(False, False)
        self.title("MorseCodeTranslator")
        self.center_window()
        
        # Entry
        self.word = tk.StringVar()
        self.entry = tk.Entry(textvariable=self.word,width=30, font=('Arial', 20))
        self.entry.insert(0, 'Enter text to translate.')
        self.entry.bind("<FocusIn>", self.entryFocusIn)
        self.entry.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

        # Submit Button
        self.button = tk.Button(text='Translate', command=lambda: self.translate(self.read_word()), state='normal')
        self.button.grid(row=0, column=2, padx=20)


        #Output
        self.out = tk.Label()
        self.out.config(text='Translated Message', font=('Arial', 20))
        self.out.grid(row=1, column=0, columnspan=3, pady=20)
        self.mainloop()


    def read_word(self) -> str:
        word = self.entry.get().lower()
        code = self.get_morse_code()
        for letter in word:
            if letter not in code.keys() and letter != " ":
                self.out.config(text=f'Unrecognised character {letter}.\nPlease enter a valid word or phrase.')
                return ""
        return word

    def translate(self, word):
        print(word)
        if word == "":
            return
        else:
            code = self.get_morse_code()
            translated = ""
            for character in word:
                if character == " ":
                    translated += "   " 
                else:
                    translated += code[character]
                    translated += " "
            self.out.config(text=translated)

    def entryFocusIn(self, event):
        if self.entry.get() == 'Enter text to translate.':
            self.entry.delete(0, tk.END)
        else:
            return
    
    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_reqwidth() - 300) / 2
        y = (screen_height - self.winfo_reqheight() -150) / 2
        self.geometry(f"+{int(x)}+{int(y)}")

if __name__ == '__main__':
    window = Ui()