from pico2d import *

window_width = 800
window_height = 600

running = True
open_canvas(window_width, window_height)
ground = load_image('TUK_GROUND.png')
character = load_image('sonic-sprite.png')
frame = 0
x = 400
y = 300
horizontal = 0
vertical = 0
speed = 0.05

def handle_events():
    global running
    global x, y, horizontal, vertical

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                horizontal += 1
            elif event.key == SDLK_LEFT:
                horizontal -= 1
            elif event.key == SDLK_UP:
                vertical += 1
            elif event.key == SDLK_DOWN:
                vertical -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                horizontal -= 1
            elif event.key == SDLK_LEFT:
                horizontal += 1
            elif event.key == SDLK_UP:
                vertical -= 1
            elif event.key == SDLK_DOWN:
                vertical += 1

ch_width = 29
ch_height = 40

while running:
    clear_canvas()
    ground.draw(window_width/2,window_height/2)

    clear_canvas()
    ground.draw(window_width / 2, window_height / 2)
    character.clip_draw(86 + 32 * frame, 447, ch_width, ch_height, x, y, ch_width / 29 * 60, ch_height / 40 * 80)

    handle_events()
    update_canvas()

    frame = (frame + 1) % 4
    x += horizontal * 7
    y += vertical * 7
    delay(speed)


close_canvas()
