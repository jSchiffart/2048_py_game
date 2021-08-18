#Import das funções dos outro ficheiros python para decorrer o jogo.
from j2048_motor_45122 import novo_jogo
from j2048_motor_45122 import esquerda
from j2048_motor_45122 import direita
from j2048_motor_45122 import acima
from j2048_motor_45122 import abaixo
from j2048_gestor_45122 import regista_jogada
from j2048_gestor_45122 import regista_pontos
from j2048_gestor_45122 import escreve_registo
from j2048_gestor_45122 import le_identificacao
from j2048_gestor_45122 import inicializa_semente
from j2048_gestor_45122 import regista_grelha_inicial
import pygame
#Inicializar o pygame.
pygame.init()

#definiçao de variaveis necessarias ao longo do codigo
le_identificacao()
inicializa_semente(None)
#jogo novamente é um tuplo
jogo=novo_jogo()
g=jogo[0]
fim=jogo[1]
vitoria=jogo[2]
pontos=jogo[3]
regista_grelha_inicial=(g[0][0], g[0][1], g[0][2], g[0][3],
                                 g[1][0], g[1][1], g[1][2], g[1][3],
                                 g[2][0], g[2][1], g[2][2], g[2][3],
                                 g[3][0], g[3][1], g[3][2], g[3][3])

######janela principal######
largura=800
altura=500
tamanho=(largura, altura)
janela=pygame.display.set_mode(tamanho)#define tamanho janela
clock=pygame.time.Clock()
pygame.display.set_caption("João Schiffart - Jogo do 2048")#nome da janela


antialias=True #suaviza o texto
frame_rate=60 #Define a framerate do jogo.
nova_frame=None
fim=False

#load das imagens
inicial      = pygame.image.load("realbackground.jpg")#fundo intro
b_play       = pygame.image.load("Start1.png")#botao play da intro
b_playrato   = pygame.image.load("Start2.png")#botao play com rato em cima
b_voltar     = pygame.image.load("back1.png")#botao voltar
b_voltarrato = pygame.image.load("back2.png")#botao voltar com rato em cima
jogojanela   = pygame.image.load("Background.jpg")#janela de jogo

#load das imagens dos numeros
nume2      = pygame.image.load("2pronto.jpg")#numero 2 na grelha
nume4      = pygame.image.load("4pronto.jpg")#numero 4 na grelha
nume8      = pygame.image.load("8pronto.jpg")#numero 8 na grelha
nume16     = pygame.image.load("16pronto.jpg")#numero 16 na grelha
nume32     = pygame.image.load("32pronto.jpg")#numero 32 na grelha
nume64     = pygame.image.load("64pronto.jpg")#numero 64 na grelha
nume128    = pygame.image.load("128pronto.jpg")#numero 128 na grelha
nume256    = pygame.image.load("256pronto.jpg")#numero 256 na grelha
nume512    = pygame.image.load("512pronto.jpg")#numero 512 na grelha
nume1024   = pygame.image.load("1024pronto.jpg")#numero 1024 na grelha
nume2048   = pygame.image.load("2048pronto.jpg")#numero 2048 na grelha
nume4096   = pygame.image.load("4096pronto.jpg")#numero 4096 na grelha
nume8192   = pygame.image.load("8192pronto.jpg")#numero 8192 na grelha
nume16384  = pygame.image.load("16384pronto.jpg")#numero 16384 na grelha
nume32768  = pygame.image.load("32768pronto.jpg")#numero 32768 na grelha
nume65536  = pygame.image.load("65536pronto.jpg")#numero 65536 na grelha
nume131072 = pygame.image.load("131072pronto.jpg")#numero 131072




#posiçao das quadriculas da grelha
x0=350
x1=450
x2=550
x3=650

y0=50
y1=150
y2=250
y3=350

pos0=(x0,y0)
pos1=(x1,y0)
pos2=(x2,y0)
pos3=(x3,y0)
pos4=(x0,y1)
pos5=(x1,y1)
pos6=(x2,y1)
pos7=(x3,y1)
pos8=(x0,y2)
pos9=(x1,y2)
pos10=(x2,y2)
pos11=(x3,y2)
pos12=(x0,y3)
pos13=(x1,y3)
pos14=(x2,y3)
pos15=(x3,y3)

pos_grelha=[[pos0,pos1,pos2,pos3],
            [pos4,pos5,pos6,pos7],
            [pos8,pos9,pos10,pos11],
            [pos12,pos13,pos14,pos15]]


#Defenir uma função para os botões.
def botao_carregavel(x,y,l,h,i,a,acao=None): #coordenada x, coordenada y, l=largura, h=altura, inativo, ativo, acao
    rato=pygame.mouse.get_pos()#verifica onde esta o cursos do rato
    click=pygame.mouse.get_pressed()#verifica se algum botao do rato esta a ser precionado
    #Quando a posição do rato se encontra entre as coordenadas entre a largura e a altura, o botão muda de sprite.
    if x+l>rato[0]>x and y+h>rato[1]>y:
        janela.blit(a, (x, y))
        #Ao clicar no botão acontece a acao.
        if click[0]==1 and acao !=None:
            acao()
    else:
        janela.blit(i, (x, y))


