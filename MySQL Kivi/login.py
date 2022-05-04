"""Comando para correr kivi
   pipenv install "kivy[base]"
   pipenv shell
 . /home/fernando/.local/share/virtualenvs/KIVI-ekXzISsz/bin/activate
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

#la clase debe ser derivada de BoxLayout
class LoginWindow(BoxLayout):
    # Este es el Constructor
    def __init__(self, **kwargs):
        # Llamar al constructor de la clase base (App)
        super().__init__(**kwargs)

    # Constructor de validacion de usuarios
    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text
        # Ciclo if para validar el boton al ingresar datos
        if uname == '' or passw == '':
            info.text = '[color=#FF0000]Se Requiere Nombre de Usuario y/o Contraseña[/color]'
        else:
            if uname == 'admin' and passw == 'admin':
                info.text = '[color=#00FF00]Ingresado Exitosamente!!![/color]'
            else:
                info.text = '[color=#FF0000]Nombre de Usuario y / o Contraseña Inválido!!![/color]'

#la clase debe ser derivada de app
class LoginApp(App):
    def build(self):
        return LoginWindow()

if __name__=="__main__":
    sa = LoginApp()
    sa.run()
