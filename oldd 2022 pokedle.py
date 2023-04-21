# Wordle Pokémon theme - by Asher - 13.04.22

import turtle, random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
y = 250

word_list = ['ekans', 'arbok', 'zubat', 'gloom', 'paras', 'golem', 'doduo', 'hypno', 'ditto', 'eevee', 'pichu', 'aipom', 'yanma', 'unown', 'magby', 'entei', 'lugia', 'ho-oh', 'lotad', 'ralts', 'minun', 'numel', 'absol', 'bagon', 'shinx', 'luxio', 'budew', 'burmy', 'gible', 'riolu', 'rotom', 'azelf', 'snivy', 'tepig', 'munna', 'throh', 'zorua', 'klink', 'klang', 'deino', 'inkay', 'goomy', 'hoopa', 'toxel', 'kubfu']
answer = random.choice(word_list) 

def popup_bonus():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="Input")
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)

def popup_showinfo():
    showinfo("Window", "Wordle for Pokémon, Guess only 5 letter Pokémon!, Close the TK when you are ready to start.")

class Application(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack()

    

        self.button_showinfo = ttk.Button(self, text="Show Info", command=popup_showinfo)
        self.button_showinfo.pack()

root = tk.Tk()

app = Application(root)

root.mainloop()

def draw_square(x,y,col): 
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(col)
    turtle.begin_fill()     
    for i in range(4):     
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill() 

def input_guess(prompt):

        my_input = turtle.textinput("5 letter pokémon", prompt)
        
        if len(my_input) == 5:
            if my_input == None: return "     "
            elif len(my_input) != 5: return my_input[0:5] 
            else: return my_input.lower()
            
            
     
def check_guess(my_input,answer,y):
    count = 0 
    x = -250
    for i in my_input:
        if i == answer[count]: draw_square(x,y,"green") 
        elif i in answer: draw_square(x,y,"yellow") 
        else: draw_square(x,y,"red")
        count+=1
        x += 75
    turtle.penup() 
    turtle.goto(x,y-25)
    turtle.write(my_input,font=("Verdana", 15, "normal"))

for i in range(6): 
    guess_prompt = "What is guess "+str(i+1)+"?"
        
    my_input = input_guess(guess_prompt) 
    check_guess(my_input,answer,y)  
    y -= 75
    
    if my_input == answer:
        turtle.penup()
        turtle.goto(-300,-200) 
        turtle.write("Congratulations!!!",font=("Verdana", 42, "normal"))
        break

else: 
    turtle.penup()
    turtle.goto(-300,-200)
    turtle.write(answer,font=("Verdana", 42, "normal"))
turtle.done() 