#Codigo da pagina inicial.
def intro_jogo():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        janela.blit(inicial, (0,0))
        botao_carregavel(150,350,234,95, b_play, b_playrato, jogar_jogo)
        pygame.display.update()
#funçao geral do jogo, a função é chamada quando suposto começar o jogo.
def jogar_jogo():
    fim=False
    jogar=True
    while jogar:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()


        #display os pontos#
        def pontuacao(pontos):
            letra=pygame.font.Font("emulogic.ttf",20)
            pontuacao_texto=letra.render("Pontos:"+str(pontos), 1,(154,222,24))
            janela.blit(pontuacao_texto, (100, 70))

        #controi uma nova frame sempre que ha uma jogada  
        def construir_nova_frame():
            global nova_frame
            global jogo
            nova_frame=pygame.Surface(tamanho)
            nova_frame.blit(jogojanela, (0,0))
            numeros_com_imagem()
            
        #define as imagens para os numeros
        def numeros_com_imagem():
            global jogo
            global pos_grelha
            grelha=jogo[0]
            for l in range(len(grelha)):
                for c in range(len(grelha[0])):
                    if(grelha[l][c]==2):
                        nova_frame.blit(nume2,pos_grelha[l][c])
                    if(grelha[l][c]==4):
                        nova_frame.blit(nume4,pos_grelha[l][c])
                    if(grelha[l][c]==8):
                        nova_frame.blit(nume8,pos_grelha[l][c])
                    if(grelha[l][c]==16):
                        nova_frame.blit(nume16,pos_grelha[l][c])
                    if(grelha[l][c]==32):
                        nova_frame.blit(nume32,pos_grelha[l][c])
                    if(grelha[l][c]==64):
                        nova_frame.blit(nume64,pos_grelha[l][c])
                    if(grelha[l][c]==128):
                        nova_frame.blit(nume128,pos_grelha[l][c])
                    if(grelha[l][c]==256):
                        nova_frame.blit(nume256,pos_grelha[l][c])
                    if(grelha[l][c]==512):
                        nova_frame.blit(nume512,pos_grelha[l][c])
                    if(grelha[l][c]==1024):
                        nova_frame.blit(nume1024,pos_grelha[l][c])
                    if(grelha[l][c]==2048):
                        nova_frame.blit(nume2048,pos_grelha[l][c])
                    if(grelha[l][c]==4096):
                        nova_frame.blit(nume4096,pos_grelha[l][c])
                    if(grelha[l][c]==8192):
                        nova_frame.blit(nume8192,pos_grelha[l][c])
                    if(grelha[l][c]==16384):
                        nova_frame.blit(nume16384,pos_grelha[l][c])
                    if(grelha[l][c]==32768):
                        nova_frame.blit(nume32768,pos_grelha[l][c])
                    if(grelha[l][c]==65536):
                        nova_frame.blit(nume65536,pos_grelha[l][c])
                    if(grelha[l][c]==131072):
                        nova_frame.blit(nume131072,pos_grelha[l][c])

#define as teclas para cada funçao
        tecla=None
        def jogadas():
            global fim
            global jogo
            global tecla
            global pontos
            pontos=jogo[3]
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    fim=True
                    regista_pontos(jogo[3])
                    mensagem_cloud=escreve_registo()
                    print(jogo[3])
                    print(mensagem_cloud)
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        jogo=esquerda(jogo)
                        tecla='a'
                        regista_jogada(tecla)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        jogo=direita(jogo)
                        tecla='d'
                        regista_jogada(tecla)
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        jogo=acima(jogo)
                        tecla='w'
                        regista_jogada(tecla)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        jogo=abaixo(jogo)
                        tecla='s'
                        regista_jogada(tecla)
                    elif event.key == pygame.K_t:
                        fim=True
                        regista_pontos(jogo[3])
                        mensagem_cloud=escreve_registo()
                        print(jogo[3])
                        print(mensagem_cloud)
                        pygame.quit()
                        quit()

                    elif event.key == pygame.K_r:
                        jogo=novo_jogo()


#ciclo while que mantem as imagens mostradas atualizadas
#Se não existir ciclo while o jogo não da update, assim não seriam representados
#os outputs no pygame.
        while not(fim):
            jogadas()
            construir_nova_frame()
            # actualizar pygame com a nova imagem
            janela.blit(nova_frame, (0, 0))
            botao_carregavel(77,452,119,63, b_voltar, b_voltarrato, intro_jogo)
            pontuacao(pontos)
            pygame.display.flip()
            pygame.display.update()
            clock.tick(frame_rate)


intro_jogo()
jogar_jogo()
pygame.quit()
quit()
