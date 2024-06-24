from clear import limpiar
from ingredientes import ingredientes as ing

limpiar()

class Pizza():
    proteinas = ing['proteinas']
    vegetales = ing['vegetales']
    masas = ing['masas']
    tamano = 'familiar'
    precio = 10000
    

    def __init__(self) -> None:
        self.proteina = None
        self.vegetal1 = None
        self.vegetal2 = None
        self.masa = None
        self.es_valida = True
    
    
    @staticmethod
    def validar_elementos(elemento, valores_posibles):
        return elemento in valores_posibles
    
    
    def tomar_pedido(self):
        self.proteina = input(f'Ingrese su proteina favorita {self.proteinas}  :   ')
        self.vegetal1 = input(f'Ingrese su primer vegetal {self.vegetales}  :   ')
        self.vegetal2 = input(f'Ingrese su segundo vegetal {self.vegetales}  :   ')   
        self.masa = input(f'Ingrese su masa predilecta {self.masas}  :   ')      
        
        
        if(
            self.validar_elementos(self.proteina, self.proteinas) and
            self.validar_elementos(self.vegetal1, self.vegetales) and
            self.validar_elementos(self.vegetal2, self.vegetales) and
            self.validar_elementos(self.masa, self.masas)
        ):
            self.es_valida = True
        else:
            self.es_valida = False


