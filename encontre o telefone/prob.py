#problema: http://dojopuzzles.com/problemas/exibe/encontre-o-telefone/#
import sys
#cria todas as letras maiusculas
letras = [chr(i) for i in range(65, 91)]
valores = {'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5, 'MNO': 6, 'PQRS':7,
           'TUV': 8, 'WXYZ': 9}

def get_valor(letra: chr)->int:
    '''recebe um caracetere e retorna o inteiro correspondente do valor'''
    for key in valores:
        if letra in key:
            return valores[key]

#lê cada linha até EOF
for linha in sys.stdin:
    #itera a string
    for letra in linha:
        #se for uma letra chama a função
        print(get_valor(letra) if letra in letras else letra, end='')
