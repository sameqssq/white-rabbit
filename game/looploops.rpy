screen click_screen():
    modal True
    add "cafe.png"
    
    # Definir áreas cliqueables
    imagebutton:
        idle "images/celular_idle.png"
        hover "images/celular_hover.png"
        action Jump("celular")
        tooltip "CELULAR"
        xpos 1600
        ypos 600

    imagebutton:
        idle "images/diario_idle.png"
        hover "images/diario_hover.png"
        action Jump("diario")
        tooltip "DIARIO"
        xpos 850
        ypos 400

    imagebutton:
        idle "images/libreta_idle.png"
        hover "images/libreta_hover.png"
        action Jump("libreta")
        tooltip "LIBRETA"
        xpos 1650
        ypos 730

    imagebutton:
        idle "images/bolso_idle.png"
        hover "images/bolso_hover.png"
        action Jump("bolso")
        tooltip "BOLSO"
        xpos 1400
        ypos 828

    imagebutton:
        idle "images/colgante_idle.png"
        hover "images/colgante_hover.png"
        action Jump("colgante")
        tooltip "COLGANTE"
        xpos 1200
        ypos 480

    imagebutton:
        idle "images/salida_idle.png"
        hover "images/salida_hover.png"
        action Jump("salida")
        tooltip "SALIDA"
        xpos 620
        ypos 165
    
    #Navegacion
    use loopinfo