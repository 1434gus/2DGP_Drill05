from pico2d import *

window_width = 800
window_height = 600

running = True
open_canvas(window_width, window_height)
ground = load_image('TUK_GROUND.png')
character = load_image('sonic-sprite.png')
frame = 0
x = 0
speed = 0.05

def handle_events():
    global running
    global x

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                x += 10
            elif event.key == SDLK_LEFT:
                x -= 10


while running:
    clear_canvas()
    ground.draw(window_width/2,window_height/2)
    character.clip_draw(0,0,30,50,x,90)
    handle_events()
    update_canvas()
    delay(speed)



close_canvas()
