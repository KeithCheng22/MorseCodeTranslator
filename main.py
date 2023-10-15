from references import Converter
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Morse Code Translator")
window.geometry("900x400")
converter = Converter()


def remove_ui():
    encode_button.destroy()
    decode_button.destroy()
    label.destroy()


def encoder():
    def submit1():
        user_input = entry.get().lower()
        try:
            output = converter.encode(user_input)
        except KeyError:
            messagebox.askretrycancel("Error", "The text is not recognised. Try Again?")
            entry.delete(0, END)
        else:
            if user_input == '':
                messagebox.showerror("Error", "Please Input Message!")
            else:
                messagebox.showinfo(title="Here's your encoded message!", message=output)
                entry.delete(0, END)

    remove_ui()

    label1 = Label(text='Enter Text to Encode')
    label1.place(x=400, y=250)

    entry = Entry()
    entry.focus()
    entry.place(x=370, y=270)

    submit = Button(text='Submit', command=submit1)
    submit.place(x=360, y=300)

    decode_instead = Button(text='Decode Instead', command=decoder)
    decode_instead.place(x=440, y=300)



def decoder():
    def submit2():
        user_input = entry.get().lower()
        try:
            output = converter.decode(user_input)
        except ValueError:
            messagebox.askretrycancel("Error", "The text is not recognised. Try Again?")
            entry.delete(0, END)
        else:
            if user_input == '':
                messagebox.showerror("Error", "Please Input Message!")
            else:
                messagebox.showinfo(title="Here's your decoded message!", message=output)
                entry.delete(0, END)

    remove_ui()

    label1 = Label(text='Enter Text to Decode')
    label1.place(x=400, y=250)
    entry = Entry()
    entry.focus()
    entry.place(x=370, y=270)

    submit = Button(text='Submit', command=submit2)
    submit.place(x=360, y=300)

    encode_instead = Button(text='Encode Instead', command=encoder)
    encode_instead.place(x=440, y=300)


# Main UI
canvas = Canvas(width=800, height=267)
hacker_img = PhotoImage(file="hacker.png")
canvas.create_image(400, 133.5, image=hacker_img)
canvas.place(x=45, y=0)

label = Label(text='Welcome to the Morse Code Translator. Select an option.')
label.place(x=270, y=250)

encode_button = Button(text='Encode', command=encoder)
encode_button.place(x=350, y=270)

decode_button = Button(text='Decode', command=decoder)
decode_button.place(x=460, y=270)

window.mainloop()
