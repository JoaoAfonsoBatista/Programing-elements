#módulo dos eventos
#os eventos teem 3 atributos:
#o tempo em que ocorrem, representado pelo primeiro elemento "t"
#o tipo de elemento que são, representado pelo segundo elemento "k"
#em que molécula vão atuar, representado pelo terceiro elemento "m"
#t é um número real, k é uma string e m é uma molécula(lista com 3 elementos)

def evento(t,k,m):
    return [t,k,m]


def mudatemp(t):
    return [t,"temperatura",[0,0,0]]

def tempo(e):
    return e[0]

def kind(e):
    return e[1]

#o tipo dos eventos pode ser:
#"cisao" correspondente à cisão de uma molécula
#"cisaob" correspondente à cisao-beta de um radical livre
#"comb" correspondente à combinação de coisa radicais livres
#"evap" correspondente à evaporação de uma molécula
#"temperatura" correspondente à mudança de temperatura da solução


def molecula(e):
    return e[2]