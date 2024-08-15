﻿# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

#define e = Character("Eileen")

define p = Character("Aspirante R01", color = "#ffffff")
define c = Character("Litha", color = "#fd96f5")
define c2 = Character("Rich", color = "#16571f")
define v = Character("Voz", color = "#a5c943")
define b = Character("Petirrojo", color = "#c72d22")
define s = Character("Sistema", color="#00f7ff")
define m = Character("Persona Misteriosa", color="#7d8db9")

default loop = None
default wr = False
default esp = False
default cafe = False

# El juego comienza aquí.

label start:

    show text "{i}Cuídate del conejo blanco."
    scene bgblack

    play music "audio/Shimmer_Deep_Cinematic_Sting.ogg" volume 0.3

    call screen message_modal

label volver:
    show prota_inicial at center
    with dissolve
    p "Creo que ya leí todo lo que necesitaba"

    s "Nuestros registros han encontrado la siguiente misión para ti. Te recomendamos revisar el informe asociado al evento y los puntos claves que ya han sido registrados por nuestros investigadores que guiarán tu interacción durante el Acomplamiento."

    #return
    jump mision 

label mision:
    hide prota_inicial
    with Dissolve(0.2)

    call screen mision
    with dissolve
    stop music fadeout 0.5

    scene laboratorio
    with Fade(0.5, 1.0, 0.5, color="#000")

    play music "audio/Drone_Cave_Wind_Deep_Dark.ogg" volume 0.3 fadein 0.5

    show cientifico at left
    show cientifica at right
    with Dissolve(0.2)

    c2 "¡Ey! ¡Ey! ¿Está todo bien por ahí?"

    hide cientifico
    hide cientifica
    with Dissolve(0.2)

    show prota_inicial at center
    with Dissolve(0.2)

    p "No puedo ver nada, ¿es normal?"

    hide prota_inicial

    show cientifico at left
    show cientifica at right
    with Dissolve(0.2)

    c "Descuida, tus sentidos permanecerán adormecidos hasta que te conectemos al huésped. Estaba revisando tus antecedentes, ¡tienes mucho potencial!"
    c "Hace tiempo no contábamos con un aspirante de tu nivel. Mi nombre es Litha, me encargaré de llevar el registro de tu nivel de consciencia y el mapeo de los marcadores genéticos temporales con los que contamos."

    hide cientifico
    hide cientifica
    with Dissolve(0.2)

    show prota_inicial at center
    with Dissolve(0.2)
    p "Ah, un gusto Litha."

    hide prota_inicial

    show cientifico at left
    show cientifica at right
    with Dissolve(0.2)
    c "Cualquier duda que tengas, háznosla saber. Que no te gane la timidez."

    hide cientifico
    hide cientifica
    with Dissolve(0.2)

    show prota_inicial at center
    with Dissolve(0.2)
    p "Gracias. Lo tendré en cuenta."

    hide prota_inicial

    show cientifico at left
    show cientifica at right
    with Dissolve(0.2)
    c2 "Bien, supongo que debo presentarme también. Soy Rich, lidero la investigación y estaré comandando la trayectoria de tu viaje."
    c2 "Ahora mismo estamos en la estación de lanzamiento, espero que la butaca en que te encuentras se sienta cómoda, pues los viajes pueden tardar un poco en desarrollarse."

    hide cientifico
    hide cientifica
    with Dissolve(0.2)

    show prota_inicial at center
    with Dissolve(0.2)
    p "Oh, sí, es bastante cómoda, jeje. Gracias, Rich."

    hide prota_inicial

    show cientifico at left
    show cientifica at right
    with Dissolve(0.2)
    c2 "El casco que llevas puesto, además de permitir la sincronización, lo hemos adaptado para integrar algunas aplicaciones de apoyo. También nos permitirá mantener un canal de comunicación estable durante el viaje."

    hide cientifico
    hide cientifica
    with Dissolve(0.2)

    show prota_inicial at center
    with Dissolve(0.2)
    p "Entiendo, eso será muy útil."

    hide prota_inicial

    show cientifico at left
    show cientifica at right
    with Dissolve(0.2)
    c2 "Prueba revisar todo antes de que comencemos"

    hide cientifico
    hide cientifica
    with Dissolve(0.2)

    show prota_inicial at center
    with Dissolve(0.2)
    p "Sí."

    p "(Vaya… ya estamos en esto. No esperaba comenzar tan pronto, pero todo debería ir bien. Admito que al principio me inscribí solo por curiosidad, pero ¿quién no querría impedir que eventos tan horribles se lleven a cabo?)"
    p "(Sé que esta misión es importante, hasta siento la adrenalina de lo que vendrá. Ya no será solo una simulación, sino un salto real, en el tiempo. Tengo que concentrarme. Sé que lo puedo hacer.)"
    p "(Esta presión fría sobre mis ojos debe ser por el casco. Veamos, veo un número arriba, ¿es un cronómetro? ¡Ah, también tengo un contador de investigaciones disponibles! ¿Para qué servirá?)"

    hide prota_inicial

    s "Durante cada loop podrás investigar ciertos lugares, personajes y objetos, pero ten en cuenta que cada una de estas acciones gastará 1 punto de investigación."
    s "Cuando hayas ocupado todos los puntos disponibles y tu tiempo de viaje se haya agotado, regresarás al laboratorio en el presente."
    show cientifico at left
    show cientifica at right
    with Dissolve(0.2)

    c2 "Aspirante, ¿recuerdas tu misión?"

    label opciones2:
        menu:
            "Sí, recabar información del evento.":
                call informacion from _call_informacion
            "Sí, impedir que el evento ocurra.":
                call impedir from _call_impedir

