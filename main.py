import pygame 

pygame.init()

w,h=740,300

m_second = 0
second = 0
minute = 0
clock = 0

stop = 0
start = 0

ekran = pygame.display.set_mode((w,h))
pygame.display.set_caption('Stopwatch ')
fps = pygame.time.Clock()

font = pygame.font.Font('Jersey10-Regular.ttf',240)
font2 = pygame.font.Font('Jersey10-Regular.ttf',90)

text_stop_rect = pygame.Rect(276,220,154,56)
text_reset_rect = pygame.Rect(486,220,184,56)
text_start_rect = pygame.Rect(26,220,186,56)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if text_stop_rect.collidepoint(mouse_pos): 
                stop = 1

            if text_reset_rect.collidepoint(mouse_pos): 
                m_second = 0
                second = 0
                minute = 0
                clock = 0

            if text_start_rect.collidepoint(mouse_pos): 
                start = 1
                stop = 0

    if start == 1 and stop==0:
        m_second += 1
        if m_second >= 100:
            m_second = 0
            second += 1  
            if second >= 60:
                second = 0
                minute += 1
                if minute >= 60:
                   minute = 0
                   clock += 1

    ekran.fill((255,255,255))
    text_clock = font.render(f'{clock}:{minute}:{int(second)}:{m_second}',True,(0,0,0))
    pygame.draw.rect(ekran,(255,250,245),text_stop_rect)
    pygame.draw.rect(ekran,(255,250,245),text_reset_rect)
    pygame.draw.rect(ekran,(255,250,245),text_start_rect)
    text_stop = font2.render('STOP',True,(0,0,0))
    text_reset = font2.render('RESET',True,(0,0,0))
    text_start = font2.render('START',True,(0,0,0))
    ekran.blit(text_clock,(30,-30))
    ekran.blit(text_stop,(280,200))
    ekran.blit(text_reset,(490,200))
    ekran.blit(text_start,(30,200))
    pygame.display.flip()
    fps.tick(20)
pygame.quit()