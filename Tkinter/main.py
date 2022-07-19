
import tkinter
window = tkinter.Tk()
window.title('My first GUI')
window.minsize(width = 600, height = 600)


# create a label

my_label = tkinter.Label(text = 'Field', font = ('Times New Roman', 25, 'italic'))

my_label.pack(side = 'left')


my_label['text'] = 'FIELD'

# my_label['text'] = 'NEW FIELD'

# BUTTON


def button_clicked():
	print('You just clicked a button')
	my_label.config(text = user_input.get())

button = tkinter.Button(text = 'click me', command = button_clicked)

button.pack(side = 'left')

# ENTRY
user_input =tkinter.Entry(width = 10)
user_input.pack()
print(user_input.get())


window.mainloop()