label informacion:
    c "Recuerda que solo tendrás un instante para comprender la situación y adaptarte a la participación del huésped en ella. Te enviaremos 342 horas antes de que el evento ocurra. Cualquier detalle será de vital importancia."
    c "La duración del viaje fluctúa en cada loop, pero creemos que está relacionado a la cantidad de información que hayas alcanzado a recabar. Así, mientras indagues en más puntos de investigación, antes regresarás."
    jump empieza_mision

label impedir:
    c "Recuerda que te enviaremos 342 horas antes de que el evento ocurra. Cualquier acción que cambie el curso temporal podría propiciar o impedir que el evento ocurra. Ten mucho cuidado, solo tendrás un instante para comprender la situación y adaptarte a la participación del huésped en ella."
    c "La duración del viaje fluctúa en cada loop, pero creemos que está relacionado a la cantidad de información que hayas alcanzado a recabar. Así, mientras indagues en más puntos de investigación, antes regresarás."
    jump empieza_mision

label empieza_mision:
    hide cientifico
    hide cientifica
    with Dissolve(0.2)

    show prota_inicial at center
    with Dissolve(0.2)      
    p "Entiendo."

    hide prota_inicial

    show cientifico at left
    show cientifica at right
    with Dissolve(0.2)   
    c2 "Bien, comenzaremos. Marcadores genéticos alineados, esperando secuencia de sincronización."
    c "Sincronización en progreso, restableciendo estímulos sensoriales."
    c2 "¡10 segundos para el inicio del bucle!"
    c " 8… 7… 6…"
    c2 "¡5 segundos!"
    
    stop music fadeout 0.5
    c "3… 2.. 1! Conexión exitosa!"

    play music "audio/Static_Hum_Tonal_Machine.ogg" volume 0.3

    $ loop = 1

    scene bgwhite
    with ImageDissolve("images/transition.png", 2.0, 128, reverse=True)

    p "¿Qué… qué es esto? Mi cabeza… Todo me está dando vueltas."

    show prota_inicial:
        matrixcolor BrightnessMatrix(value=0.5)
        blur 2.5
        center
    with Dissolve(1.0)

    show prota_trance:
        matrixcolor BrightnessMatrix(value=0.5)
        blur 2.5
        center
    with Dissolve(1.5)

    hide prota_inicial
    with dissolve
    
    p "¡Es como si bajara en un ascensor! ¿Rich? ¿Litha? Alguien…"

    p "¡Aaaah…!"

