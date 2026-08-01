def on_button_pressed_ab():
    stop_scan()
    basic.show_leds("""
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        # # # # #
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
    control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)


def on_logo_pressed():
    global cursor_x, cursor_y
    if not scan_active:
        note_grid[cursor_x][cursor_y] = not note_grid[cursor_x][cursor_y]
        render_scene()
        if cursor_y == 4:
            music.play(music.create_sound_expression(WaveShape.SQUARE,
                    220,
                    1,
                    180,
                    0,
                    40,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.CURVE),
                music.PlaybackMode.UNTIL_DONE)
        else:
            music.play(music.tone_playable(WhatNote, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)


def on_button_pressed_a():
    stop_scan()


def on_button_pressed_b():
    stop_scan()


input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)


def on_gesture_shake():
    global scan_active, scan_column
    scan_active = True
    scan_column = 0
    render_scene()


input.on_gesture(Gesture.SHAKE, on_gesture_shake)

WhatNote = 0
cursor_x = 4
cursor_y = 0
scan_active = False
scan_column = 0
note_grid = [[False for _ in range(5)] for _ in range(5)]
blink_state = False
blink_timer = 0


def render_scene():
    basic.clear_screen()
    for x in range(5):
        for y in range(5):
            is_cursor_cell = x == cursor_x and y == cursor_y
            cursor_on_note = note_grid[cursor_x][cursor_y]
            should_hide_cursor = is_cursor_cell and cursor_on_note and not blink_state
            if note_grid[x][y] and not should_hide_cursor:
                led.plot(x, y)
    if scan_active:
        for y in range(5):
            if not (scan_column == cursor_x and y == cursor_y and not blink_state):
                led.plot(scan_column, y)
    if not scan_active:
        if note_grid[cursor_x][cursor_y]:
            if blink_state:
                led.plot(cursor_x, cursor_y)
        else:
            led.plot(cursor_x, cursor_y)


def stop_scan():
    global scan_active
    scan_active = False
    render_scene()


def set_what_note():
    global WhatNote
    if cursor_y == 0:
        WhatNote = 262
    elif cursor_y == 1:
        WhatNote = 311
    elif cursor_y == 2:
        WhatNote = 349
    elif cursor_y == 3:
        WhatNote = 392
    else:
        WhatNote = 0


set_what_note()
render_scene()


def on_forever():
    global cursor_x, cursor_y
    if not scan_active and input.button_is_pressed(Button.B):
        basic.pause(150)
        cursor_x = (cursor_x + 1) % 5
        set_what_note()
        render_scene()
basic.forever(on_forever)


def on_forever2():
    global cursor_y
    if not scan_active and input.button_is_pressed(Button.A):
        basic.pause(150)
        cursor_y = (cursor_y + 1) % 5
        set_what_note()
        render_scene()
basic.forever(on_forever2)


def on_forever3():
    global scan_active, scan_column
    if scan_active:
        render_scene()
        basic.pause(50)
        scan_column = (scan_column + 1) % 5
        if input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
            stop_scan()
basic.forever(on_forever3)


def on_forever4():
    global blink_state, blink_timer
    blink_timer += 1
    if blink_timer >= 0:
        blink_timer = 0
        blink_state = not blink_state
        render_scene()
    basic.pause(1)
basic.forever(on_forever4)
