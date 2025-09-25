from pico2d import *

window_width = 800
window_height = 600

running = True
open_canvas(window_width, window_height)
ground = load_image('TUK_GROUND.png')
character = load_image('sonic-sprite.png')
frame = 0
x = 0
dir = 0
speed = 0.1

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

ch_width = 29
ch_height = 40

while running:
    clear_canvas()
    ground.draw(window_width/2,window_height/2)
    # character.clip_draw(0,0,30,50,x,90)

    clear_canvas()
    ground.draw(window_width / 2, window_height / 2)
    character.clip_draw(86 + 32 * frame, 447, ch_width, ch_height, 400 + x, 300, ch_width / 29 * 300, ch_height / 40 * 400)
    handle_events()
    update_canvas()
    frame = (frame + 1) % 4
    delay(speed)



close_canvas()