label cafe:

    scene cafe:
        blur 5.0
        matrixcolor BrightnessMatrix(value=0.3)
    with ImageDissolve("images/transition.png", 2.0, 128, reverse=True)

    stop music fadeout 0.5

    p "Aaah… Ah, no, ya… creo que ya se detuvo… Eso fue intenso. Hay luz, ya puedo ver…"
    p "Bien, ¿dónde estoy? Parece… ¿una cafetería?"

    scene cafe
    with Dissolve(0.7)

    p "¡Qué bien se siente! El aroma del pan me hace rugir el estómago, ¿debería pedir algo? Hay tanta gente a mi alrededor, ¿dónde está la fila? No, espera. Necesito encontrar información, para eso vine."

    show prota_serio at center 
    with dissolve

    p "Vaya, ¿así me veo ahora?"

    show prota_inicial:
        xalign 0.7
        yalign 1.0
        matrixcolor OpacityMatrix(value=0.7)
    with dissolve

    p "No, en realidad este es el huésped con el que me he acoplado. Es bastante joven, ¿cómo se involucró en algo así?"
    p "¿Podré acceder a sus recuerdos? Mmm… No, no tengo acceso a sus pensamientos…"
    p "Pero, siento algo. Una urgencia."
    p "¡Eso es! Puedo percibir lo que siente y de algún modo, las decisiones que tomará. Qué extraño, se siente como ir de copiloto en el vehículo de alguien más."
    p "Veamos qué llevo..."     

    hide prota_serio
    hide prota_inicial
    with Dissolve(0.2)

    call screen systemnotice2("Actualmente posees 6 puntos de investigación.\n\nCada vez que selecciones un objeto, interactúes con un personaje o elemento del espacio, gastarás 1 punto de investigación.\n\nCuando tus puntos de investigación lleguen a 0, regresarás al laboratorio.")

label click:
    if actions > 0:

        #stop music fadeout 0.5
        play music "audio/Bowed_Metal_Tonal_Mystical_Eerie.ogg" volume 0.5 fadein 0.5

        call screen click_screen

    else:
        stop music fadeout 0.5
        jump sin_acciones

    return
    
label celular:
    if "celular" not in objetos_clickeados:
        #Aquí checkea si el objeto está dentro de la lista

        show celular: 
            yalign 0.7
            xalign 0.5
            zoom 1.8
        with Dissolve(0.2)
        p "¡Vaya, recuerdo este modelo! Es de una línea muy económica, pero de grandes prestaciones. Da unas fotos preciosas. ¿Tendrá alguna guardada?"
        p "Ah, me pide desbloquear la pantalla."
        p "Marca las 11:15 am. Veamos, ¿qué patrón usará? Mmm… No, fallé."

        "Llamada entrante: Número desconocido..."

        p "(¿Debería contestar?...)"

        hide celular
        with Dissolve(0.2)

        show prota_serio at center
        with Dissolve(0.2)

        p "¿Aló?"
        v "¿Dónde estás?"
        p "¿Quién habla?"
        v "¿Cómo que quién? ¡Ey, me debes dinero! No me he olvidado de tu cara, más te vale zanjar esto luego, ¿estás escuchando?"

        hide prota_serio
        show prota_confusion at center
        with Dissolve(0.2)

        p "Sí… sí, te escucho."
        v "Bien, porque pasaré por ti hoy en la noche. ¡Más te vale estar ahí! Adiós."

        hide prota_confusion
        with Dissolve(0.2)

        p "Cortó… ¿Quién era esta persona? ¿Estará vinculada a la organización?"
        $ actions -= 1
        $ objetos_clickeados.add("celular")
        #Si ve que el objeto no está en la lista lo guarda ahí
        
        call screen systemnotice

    else:
        "Ya revisaste este objeto."
    jump click

label diario:
    if "diario" not in objetos_clickeados:

        show diario:
            yalign 0.7
            xalign 0.5
            zoom 2.0
        with Dissolve(0.2)
        "{i}10 de diciembre de 2063{/i}"
        "{i}¡Reportan nuevos avistamientos de estrellas fugaces en el Cono Sur!{/i}"
        "{i}Durante esta semana una hermosa lluvia de estrellas podrá ser captada desde los cielos privilegiados del hemisferio sur.{/i}"
        "{i}Se espera que la trayectoria de esta congregación de asteroides visite la costa del Pacífico entre las 03:50 de la madrugada del día 12 de diciembre, abarcando aproximadamente dos horas de duración.{/i}"
        "{i}Para los amantes de la astronomía…{/i}"
    
        hide diario
        with Dissolve(0.2)

        show prota_serio at center
        with Dissolve(0.2)
        p "..."
        p "Bueno, con esto puedo confirmar que estamos en el año correcto, dos semanas y poco más antes del evento. Y lo que siento en este momento… No se acerca en lo más mínimo a querer estallar una bomba en medio de la ciudad."

        hide prota_serio
        with Dissolve(0.2)
        $ actions -= 1
        $ objetos_clickeados.add("diario")

        call screen systemnotice
    else:
        "Ya revisaste este objeto."
    jump click

