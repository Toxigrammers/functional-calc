KV = """
ScreenManager:
    MainScreen:
<<<<<<< Updated upstream
    EquazioniSecondo:
    RazionaliFratte:
=======
    EquationResolver:
    FunctionResolver:
>>>>>>> Stashed changes
<MainScreen>:
    name: 'main'
    MDLabel:
        text:"Risolvi funzione"
        font_style:"H3"
        pos_hint:{'center_x':0.5,'center_y':0.94}
    MDRectangleFlatButton:
        text: 'Equazioni di secondo grado'
        pos_hint: {'center_x':0.5,'center_y':0.6}
<<<<<<< Updated upstream
        on_press: root.manager.current = 'equazione'
    MDRectangleFlatButton:
        text: 'Funzioni razionali fratte'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'funzioni'
    
<EquazioniSecondo>:
    name: 'equazione'
=======
        on_press: root.manager.current = 'equation'
    MDRectangleFlatButton:
        text: 'Funzioni razionali fratte'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'function'
    
<EquationResolver>:
    name: 'equation'
>>>>>>> Stashed changes
    
    MDToolbar:
        title:"Inserisci l'equazione"
        pos_hint: {'top':1}

    MDTextField:
        id:equazione
        size_hint_x:None
        width:400
        pos_hint:{'center_x':0.5,'center_y':0.6}
        hint_text:"inserisci l'equazione separata da spazi"
        helper_text: "inserisci l'equazione separata da spazi"

    MDRectangleFlatButton:
        text:"Risolvi"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_release: app.get_equation_result()

    MDIconButton:
        icon: 'arrow-left'
        pos_hint: {'center_x':0.09,'center_y':0.1}
        on_press: root.manager.current = 'main'

<<<<<<< Updated upstream
<RazionaliFratte>:
    name: 'fuzioni'
=======
<FunctionResolver>:
    name: 'function'
>>>>>>> Stashed changes
    MDToolbar:
        title:"Inserisci la funzione razionale fratta"
        pos_hint:{'top':1}
    MDTextField:
        name:"numeratore"
        size_hint_x:None
        width:400
        pos_hint:{'center_x':0.5,'center_y':0.6}
        hint_text:"Numeratore"
        helper_text: "Numeratore"

    MDTextField:
        name:"denominatore"
        size_hint_x:None
        width:400
        pos_hint:{'center_x':0.5,'center_y':0.5}
        hint_text:"Denominatore"
        helper_text: "Denominatore"

    MDRectangleFlatButton:
        text:"Risolvi"
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_release: app.resolve_second_grade_equation()

    MDIconButton:
        icon: 'arrow-left'
        pos_hint: {'center_x':0.09,'center_y':0.1}
        on_press: root.manager.current = 'main'   
"""