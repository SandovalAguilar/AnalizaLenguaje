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
                'q14',},
        input_symbols={'a', 'b'},
        tape_symbols={'a', 'b', 'x', 'y', '.'},
        transitions={
            'q0': {
                '.': ('q1', '.' ,'R')
            },
            'q1': {
                'a': ('q2', '.', 'R')
            },
            'q2': {
                'a': ('q2', 'a', 'R'),
                'b': ('q3', 'b', 'R')
            },
            'q3': {
                'a': ('q4', 'a','R')
            },
            'q4': {
                'b': ('q5', 'b', 'R')
            },
            'q5': {
                'b': ('q3', 'b', 'R'),
                '.': ('q6', '.', 'L')
            },
            'q6': {
                'b': ('q7', '.', 'L')
            },
            'q7': {
                'a': ('q8', '.', 'L')
            },
            'q8': {
                'b': ('q9', '.', 'L')
            },
            'q9': {
                '.': ('q10', '.', 'R'),
                'b': ('q11', 'b', 'L')
            },
            'q11': {
                'a': ('q12', 'a', 'L')
            },
            'q12': {
                'b': ('q13', 'b', 'L')
            },
            'q13': {
                'b': ('q11', 'b', 'L'),
                'a': ('q14', 'a', 'L')
            },
            'q14': {
                'a': ('q14', 'a', 'L'),
                '.': ('q1', '.', 'R')
            },
        },
        initial_state='q0',
        blank_symbol='.',
        final_states={'q10'}
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
        
        cadena = '.' + str(input()) + '.'
        
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