label libreta:
    if "libreta" not in objetos_clickeados:

        show libreta:
            yalign 0.7
            xalign 0.5
            zoom 2.0
        with Dissolve(0.2)

        p "Esta libreta es muy pequeña, casi queda completamente oculta en mi palma. Sería ideal para revisar información sin que otros se dieran cuenta. Tengo que descubrir si existe algo relevante dentro, a ver…"
        p "{i}Arroz, carne de soya, apio, zanahorias, cebollas, salsa de tomates, azúcar, harina…{/i}"
        p "¿Será un código?"
        p "{i}70.159 (ayer)… 195.000 (regresar a M)… 210.110 (del total)…{/i}"
        p "¿Qué es esto?"
        p "{i}y por eso cuando te veo creo que se me va a reventar el cerebro, pero al final lo soporto porque el chocolate aquí sabe muy bien…{/i}"

        hide libreta
        with Dissolve(0.2)

        show prota_serio at center
        with Dissolve(0.2)
        p "No creo que pueda sacar nada en limpio de esto."

        hide prota_serio
        with Dissolve(0.2)

        p "¡Oh, me muevo…! Espera, espera… ¿Por qué el huesped quiere irse justo ahora? Vamos, no está tan lleno, podemos esperar un poco más a que alguien nos atienda."

        show prota_inicial:
            center
            matrixcolor OpacityMatrix(value=0.7)
        with Dissolve(0.2)
        
        p "No tiene caso, ¿no puedo influir en sus pensamientos desde aquí? ¡Y tengo tanta hambre que podría comerme un dinosaurio! No quiero irme todavía…"

        hide prota_inicial
        with Dissolve(0.2)

        pause 0.5

        b "¡Ratagris! ¡Ratagris!"

        show prota_inicial:
            xalign 0.8
            yalign 1.0
            matrixcolor OpacityMatrix(value=0.7)
        show prota_sorpresa:
            xalign 1.0
            yalign 1.0
        with Dissolve(0.2)
        p "(¿Qué?... ¿Soy Ratagris? Parece que alguien me están llamando. Al menos este huesped ya no quiere salir. Eso es, volvamos a la fila, camarada.)"
    
        show petirrojo at left
        with Dissolve(0.2)
        b "¡Ey, Ratagris!"
        p "(Esta persona se llama...)"

        hide prota_inicial
        with Dissolve(0.5)
        show prota_sorpresa:
            xalign 0.8
            yalign 1.0
        with move
        p "¿Petirrojo?"
        $ actions -= 1
        $ objetos_clickeados.add("libreta")

        call screen systemnotice

        b "¡Creí que ya no vendrías! ¿Qué vas a pedir? Tenemos nuestro Barros Jarpa especial y un chocolate caliente que está delicioso."
        p "(Ya he gastado varios puntos de investigación, necesito tomar una decisión. Si pudiera cambiar en algo las cosas…)"

        menu:
            "¡Suena bien! Muero de hambre…":
                call evento1 from _call_evento1
            "Hoy solo tomaré un café.":
                call evento2 from _call_evento2
    else:
        "Ya revisaste este objeto."
    jump click

label evento1:

    b "¡Genial! Dame un segundo y te entrego lo que pediste."

    hide petirrojo
    with Dissolve(0.2)

    show prota_inicial:
        xalign 1.0
        yalign 1.0
        matrixcolor OpacityMatrix(value=0.7)
    with Dissolve(0.2)
    show prota_sorpresa:
        xalign 0.8
        yalign 1.0

    p "(Ey, ey, ey, ¡mis manos sudan! ¿Por qué siento tanto nerviosismo de pronto? ¿Esta era la decisión correcta? Nadie más me presta atención. No entiendo cómo este momento fue decisivo para el evento…)"
    p "(Oh, aquí viene.)"

    hide prota_inicial
    with Dissolve(0.2)

    show petirrojo at left
    with Dissolve(0.2)
    b "¡Listo! Aquí tienes. Qué bueno que pudiste pasar, ¿todo bien en el trabajo?"
    p "Gracias, sí… Todo va muy bien."
    b "Me alegro… Por cierto, Ratagris, esta noche habrá un concierto de Corazón de Ángel… Pensaba, no sé, de pronto podía interesarte ir…"
    p "(¡Ese nombre! Estaba en el informe… Pero no era una banda. Debe ser el código que usan para encriptar sus actividades. Entonces, ¿Petirrojo es el contacto?)"

    hide prota_sorpresa
    show prota_sonrisa:
        xalign 0.8
        yalign 1.0
    with Dissolve(0.2)
    p "¡Corazón de Ángel! ¡Me encanta esa banda! ¿En serio vendrán?"

    show petirrojo:
        xalign 0.2
        yalign 1.0
    with move
    b "¡Sí! ¡Sabía que te podía gustar! Dame tu número y te envío el código de las entradas…"
    p "Claro…"
    p "(¿Eh? Ahora que está más cerca… Ese colgante que lleva Petirrojo, ¿no lo había visto antes? ¿A qué me recuerda…?)"

    hide petirrojo
    hide prota_sonrisa
    with Dissolve(0.2)

    jump click

