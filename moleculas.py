#módulo moléculas
#cada molécula é representada por uma lista com 3 elementos
#o número de carbonos da molécula
#o número de eletrões livres da molécula
#o identificar molécular, para diferenciar cada molécula

import random

identificadormolecular=0

def novamolecula(n):
    global identificadormolecular
    identificadormolecular = identificadormolecular + 1
    return [n,0,identificadormolecular]
#uma nova molécula com n carbonos

def novoradical1(n):
    global identificadormolecular
    identificadormolecular = identificadormolecular + 1
    return [n,1,identificadormolecular]
#uma nova molécula que é um radical livre com n carbonos e 1 eletrão livre

def novoradical2(n):
    global identificadormolecular
    identificadormolecular = identificadormolecular + 1
    return [n,2,identificadormolecular]
#uma nova molédcula que é um radical livre com n carbonos e 2 eletrao livres

def novoalceno():
    global identificadormolecular
    identificadormolecular = identificadormolecular + 1
    return [2,"alceno",identificadormolecular]
#forma um novo alceno, só vai ser usado para colocar alcenos no condensador,
#porque mal ele se forma na solução evapora instantaneamente

def carbonos(m):
    return m[0]
#número de arbonos de m

def ordem(m):
    return m[1] 
#devolve o número de eletrões livre. equivalente à "ordem" da molécula

def identificador(m):
    return m[2]
#devolve o identificador molecular da molécula m
    
def radQ(m):
    if m[1]==0 or m[1]=="alceno":
        return False
    else:
        return True
#devolve True se a molécula for um radical e falso em caso contrário

def alcenoQ(m):
    if m[1]=="alceno":
        return True
    else:
        return False

def cisao(m):
    p=random.randint(1,m[0]-1)
    if m[1]==0:
        m1=novoradical1(p)
        m2=novoradical1(m[0]-p)
    elif m[1]==1:
        m1=novoradical2(p)
        m2=novoradical1(m[0]-p)
    else:
        m1=novoradical2(p)
        m2=novoradical2(m[0]-p)
    return m1,m2
        
#divide molécula em 2. atribuindo os eletroes livres às moléculas resultantes

def cisaobeta(m):
    assert m[1]!=0 and not alcenoQ(m)
    if m[1]==1:
        m1=novoradical1(m[0]-2)
    else:
        m1=novoradical2(m[0]-2)
    return m1
#cisao beta de radicais livres, nao esquecer que, apos este tipo de cisao
#entra no condensaor um alceno.

def combinarad(m1,m2):
    assert radQ(m1) and radQ(m2)
    if m1[1]==1 and m2[1]==1:
        m=novamolecula(m1[0]+m2[0])
    elif m1[1]==2 and m2[1]==2:
        m=novoradical2(m1[0]+m2[0])
    else:
        m=novoradical1(m1[0]+m2[0])
    return m      
#combina dois radicais      