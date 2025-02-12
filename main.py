import random, pygame

pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
pygame.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)
pygame.set_caption("American dog!")

clock = pygame.time.Clock()
FPS = 60


score = 0
burger_points = 0
burgers_eaten = 0
PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100
STARTING_BURGER_VELOCITY = 3
BURGER_ACCELERATION = 0.5
BUFFER_DISTANCE = 100

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY
boost_level = STARTING_BOOST_LEVEL
burger_velocity = STARTING_BURGER_VELOCITY

black = (0,0,0)
white = (250,250,250)
orange = (246, 170, 54)


font = pygame.font.Font("WashYourHand.ttf",32)


def prep_text(text: str, background_color: tuple[int, int, int], **locations):
   
    text_to_return = font.render(text, True, background_color)
    rect = text_to_return.get_rect()
    for location in locations:
        if location == "topleft":
            rect.topleft = locations["topleft"]
        elif location == "centerx":
            rect.centerx = locations["centerx"]
  
        elif location == "y":
            rect.y = locations["y"]
 
        elif location == "topright":
            rect.topright = locations["topright"]

        elif location == "center":
            rect.center = locations["center"]
  
points_text, points_rect = prep_text(f"Burger Points: {burger_points}", orange, topleft=(10,10))


score_text, score_rect = prep_text(f"Score: {score}", orange, topleft=(10,50))

title_text, title_rect = prep_text("American dog", orange, centerx=WINDOW_WIDTH // 2, y=10)

eaten_text, eaten_rect = prep_text(f"Burgers Eaten: {burgers_eaten}", orange,centerx=WINDOW_WIDTH // 2, y=50)

lives_text, lives_rect = prep_text(f"Lives: {player_lives}", orange,topright=(WINDOW_WIDTH - 10, 10))

boost_text, boost_rect = prep_text(f"Boost: (boost_level)", orange, topright=(WINDOW_WIDTH - 10, 50))

game_over_text, game_over_rect = prep_text(f"FINAL SCORE: {score}", orange, center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

continue_text, continue_rect = prep_text("Press any key to play again", orange,center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT //2 + 64))

bark_sound = pygame.mixer.Sound("bark_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
pygame.mixer.Sound("bd_background_music.wav")
player_image_right = pygame.image.load("dog_right.png")
player_image_left = pygame.image.load("dog_left.png")
player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH // 2
player_rect.bottom = WINDOW_HEIGHT


burger_image = pygame.image.load("burger.png")
burger_rect = burger_image.get_rect()
burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
