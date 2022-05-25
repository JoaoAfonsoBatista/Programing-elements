#módulo da agenda.
#uma agenda é representada por uma lista de eventos
#os eventos estão ordenados por ordem crescente de tempo, ou seja,
#o evento que vai acontecer primeiro está em primeiro lugar, o segundo em segundo...

import eventos
import moleculas
import math

def newa():
    return []

def coloca1(e,a):
    d=0
    w=True
    a1=[]
    a2=[]
    while d<len(a) and w:
        if eventos.tempo(a[d])<=eventos.tempo(e):
            a1 = a1 + [a[d]]
            d=d+1
        else:
            w=False
            a2=a[d:]
    a=a1+[e]+a2
    return a
#junta um evento à lista



def eliminaproximo(a):
    if len(a)==0:
        return a
    else:
        return a[1:]
#elimina o próximo evento na agenda

def coloca(e,a):
    lo=-1
    up=len(a)
    while up-lo>1:
        mid=math.floor((lo+up)/2)
        if eventos.tempo(a[mid])<eventos.tempo(e):
            lo=mid
        else:
            up=mid
    return a[:up]+[e]+a[up:]
#novo coloca

def eliminaid(id,a):
    if len(a)==0:
        return a
    else:
        d=0
        w=True
        while d<len(a) and w:
            if moleculas.identificador(eventos.molecula(a[d]))==id:
                w=False
            else:
                d=d+1
        if w:
            return a
        else:
            a1=a[:d]
            a2=a[d+1:]
            a=a1+a2
            return a
                
        
#elimina eventos direcionados a uma molécula específica, idenficada pelo seu
#identificador molecular

def eliminam(m,a):
    if len(a)==0:
        return a
    else:
        d=0
        while d<len(a):
            if eventos.molecula(a[d])==m:
                a=a[:d]+a[d+1:]
            else:
                d=d+1
        return a
#elimina um evento identificado pela sua molécula alvo 

def proximoe(a):
    if len(a)>0:
        return a[0]
    else:
        return[10000000,"cisao",[0,0,0]]
#ver qual é o próximo evento

def ver(a):
    return a

def numeroeventos(a):
    return len(a)
#numero de eventos agendados em a

def primeiroevento(w):
    d=0
    e=w[0]
    while d<len(w):
        if eventos.tempo(w[d])<eventos.tempo(e):
            e=w[d]
            d=d+1
        else:
            d=d+1
    return e

#w é uma lista de eventos. a definição calcula o evento com o tempo menor
#para ser adicionado a agenda

def eventoposicao(n,a):
    return a[n]
#devolve o evento que está na posição n de uma agenda