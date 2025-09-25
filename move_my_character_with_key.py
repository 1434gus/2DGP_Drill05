from pico2d import *

window_width = 800
window_height = 600

open_canvas(window_width, window_height)

ground = load_image('TUK_GROUND.png')
ground.draw(window_width/2,window_height/2)
update_canvas()
delay(1)

close_canvas()
