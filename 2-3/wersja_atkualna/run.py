from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.app import App
from cyphers.rail import rail
from cyphers.matrix_translation_a import matrix_translation_a
from cyphers.matrix_translation_b import matrix_translation_b
from cyphers.matrix_translation_c import matrix_translation_c
from cyphers.caesar import caesar
from cyphers.vigenere import vigenere

class Cypher:
    root = None
    cypher = None
    encrypt_button = None
    decrypt_button = None
    encrypted = None
    decrypted = None
    key = None
    def __init__(self, title, cypher, key = None, no_decrypt = False):
        self.root = BoxLayout(orientation='vertical')
        self.cypher = cypher
        inputs = BoxLayout(orientation='horizontal')
        buttons = BoxLayout(orientation='horizontal')
        titlebar = BoxLayout(orientation='horizontal')
        label = Label(text = title,bold = True, font_size = 25, size_hint_x = 0.5)

        self.encrypted = TextInput(multiline = False)
        self.decrypted = TextInput(multiline = False)
        self.encrypt_button = Button(text='Encrypt')
        self.encrypt_button.bind(on_press=lambda x: self.encrypt())
        buttons.add_widget(self.encrypt_button)

        if not no_decrypt:
            self.decrypt_button = Button(text='Decrypt')
            buttons.add_widget(self.decrypt_button)
            self.decrypt_button.bind(on_press=lambda x: self.decrypt())
        
        inputs.add_widget(self.decrypted)
        inputs.add_widget(self.encrypted)

        titlebar.add_widget(label)
        if key is None:
            self.key = TextInput(multiline = False, size_hint_x = 0.5)
        elif type(key) == list:
            self.key = Spinner(
            text=key[0],
            values=tuple(key),
            size_hint_x = 0.5)
        else:
            self.key = Button(text=key,size_hint_x = 0.5)
        
        titlebar.add_widget(self.key)

        self.root.add_widget(titlebar)
        self.root.add_widget(inputs)
        self.root.add_widget(buttons)

    def encrypt(self):
        c = self.cypher(self.key.text)
        self.encrypted.text = c.encrypt(self.decrypted.text)
        self.decrypted.text = ""
    def decrypt(self):
        c = self.cypher(self.key.text)
        self.decrypted.text = c.decrypt(self.encrypted.text)
        self.encrypted.text = ""

class DemoApp(App):
    sc = None
    def build(self):
        self.sc = GridLayout(cols=1, row_force_default=True, row_default_height=90, spacing = 15)
        r = Cypher("Rail Fence", rail, list("234567"))
        m1 = Cypher("Matrix Translation A", matrix_translation_a, "3-4-1-5-2")
        m2 = Cypher("Matrix Translation B", matrix_translation_b)
        m3 = Cypher("Matrix Translation C", matrix_translation_c, no_decrypt=True)
        c = Cypher("Caesar Cypher", caesar, "21,13,31,51,15,25,52,14,41".split(","))
        v = Cypher("Vigenere Cypher", vigenere, no_decrypt=True)
        
        self.sc.add_widget(r.root)
        self.sc.add_widget(m1.root)
        self.sc.add_widget(m2.root)
        self.sc.add_widget(m3.root)
        self.sc.add_widget(c.root)
        self.sc.add_widget(v.root)
        return self.sc

if __name__ == '__main__':
    x = DemoApp()
    x.run()