from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class rotuloapp(app):
    def build(self):a 
        layout = BoxLayout(orientation='vertical')
        self.lab1 = label(
            text='SENAI', color=[1,0,0,1],
            font_size=40, bold= true
        )
self.lab2 = label(
    text='SESI', color=[0,1,0,1],
    font_dize=40 italic= true
)
self.lab3 = label(
    text='ENEM', color=[0,0,1,1],
    font_size=40, font_name='Arial',
    underline= True
)

layout.add_widget(self.lab1)
layout.add_widget(self.lab2)
layout.add_widget(self.lab3)
return layout 
if __name__ == '__main__':
    RotuloApp().run()