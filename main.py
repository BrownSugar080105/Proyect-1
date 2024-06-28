from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

Builder.load_file('main.kv')

class WelcomeScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.change_screen, 3)
    
    def change_screen(self,dt):
        self.manager.current = 'presentation'


class PresentationScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class Neslab(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(PresentationScreen(name='presentation'))
        sm.add_widget(LoginScreen(name='login'))
        return sm

if __name__ == '__main__':
    Neslab().run()