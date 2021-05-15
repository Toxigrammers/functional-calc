from kivymd.app import MDApp
# from kivy.app import AppK
from kivy.core.window import Window
# from kivy.base import stopTouchApp  
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from gui_style.styled_components import *
from equation_controls.equation_resolver import *
from kivy.uix.screenmanager import ScreenManager, Screen
from function_type.fractional_rational import rational_function
from cli import run_cli

Window.size = (500, 500)


class MainScreen(Screen):
    pass


class EquationResolver(Screen):
    pass


class FunctionResolver(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(EquationResolver(name='equation'))
sm.add_widget(FunctionResolver(name='function'))


class DemoApp(MDApp):
    dialog = None
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "A700"
        return self.screen

    def show_alert_dialog(self, *args):
        equation = self.root.get_screen('equation')
        equ = equation.ids.equation.text
        sol = solve_equation(equ)
        if sol:
            if not self.dialog:
                self.dialog = MDDialog(
                    text=str(sol),
                )
            self.dialog.open()
        else: 
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Calcolo impossibile",
                )
            self.dialog.open()


    def goto_cli(self):
        run_cli()
        DemoApp().Stop()

"""     def resolve_functional_rational(self):
            equation = self.root.get_screen('function')

    def get_function_result(self):
        x1 = self.root.get_screen('numerator')
        x2 = self.root.get_screen('denominator')
        rational_function(x1, x2) """


if __name__ == '__main__':
    DemoApp().run()