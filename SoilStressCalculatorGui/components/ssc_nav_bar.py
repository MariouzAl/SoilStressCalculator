from tkinter import Button, Frame,TOP, BOTH, LEFT, Menubutton, Menu

class SoilStressCalculatorNavBar (Frame):
    def __init__(self,parent,color="#1f2329"):
        super().__init__(parent)
        self.configure(height=50, background=color,border=5 )
        self.addButtons()
        
    def addButtons(self):
        button = Button(self,text="Abrir", bd=0, bg="#1f2329")
        button.pack(side=LEFT)
        
        menu_button= Menubutton(self,text='Archivo', border=5)
        menu_button.pack(side=LEFT)

        menu= Menu(menu_button)
        menu_button.config(menu=menu)

        menu.add_command(label="Abrir")
        menu.add_command(label="Guardar")
