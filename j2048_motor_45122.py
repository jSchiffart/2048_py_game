
#motor do jogo 2048


from random import random
from random import choice

def get_2ou4():
    x = random()
    if x > 0.1:
        return 2
    else:
        return 4


def obter_posicoes_vazias(g):
    lista_posicoes_vazias = []
    for linha in [0, 1, 2, 3]:
        for coluna in [0, 1, 2, 3]:
            if g[linha][coluna] == 0:
                lista_posicoes_vazias.append([linha, coluna])
    return lista_posicoes_vazias
    

def inserir_2ou4(g):
    #1. obter um 2 ou um 4 com probabilidades 90% e 10%, respetivamente
    #2. obter uma posiçao vazia
    #3. inserir na posiçao (obtida em 2.) de g o valor obtido em 1.
    dois_ou_quatro  = get_2ou4()
    posicoes_vazias = obter_posicoes_vazias(g)
    posicao_vazia   = choice(posicoes_vazias)
    #indices de linha e coluna da posiçao vazia
    linha  = posicao_vazia[0]
    coluna = posicao_vazia[1]
    g[linha][coluna] = dois_ou_quatro
    

def novo_jogo():
    """A operaçao novo "novo_jogo":
1. Coloca todas as posiçoes da grelha vazias;
2. Cloca 2 ou 4, escolhidos aleatoriamente (2 com prob. 90%, e 4 com prob. 10%) em duas posições vazias, escolhidas aleatoriamente.
3. Re-inicializa "fim" a False, "vitoria" a False e "pontos" a 0.
"""
    grelha  = [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]
    fim     = False #bool
    vitoria = False #bool
    pontos  = 0 #int

    inserir_2ou4(grelha)
    inserir_2ou4(grelha)

    return (grelha, fim, vitoria, pontos)

def mover_esquerda(uma_lista):
    resultado=[]
    llista=len(uma_lista)
    for indice in range(llista):
        valor=uma_lista[indice]
        if valor!=0:
            resultado.append(valor)
    while len(resultado)<llista:
        resultado.append(0)
    return resultado

def somar_esquerda(uma_lista):
    resultado=[]
    llista=len(uma_lista)
    pontos=0
    indice=0
    while indice<llista-1:
        valor=uma_lista[indice]
        if valor==uma_lista[indice+1]:
            soma=valor+valor
            resultado.append(soma)
            pontos=pontos+soma
            indice=indice+2
        else:
            resultado.append(valor)
            indice=indice+1
    if indice==llista-1:#tratar a ultima posiçao quando nao é igual à penultima
        resultado.append(uma_lista[indice])
    while len(resultado)<llista:
        resultado.append(0)
    return (resultado, pontos)

def valor(jogo, linha, coluna): #jogo é o tuplo "(grelha, fim, vitoria, pontos)" [acima retornado]
    grelha = jogo[0]
    return grelha[linha-1][coluna-1]


def copiar_grelha(grelha):
    resultado=[]
    numero_linhas=len(grelha)
    numero_colunas=len(grelha[0]) #assume-se que grelha nao é uma lista vazia
    for l in range(numero_linhas):
        nova_linha=[]
        for c in range(numero_colunas):
            nova_linha.append(grelha[l][c])
        resultado.append(nova_linha)
    return resultado

                              
def atualizar_grelha(grelha_inicial,grelha):
    diferentes=False
    numero_linhas=len(grelha)
    numero_colunas=len(grelha[0])
    for l in range(numero_linhas):
        for c in range(numero_colunas):
            if grelha_inicial[l][c]!=grelha[l][c]:
                diferentes=True
    if diferentes==True:
        posicoes_vazias = obter_posicoes_vazias(grelha)
        if len(posicoes_vazias)!=0:
            inserir_2ou4(grelha)


