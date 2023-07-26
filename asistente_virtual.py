''' La propuesta aquí es crear un software que sea capaz de interactuar con el usuario, 
para que el usuario se sienta cómodo para aceptar un acompañamiento intervención estratégica.'''
'''La propuesta aquí es desarrollar un código de interacción social con el objetivo 
de realizar un cribado de personas con posibles problemas emocionales.'''
print('\33[34mBuen dia!\33[m \n    ¿hablamos?\n    Mi nombre es \33[34mEsther!\33[m')  # A través de un enfoque humanizado, intentaremos que la persona se sienta más cómoda para hablar.
nome = str(input('¿Como te llamas? : '))
print('\33[34m Tienes un nombre precioso \33[32m{}\33[m, \33[34mEs un placer conocerte!!\33[m'.format(nome.capitalize()))
ps = str(input('¿Cómo te sientes hoy? '))
#El objetivo aquí es tratar de averiguar cómo se siente el usuario en este día..
if ps == 'um poco triste' or ps == 'triste' or ps == 'preocupado' or ps == 'mal' or ps == 'culpable' or ps == 'deprimido' or ps =='solo' or ps == 'ansioso' or ps == 'asustado':
    print('  \33[34mLamento que te sientas así!\33[m')
    aj = str(input('  \33[34mMe encantaría ayudarte! \n  \33[32m{}!\33[m\n \33[33mTe gustaría hablar con alguien amigable que te escuche atentamente y te ayude.?\33[m   '.format(nome.capitalize())))
    if aj == 'si':
        print('    \33[34mExcelente, voy a llamar a un gran amigo para hablar contigo personalmente!\33[m') #Aquí intentaremos dirigir al usuario a un profesional de la zona.
    elif aj == 'no':
        print('     \33[34mEstá bien, lo entiendo, pero si lo necesito, estaré aquí!\33[m')
else:
    print('Muy bien, entiendo!')
print('\33[30;43mQue tengas un gran día!! {}\33[m'.format(nome.capitalize()))