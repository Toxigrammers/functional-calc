from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.dialog import MDDialog
from gui_style.styled_components import *
from equation_controls.equation_resolver import *
from kivy.uix.screenmanager import ScreenManager, Screen
from function_type.fractional_rational import rational_function

class MainScreen(Screen):
    pass


class EquazioniSecondo(Screen):
    pass


class RazionaliFratte(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(EquazioniSecondo(name='login'))
sm.add_widget(RazionaliFratte(name='register'))


class DemoApp(MDApp):
    dialog = None 

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "A700"
        self.screen = Builder.load_string(KV)
        return self.screen

    def get_equation_result(self):
        equation = self.root.get_screen('login')
        equ = str(equazione.ids.equazione.text)
        sol = solve_equation(equ)
        if not self.dialog:
            self.dialog = MDDialog(
                text=str(sol),
            )
        self.dialog.open()
        
    def get_function_result(self):
        x1 = self.root.get_screen('numeratore')
        x2 = self.root.get_screen('denominator')
        rational_function(x1, x2)

        
if __name__ == '__main__':
    DemoApp().run()
