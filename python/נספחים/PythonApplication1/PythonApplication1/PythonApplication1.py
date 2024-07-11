import pygame
from sys import exit
from random import randint, choice 


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_walk_1 = pygame.image.load('graphics/player/charedi_walk_1.png').convert_alpha()
		player_walk_2 = pygame.image.load('graphics/player/charedi_walk_2.png').convert_alpha()
		self.player_down = pygame.image.load('graphics/player/charedi_down.png').convert_alpha()
		
		self.player_walk = [player_walk_1,player_walk_2]
		self.player_index = 0
		self.player_jump = pygame.image.load('graphics/player/charedi_walk_2.png').convert_alpha()
		

		self.image = self.player_walk[self.player_index]
		
		self.rect = self.image.get_rect(midbottom = (80,300))
		self.gravity = 0
		
		self.jump_sound = pygame.mixer.Sound('audio/jump_sound1.mp3')
		
		self.is_down = False

	def player_input(self):
		self.keys = pygame.key.get_pressed()
		if self.keys[pygame.K_SPACE] and self.rect.bottom >= 300:
			self.gravity = -20
			self.jump_sound.play()
			
		if self.keys[pygame.K_DOWN]and self.rect.bottom >= 300:
			self.is_down=True
		else:
			self.is_down= False
		
	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 300:
			self.rect.bottom = 300

	def animation_state(self):
		if self.rect.bottom < 300: 
			self.image = self.player_jump
			
		elif self.is_down:
			self.image =self.player_down
			self.rect.y += 40
		 	
		else:
			
			self.player_index += 0.1
			if self.player_index >= len(self.player_walk):
				self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]

	def update(self):
		self.player_input()
		self.apply_gravity()
		self.animation_state()
		
class Obstacle(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()
		
		if type == 'fly':
			fly_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
			fly_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
			self.frames = [fly_1,fly_2]
			y_pos = 210
		if type == 'woman1':
			woman_1 = pygame.image.load('graphics/woman/woman1.png').convert_alpha()
			woman_2 = pygame.image.load('graphics/woman/woman2.png').convert_alpha()
			self.frames = [woman_1,woman_2]
			y_pos  = 300
		if type == 'woman2':
			woman_1 = pygame.image.load('graphics/woman/woman2_1.png').convert_alpha()
			woman_2 = pygame.image.load('graphics/woman/woman2_2.png').convert_alpha()
			woman_3 = pygame.image.load('graphics/woman/woman2_3.png').convert_alpha()
			woman_4 = pygame.image.load('graphics/woman/woman2_4.png').convert_alpha()
			woman_5 = pygame.image.load('graphics/woman/woman2_5.png').convert_alpha()
			self.frames = [woman_1,woman_2,woman_3,woman_4,woman_5]
			y_pos  = 300

		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

	def animation_state(self):
		self.animation_index += 0.1 
		if self.animation_index >= len(self.frames): self.animation_index = 0
		self.image = self.frames[int(self.animation_index)]
		
	def destroy(self):
		if self.rect.x <= -100: 
			self.kill()
			
	def update(self):
		self.animation_state()
		self.rect.x -= 6
		self.destroy()
 
class Coin(pygame.sprite.Sprite):
    cont = 0

    def __init__(self, type):
        super().__init__()
        coin1 = pygame.image.load('graphics/coin/coin1.png').convert_alpha()
        coin2 = pygame.image.load('graphics/coin/coin2.png').convert_alpha()
        coin3 = pygame.image.load('graphics/coin/coin3.png').convert_alpha()
        coin4 = pygame.image.load('graphics/coin/coin4.png').convert_alpha()
        coin5 = pygame.image.load('graphics/coin/coin5.png').convert_alpha()
        coin6 = pygame.image.load('graphics/coin/coin6.png').convert_alpha()
        self.frames = [coin1, coin2,coin3,coin4,coin5,coin6]
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), 100))
		
    def animation_of_coin(self):
        self.animation_index += 0.2
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def coin_destroy(self):
        if collision_coin_sprite():  
            self.kill()
            Coin.cont +=1			
			
    def update(self):
        self.animation_of_coin()
        self.rect.x -= 6
        self.coin_destroy()


def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
	score_rect = score_surf.get_rect(center = (400,50))
	screen.blit(score_surf,score_rect)
	return current_time

def collision_sprite():
	if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
		bg_music.set_volume(0.0)
		sound_end = pygame.mixer.Sound('audio/game_over.mp3')
		sound_end.play()
		obstacle_group.empty()
		return False
	else: return True

def collision_coin_sprite():
	if pygame.sprite.spritecollide(player.sprite,coin_group,False):
		coin_sound = pygame.mixer.Sound('audio/coin_sound.wav')
		coin_sound.play()
		return True
	else:return False

def Screen_coin():
	coin_show = test_font.render(f'coins : {Coin.cont}',False,"gold")
	coin_rect = coin_show.get_rect(center = (700,20))
	screen.blit(coin_show,coin_rect)




pygame.init()
screen = pygame.display.set_mode((800,400))

pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
 
game_active = False
start_time = 0
score = 0

#sound of game
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.5)
bg_music.play(loops = -1)

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Intro screen
player_stand = pygame.image.load('graphics/player/charedi_stert.png').convert_alpha()
#player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,170))

game_name = test_font.render('Charedi Runner',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,50))

game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))


# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,2000)

coin_timer = pygame.USEREVENT + 2
pygame.time.set_timer(coin_timer,3000) 

#Loop variables
coin_x=0
record_of_score=0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		if game_active:
			if event.type == obstacle_timer:
				obstacle_group.add(Obstacle(choice(['fly','woman2','woman1','woman2'])))
				
			if event.type == coin_timer:
				coin_group.add(Coin("coin"))
				
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				start_time = int(pygame.time.get_ticks() / 1000)


	if game_active:
		bg_music.set_volume(0.5)
		coin_x = Coin.cont
		screen.blit(sky_surface,(0,0))
		screen.blit(ground_surface,(0,300))
		score = display_score()
		Screen_coin()
		if record_of_score<score:
			record_of_score=score
		
		player.draw(screen)
		player.update()

		obstacle_group.draw(screen)
		obstacle_group.update()

		coin_group.draw(screen)
		coin_group.update()
		
		game_active = collision_sprite()
		
	
		
		
		  
	else:
		
		
		Coin.cont=0
		
		screen.fill((94,129,162))
		screen.blit(player_stand,player_stand_rect)

		
		score_message = test_font.render(f'Your score: {score}   Record :{record_of_score}',False,(111,196,169))
		score_message_rect = score_message.get_rect(center = (400,300))
		screen.blit(game_name,game_name_rect)

		coin_message = test_font.render(f"Your coins : {coin_x}", False,(111,196,169))
		coin_message_rect = coin_message.get_rect(center = (400,330)) 
		
		
		game_message_end_rect = game_message.get_rect(center = (400,360))

		
		if score == 0:
			screen.blit(game_message,game_message_rect)
			
		else:
			screen.blit(score_message,score_message_rect)
			screen.blit(coin_message,coin_message_rect)
			screen.blit(game_message,game_message_end_rect)
		

	pygame.display.update()
	clock.tick(60)
	
