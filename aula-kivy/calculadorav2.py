from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class FormCalculadora(App):
    def build(self):
        box1 = BoxLayout(orientation='horizontal')
        lblNumero1 = Label(text="Digite o primeiro número: ")
        txtNumero1 = TextInput()
        box1.add_widget(lblNumero1)
        box1.add_widget(txtNumero1)
        
        box2 = BoxLayout(orientation='horizontal')
        lblNumero2 = Label(text="Digite o segundo número: ")
        txtNumero2 = TextInput()
        box2.add_widget(lblNumero2)
        box2.add_widget(txtNumero2)

        boxPrincipal = BoxLayout(orientation='vertical')
        btnSomar = Button(text="somar")
        boxPrincipal.add_widget(box1)
        boxPrincipal.add_widget(box2)
        boxPrincipal.add_widget(btnSomar)
        return boxPrincipal

objCalculadora = FormCalculadora()
objCalculadora.run()