import claseMaquina

initial_state = "q1",
accepting_states = ["qf"],
transition_function = {
  ("q1","0"):("q2", "1", "R"),
  ("q1","1"):("qf", "1", "L"),
  ("q2","0"):("q1", "1", "R"),
  ("q2","1"):("q1", "0", "R"),
}
final_states = {"qf"}

t = claseMaquina.MaquinaTuring("0101000100111001", 
                  estado_inicial = "q1",
                  estados_finales = final_states,
                  transiciones=transition_function)

print("Dato de entrada en la cinta:\n" + "\n" + t.get_tape() + " -> " + "q1")

while not t.final():
    t.step()

print("\n" + "Resultado del cálculo de la máquina de Turing:")
print(t.get_tape())
