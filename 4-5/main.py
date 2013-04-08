import kivy
kivy.require('1.0.8')

from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.base import runTouchApp
from functools import partial
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox

if __name__ == '__main__':
    root = FloatLayout();
    Window.clearcolor = (.64, .64, .64, 1)
    Window.set_title("BSK - PRACOWNIA SPECJALISTYCZNA 2-3")
    def zakoduj_rail(textbox1, textbox2, *args):
        popup = Popup(title='Podczas szyfrowania wystapil blad!',content=Label(text='Nie podales wartosci w polu tekstu do zaszyfrowania'),size_hint=(None, None), size=(500, 150))
        popup.open()
  
    def on_checkbox_active(sender,btn_sender,*args):
        if(sender.active): btn_sender.text = "Dekoduj"
        else: btn_sender.text = "Zakoduj"
    #######################ZADANIE1##################################
    label_zad_1_text = 'Zadanie 1 - Wprawdz napis do zakodowania - Rail Fence'
    label_zad_1 = Label(text=label_zad_1_text, size_hint_y=None, height=50, pos=(0,550))
    root.add_widget(label_zad_1)
    s = Scatter(size_hint=(None, None), pos=(410, 500))
    textbox1 = TextInput(size_hint=(None, None), size=(280, 300),multiline=True)
    s.add_widget(textbox1)
    root.add_widget(s)
    
    s = Scatter(size_hint=(None, None), pos=(85, 500))
    textbox2 = TextInput(size_hint=(None, None), size=(300, 300),multiline=True)
    s.add_widget(textbox2)
    root.add_widget(s)
    
    
    checkbox_zad1 = CheckBox(pos=(660,475), size_hint=(None, None))
    root.add_widget(checkbox_zad1)
    checkbox_zad2 = CheckBox(pos=(660,305), size_hint=(None, None))
    root.add_widget(checkbox_zad2)
    checkbox_zad3 = CheckBox(pos=(660,135), size_hint=(None, None))
    
    runTouchApp(root)