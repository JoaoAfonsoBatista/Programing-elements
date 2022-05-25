#a solução é uma lista de moléculas

import moleculas
import random

def novasolucao():
    return []

def versolucao(s):
    return s
#mostrar o solucao s

def emptyQ(s):
    if len(s)==0:
        return True
    else:
        return False
#verifica se solucao é vazio ou não
    
def insert(x,s):
    s=s+[x]
    return s
#insere uma molecula x na solucao

def remove(x,s):
    d=0
    w=True
    while d<len(s) and w:
        if x==s[d]:
            s=s[:d]+s[d+1:]
            w=False
        else:
            d=d+1
    return s
#retira uma molecula x em solucao

def removeid(i,s):
    d=0
    w=True
    while d<len(s) and w:
        if moleculas.identificador(s[d])==i:
            s=s[:d]+s[d+1:]
            w=False
        else:
            d=d+1
    return s
#remove a molécula com idenficador molecular i da solução s

def tamanho(s):
    return len(s)
#quantas moleculas tem a solucao

def numeroradicais(s):
    d=0
    r=0
    while d<len(s):
        if moleculas.ordem(s[d])>0:
            r=r+1
            d=d+1
        else:
            d=d+1
    return r
#número de radicais livres na solução

def numeroalcenos(s):
    d=0
    r=0
    while d<len(s):
        if moleculas.alcenoQ(s[d]):
            r=r+1
            d=d+1
        else:
            d=d+1
    return r
#ver quantos alceno tem a solucao

def numeromoleculascomordem(c,e,s):
    d=0
    r=0
    while d<len(s):
        if moleculas.carbonos(s[d])==c and moleculas.ordem(s[d])==e:
            r=r+1
            d=d+1
        else:
            d=d+1
    return r
#quantas moléculas com c carbonos e e eletroes livres existem na solução s

def numeromoleculascomcarbonos(c,s):
    d=0
    r=0
    while d<len(s):
        if moleculas.carbonos(s[d])==c:
            r=r+1
            d=d+1
        else:
            d=d+1
    return r
#quantas moléculas com c carbonos existem na solução s

def contagem(s,n):
    d=1
    r=[]
    z=0
    a=numeroalcenos(s)
    while d<=n:
        z=numeromoleculascomcarbonos(d,s)
        r=r+[[d-1,z]]
        d=d+1
    r[1][1]=r[1][1]-a
    r=r+[["alcenos",a]]
    return r
#devolve lista de lista onde cada sublista tem o número de ligaçoes e o número
#de moléculas com esse número de ligaçoes em s, até n ligações
#utilizada no final para ver o conteúdo do condensador

def contagem1(s,n):
    d=1
    r=[]
    z=0
    while d<=n:
        z=numeromoleculascomcarbonos(d,s)
        r=r+[z]
        d=d+1
    return r

def escolherradical1(m,s):
    r=novasolucao()
    d=0
    while d<len(s):
        if (moleculas.ordem(s[d])==1 or moleculas.ordem(s[d])==2) and s[d]!=m:
            r=insert(s[d],r)
            d=d+1
        else:
            d=d+1
    x=random.randint(1,len(r))
    return r[x-1]
#para escolher um radiccal livre da solução s, que nao seja m, para se combinar com m

def escolherradical(m,s):
    r=random.randint(0,len(s)-1)
    if s[r]!=m and moleculas.ordem(s[r])>0:
        return s[r]
    else:
        return escolherradical(m,s)

def moleculaQ(m,s):
    d=0
    r=False
    while d<len(s) and not r:
        if s[d]==m:
            r=True
        else:
            d=d+1
    return r
#verificar se m está na solução s

def moleculaposicao(n,s):
    return s[n]
#molécuna na posição n da solução s