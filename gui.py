from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.dialog import MDDialog
from gui_style.styled_components import *
from equation_controls.equation_resolver import *
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class RegisterScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(RegisterScreen(name='register'))


class DemoApp(MDApp):
    dialog = None 

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "A700"
        self.screen = Builder.load_string(KV)
        return self.screen

    def show_alert_dialog(self):
        equation = self.root.get_screen('login')
        equ = str(equation.ids.email.text)
        sol = solve_equation(equ)
        if not self.dialog:
            self.dialog = MDDialog(
                text=sol,
            )
        self.dialog.open()
        

if __name__ == '__main__':
    DemoApp().run()
