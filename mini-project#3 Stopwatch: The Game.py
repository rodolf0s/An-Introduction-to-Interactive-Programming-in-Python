# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
point = 0
click = 0
marcador = "0/0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t // 600
    b = (t % 600) // 100
    c = ((t % 600) // 10) % 10
    d = (t % 600) % 10
    return str(a) + ':' + str(b) + str(c) + '.' + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global point, click, marcador
    if timer.is_running():
        timer.stop()
        if time % 50 == 0:
            point += 1
        click += 1
        marcador = str(point) + "/" + str(click)

def reset():
    global time, point, click, marcador
    timer.stop()
    time = 0
    point = 0
    click = 0
    marcador = "0/0"

# define event handler for timer with 0.1 sec interval
def timer():
    global time, prueba
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(marcador, [126, 24], 24, "Green")
    canvas.draw_text(format(time), [60, 80], 30, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 180, 140)
timer = simplegui.create_timer(100, timer)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# start frame
frame.start()