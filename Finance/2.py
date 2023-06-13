from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Teste(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        botão = Button(text='É Foda bixo')
        texto = Label(text='É complicado kkkk')
        box.add_widget(botão)
        box.add_widget(texto)

        box2 = BoxLayout()
        botão2 = Button(text='É Foda bixo')
        texto2 = Label(text='É complicado kkkk')
        box2.add_widget(botão2)
        box2.add_widget(texto2)
        box.add_widget(box2)
        return box

Teste().run()