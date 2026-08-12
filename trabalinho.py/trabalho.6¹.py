class Aplicativo:
    def __init__(self, nome, consumo_bateria):

        self.nome = nome
        self.consumo_bateria = consumo_bateria


class Celular:
    def __init__(self, marca, modelo, bateria=100):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"O {self.marca} {self.modelo} foi ligado.")

    def executar_app(self, app):
        
        if not self.ligado:
            print(f"Não é possível executar o {app.nome}: o celular está desligado.")
            return

        if self.bateria >= app.consumo_bateria:
            
            self.bateria -= app.consumo_bateria
            print(f"Executando o aplicativo '{app.nome}'... Bateria restante: {self.bateria}%")
        else:
            print(f"Bateria insuficiente ({self.bateria}%) para executar o aplicativo '{app.nome}' (requer {app.consumo_bateria}%).")



app1 = Aplicativo("Instagram", 15)
app2 = Aplicativo("Jogo 3D", 40)


meu_celular = Celular("Samsung", "Galaxy S23")

meu_celular.ligar()
meu_celular.executar_app(app1)
meu_celular.executar_app(app2)