label evento2:
    $ cafe = True

    hide petirrojo
    show petirrojo_frio at left
    with Dissolve(0.2)

    b "Oh, bueno… Dame un segundo."

    hide petirrojo_frio
    with Dissolve(0.2)

    show prota_inicial:
        xalign 1.0
        yalign 1.0
        matrixcolor OpacityMatrix(value=0.7)
    with Dissolve(0.2)
    show prota_sorpresa:
        xalign 0.8
        yalign 1.0

    p "(¡Rayos, tengo tanta hambre! Si tomo las decisiones opuestas a lo que siento ¿podré cambiar el curso de eventos? Ah, aquí viene.)"

    hide prota_inicial
    with Dissolve(0.2)

    show petirrojo_frio at left
    with Dissolve(0.2)

    b "Aquí tienes… ¿Quién sigue?"
    p "Gracias…"

    hide petirrojo_frio
    with Dissolve(0.2)

    show prota_inicial:
        xalign 1.0
        yalign 1.0
        matrixcolor OpacityMatrix(value=0.7)
    show prota_serio:
        xalign 0.8
        yalign 1.0
    with Dissolve(0.2)

    p "(Qué actitud más fría! ¿Se habrá molestado? Parece que ya no me pone atención…)"
    p "(Tengo que buscar algo más en este lugar. Se ve como una cafetería de paso y todo está tan lleno, no hay ni una mesa donde disfrutar este café… )"
    p "(¡Agh, está agrio! ¿Qué clase de cafetería es esta?)"
    p "(No creo que encuentre nada interesante por aquí.)"

    hide prota_inicial
    hide prota_serio
    hide prota_sorpresa
    with Dissolve(0.2)

    jump click


label bolso:
    if "bolso" not in objetos_clickeados:

        show bolso:
            zoom 1.4
            yalign 0.7
            xalign 0.5
        with Dissolve(0.2)

        "Es un bolso tipo morral y se ve muy, muy viejo. La tela es suave, pero está desgastada en los bordes. Ah, creo que esto es un arañazo. Y hay algunos rastros de pelaje naranjo por aquí."
        p "¡Claro! El huesped tiene un gato naranjo que adora echarse a dormir sobre este bolso. Si fuera mi gato lo llamaría… Lo llamaría…"

        hide bolso
        with Dissolve(0.2)

        p "En fin, no creo que sea relevante para el caso."

        $ actions -= 1
        $ objetos_clickeados.add("bolso")

        call screen systemnotice

    else:
        "Ya revisaste este objeto."
    
    jump click

label colgante:
    if "colgante" not in objetos_clickeados:

        show colgante:
            zoom 2.0
            yalign 0.7
            xalign 0.5
        with Dissolve(0.2)

        p "(Es un colgante muy sencillo del que cuelga un pequeño dije plateado de un corazón con un par de alas a los costados. Me produce cierta nostalgia. ¿Dónde lo he visto? Creo que lo conozco de algo.)"

        hide colgante
        with Dissolve(0.2)

        show petirrojo at left
        show prota_sorpresa:
            xalign 0.8
            yalign 1.0
        with Dissolve(0.2)

        b "¿Pasa algo?"
        p "Ah, sí… Estaba intentando hacer memoria. Este colgante… ¿De dónde es?"

        hide petirrojo
        show petirrojo_frio at left
        with Dissolve(0.2)
        b "De… ¿dónde?"
        p "Sí, es que me recuerda algo…"
        b "En realidad… este colgante es de alguien más… Ah, rayos, ¡ya me puse sentimental! Es un poco triste, lo siento."
        p "¡Ah, no me hagas caso! Debo haberme confundido. Olvídalo, ¿si?"
        b "Disculpa…"
        p "No, tú disculpa. No debí entrometerme tanto."

        hide petirrojo_frio
        hide prota_sorpresa
        with Dissolve(0.2)

        $ actions -= 1
        $ objetos_clickeados.add("colgante")

        call screen systemnotice

    else:
        "Ya revisaste este objeto."
    jump click

    label salida:
    if "salida" not in objetos_clickeados:

        p "Me pregunto a dónde lleva esta puerta..."
        show cafe:
            matrixcolor TintMatrix(color="#1a181d")
        with Dissolve(0.2)
        "Afuera se ve una pequeña terraza, todas las mesas están ocupadas."
        p "(Qué lástima, se veía como un buen lugar para sentarse a tomar algo.)"
        "Alguien choca contigo al entrar nuevamente a la cafetería." with vpunch

        show mystery:
            xalign 0.2
            yalign 1.0
        show prota_confusion:
            xalign 0.8
            yalign 1.0
        with Dissolve(0.2)
        m "¡Cuidado por dónde pisas!" with vpunch
        p "¡Oiga! ¡No me empuje! ¿Qué le pasa? ¡Oiga!" with vpunch

        hide mystery
        with Dissolve(0.2)

        hide prota_confusion
        show prota_serio:
            xalign 0.8
            yalign 1.0
        with Dissolve(0.2)
        p "(Se fue… ¿Eh? ¿Qué es esto? ¿Me dejó un flyer?)"
        "En el flyer se lee: Corazón de Ángel tocará esta noche en el bar Pelea de Gallos…"
        p "(Ese nombre me suena de algo. Sí, estaba en el informe. Pero no era una banda, ¿será un código que usan para las reuniones de la organización?)"

        hide prota_serio
        with Dissolve(0.2)
        $ actions -= 1
        $ objetos_clickeados.add("salida")

        call screen systemnotice

    else:
        "Ya revisaste este objeto."
    jump click

