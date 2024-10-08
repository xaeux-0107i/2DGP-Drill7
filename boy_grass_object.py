from pico2d import *
import random

# Game object class here
class Grass:
    # 생성자 함수 : 객체의 초기 상태를 설정
    def __init__(self):
        # 모양 없는 납작한 붕어빵의 초기 모습 결정
        self.image = load_image('grass.png')


    def update(self):
        pass


    def draw(self):
        self.image.draw(400, 30)


    pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')


    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5


    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class Smallball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.dy = random.randint(10, 20)
        self.image = load_image('ball21x21.png')


    def update(self):
        if self.y >= 80:
            self.y -= self.dy
        if self.y < 90:
            self.y = 70


    def draw(self):
        self.image.draw(self.x, self.y)


class Bigball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.dy = random.randint(10, 20)
        self.image = load_image('ball41x41.png')


    def update(self):
        if self.y >= 90:
            self.y -= self.dy
        if self.y < 90:
            self.y = 80


    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global smallBalls
    global bigBalls
    global team
    global world

    running = True
    world = []

    grass = Grass() # 잔디 생성
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    smallBalls = [Smallball() for i in range(10)]
    world += smallBalls

    bigBalls = [Bigball() for i in range(10)]
    world += bigBalls

running = True

def update_world():
    for o in world:
        o.update()
    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()
    pass

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    # game logic
    handle_events()
    update_world() # 상호작용을 시뮬레이션
    render_world() # 그 결과를 보여준다
    delay(0.05)


# finalization code
close_canvas()
