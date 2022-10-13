from cmath import pi
import math


class Planeta:
    def __init__(self, nome, velocidade, distSol, massa):
        self.nome = nome
        self.velocidade = velocidade
        self.distSol = distSol
        self.massa = massa
        self.orbitaComp = 2*pi * distSol 
    pass


mercurio = Planeta("Mercúrio", 35.00, 0.4, 3.285 * math.pow(10, 23))
venus = Planeta("Venus", 35.00, 0.7, 4.867 * math.pow(10, 24))
terra = Planeta("Terra", 1666.00, 1, 5.972 * math.pow(10, 24))
marte = Planeta("Marte", 24.077, 1.5, 6.39 * math.pow(10, 23))
jupiter = Planeta("Júpiter", 13.1, 0, 1.898 * math.pow(10, 27))
saturno = Planeta("Saturno", 9.69, 9.6, 5.683 * math.pow(10, 26))
urano = Planeta("Urano", 27400.00, 19.00, 8.681 * math.pow(10, 25))
netuno = Planeta("Netuno", 5.45, 30, 1.024 * math.pow(10, 26))
