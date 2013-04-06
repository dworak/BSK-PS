import kivy
import itertools
from zad1 import rail
from zad2 import matrix_translation
from zad5 import vigenere
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
        if(textbox2.text!=""):
            a=rail(3)
            textbox1.text = a.encrypt(textbox2.text)
        else:
            popup = Popup(title='Podczas szyfrowania wystapil blad!',content=Label(text='Nie podales wartosci w polu tekstu do zaszyfrowania'),size_hint=(None, None), size=(500, 150))
            popup.open()
    def odkoduj_rail(textbox1, textbox2, *args):
        if(textbox2.text!=""):
            a=rail(3)
            textbox1.text = a.decrypt(textbox2.text,a.key)
        else:
            textbox1.text = "Podaj wartosc, do odkodowania"

    def obsluga_rail(textbox1,textbox2,checkbox, *args):
        if(checkbox.active):
            zakoduj_rail(textbox1,textbox2)
        else:
            odkoduj_rail(textbox1,textbox2)

    def zakoduj_matrix(textbox2, textbox3, *args):
        if(textbox3.text!=""):
            a=matrix_translation("34152",5)
            textbox2.text = a.encrypt(textbox3.text)
        else:
            popup = Popup(title='Podczas szyfrowania wystapil blad!',content=Label(text='Nie podales wartosci w polu tekstu do zaszyfrowania'),size_hint=(None, None), size=(500, 150))
            popup.open()
    def odkoduj_matrix(textbox2, textbox3, *args):
        if(textbox2.text!=""):
            a=rail(3)
            textbox1.text = a.encrypt(textbox2.text)
        else:
            textbox1.text = "Podaj wartosc, do odkodowania"

    def obsluga_matrix(textbox1,textbox2,checkbox, *args):
        if(checkbox.active):
            zakoduj_rail(textbox1,textbox2)
        else:
            odkoduj_rail(textbox1,textbox2)

    def zakoduj_vigenere(textbox4, textbox5, *args):
        if(textbox5.text!=""):
            a=vigenere("BREAKBREAKBR",textbox5.text)
            textbox4.text = a.encrypt()
        else:
            popup = Popup(title='Podczas szyfrowania wystapil blad!',content=Label(text='Nie podales wartosci w polu tekstu do zaszyfrowania'),size_hint=(None, None), size=(500, 150))
            popup.open()
    def odkoduj_vigenere(textbox3, textbox4, *args):
        if(textbox4.text!=""):
            a=rail(3)
            textbox1.text = a.decrypt()
        else:
            textbox1.text = "Podaj wartosc, do odkodowania"

    def obsluga_vigenere(textbox1,textbox2,checkbox, *args):
        if(checkbox.active):
            zakoduj_rail(textbox1,textbox2)
        else:
            odkoduj_rail(textbox1,textbox2)

    def on_checkbox_active(sender,btn_sender,*args):
        if(sender.active): btn_sender.text = "Dekoduj"
        else: btn_sender.text = "Zakoduj"
    #######################ZADANIE1##################################
    label_zad_1_text = 'Zadanie 1 - Wprawdz napis do zakodowania - Rail Fence'
    label_zad_1 = Label(text=label_zad_1_text, size_hint_y=None, height=50, pos=(0,550))
    root.add_widget(label_zad_1)
    s = Scatter(size_hint=(None, None), pos=(410, 500))
    textbox1 = TextInput(size_hint=(None, None), size=(280, 50),multiline=False)
    s.add_widget(textbox1)
    root.add_widget(s)
    
    s = Scatter(size_hint=(None, None), pos=(85, 500))
    textbox2 = TextInput(size_hint=(None, None), size=(300, 50),multiline=False)
    s.add_widget(textbox2)
    root.add_widget(s)
    
    
    checkbox_zad1 = CheckBox(pos=(660,475), size_hint=(None, None))
    root.add_widget(checkbox_zad1)
    checkbox_zad2 = CheckBox(pos=(660,305), size_hint=(None, None))
    root.add_widget(checkbox_zad2)
    checkbox_zad3 = CheckBox(pos=(660,135), size_hint=(None, None))
    
    btn = Button(text='Zakoduj', size_hint=(None, None),pos=(85, 440), size=(625,40),on_press=partial(obsluga_rail,textbox1,textbox2,checkbox_zad1))
    root.add_widget(btn)
        #######################ZADANIE2##################################
    label_zad_2_text = 'Zadanie 2 - Wprawdz napis do zakodowania - przestrzenie macierzowe'
    label_zad_2 = Label(text=label_zad_2_text, size_hint_y=None, height=50, pos=(0,380))
    root.add_widget(label_zad_2)

    s = Scatter(size_hint=(None, None), pos=(410, 330))
    textbox2 = TextInput(size_hint=(None, None), size=(280, 50),multiline=False)
    s.add_widget(textbox2)
    root.add_widget(s)

    s = Scatter(size_hint=(None, None), pos=(85, 330))
    textbox3 = TextInput(size_hint=(None, None), size=(300, 50),multiline=False)
    s.add_widget(textbox3)
    root.add_widget(s)

    btn2 = Button(text='Zakoduj', size_hint=(None, None),pos=(85, 270), size=(625,40), on_press=partial(obsluga_matrix,textbox2,textbox3,checkbox_zad2))
    root.add_widget(btn2)
        #######################ZADANIE5##################################
    label_zad_3_text = 'Zadanie 3 - Wprawdz napis do zakodowania - szyfrowanie Vigenere\'a'
    label_zad_3 = Label(text=label_zad_3_text, size_hint_y=None, height=50, pos=(0,210))
    root.add_widget(label_zad_3)

    s = Scatter(size_hint=(None, None), pos=(410, 160))
    textbox4 = TextInput(size_hint=(None, None), size=(280, 50),multiline=False)
    s.add_widget(textbox4)
    root.add_widget(s)
    
    s = Scatter(size_hint=(None, None), pos=(85, 160))
    textbox5 = TextInput(size_hint=(None, None), size=(300, 50),multiline=False)
    s.add_widget(textbox5)
    root.add_widget(s)

    btn3 = Button(text='Zakoduj', size_hint=(None, None),pos=(85, 100), size=(625,40), on_press=partial(obsluga_vigenere,textbox4,textbox5,checkbox_zad3))
    root.add_widget(btn3)

    root.add_widget(checkbox_zad3)
    checkbox_zad1.bind(active=partial(on_checkbox_active,checkbox_zad1,btn))
    checkbox_zad2.bind(active=partial(on_checkbox_active,checkbox_zad2,btn2))
    checkbox_zad3.bind(active=partial(on_checkbox_active,checkbox_zad3,btn3))
    
    runTouchApp(root)