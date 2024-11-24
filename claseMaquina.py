import time

class Cinta(object):
    
    simbolo_blanco = " "
    
    def __init__(self,
                 string_cinta = ""):
        self.__cinta = dict((enumerate(string_cinta)))
        
    def __str__(self):
        s = ""
        index_min = min(self.__cinta.keys()) 
        index_max = max(self.__cinta.keys())
        for i in range(index_min, index_max):
            s += self.__cinta[i]
        return s    
   
    def __getitem__(self,
                    index):
        if index in self.__cinta:
            return self.__cinta[index]
        else:
            return Cinta.simbolo_blanco

    def __setitem__(self, pos, char):
        self.__cinta[pos] = char 

class MaquinaTuring(object):
    
    def __init__(self, 
                 cinta = "", 
                 simbolo_blanco = " ",
                 estado_inicial = "",
                 estados_finales = None,
                 transiciones = None):
        self.__cinta = Cinta(cinta)
        self.__posicion_cabeza = 0
        self.__simbolo_blanco = simbolo_blanco
        self.__estado_actual = estado_inicial
        if transiciones == None:
            self.__transiciones = {}
        else:
            self.__transiciones = transiciones
        if estados_finales == None:
            self.__final_states = set()
        else:
            self.__final_states = set(estados_finales)
        
    def get_tape(self): 
        return str(self.__cinta)
    
    def step(self):
        char_cabeza = self.__cinta[self.__posicion_cabeza]
        x = (self.__estado_actual, char_cabeza)
        if x in self.__transiciones:
            y = self.__transiciones[x]
            self.__cinta[self.__posicion_cabeza] = y[1]
            if y[2] == "R":
                self.__posicion_cabeza += 1
            elif y[2] == "L":
                self.__posicion_cabeza -= 1
            self.__estado_actual = y[0]
        time.sleep(1)
        print(self.get_tape() + " -> " + self.__estado_actual)

    def final(self):
        if self.__estado_actual in self.__final_states:
            return True
        else:
            return False
