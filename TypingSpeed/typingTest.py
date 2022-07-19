import tkinter as tk
import time
import random
import difflib

ROW = 6
COLUMN = 3
BGC = '#00154F'
#FG =



class Canvas:

    @staticmethod
    def set_row_col_weight(root):
        for row in range(ROW):
            root.grid_rowconfigure(row, weight = 1)
            # 1 here means if there is an extra space then make the row bigger
        for col in range(COLUMN):
            root.grid_columnconfigure(col, weight = 1)
            
            
    def __init__(self, root):
        self.text = ["The greatest glory in living lies not in never falling, but in rising every time we fall.",
                     "The way to get started is to quit talking and begin doing.",
                     "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
                     "If life were predictable it would cease to be life, and be without flavor.",
                     "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
                     "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
                     "Life is what happens when you're busy making other plans.",
                     "One day the people that don’t even believe in you will tell everyone how they met you.",
                     "The true meaning of life is to plant trees, under whose shade you do not expect to sit.",
                     "The quick brown fox jumps over the lazy dog."]
        self.speed = 0
        self.accuracy = 0
        self.time_start = 0
        self.time_end = 0
        root.title('Typing Speed Test')
        root.minsize(700, 700)
        root.configure(bg = BGC)
        self.upper_label = tk.Label(root, text = 'Measure your speed and accuracy', anchor = 'center', font = 'TkCaptionFont 50', bg = BGC, fg = 'white')
        
        self.text_to_type = tk.Label(root, text = '', anchor = 'center', font = 'TkCaptionFont 15', bg = BGC, fg = 'white')
        
        self.upper_label.grid(row = 1, column = 0, columnspan = COLUMN, sticky = 'wesn')
        
        self.upper_label.grid(row = 0, column = 0, columnspan = COLUMN, sticky = 'wesn')
        self.user_input = tk.Text(root, width = '5', font = ('Arial 12'))
        self.user_input.grid(column=0, row=2, columnspan=3, sticky="nsew")
        self.btn_start = tk.Button(root, text="Start/Restart", command=self.start)
        self.btn_start.grid(column=0, row=3, columnspan=1, sticky="nsew")
        self.btn_stop = tk.Button(root, text="Stop", command=self.stop)
        self.btn_stop.grid(column=1, row=3, columnspan=1, sticky="nsew")
        self.btn_newtext = tk.Button(root, text="New Text", command=self.new_text)
        self.btn_newtext.grid(column=2, row=3, columnspan=1, sticky="nsew")
        
        
        self.label_speed = tk.Label(
            root, text=f"Your typing speed is {self.speed} WPM")
        self.label_speed.grid(row=4, column=0, columnspan=3, sticky="nsew")

        self.label_accuracy = tk.Label(
            root, text=f"Your typing accuracy is {self.speed} %")
        self.label_accuracy.grid(row=5, column=0, columnspan=3, sticky="nsew")
        
        
    def start(self):
        self.time_start = time.time()
    
    def stop(self):
        self.time_end = time.time()
        words = self.user_input.get().split(' ')
        self.speed = round(len(words)/((self.time_end - self.time_start)/60))
        self.label_speed.config(
            text=f"Your typing Speed is {self.speed} WPM")
        self.accuracy = round(difflib.SequenceMatcher(None, self.text_to_type.cget(
            "text"), self.user_input.get("1.0", 'end-1c')).ratio()*100)
        self.label_accuracy.config(
            text=f"Your typing accuracy is {self.accuracy} %")
            
    def new_text(self):
        self.text_to_type.config(
            text=self.text[random.randint(0, len(self.text)-1)])
        self.user_input.delete('0', 'end')

def run():
    root = tk.Tk()
    gui = Canvas(root)
    root.mainloop()

if __name__ == '__main__':
    run()
        
