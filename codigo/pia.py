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
        states={'q0', 
                'q1', 
                'q2', 
                'q3', 
                'q4',
                'q5',
                'q6',
                'q7',
                'q8',
                'q9',
                'q10',
                'q11',
                'q12',
                'q13',
                'q14'},
        input_symbols={'a', 'b'},
        tape_symbols={'a', 'b', 'x', 'y', '.'},
        transitions={
            'q0': {
                '.': ('q1', 'R')
            },
            'q1': {
                'a': ('q2', '.', 'R')
            },
            'q2': {
                'a': ('q2', 'R'),
                'b': ('q3', 'R')
            },
            'q3': {
                'y': ('q4', 'R')
            },
            'q4': {
                'b': ('q5', 'R')
            },
            'q5': {
                '0': ('q2', '0', 'L'),
                'x': ('q0', 'x', 'R')
            },
            'q6': {
                '0': ('q2', '0', 'L'),
                'x': ('q0', 'x', 'R'),
                'y': ('q2', 'y', 'L')
            },
            'q7': {
                '0': ('q2', '0', 'L'),
                'x': ('q0', 'x', 'R'),
                'y': ('q2', 'y', 'L')
            },
            'q8': {
                '0': ('q2', '0', 'L'),
                'x': ('q0', 'x', 'R'),
                'y': ('q2', 'y', 'L')
            },
            'q9': {
                '0': ('q2', '0', 'L'),
                'x': ('q0', 'x', 'R'),
                'y': ('q2', 'y', 'L')
            },
            'q10': {
                '0': ('q2', '0', 'L'),
                'x': ('q0', 'x', 'R'),
                'y': ('q2', 'y', 'L')
            },
            'q11': {
                '0': ('q2', '0', 'L'),
                'x': ('q0', 'x', 'R'),
                'y': ('q2', 'y', 'L')
            },
            'q12': {
                '0': ('q2', '0', 'L'),
                'x': ('q0', 'x', 'R'),
                'y': ('q2', 'y', 'L')
            },
            'q13': {
                '0': ('q2', '0', 'L'),
                'x': ('q0', 'x', 'R'),
                'y': ('q2', 'y', 'L')
            },
            'q14': {
                '0': ('q2', '0', 'L'),
                'x': ('q0', 'x', 'R'),
                'y': ('q2', 'y', 'L')
            },
        },
        initial_state='q0',
        blank_symbol='.',
        final_states={'q14'}
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