class Email:
    def __init__(self):
        self.enviado = False
    def enviar_corre(self):
        self.enviado = True
mi_correo = Email()
print(mi_correo.enviado)
mi_correo.enviar_corre()
print(mi_correo.enviado)