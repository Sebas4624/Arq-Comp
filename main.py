import claseMaquina

estado_inicial_ = "q1",
estados_aceptados = ["qf"],
transiciones = {
  ("q1","0"):("q1", "1", "R"),
  ("q1","1"):("q1", "0", "R"),
  ("q1"," "):("qf", "", "R"),
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

  with open('test.txt', 'r') as f:
    numeroBin = f.read().replace("\n", "")
  
  if not validarBinario(numeroBin):
    print("El dato de entrada debe ser un número binario, de entre 1 y 200 caractéres, pero se introdujo:\n" + str(numeroBin))
    return

  t = claseMaquina.MaquinaTuring(numeroBin, 
                    estado_inicial = "q1",
                    estados_finales = estado_final_,
                    transiciones = transiciones)

  print("Dato de entrada en la cinta: " + t.get_tape() + "\n" + "\n" + t.get_tape() + " -> " + "q1")

  while not t.final():
    t.step()

  print("\n" + "Resultado del cálculo de la máquina de Turing:")
  print(t.get_tape())
  return

main()
