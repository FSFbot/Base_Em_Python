class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura  = altura
        
    def calcular_area(self):
            return self.base * self.altura
        
    def calcular_perimetro(self):
            return 2 * (self.base + self.altura)
        
Retangulo_A = Retangulo(10,5)

area = Retangulo_A.calcular_area()
perimetro = Retangulo_A.calcular_perimetro()

print(f"Retangulo com base {Retangulo_A.base} e altura de {Retangulo_A.altura} possui:\n- Area: {area}\n- Perimetro: {perimetro}")

