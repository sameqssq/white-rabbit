default puntosmax = 6
default actions = puntosmax
default mental = 100

default objetos_clickeados = set()

screen loopinfo():
    modal False
    style_prefix "infoloop"

    viewport:
        xalign 0.5
        ypos 10
        image "images/informacion.png":
            alpha 0.9

        hbox:
            spacing 100
            ypos 20
            xpos 300
            vbox:
                text "{b}Loop Actual:{/b}"
                text "{b}[loop]{/b}":
                    size 35
                    xalign 0.5
            vbox:
                spacing 10
                text "{b}PUNTOS DE INVESTIGACIÓN: [actions]{/b}"
                text "{b}ESTABILIDAD MENTAL: [mental]{/b}"
            vbox:
                spacing 10
                text "{b}Tiempo:{/b}"
                text "{b}342 horas antes del evento{/b}"
        
            vbox:
                spacing 10
                text "{b}Objeto:{/b}"
                $ tooltip = GetTooltip("click_screen")
                if tooltip:
                    text "{b}[tooltip]{/b}"

        #textbutton "VOLVER AL\nLABORATORIO":
        #    action Jump("laboratorio")
        #    xpos 1700
        #    ypos 20

style infoloop_text:
    size 20

style infoloop_button_text:
    size 20
    idle_color "#bebebe"
    hover_color "#00ffff"
    text_align 0.5


screen systemnotice():
    modal True
    style_prefix "systemnotice"

    frame:
        xsize 720
        xalign 0.5
        yalign 0.5
        background Frame("images/frame3.png", 20, 20, 20, 20)
        vbox:
            spacing 30
            xalign 0.5
            yalign 0.5
            xmaximum 650
            label "SISTEMA":
                xalign 0.5
            text "Te quedan [actions] acciones":
                color "#fff"
                xalign 0.5
            textbutton "CERRAR":
                xalign 0.5
                action Hide("systemnotice"), Return()
            text ""


screen systemnotice2(message):
    modal True
    style_prefix "systemnotice"

    frame:
        xsize 720
        xalign 0.5
        yalign 0.5
        background Frame("images/frame3.png", 20, 20, 20, 20)
        vbox:
            spacing 30
            xalign 0.5
            yalign 0.5
            xmaximum 650
            label "SISTEMA":
                xalign 0.5
            text "[message]":
                color "#fff"
                xalign 0.5
                justify True
            textbutton "CERRAR":
                xalign 0.5
                action Return()
            text ""

screen systemnotice3(message):
    modal True
    style_prefix "systemnotice"

    frame:
        xsize 720
        xalign 0.5
        yalign 0.5
        background Frame("images/frame3.png", 20, 20, 20, 20)
        vbox:
            spacing 30
            xalign 0.5
            yalign 0.5
            xmaximum 650
            label "SISTEMA":
                xalign 0.5
            text "[message]":
                color "#fff"
                xalign 0.5
                justify True
            hbox:
                spacing 50
                textbutton "GUARDAR":
                    xalign 0.5
                    action ShowMenu("save")
                textbutton "SALIR":
                    xalign 0.5
                    action Quit(confirm=False)
            text ""

style systemnotice_label_text:
    font "gui/fonts/RockSalt-Regular.ttf"
    color "#00ffff"
    size 30
    outlines [(absolute(1), "#000000", absolute(1), absolute(1))]

style systemnotice_button_text:
    idle_color "#00ffff"
    hover_color "#000"
    size 20

style systemnotice_text:
    outlines [(absolute(1), "#000000", absolute(0), absolute(0))]
    color "#fff"   


