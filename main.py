import claseMaquina
import time

estado_inicial_ = "q1",
estados_aceptados = ["qf"],
transiciones = {
  ("q1","0"):("q2", "1", "R"),
  ("q1","1"):("q1", "0", "R"),
  ("q1"," "):("q3", "1", "R"),
  
  ("q2","0"):("q1", "0", "R"),
  ("q2","1"):("qf", "0", "L"),
  ("q2"," "):("q2", "1", "L"),

  ("q3","0"):("q1", "1", "L"),
  ("q3","1"):("q2", "1", "L"),
  ("q3"," "):("q3", "1", "R"),
}
estado_final_ = {"qf"}

def validarBinario(binario):
  strBinario = str(binario)

  for numero in strBinario:
    if numero not in '01':
      return False

  if (len(list(strBinario)) == 0) or (len(list(strBinario)) > 200):
    return False

  return True

def main():
  numeroBin = ""

  with open('input.txt', 'r') as f:
    numeroBin = f.read().replace("\n", "").replace(" ", "")
  
  if not validarBinario(numeroBin):
    print("El dato de entrada debe ser un número binario, de entre 1 y 200 caractéres, pero se introdujo:\n" + str(numeroBin))
    return

  t = claseMaquina.MaquinaTuring(numeroBin, 
                    estado_inicial = "q1",
                    estados_finales = estado_final_,
                    transiciones = transiciones)
  
  print("\nTabla de reglas de la máquina\n\n Qi   Sj | Qij   Sij   Dij\n" +
        "—————————┼————————————————")
  
  for key, value in transiciones.items():
    r = value[1]

    if r == "":
      r = " "

    print(f" {key[0]}   {key[1]}  | {value[0]}     {r}     {value[2]} \n" +
          "—————————┼————————————————")

  time.sleep(3)

  numeroOg = t.get_cinta()

  print("\nDato de entrada en la cinta: " +
        t.get_cinta() + "\n\n" +
        "Cinta -> Estado" + "\n\n" +
        t.get_cinta() + " -> " + "q1")

  while not t.final():
    t.step()

  print("\n" + "Resultado del cálculo de la máquina de Turing:\n" +
        "Entrada:   " + numeroOg + "\n" +
        "Salida:    " + t.get_cinta() + "\n")
  return

main()
