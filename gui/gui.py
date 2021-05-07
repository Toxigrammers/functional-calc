from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

KV = """
ScreenManager:
    MainScreen:
    LoginScreen:
    RegisterScreen:
<MainScreen>:
    name: 'main'
    MDLabel:
        text:"Risolvi funzione"
        font_style:"H3"
        pos_hint:{'center_x':0.5,'center_y':0.94}
    MDRectangleFlatButton:
        text: 'Equazioni di secondo grado'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'login'
    MDRectangleFlatButton:
        text: 'Funzioni razionali fratte'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'register'
    
<LoginScreen>:
    name: 'login'
    
    MDToolbar:
        title:"Inserisci l'equazione"
        pos_hint: {'top':1}

    MDTextField:
        id:email
        size_hint_x:None
        width:400
        pos_hint:{'center_x':0.5,'center_y':0.6}
        hint_text:"inserisci l'equazione separata da spazi"
        helper_text: "inserisci l'equazione separata da spazi"

    MDRectangleFlatButton:
        text:"Risolvi"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_release: app.login()

    MDIconButton:
        icon: 'arrow-left'
        pos_hint: {'center_x':0.09,'center_y':0.1}
        on_press: root.manager.current = 'main'

<RegisterScreen>:
    name: 'register'
    MDToolbar:
        title:"Inserisci la funzione razionale fratta"
        pos_hint:{'top':1}
    MDTextField:
        name:"email"
        size_hint_x:None
        width:400
        pos_hint:{'center_x':0.5,'center_y':0.6}
        hint_text:"Numeratore"
        helper_text: "Numeratore"

    MDTextField:
        name:"password"
        size_hint_x:None
        width:400
        pos_hint:{'center_x':0.5,'center_y':0.5}
        hint_text:"Denominatore"
        helper_text: "Denominatore"

    MDRectangleFlatButton:
        text:"Risolvi"
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_release: app.login()

    MDIconButton:
        icon: 'arrow-left'
        pos_hint: {'center_x':0.09,'center_y':0.1}
        on_press: root.manager.current = 'main'
        
"""


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
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "A700"
        self.screen = Builder.load_string(KV)
        return self.screen

    def login(self):
        login_screen = self.root.get_screen('login')
        print(login_screen.ids.email.text)

    
if __name__ == '__main__':
    DemoApp().run()