def get_vitoria(grelha):
    numero_linhas=len(grelha)
    numero_colunas=len(grelha[0])
    vitoria=False
    for l in range(numero_linhas):
        for c in range(numero_colunas):
            if grelha[l][c]==2048:
                vitoria=True
    return vitoria


def ha_iguais_adjacentes(grelha):
    ha=False
    numero_linhas=len(grelha)
    numero_colunas=len(grelha[0])
    for l in range(numero_linhas):
        for c in range(numero_colunas-1):
            if grelha[l][c]==grelha[l][c+1]:
                ha=True
    for l in range(numero_linhas-1):
        for c in range(numero_colunas):
            if grelha[l][c]!=0 and grelha[l][c]==grelha[l+1][c]:
                ha=True
    return ha


def get_fim(grelha):
    fim=False
    ha_posicoes_vazias=True
    posicoes_vazias=obter_posicoes_vazias(grelha)
    if len(posicoes_vazias)==0:
        posicoes_vazias=False
    if not(ha_posicoes_vazias) and not(ha_iguais_adjacentes(grelha)):
        print("coisooo")
        fim=True
    return fim


def reverte_linhas(grelha):
    nlinhas=len(grelha)
    ncolunas=len(grelha[0])
    for l in range(nlinhas):
        linha=[0]*ncolunas
        for c in range(ncolunas):
            linha[c]=grelha[l][ncolunas-1-c]
        grelha[l]=linha    
    return grelha


def trocar_linhas_com_colunas(grelha):
    nova_grelha=[]
    for l in range(len(grelha[0])):
        linha=[]
        for c in range(len(grelha)):
            linha.append(grelha[c][l])
        nova_grelha.append(linha)
    return nova_grelha
            
    
def esquerda(jogo): #jogo é o tuplo "(grelha, fim, vitoria, pontos)" [acima retornado]
    grelha=jogo[0]
    fim=jogo[1]
    vitoria=jogo[2]
    pontos=jogo[3]
    grelha_inicial=copiar_grelha(grelha) #fazer copia da grelha para poder comparar com a grelha processada
    numero_linhas=len(grelha)
    for l in range(numero_linhas):
        linha=grelha[l]
        linha2=mover_esquerda(linha)
        (linha3, pontos_a_adicionar)=somar_esquerda(linha2)
        grelha[l]=linha3
        pontos=pontos+pontos_a_adicionar
    atualizar_grelha(grelha_inicial,grelha)
    vitoria=get_vitoria(grelha)
    fim=get_fim(grelha)
    return (grelha, fim, vitoria, pontos)


def direita(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_revertida = reverte_linhas(grelha)
    jogo_revertido = (grelha_revertida, fim, vitoria, pontos)
    jogo_revertido_atualizado = esquerda(jogo_revertido)
    (grelha, fim, vitoria, pontos) = jogo_revertido_atualizado
    grelha_revertida = reverte_linhas(grelha)
    jogo_atualizado = (grelha_revertida, fim, vitoria, pontos)
    return jogo_atualizado


def acima(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)
    jogo_transposto_atualizado = esquerda(jogo_transposto)
    (grelha, fim, vitoria, pontos) = jogo_transposto_atualizado
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_atualizado = (grelha_transposta, fim, vitoria, pontos)
    return jogo_atualizado


def abaixo(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)
    jogo_transposto_atualizado = direita(jogo_transposto)
    (grelha, fim, vitoria, pontos) = jogo_transposto_atualizado
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_atualizado = (grelha_transposta, fim, vitoria, pontos)
    return jogo_atualizado

    
def ganhou_ou_perdeu(jogo): #jogo é o tuplo "(grelha, fim, vitoria, pontos)"
    return jogo[2]


def terminou(jogo): #jogo é o tuplo "(grelha, fim, vitoria, pontos)"
    return jogo[1]

    
def pontuacao(jogo): #jogo é o tuplo "(grelha, fim, vitoria, pontos)"
    return jogo[3]
