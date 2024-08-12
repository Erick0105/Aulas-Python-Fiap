from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button


class HelloWorld(App):
    def build(self):
        return Button(text="botãozinho",
                color="green",
                font_size="20px")
    


if __name__ == "__main__":
    HelloWorld().run()  