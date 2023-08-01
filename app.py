import customtkinter as ctk
from assets.images import logo_images as li

class App(ctk.CTk):
    def __init__(self, tamanho):
        # MAIN SETUP
        super().__init__()
        self.title('Ludani School')
        self.geometry(f'{tamanho[0]}x{tamanho[1]}')
        self.resizable(False,False)
        self._set_appearance_mode('light')

        # WIDGETS
        Login(self)

class Login(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        # CONFIG FRAME
        self.configure(corner_radius=0, bg_color='#f6e7d8', fg_color='transparent')
        self.columnconfigure(0, weight = 2, uniform = 'a')
        self.columnconfigure(1, weight = 1, uniform = 'a')
        self.rowconfigure((0,1,2,3,4), weight = 1, uniform = 'a')
        self.pack(expand = True, fill = 'both')

        # WIDGETS
        lb_logo = ctk.CTkLabel(self, text = '', fg_color='#f6e7d8', image = li.img_logo_sem_fundo)
        lb_login = ctk.CTkLabel(self, text = 'Seja Bem Vindo\nFaça o Login', font = ('Calibri', 24, 'bold'), anchor = 's', text_color='#1c191a', bg_color='#f6e7d8', fg_color='transparent')
        

        # GRIDS
        lb_logo.grid(row = 0, column = 0, rowspan = 5, sticky = 'swne')
        lb_login.grid(row = 0, column = 1, sticky = 'nsew')

if __name__ == '__main__':
    App((900,500)).mainloop()