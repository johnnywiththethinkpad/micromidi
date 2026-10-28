from microbit import *
import music
uart.init(baudrate=115200)

FREQS = [233, 262, 311, 349, 392]    
MIDI_NOTES = [58, 60, 63, 65, 67]       
PAUSES = [200, 140, 90, 60]             

notes = set()          
cx, cy = 4, 0         
midimode = False
scrolling = False
speed_level = 0
radar_x = 0
logo_was_touched = False

def send_midi(y):
    uart.write(bytes([144, MIDI_NOTES[y], 127]))

def play_one(y, duration, wait=False):
    if midimode:
        send_midi(y)
    else:
        music.pitch(FREQS[y], duration, wait=wait)
        
def play_column(x):
    ys = sorted([y for (nx, y) in notes if nx == x])
    if not ys:
        return
    if midimode:
        for y in ys:
            send_midi(y)
    elif len(ys) == 1:
        music.pitch(FREQS[ys[0]], 250, wait=False)
    else:
        slice_ms = max(30, PAUSES[speed_level] // len(ys))
        for y in ys:
            music.pitch(FREQS[y], slice_ms, wait=True)

def draw(blink_on=True):
    display.clear()
    for (x, y) in notes:
        display.set_pixel(x, y, 9)
    if scrolling:
        for y in range(5):
            if (radar_x, y) not in notes:
                display.set_pixel(radar_x, y, 4)
    else:
        if (cx, cy) in notes:
            display.set_pixel(cx, cy, 9 if blink_on else 0)
        else:
            display.set_pixel(cx, cy, 5)

def stop_scrolling():
    global scrolling, cx, cy, speed_level
    scrolling = False
    cx, cy = 4, 0
    speed_level = 0

def toggle_mode():
    global midimode
    if midimode:
        midimode = False
        music.pitch(1000, 100, wait=False)
        display.show(Image("90009:09090:00900:09090:90009"))
    else:
        midimode = True
        music.pitch(2000, 100, wait=False)
        display.show(Image("00000:00000:00000:99999:90909"))
    sleep(150)

def on_shake():
    global scrolling, speed_level, radar_x
    if scrolling:
        speed_level = (speed_level + 1) % 4
        music.pitch(392 if speed_level == 0 else 523, 60, wait=False)
    else:
        scrolling = True
        speed_level = 0
        radar_x = 0
        music.pitch(392, 120, wait=False)

def on_logo():
    if (cx, cy) in notes:
        notes.remove((cx, cy))
        music.pitch(54, 100, wait=False)
    else:
        play_one(cy, 500)
        notes.add((cx, cy))

while True:
    a = button_a.was_pressed()
    b = button_b.was_pressed()
    if a or b:
        sleep(60)  
        a = a or button_a.was_pressed()
        b = b or button_b.was_pressed()

        if a and b:
            toggle_mode()
        elif scrolling:
            stop_scrolling()
        elif a:
            cy = (cy + 1) % 5
        elif b:
            cx = (cx + 1) % 5

    if accelerometer.was_gesture("shake"):
        on_shake()

    touched = pin_logo.is_touched()
    if touched and not logo_was_touched and not scrolling:
        on_logo()
    logo_was_touched = touched

    if scrolling:
        t0 = running_time()
        play_column(radar_x)
        draw()
        elapsed = running_time() - t0
        sleep(max(0, PAUSES[speed_level] - elapsed))
        radar_x = (radar_x + 1) % 5
    else:
        draw((running_time() // 300) % 2 == 0)
        sleep(20)