screen mision():
    modal True
    style_prefix "mision"

    image "images/cuadromision.png":
        xpos 500
        ypos 50

    viewport:
        xysize(900, 880)
        xpos 525
        ypos 75
        mousewheel True
        scrollbars "vertical"

        vbox:
            spacing 30
            xalign 0.5
            yalign 0.5
            xmaximum 800
            
            label "SISTEMA":
                xalign 0.5
                ypos 10
            
            vbox:
                xpos 50
                ypos 40
                spacing 30
                text "{b}Misión: Atentado en Estación Subterránea 12/25{/b}"
                vbox:
                    xpos 50
                    text "Fecha: 25 de diciembre 2063"
                    text "Hora: 15:10"
                    text "Lugar: Rieles de ingreso a Estación Subterránea Plaza de la Ciudadanía."
                text "Evento: Explosión en andén provocada por una bomba única depositada por un agente de la organización terrorista {i}Corazón de Ángel{/i} causando la muerte inmediata de {b}1.360 personas{/b} por el derrumbe de la estación y la colisión de los trenes, además de otros mil quinientos heridos encontrados en los alrededores."
                text "Tras el atentado, fue posible desbaratar una de las sedes de reunión de la organización y dar captura al agente involucrado y a tres colaboradores, actualmente procesados y bajo condena en la unidad penitenciaria de alta seguridad MT25."
                text "Según el análisis efectuado a los registros encontrados en la sede y los interrogatorios realizados al agente y colaboradores, los motivos del atentado respondían a razones de naturaleza sectaria y religiosa, impulsados por un líder de rol mesiánico, del cual no se han logrado encontrar mayores antecedentes."
                text "{b}Objetivos:{/b}"
                text "Recolectar información de agentes involucrados con la organización terrorista, lugares de encuentro, fechas de reunión y cualquier detalle relevante para desarticular sus operaciones y/o dar con el paradero e identidad de su líder."
                text "Loops de Acoplamiento:\n5 marcadores temporales establecidos."

            button:
                xalign 0.5
                ypos 70
                idle_background im.FactorScale("images/rabbit_idle.png", 0.2)
                hover_background im.FactorScale("images/rabbit_hover.png", 0.2)
                text "ACEPTAR  MISIÓN":
                    xpos 60
                    yoffset -5
                    font "gui/fonts/RockSalt-Regular.ttf"
                    idle_color "#000000"
                    hover_color "#00fff2"
                    outlines [(absolute(0), "#000000", absolute(0), absolute(0))]
                    size 25
                    text_align 0.5
                action Return()
            label ""
            

style mision_label_text:
    font "gui/fonts/RockSalt-Regular.ttf"
    color "#00ffff"
    size 30
    outlines [(absolute(1), "#000000", absolute(1), absolute(1))]

style mision_text:
    justify True
    outlines [(absolute(1), "#000000", absolute(0), absolute(0))]

style mision_button_text:
    idle_color "#00ffff"
    hover_color "#000"
    size 30


screen mision_resumen():
    modal True
    style_prefix "mision"

    image "images/cuadromision.png":
        xpos 500
        ypos 50

    viewport:
        xysize(900, 880)
        xpos 525
        ypos 100
        mousewheel True
        scrollbars "vertical"

        vbox:
            spacing 30
            xalign 0.5
            yalign 0.5
            xmaximum 800
            
            label "SISTEMA":
                xalign 0.5
                ypos 10
            
            vbox:
                xpos 50
                ypos 40
                spacing 30
                text "{b}Misión: Atentado en Estación Subterránea 12/25{/b}"
                vbox:
                    xpos 50
                    text "Fecha: 25 de diciembre 2063"
                    text "Hora: 15:10"
                    text "Lugar: Rieles de ingreso a Estación Subterránea Plaza de la Ciudadanía."
                if cafe == True:
                    text "Evento: Explosión en andén provocada por una bomba única depositada por un agente de la organización terrorista {i}Corazón de Ángel{/i} causando la muerte inmediata de {b}1.361{/b} personas por el derrumbe de la estación y la colisión de los trenes, además de otros mil quinientos heridos encontrados en los alrededores."
                else:
                    text "Evento: Explosión en andén provocada por una bomba única depositada por un agente de la organización terrorista {i}Corazón de Ángel{/i} causando la muerte inmediata de {b}1.360{/b} personas por el derrumbe de la estación y la colisión de los trenes, además de otros mil quinientos heridos encontrados en los alrededores."                    
            button:
                xalign 0.5
                ypos 70
                idle_background im.FactorScale("images/rabbit_idle.png", 0.2)
                hover_background im.FactorScale("images/rabbit_hover.png", 0.2)
                text "CERRAR":
                    xpos 60
                    yoffset -5
                    font "gui/fonts/RockSalt-Regular.ttf"
                    idle_color "#000000"
                    hover_color "#00fff2"
                    outlines [(absolute(0), "#000000", absolute(0), absolute(0))]
                    size 25
                    text_align 0.5
                action Return()
            label ""