label sin_acciones:
    if actions == 0:
        call screen systemnotice2("Has consumido todos los puntos de investigación disponibles. Regresarás al laboratorio central.")

        jump volver_lab

    else:
        "Aún te quedan acciones por realizar."

label volver_lab:

    stop music fadeout 0.5

    scene bgblack
    with ImageDissolve("images/transition.png", 2.0, 128, reverse=True)

    play music "audio/Static_Hum_Tonal_Machine.ogg" volume 0.3 fadein 0.5

    show prota_trance:
        center
        matrixcolor OpacityMatrix(value=0.2)
        blur 2.0
    with Dissolve(1.5)

    p "Todo se está oscureciendo ¿Ya voy a regresar? ¡Todo se va alejando tan pronto!"
    p "Este mareo desagradable… ¿Así será cada viaje? ¿Cuándo podré salir de este trance? Mi cabeza va a reventar. No puedo ver, no puedo pensar…"

    show prota_inicial:
        center
        matrixcolor OpacityMatrix(value=0.2)
        blur 2.0
    with Dissolve(1.5)

    hide prota_trance
    with Dissolve(1.0)

    p "Por favor, que se dentenga de una vez… ¡Por favor!"

label lab_2:
    c "3… 2… 1! Conexión exitosa!"

    scene laboratorio
    with ImageDissolve("images/transition.png", 2.0, 128, reverse=True)

    stop music fadeout 0.5

    play music "audio/Drone_Cave_Wind_Deep_Dark.ogg" volume 0.3 fadein 0.5

    show prota_inicial at center
    with Dissolve(0.2)
    p "¿Qu-qué pasó?"

    hide prota_inicial
    with Dissolve(0.2)

    show cientifico at left
    show cientifica at right
    with Dissolve(0.2)
    c2 "Tuvimos una ruptura en la sincronización. Perdimos el viaje…"

    hide cientifico
    hide cientifica
    with Dissolve(0.2)

    show prota_inicial at center
    with Dissolve(0.2)
    p "¿Qué? No… "

    hide prota_inicial
    with Dissolve(0.2)

    show cientifico at left
    show cientifica at right
    with Dissolve(0.2)
    c "¡Qué lástima! Y justo era tu primer viaje. Danos un momento, volveremos a habilitar el portal. A veces el sistema se satura."

    hide cientifico
    hide cientifica
    with Dissolve(0.2)

    show prota_inicial at center
    with Dissolve(0.2)
    p "No, no. Yo viajé."

    hide prota_inicial
    with Dissolve(0.2)

    show cientifico at left
    show cientifica at right
    with Dissolve(0.2)
    c "¿Qué?"

    hide cientifico
    hide cientifica
    with Dissolve(0.2)

    show prota_inicial at center
    with Dissolve(0.2)
    p "Viajé, acabo de regresar… Todo fue tan abrupto."

    hide prota_inicial
    with Dissolve(0.2)

    show cientifico at left
    show cientifica at right
    c "Entonces, ¿volviste justo al mismo instante en que partiste?"

    hide cientifico
    hide cientifica
    with Dissolve(0.2)

    show prota_inicial at center
    with Dissolve(0.2)  
    p "Sí..."

    hide prota_inicial
    with Dissolve(0.2)

    show cientifico at left
    show cientifica at right
    with Dissolve(0.2)
    c "Eso es… curioso. ¿Qué fue lo que viste?"

    hide cientifico
    hide cientifica
    with Dissolve(0.2)

    if cafe == True:

        show prota_inicial at center
        with Dissolve(0.2)  
        p "Estuve en una cafetería, pedí un café horrible, salí de ahí y luego…  regresé. Lo siento, tengo un poco revueltas mis ideas. ¡Todo se sintió tan real!"

        hide prota_inicial
        with Dissolve(0.2)

        show cientifico at left
        show cientifica at right
        with Dissolve(0.2)
        c2 "Respira, no hay prisa. La recuperación después de un desplazamiento de consciencia no es inmediata. ¿Recuerdas haber visto un calendario, reloj o algo que te permitiera orientarte?"

        hide cientifico
        hide cientifica
        with Dissolve(0.2)

        show prota_inicial at center
        with Dissolve(0.2)  
        p "Sí, había un diario fechado en el 10 de diciembre de 2063. Creo que eran las 11:15 de la mañana."

        hide prota_inicial
        with Dissolve(0.2)

        show cientifico at left
        show cientifica at right
        with Dissolve(0.2)

        c2 "¡Eso coincide con el bucle establecido!"   
        c "Bien, ¿recuerdas algo que te llamara la atención?"

        hide cientifico
        hide cientifica
        with Dissolve(0.2)
    
        show prota_inicial at center
        with Dissolve(0.2)  
        p "Sí, tenía muchísima hambre, pero probé si podía alterar las decisiones del huésped y pedí tan solo un café."

        hide prota_inicial
        with Dissolve(0.2)

        show cientifico at left
        show cientifica at right
        with Dissolve(0.2)
        c2 "Interesante. Por favor, corrobora la ficha de información para detectar si se ha producido algún cambio en los hechos."

        hide cientifico
        hide cientifica
        with Dissolve(0.2)

        call screen mision_resumen

        show prota_inicial at center
        with Dissolve(0.2)  
        p "(De acuerdo a esta información… Todo se ve igual… ¿Eh?)"
        p "Esto... es muy extraño."

        hide prota_inicial
        with Dissolve(0.2)

        show cientifico at left
        show cientifica at right
        with Dissolve(0.2)
        c2 "¿Qué ocurrió?"

        hide cientifico
        hide cientifica
        with Dissolve(0.2)

        show prota_inicial at center
        with Dissolve(0.2)  
        p "No lo sé, parece que el número de víctimas varió, pero solo por una persona…"

        hide prota_inicial
        with Dissolve(0.2)

        show cientifico at left
        show cientifica at right
        with Dissolve(0.2)
        c "¿Salvaste a alguien?"

        hide cientifico
        hide cientifica
        with Dissolve(0.2)

        show prota_inicial at center
        with Dissolve(0.2)  
        p "No. Provoqué la muerte de alguien más…"

        hide prota_inicial
        with Dissolve(0.2)

        show cientifico at left
        show cientifica at right
        with Dissolve(0.2)
        c2 " De acuerdo. Dejaremos registrado este antecedente. Aspirante, nuestro objetivo final es detener por completo el atentado."
        c2 "Este ha sido solo el primer Loop, utilizaremos toda la información disponible para llevar muestra misión a cabo. Somos un equipo. No lo olvides."

        hide cientifico
        hide cientifica
        with Dissolve(0.2)

        show prota_inicial at center
        with Dissolve(0.2)  
        p "Sí…"

        hide prota_inicial
        with Dissolve(0.2)

        show cientifico at left
        show cientifica at right
        with Dissolve(0.2)
        c2 "¿Algo más que recuerdes? ¿O alguien?"

        hide cientifico
        hide cientifica
        with Dissolve(0.2)

        show prota_inicial at center
        with Dissolve(0.2)  
        p "Sí, había un sujeto extraño fuera de la cafetería. El imbécil me empujó y me dejó un flyer para un concierto de una banda: Corazón de Ángel."
        p "Tocarían esa misma noche."

        hide prota_inicial
        with Dissolve(0.2)

        show cientifico at left
        show cientifica at right
        with Dissolve(0.2)
        c2 "Corazón de Ángel era el alias de la cápsula terrorista responsable del atentado. ¿Seguro fue un sujeto extraño el que te dejó el flyer?"

        hide cientifico
        hide cientifica
        with Dissolve(0.2)

        show prota_inicial at center
        with Dissolve(0.2)  
        p "Sí, tenía la ubicación del bar y todo ¿Por qué?"

        hide prota_inicial
        with Dissolve(0.2)

        show cientifico at left
        show cientifica at right
        with Dissolve(0.2)
        c2 "Según nuestros reportes, el vector que intermediaría entre el huésped y la cápsula terrorista era un civil apodado Petirrojo…" 
        c2 "Pero si la información te la dio este sujeto, ¿qué rol cumplió Petirrojo en todo esto? Y además, tenemos esta muerte extra en el registro. Necesitamos analizar esta situación."
        c "Por supuesto. Primero examinaremos los datos registrados por el sistema operativo vinculado a tu casco de navegación."

        call screen systemnotice2("Aspirante R01.\n\nHoras de viaje efectuadas: 0.5.\n\nPuntos de investigación consumidos: 6.\n\nRequisitos para pasar al siguiente Loop: Completados.")

        c "Excelente. ya podemos avanzar al siguiente nivel. Esta vez te devolveremos a un tiempo anterior a este. Intenta reunir la mayor cantidad de información posible. Todo será clave para detener este terrible atentado."
        hide cientifico
        hide cientifica
        with Dissolve(0.2) 

        jump fin        
    
    else:
        show prota_inicial at center
        with Dissolve(0.2)  
        p "Estuve en una cafetería, pedí un sandwich y…  regresé. Lo siento, tengo un poco revueltas mis ideas. ¡Todo se sintió tan real!"

        hide prota_inicial
        with Dissolve(0.2)

        show cientifico at left
        show cientifica at right
        with Dissolve(0.2)
        c "Respira, no hay prisa. La recuperación después de un desplazamiento de consciencia no es inmediata. ¿Recuerdas haber visto un calendario, reloj o algo que te permitiera orientarte?"

    
        hide cientifico
        hide cientifica
        with Dissolve(0.2)

        show prota_inicial at center
        with Dissolve(0.2)  
        p "Sí, había un diario fechado en el 10 de diciembre de 2063. Creo que eran las 11:15 de la mañana."

        hide prota_inicial
        with Dissolve(0.2)

        show cientifico at left
        show cientifica at right
        with Dissolve(0.2)
        c2 "¡Eso coincide con el bucle establecido!"
        c "Bien, ¿recuerdas algo que te llamara la atención? ¿O alguien?"
    
        hide cientifico
        hide cientifica
        with Dissolve(0.2)

        show prota_inicial at center
        with Dissolve(0.2)  
        p "Alguien… ¡Sí, había alguien! Creo que puede ser uno de los agentes que propiciaron el evento. Se llamaba… Petirrojo."

        hide prota_inicial
        with Dissolve(0.2)

        show cientifico at left
        show cientifica at right
        with Dissolve(0.2)
        c "Esa cafetería fue considerada un punto crucial en la investigación. Se logró establecer que uno de los vectores que vinculó al agente terrorista con el evento fue un civil apodado Petirrojo. ¿Pudiste hacer contacto con ese vector?"

        hide cientifico
        hide cientifica
        with Dissolve(0.2)

        show prota_inicial at center
        with Dissolve(0.2)  
        p "Sí… me invitó a un concierto de Corazón de Ángel."

        hide prota_inicial
        with Dissolve(0.2)

        show cientifico at left
        show cientifica at right
        with Dissolve(0.2)
        c2 "¿Corazón de Ángel? Excelente, vamos por buen camino."
        c "Bien, ahora examinaremos los datos registrados por el sistema operativo vinculado a tu casco de navegación." 

        call screen systemnotice2("Aspirante R01.\n\nHoras de viaje efectuadas: 0.5.\n\nPuntos de investigación consumidos: 6.\n\nRequisitos para pasar al siguiente Loop: Completados.")

        c "Excelente. ya podemos avanzar al siguiente nivel. Esta vez te devolveremos a un tiempo anterior a este. Intenta reunir la mayor cantidad de información posible. Todo será clave para detener este terrible atentado."
        hide cientifico
        hide cientifica
        with Dissolve(0.2) 

        jump fin


label fin:

    scene bgblack
    with ImageDissolve("images/transition.png", 2.0, 128, reverse=True)

    call screen systemnotice3("Fin del primer loop.")

    stop music fadeout 0.5

    #Fin del juego
    
      
  
