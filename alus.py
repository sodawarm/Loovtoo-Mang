import pygame, sys

pygame.init()
screen = pygame.display.set_mode([1280,720])
pygame.display.set_caption("Seiklusmäng")

def vastus(pildi_aadress, küsimus, valikud):
  
    pilt = pygame.image.load(pildi_aadress)
    pilt = pygame.transform.scale(pilt, (1280, 720))
    laius = pilt.get_width()
    kõrgus = pilt.get_height()

    myfont = pygame.font.SysFont("monospace", 32, bold=True)
    myfont2 = pygame.font.SysFont("monospace", 24, bold=True, italic=False)

    question = myfont2.render(küsimus, 1, (255,225,225))
    labels = [myfont.render(e, 1, (255,255,255)) for e in valikud]
    labels_select = [myfont.render(e, 1, (255,0,0)) for e in valikud]

    suurim_tekst = max([l.get_width() + 70 for l in labels+[question]])

    screen = pygame.display.set_mode([max(suurim_tekst, laius), kõrgus + 70 + len(valikud) * 50])
    
    while True:

        x, y = pygame.mouse.get_pos()
        
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(valikud)):
                    if y > kõrgus + 70 + 50 * i and y < kõrgus + 70 + 50 * i + 32:
                        return valikud[i]
                
        screen.fill([0,0,0])
        screen.blit(pilt, [0, 0])
        
        screen.blit(question, (20, kõrgus + 20))
        for i in range(len(labels)):
            if y > kõrgus + 70 + 50 * i and y < kõrgus + 70 + 50 * i + 32:
                screen.blit(labels_select[i], (50, kõrgus + 70 + 50 * i))
            else:
                screen.blit(labels[i], (50, kõrgus + 70 + 50 * i))
                
        pygame.display.flip()
        pygame.time.delay(16)

def plt(pildi_aadress, teade):
    vastus(pildi_aadress, teade, ["Fin"])
    

if __name__ == "__main__":
    pygame.quit()
