from kivy.app import app 
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

class Minhaapp(app):
    def build(self):
        return button(text='Clique Aqui', background_color=get_color_from_hex("#3492db"))

if __name__ == "__main__":
    Minhaapp().run()