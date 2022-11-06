import pygame, sys,time, random
#importamos librerias

#speed velocidad
speed= 13

#tamaño de la ventana
tamaño_ancho=720
tamaño_alto=480


check_errors = pygame.init()
if(check_errors[1]>0):
    print("Error "+ check_errors[1])
else:
    print("Iniciando juego Snake ")  
    
#Se abre la ventana del juego

pygame.display.set_caption("Snake Game")
game_Window = pygame.display.set_mode((tamaño_ancho, tamaño_alto))

# Colores de los objetos del juego
black = pygame.Color(0,0,0)
white =pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green= pygame.Color(0,255,0)
blue= pygame.Color(0,0,255)

#logica juego
fps_controller = pygame.time.Clock()
#tamaño de serpient x cuadro
cuadro_tamaño=20
def init_vars():
    #definir variables generales para definir tamaños y posiciones de los objetos
    global head_pos, snake_body, food_pos, food_spawn, score, direction
    direction = "RIGHT"
    head_pos = [120,60]
    snake_body =[[120,60]]
    food_pos = [random.randrange(1,(tamaño_ancho//cuadro_tamaño))* cuadro_tamaño,
                random.randrange(1,(tamaño_alto//cuadro_tamaño))* cuadro_tamaño]
    food_spawn = True
    score =0
    
init_vars()

def show_Score(choice, color, font, size):
    score_font = pygame.font.SysFont(font,size)
    score_surface = score_font.render("Score: "+ str(score),True,color)
    score_rect = score_surface.get_rect()
    if choice ==1:
        score_rect.midtop = (tamaño_ancho/10,15)
    else:
        score_rect.midtop = (tamaño_ancho/2, tamaño_alto/1.25)
    game_Window.blit(score_surface,score_rect)

    #print("showing score")
    
#Game Loop 
# Restriciones d emovimiento de serpiente
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key ==pygame.K_UP or event.key == ord("w")
                and direction != "DOWN"):
                direction = "UP"
            elif (event.key ==pygame.K_DOWN or event.key == ord("s")
                and direction != "UP"):
                direction = "DOWN"
            elif (event.key ==pygame.K_LEFT or event.key == ord("a")
                and direction != "RIGHT"):
                direction = "LEFT"
            elif (event.key ==pygame.K_RIGHT or event.key == ord("d")
                and direction != "LEFT"):
                direction = "RIGHT"
# restriciones de moverse en extremos de la pantalla
    if direction =="UP":
        head_pos[1] -= cuadro_tamaño
    elif direction =="DOWN":
        head_pos[1] += cuadro_tamaño
    elif direction== "LEFT":
        head_pos[0]-= cuadro_tamaño
    else:
        head_pos[0] += cuadro_tamaño
        
    if head_pos[0] <0:
        head_pos[0] = tamaño_ancho - cuadro_tamaño
    elif head_pos[0] > tamaño_ancho-cuadro_tamaño:
        head_pos[0]=0
    elif head_pos[1]<0:
        head_pos[1] =tamaño_alto-cuadro_tamaño
    elif head_pos[1] > tamaño_alto-cuadro_tamaño:
        head_pos[1]=0
    #colision con manza
    snake_body.insert(0,list(head_pos))
    if head_pos[0]== food_pos[0] and head_pos[1]== food_pos[1]:
        score +=5
        food_spawn =False
    else:
        snake_body.pop()
        
    # aparicion manzana // posicion - y cuando ocurre
    if not food_spawn:
        food_spawn = [random.randrange(1,(tamaño_ancho//cuadro_tamaño))* cuadro_tamaño,
                random.randrange(1,(tamaño_alto//cuadro_tamaño))* cuadro_tamaño]
        food_spawn =True
    #GFX
    game_Window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_Window,green,pygame.Rect(
            
            pos[0]+2,pos[1] +2,
            cuadro_tamaño-2,cuadro_tamaño ))
    # dibujarr uwu
    
    pygame.draw.rect(game_Window,red,pygame.Rect(food_pos[0],
                    food_pos[1],cuadro_tamaño,cuadro_tamaño )) 
    
    #condiciones apra que termine el juego
    
    for block in snake_body[1:]:
        if head_pos[0]== block[0] and head_pos[1] == block[1]:
            init_vars()
        # se vuelve a iniciar el juego con bvalores iniciales
        
    show_Score(1,white,'consolas',20)
    pygame.display.update()
    fps_controller.tick(speed)






    
    
    