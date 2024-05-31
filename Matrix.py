from tkinter import Frame, Tk, Canvas
from random import choice

class Matrix(Frame):
    def __init__(self, master):
            super().__init__(master)
        
            self.canvas = Canvas(master, bg= 'black')
            self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        
            self.velocidad = [i for i in range(0, 30, 5)]
            self.pos = [i for i in range(-200, 200, 20)]
            self.latters = []
            self.green = 0
            self.caracters = [
                  "a", "k", "u", "u", "u", "u", "u",
                  "b", "l", "v", "v", "v", "v", "v",
                  "c", "m", "w", "w", "w", "w", "w",
                  "d", "n", "x", "x", "x", "x", "x",
                  "e", "o", "y", "y", "y", "y", "y",
                  "f", "p", "z", "z", "z", "z", "z",
                  "g", "q", "1", "1", "1", "1", "1",
                  "h", "r", "2", "2", "2", "2", "2",
                  "i", "s", "3", "3", "3", "3", "3",
                  "j", "t", "4", "4", "4", "4", "4",
            
        ]
        
            self.draw()
            self.update()
        
def draw(self):
    for x in range(0, 1600, 20):
           y = choice(self.pos)
           for j in range(0, choice([180, 220, 280]), 20):
               self.obj = self.canvas.create_text(20+x, -200+y+j, text= choice(self.caracteres),
                        fill = 'green2', font= ('Arial', 14))
               self.letters.append(self.obj)
               
def update(self):
        for letter in self.letters:
               v = choice(self.velocidad)
               self.green +=5
               color = '#{:02x}{:02x}{:02x}'.format(0, self.green,0)
               self.canvas.itemconfig(letter, fill=color)
               self.canvas.move(letter, 0, v)
               y = self.canvas.coords(self.obj)
         
               if self.green >=250:
                       self.green = 0
                
        if y[1] >=800:
                self.draw()
                if y[1]>= 1200:
                         self.letters.clear()
                         self.canvas.delete('all')
                self.canvas.after(80, self.update)
         
if __name__ == '__main__':
    root = Tk()
    root.title('Matrix Animation')
    root.config(bg= 'black')
    root.attributes('-fullscreen', True)
    app = Matrix(root)
    app.mainloop()
    
    
    
           
