'''
-----------------------------------
Producto Integrador de Aprendizaje
Teoria de Automatas
Equipo III
-----------------------------------
'''

# Librerias 
import os
from automata.tm.dtm import DTM       

# Imprime los resultados de la Maquina de Turing
def imprimeResultado(cadena, turing_machine):
    tupla = turing_machine.validate_input(cadena, step = True)

    try:
        turing_machine.validate_input(cadena)
    except Exception as error_message: 
        print("Transicion no definida en " + str(error_message)[-7:])
        print("[Cadena invalida]")
    else:
        for i in tupla:
            print(i)
        
        print("\n")
        print("[Cadena valida]")
        
# Programa principal 
def main():
    turing_machine = DTM(
        states={'q0', 'q1', 'q2', 'q3', 'q4'},
        input_symbols={'0', '1'},
        tape_symbols={'0', '1', 'x', 'y', '.'},
        transitions={
            'q0': {
                '0': ('q1', 'x', 'R'),
                'y': ('q3', 'y', 'R')
            },
            'q1': {
                '0': ('q1', '0', 'R'),
                '1': ('q2', 'y', 'L'),
                'y': ('q1', 'y', 'R')
            },
            'q2': {
                '0': ('q2', '0', 'L'),
                'x': ('q0', 'x', 'R'),
                'y': ('q2', 'y', 'L')
            },
            'q3': {
                'y': ('q3', 'y', 'R'),
                '.': ('q4', '.', 'R')
            }
        },
        initial_state='q0',
        blank_symbol='.',
        final_states={'q4'}
    )
    
    centinela = True

    while(centinela):
        os.system('cls||clear')

        print("======       Teoria de Automatas: PIA        ======")
        print("======               Equipo III              ======")
        print("---------------------------------------------------")
        print("Lenguaje: L = {a^n (bab)^n | n > 0}")
        print("---------------------------------------------------")
        print("Ingrese una cadena para ser validada:")
        
        cadena = str(input())
        
        print("---------------------------------------------------")
       
        imprimeResultado(cadena, turing_machine)
        
        print("---------------------------------------------------")
        print("¿Desea ingresar otra cadena? [S/N]:")
        
        opcion = input()

        if opcion.upper() == 'S':
            centinela = True
        elif opcion.upper() == 'N':
            centinela = False
        else:
            print("Opcion incorrecta. Ingrese una opcion valida.")
            input("Presione cualquier tecla para continuar...")

if __name__=="__main__":
    main()