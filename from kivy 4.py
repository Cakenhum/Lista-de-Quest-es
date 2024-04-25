from kivy.app import App
from kivy.uix.button import Button

def botao_pressionado(instance):
    print("botão pressionado")

class minhaApp(App):
    def build(self):
        btn = button(text='Clique Aqui')
        btn.bind(on_press=botao_pressionado)
        return btn
if __name__ == "__main__":
    MinhaApp().run()

    