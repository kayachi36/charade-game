#Bibliotheques
import pygame
import random


#Screen specifities
WIDTH = 550
HEIGHT = 450
GREEN = (0,255,0)
BLACK = (0,0,0)
RED= (255,0,0)
BLUE= (0,0,255)
WHITE = (255,255,255)

#Data
mon_premier= ["se trouve dans la gueule du loup.", "est un oiseau noir à queue blanche.", "est au milieu de la figure.", "ouvre les portes.", "est le contraire de haut.", "se trouve au milieu du visage.", "est entre 1 et 3.", "est un animal qui vit sur les têtes.", "est un insecte qui vit dans les cheveux.", "est le trou d’une aiguille.", "se trouve sur le visage des personnes âgées.", "est un objet qui sert à faire le ménage.", "est un animal herbivore.", "est un métal précieux.", "est un rongeur à queue longue."]
#rep_premier= ["croc", "pie", "nez", "clé", "bas", "nez", "deux", "pou", "poux", "chas", "ride", "sceau ", "cerf", "or", "rat"]
mon_deuxieme= ["est indispensable à la vie.", "coule dans mon corps ", "est le contraire d'habillé.", "est vitale.", "est le contraire de rapide.", "est un métal. ", "est l'inverse de la mort.", "est le liquide que nous donnent les vaches.", "est le contraire de laide.", "est un poisson.", "est une boisson.", "est une petite montagne.", "est le roi de la volaille. Très joli.", "est un habitant des cieux.", "est le contraire de tard"]
#rep_deuxieme= ["eau", "sang", "nu", "eau", "lent", "fer", "vie", "Lait", "belle", "thon", "eau", "mont", "paon", "ange", "tôt "]
mon_troisieme= ["est un jeu.", "est l'objet ou l'on dort.", "dirige les bateaux en mer la nuit.", "est garde les troupeaux.", "est le contraire de matin.", "est un célèbre canari que gros minet aimerait bien manger.", "est l'inverse de flou.","", "", "", "", "", "", "",""]
#rep_troisieme=["dé", "lit", "phar", "pâtre", "soir", "titi", "nez", "", "", "", "", "", "", "",""]
mon_quatrieme= ["est au milieu de la mer.", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
#rep_quatrieme=["ile", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
mon_tout= ["vit dans les fleuve d’Amazonie.", "est une fleur.", "est une fleur sur l'eau.", "est un(e) grand personnage historique !", "s’accroche aux branches des arbres.", "a été une reine d’Égypte.", "est ce que tu fais en pensant au tout.", "est bon quand il est rôti.", "est vide dans un camion", "est un bébé animal.", "est un tissus.", "est un poisson très bon.", "est un reptile venimeux.", "est un fruit délicieux.", "est un objet utile quand on fait le jardin."]
rep_tout= ["crocodile", "pissenlit", "nenuphar", "cleopatre", "balancoire", "nefertiti", "devinette", "poulet", "poubelle", "chaton", "rideau", "saumon", "serpent", "orange", "rateau "]

#Input
rep_user = ["","","",""]

#initialistation de pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
fond = pygame.image.load("background00.jpg").convert()

font_name = pygame.font.match_font('times new roman')
def draw_text(surface,color,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,color)
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surface.blit(text_surface,text_rect)

userInput = ""
currentCharade = random.randint(0,14)
score = 0
correctVisible = False
compteur = 0
listIndexUsedCharade = []
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN and compteur < 4:
			if event.key == pygame.K_a:
				userInput = userInput + 'a'
			if event.key == pygame.K_b:
				userInput = userInput + 'b'
			if event.key == pygame.K_c:
				userInput = userInput + 'c'
			if event.key == pygame.K_d:
				userInput = userInput + 'd'
			if event.key == pygame.K_e:
				userInput = userInput + 'e'
			if event.key == pygame.K_f:
				userInput = userInput + 'f'
			if event.key == pygame.K_g:
				userInput = userInput + 'g'
			if event.key == pygame.K_h:
				userInput = userInput + 'h'
			if event.key == pygame.K_i:
				userInput = userInput + 'i'
			if event.key == pygame.K_j:
				userInput = userInput + 'j'
			if event.key == pygame.K_k:
				userInput = userInput + 'k'
			if event.key == pygame.K_l:
				userInput = userInput + 'l'
			if event.key == pygame.K_m:
				userInput = userInput + 'm'
			if event.key == pygame.K_n:
				userInput = userInput + 'n'
			if event.key == pygame.K_o:
				userInput = userInput + 'o'
			if event.key == pygame.K_p:
				userInput = userInput + 'p'
			if event.key == pygame.K_q:
				userInput = userInput + 'q'
			if event.key == pygame.K_r:
				userInput = userInput + 'r'
			if event.key == pygame.K_s:
				userInput = userInput + 's'
			if event.key == pygame.K_t:
				userInput = userInput + 't'
			if event.key == pygame.K_u:
				userInput = userInput + 'u'
			if event.key == pygame.K_v:
				userInput = userInput + 'v'
			if event.key == pygame.K_w:
				userInput = userInput + 'w'
			if event.key == pygame.K_x:
				userInput = userInput + 'x'
			if event.key == pygame.K_y:
				userInput = userInput + 'y'
			if event.key == pygame.K_z:
				userInput = userInput + 'z'
			if event.key == pygame.K_BACKSPACE:
				userInput = userInput[0:len(userInput)-1]
			#reste a faire les autres lettre de aphabet, notemment accents
			if event.key == pygame.K_SPACE:
				print(userInput)
				print(currentCharade)
				if userInput == rep_tout[currentCharade]:
					print('passed')
					score += 1
					compteur += 1
					currentCharade	 = random.randint(0,15)
					while (currentCharade  in listIndexUsedCharade):
						currentCharade	= random.randint(0,15)
						pass
					listIndexUsedCharade += [currentCharade]
		
					userInput = ''
					correctVisible = False

				else:
					correctVisible = True

					#afficher msg bonne rep
			
					#afficher msg mauv rep
	screen.blit(fond, (0,0))

	if ( compteur < 4): 
		draw_text(screen,BLACK,'Mon premier ' + mon_premier[currentCharade],16,WIDTH/2,120)
		draw_text(screen,BLACK,'Mon deuxieme ' + mon_deuxieme[currentCharade],16,WIDTH/2,150)
		if mon_troisieme[currentCharade] != "":
			draw_text(screen,BLACK,'Mon troisieme ' + mon_troisieme[currentCharade],16,WIDTH/2,180)
		if mon_quatrieme[currentCharade] != "":
			draw_text(screen,BLACK,'Mon quatrieme ' + mon_quatrieme[currentCharade],16,WIDTH/2,210)
		draw_text(screen,BLACK,'Mon tout ' + mon_tout[currentCharade],16,WIDTH/2,240)
		draw_text(screen,BLUE,'Votre score est: ' + str(score),16,70,95)
		draw_text(screen,RED,userInput,16,WIDTH/2,280)

		if correctVisible:
			draw_text(screen,BLACK,'Mauvaise reponse , ressayer' ,16,WIDTH/2,300)

	else:
		draw_text(screen,BLACK,'Bravo! Vous pouvez passez au prochain niveau!',16,WIDTH/2,HEIGHT/2)

	pygame.display.update()



pygame.quit()







'''TODOS




change background
change font
change input button ( userInput and score)

'''
























