import kivy

kivy.required("1.9.1")

from kivy.app import App

from kivy.uix.vkeyboard import VKeyboard

class test(VKeyboard):
    player = VKeyboard()

class VKeyboardApp(App):
    def build(self):
        return test()

if __name__ == '__main__':
    VKeyboardApp().run()