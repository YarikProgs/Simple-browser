from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from google import google

_ = []


class InptutScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)

        vl.add_widget(Label(text='Google', font_size='100sp'))
        vl.add_widget(Label(text='Type your request to\nthis field, and Google!', font_size='20sp'))

        inp = TextInput()
        inp.font_size = '70sp'
        btn = Button(text='Google it!')
        btn.on_press = lambda: self.press(inp.text)
        btn.size_hint = (1, .4)
        vl.add_widget(inp)
        vl.add_widget(btn)
        self.add_widget(vl)

    def press(self, text):
        self.manager.transition.direction = 'left'
        scr2.update_labels(text)
        self.manager.current = 'second'


class OutputScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.vl = BoxLayout(orientation='vertical', padding=8, spacing=8)

    def update_labels(self, text):
        _ = google(text)
        for request in _:
            self.vl.add_widget(Label(text=request))
        self.add_widget(self.vl)


scr1 = InptutScreen(name='first')
scr2 = OutputScreen(name='second')


class MainApp(App):
    def build(self):
        manager = ScreenManager()

        manager.add_widget(scr1)
        manager.add_widget(scr2)

        return manager


if __name__ == '__main__':
    MainApp().run()
