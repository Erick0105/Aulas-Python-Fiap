from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class FormDados(App):
    def build(self):
        boxNome = BoxLayout(orientation='horizontal')
        lblNome = Label(text="Nome: ")
        txtNome = TextInput()
        boxNome.add_widget(lblNome)
        boxNome.add_widget(txtNome)
        
        boxTelefone = BoxLayout(orientation='horizontal')
        lblTelefone = Label(text="Telefone: ")
        txtTelefone = TextInput()
        boxTelefone.add_widget(lblTelefone)
        boxTelefone.add_widget(txtTelefone)
        
        boxEmail = BoxLayout(orientation='horizontal')
        lblEmail = Label(text="Email: ")
        txtEmail = TextInput()
        boxEmail.add_widget(lblEmail)
        boxEmail.add_widget(txtEmail)

        boxButtons = BoxLayout(orientation='horizontal')
        btnSalvar = Button(text="Salvar")
        btnPesq = Button(text='Pesquisar')
        boxButtons.add_widget(btnSalvar)
        boxButtons.add_widget(btnPesq)

        boxPrincipal = BoxLayout(orientation='vertical')
        boxPrincipal.add_widget(boxNome)
        boxPrincipal.add_widget(boxTelefone)
        boxPrincipal.add_widget(boxEmail)
        boxPrincipal.add_widget(boxButtons)

        return boxPrincipal

objForm = FormDados()
objForm.run()