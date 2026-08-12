class Bicicleta:
    def __init__(self, modelo, velocidade=0):
        self.modelo = modelo
        self.velocidade = velocidade

    def pedalar(self):
        velocidade_antes = self.velocidade
        self.velocidade = min(60, self.velocidade + 5)
        print(f"Pedalando... Velocidade antes: {velocidade_antes} km/h | Velocidade depois: {self.velocidade} km/h")

    def freiar(self):
        velocidade_antes = self.velocidade
        self.velocidade = max(0, self.velocidade - 5)
        print(f"Freiando... Velocidade antes: {velocidade_antes} km/h | Velocidade depois: {self.velocidade} km/h")

    def radar_de_velocidade(self):
        print(f"[RADAR] A bicicleta {self.modelo} está a {self.velocidade} km/h.")

minha_bike = Bicicleta("Caloi")


minha_bike.pedalar()
minha_bike.pedalar()

minha_bike.radar_de_velocidade()

minha_bike.freiar()
minha_bike.freiar()
minha_bike.freiar()