screen message_modal():
    modal True
    zorder 100
    style_prefix "message_modal"

    # Fondo para el modal
    frame:
        xsize 850
        xalign 0.5
        yalign 0.5
        background "#050400"
        
        vbox:
            spacing 15
            ypos 20
            xpos 30
            xmaximum 800
            text "¡Felicidades!" size 32 color "#ffffff"
            text "Has aprobado todos los cursos básicos de operatividad del Programa de Biohacking White Rabbit.\n\nSabemos que no ha sido fácil, solo 5 reclutas han logrado completar la totalidad del programa y de ellos, eres quien ha superado los desafíos con la máxima distinción. ¡Nos has sorprendido muchísimo!\n\nMientras esperas, tenemos algo de información adicional que puedes revisar."

            # Botón de cerrar
            textbutton "Sobre {i}White Rabbit{/i}" action SetVariable("wr", True) , Hide("message_modal"), Show("message2_modal")
            textbutton "Especialización" action SetVariable("esp", True) , Hide("message_modal"), Show("message3_modal")
            #textbutton "Cerrar" action Jump("volver")
            text ""

style message_modal_text:
    justify True

screen message2_modal():
    modal True
    zorder 100
    style_prefix "message_modal"

    # Fondo para el modal
    frame:
        xsize 850
        xalign 0.5
        yalign 0.5
        background"#050400"

        viewport:
            scrollbars "vertical"
            mousewheel True
            ysize 700

            vbox:
                spacing 15
                ypos 20
                xpos 30
                xmaximum 800
                if wr == True:
                    label "WHITE RABBIT"
                    text "White Rabbit es un programa de investigación especializado en psicopatología y cognición que actualmente lleva 16 años en desarrollo. ¡Sí, estamos en la adolescencia de nuestra organización!\n\nComo sabrás, operamos como una rama oficial del Ministerio de Seguridad Nacional, para el tratamiento de Casos y Eventualidades de Máxima Prioridad, definidos en el Artículo n°25 párrafo 2 del Protocolo de Emergencias Extraordinarias y Catastróficas.\n\nWhite Rabbit es un programa pionero, único en su tecnología y disciplina, que actualmente cuenta con siete sedes de investigación y reporte, y una sede central de experimentación, donde nos encontramos en este momento.\n\nFundado por Gretta Hamilton y su amplia trayectoria en la investigación de marcadores temporales genéticos; y Roberta Machado por sus constantes y fructíferos descubrimientos en el Acoplamiento y Desplazamiento sincrónico de la consciencia."            
                if esp == False:
                    textbutton "Especialización" action Hide("message2_modal"), SetVariable("esp", True), Show("message3_modal")
                textbutton "Cerrar" action Hide("message2_modal"), Hide("message3_modal"), Jump("volver")
            
screen message3_modal():
    modal True
    zorder 100
    style_prefix "message_modal"

    # Fondo para el modal
    frame:
        xsize 850
        xalign 0.5
        yalign 0.5
        background"#050400"

        viewport:
            scrollbars "vertical"
            mousewheel True
            ysize 700

            vbox:
                spacing 15
                ypos 20
                xpos 30
                xmaximum 800
                if esp == True:
                    label "ESPECIALIZACIÓN"
                    text "Por haber completado todos los cursos básicos del programa, tenemos una noticia muy importante para ti.\n\nSegún los reportes de tus evaluadores y el progreso registrado en nuestra base de datos, cuentas con las condiciones necesarias para cursar el programa de Biohacker Catalysta.\n\nEste programa te dará acceso a nuevas funciones de sincronización, como la modificación en la velocidad del tiempo compartido, salto de huésped dentro de un mismo marcador temporal y la posibilidad de generar semilleros conductuales en los huéspedes intervenidos.\n\nPara cursar este programa necesitas completar 500 horas de servicio efectivo, que serán contabilizadas de acuerdo a las misiones que puedas completar. Dadas tus condiciones, no te será muy difícil conseguirlo.\n\n¡Estaremos esperando tu solicitud!"
                if wr == False:
                    textbutton "Sobre {i}White Rabbit{/i}" action Hide("message2_modal"), SetVariable("wr", True), Show("message2_modal")
                textbutton "Cerrar" action Hide("message3_modal"), Hide("message2_modal"), Jump("volver")