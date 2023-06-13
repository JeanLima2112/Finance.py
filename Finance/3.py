from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Teste(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        botão = Button(text='É Foda bixo',font_size=30,on_release=self.incrementar)
        self.texto = Label(text='1',font_size=30)
        box.add_widget(botão)
        box.add_widget(self.texto)
        return box
    def incrementar(self,botão):
        botão.text = 'pressionado'
        self.texto.text = str(int(self.texto.text)+1)



Teste().run()