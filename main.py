import customtkinter as ctk
from tkinter.filedialog import askopenfilename
import pygame
from PIL import Image
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        self.title("Radio")
        self.iconbitmap("images/icon.ico")
        self.minsize(width=900,height=600)
        self.maxsize(width=900,height=600)

        self.music_path_label = None
        self.music_path = None
        self.radio_box()

    def radio_box(self):

        radio_image = ctk.CTkImage(dark_image=Image.open("images/radio.png"), light_image=Image.open("images/radio.png"), size=(800, 800))
        radio_image_label = ctk.CTkLabel(self, width=600, height=600, text="", image=radio_image)
        radio_image_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        volume_slider = ctk.CTkSlider(self,command=volume_settings,width=440,height=30,border_width=10,border_color="pink",progress_color="purple",button_color="pink",button_hover_color="pink")
        volume_slider.set(0.5)
        pygame.mixer.music.set_volume(0.5)
        volume_slider.place(relx=0.2565,rely=0.375)

        load_tape_icon = ctk.CTkImage(dark_image=Image.open("images/load-tape.png"),light_image=Image.open("images/load-tape.png"), size=(100,80))
        load_music_button = ctk.CTkButton(self,text="",border_width=0,corner_radius=0,height=95,width=147,image=load_tape_icon,command=self.load_music)
        load_music_button.place(relx=0.4275,rely=0.4800)

        continue_music_icon = ctk.CTkImage(dark_image=Image.open("images/play-icon.png"),light_image=Image.open("images/play-icon.png"), size=(46, 46))
        continue_music_button = ctk.CTkButton(self, text="", border_width=0, corner_radius=0, height=38, width=147, image=continue_music_icon, fg_color="dark blue", hover_color="blue",command=continue_music)
        continue_music_button.place(relx=0.4275, rely=0.6475)

        pause_music_icon = ctk.CTkImage(dark_image=Image.open("images/pause-icon.png"), light_image=Image.open("images/pause-icon.png"), size=(30, 30))
        pause_music_button = ctk.CTkButton(self, text="", border_width=0, corner_radius=0, height=30, width=147, image=pause_music_icon, fg_color="purple", hover_color="#301934", command=pause_music)
        pause_music_button.place(relx=0.4275, rely=0.7450)

        self.music_path_label = ctk.CTkLabel(self,font=('Arial',16,'bold'))

    def load_music(self):
        self.music_path = askopenfilename(filetypes=[("Mp3 Files", "*.mp3")])
        music_name = os.path.basename(self.music_path)

        self.music_path_label.configure(text=f"{music_name}")
        self.music_path_label.place(relx=0.5,rely=0.05,anchor=ctk.CENTER)

        if self.music_path:
            pygame.mixer.music.load(self.music_path)
            pygame.mixer.music.play()
            pygame.mixer.music.pause()

def volume_settings(volume):
    pygame.mixer.music.set_volume(volume)

def continue_music():
    pygame.mixer.music.unpause()

def pause_music():
    pygame.mixer.music.pause()

if __name__ == "__main__":
    window  = App()
    window.mainloop()