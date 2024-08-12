from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class CalculadoraSoma(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        lblNumero1 = Label(text="Digite o 1º Número:")
        txtNumero1 = TextInput()
        lblNumero2 = Label(text="Digite o 2º Número:")
        txtNumero2 = TextInput()
        btnSomar = Button(text="somar")
        box.add_widget(lblNumero1)
        box.add_widget(txtNumero1)
        box.add_widget(lblNumero2)
        box.add_widget(txtNumero2)
        box.add_widget(btnSomar)
        return box


obj_calculadora_soma = CalculadoraSoma()
obj_calculadora_soma.run()