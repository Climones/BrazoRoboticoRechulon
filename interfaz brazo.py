import PySimpleGUI as sg

sg.theme('DarkAmber')
# image_pause = './ButtonGraphics/Pause.png'
flechaArriba = 'boton arriba.png'
flechaAbajo = 'boton abajo.png'
gradom1 = 0 
gradom2= 0
gradom3 = 0
gradom4 = 0
gradom5 = 0
grados = 15 #Podemos añadir a la interfaz la posibilidad de cambiar los grados

layout = [[sg.Text('Pulsa las flechas para controlar el brazo'), sg.Text(size=(15,1), key='-OUTPUT-')],
          # creo los botones arriba y abajo de cada motor y un número que indica los grados que tiene
          [sg.Text('Motor 1'), sg.ReadFormButton('', key = 'M1Arriba', button_color=sg.TRANSPARENT_BUTTON,
                                image_filename= flechaArriba, image_size=(40, 40), image_subsample=13, border_width=0),
                                sg.Text(' ' * 2), 
                                sg.ReadFormButton('', key = 'M1Abajo', button_color=sg.TRANSPARENT_BUTTON,
                                image_filename= flechaAbajo, image_size=(40, 40), image_subsample=13, border_width=0),
                                sg.Text(' ' * 2),
                                sg.Text('Grado: '),
                                sg.Text('0', key ='GradoM1')],
          [sg.Text('Motor 2'), sg.ReadFormButton('', key = 'M2Arriba', button_color=sg.TRANSPARENT_BUTTON,
                                image_filename= flechaArriba, image_size=(40, 40), image_subsample=13, border_width=0),
                                sg.Text(' ' * 2), 
                                sg.ReadFormButton('', key = 'M2Abajo', button_color=sg.TRANSPARENT_BUTTON,
                                image_filename= flechaAbajo, image_size=(40, 40), image_subsample=13, border_width=0),
                                sg.Text(' ' * 2),
                                sg.Text('Grado: '),
                                sg.Text('0', key ='GradoM2')],
          [sg.Text('Motor 3'), sg.ReadFormButton('', key = 'M3Arriba', button_color=sg.TRANSPARENT_BUTTON,
                                image_filename= flechaArriba, image_size=(40, 40), image_subsample=13, border_width=0),
                                sg.Text(' ' * 2), 
                                sg.ReadFormButton('', key = 'M3Abajo', button_color=sg.TRANSPARENT_BUTTON,
                                image_filename= flechaAbajo, image_size=(40, 40), image_subsample=13, border_width=0),
                                sg.Text(' ' * 2),
                                sg.Text('Grado: '),
                                sg.Text('0', key ='GradoM3')],
          [sg.Text('Motor 4'), sg.ReadFormButton('', key = 'M4Arriba', button_color=sg.TRANSPARENT_BUTTON,
                                image_filename= flechaArriba, image_size=(40, 40), image_subsample=13, border_width=0),
                                sg.Text(' ' * 2), 
                                sg.ReadFormButton('', key = 'M4Abajo', button_color=sg.TRANSPARENT_BUTTON,
                                image_filename= flechaAbajo, image_size=(40, 40), image_subsample=13, border_width=0),
                                sg.Text(' ' * 2),
                                sg.Text('Grado: '),
                                sg.Text('0', key ='GradoM4')],
          [sg.Text('Motor 5'), sg.ReadFormButton('', key = 'M5Arriba', button_color=sg.TRANSPARENT_BUTTON,
                                image_filename= flechaArriba, image_size=(40, 40), image_subsample=13, border_width=0),
                                sg.Text(' ' * 2), 
                                sg.ReadFormButton('', key = 'M5Abajo', button_color=sg.TRANSPARENT_BUTTON,
                                image_filename= flechaAbajo, image_size=(40, 40), image_subsample=13, border_width=0),
                                sg.Text(' ' * 2),
                                sg.Text('Grado: '),
                                sg.Text('0', key ='GradoM5')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window("Brazo Robótico", layout, margins=(20, 75))

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
#motor 1 flechitas
    if event == 'M1Arriba':
        if gradom1 == 360 - grados:
         gradom1 =0
        else:
         gradom1 += grados
        
        window['GradoM1'].update(gradom1)
        window.write_event_value('-UPDATE-', (gradom1,))

    if event == 'M1Abajo':
        if gradom1 == 0:
         gradom1 = 360 - grados
        else:
         gradom1 -= grados
        window['GradoM1'].update(gradom1)
        window.write_event_value('-UPDATE-', (gradom1,))

#motor 2 flechitas
    if event == 'M2Arriba':
        if gradom2 == 360 - grados:
         gradom2 =0
        else:
         gradom2 += grados
        window['GradoM2'].update(gradom2)
        window.write_event_value('-UPDATE-', (gradom2,))

    if event == 'M2Abajo':
        if gradom2 == 0:
         gradom2 = 360 - grados
        else:
         gradom2 -= grados
        window['GradoM2'].update(gradom2)
        window.write_event_value('-UPDATE-', (gradom2,))
#motor 3 flechitas
    if event == 'M3Arriba':
        if gradom3 == 360 - grados:
         gradom3 =0
        else:
         gradom3 += grados
        window['GradoM3'].update(gradom3)
        window.write_event_value('-UPDATE-', (gradom3,))

    if event == 'M3Abajo':
        if gradom3 == 0:
         gradom3 = 360 - grados
        else:
         gradom3 -= grados
        window['GradoM3'].update(gradom3)
        window.write_event_value('-UPDATE-', (gradom3,))

#motor 4 flechitas
    if event == 'M4Arriba':
        if gradom4 == 360 - grados:
         gradom4 =0
        else:
         gradom4 += grados
        window['GradoM4'].update(gradom4)
        window.write_event_value('-UPDATE-', (gradom4,))

    if event == 'M4Abajo':
        if gradom4 == 0:
         gradom4 = 360 - grados
        else:
         gradom4 -= grados
        window['GradoM4'].update(gradom4)
        window.write_event_value('-UPDATE-', (gradom4,))

#motor 5 flechitas
    if event == 'M5Arriba':
        if gradom5 == 360 - grados:
         gradom5 =0
        else:
         gradom5 += grados
        window['GradoM5'].update(gradom5)
        window.write_event_value('-UPDATE-', (gradom5,))

    if event == 'M5Abajo':
        if gradom5 == 0:
         gradom5 = 360 - grados
        else:
         gradom5 -= grados
        window['GradoM5'].update(gradom5)
        window.write_event_value('-UPDATE-', (gradom5,))

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        window['-OUTPUT-'].update(values['-IN-'])
    #AQUÍ VTENEMOS QUE PONER EL ARDUINO NERVOZIO
    #Una serie de comandos que tenemos que tener ya establecidos.
    #Nos conectamos con el server, usamos ECHO, y dependiendo de los gradoi i = 1...5 tenemos que mandar un socket que va a recibir
    #el ESP8266 y este interpretará la instrucción y moverá el brazo. Lo que tenemos que mandar es el grado.
    
    if event == '-UPDATE-':
        #gradom1 = values['-UPDATE-'][0]
        window['GradoM1'].update(gradom1)
 
        #gradom2 = values['-UPDATE-'][0]
        window['GradoM2'].update(gradom2)

        #gradom3 = values['-UPDATE-'][0]
        window['GradoM3'].update(gradom3)

        #gradom4 = values['-UPDATE-'][0]
        window['GradoM4'].update(gradom4) 

        #gradom5 = values['-UPDATE-'][0]
        window['GradoM5'].update(gradom5)

window.close()

