from customtkinter import CTkImage
from PIL import Image

img_logo_com_fundo = CTkImage(  dark_image=Image.open('assets/images/logo_light_com_fundo.png'),
                                light_image=Image.open('assets/images/logo_dark_com_fundo.png'),
                                size=(800,800))

img_logo_sem_fundo = CTkImage(  dark_image=Image.open('assets/images/logo_light_sem_fundo.png'),
                                light_image=Image.open('assets/images/logo_dark_sem_fundo.png'),
                                size=(400,400))