def stop_scrolling():
    global scrolling, Cursor, cursor_flash_on
    scrolling = False
    if scroll1 != None:
        scroll1.delete()
    if scroll2 != None:
        scroll2.delete()
    if scroll3 != None:
        scroll3.delete()
    if scroll4 != None:
        scroll4.delete()
    if scroll5 != None:
        scroll5.delete()
    Cursor = game.create_sprite(4, 0)
    cursor_flash_on = True
    set_cursor_brightness(255)

def on_button_pressed_a():
    global scrolling2
    if scrolling:
        stop_scrolling()
        scrolling2 = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def start_scrolling():
    global scrolling, scroll1, scroll2, scroll3, scroll4, scroll5, Cursor
    scrolling = True
    scroll1 = game.create_sprite(0, 0)
    scroll2 = game.create_sprite(0, 1)
    scroll3 = game.create_sprite(0, 2)
    scroll4 = game.create_sprite(0, 3)
    scroll5 = game.create_sprite(0, 4)
    if Cursor != None:
        Cursor.delete()
    Cursor = None
def scroll():
    if scroll1 != None:
        if scroll1.get(LedSpriteProperty.X) == 4:
            scroll1.set(LedSpriteProperty.X, 0)
        else:
            scroll1.change(LedSpriteProperty.X, 1)
    if scroll2 != None:
        if scroll2.get(LedSpriteProperty.X) == 4:
            scroll2.set(LedSpriteProperty.X, 0)
        else:
            scroll2.change(LedSpriteProperty.X, 1)
    if scroll3 != None:
        if scroll3.get(LedSpriteProperty.X) == 4:
            scroll3.set(LedSpriteProperty.X, 0)
        else:
            scroll3.change(LedSpriteProperty.X, 1)
    if scroll4 != None:
        if scroll4.get(LedSpriteProperty.X) == 4:
            scroll4.set(LedSpriteProperty.X, 0)
        else:
            scroll4.change(LedSpriteProperty.X, 1)
    if scroll5 != None:
        if scroll5.get(LedSpriteProperty.X) == 4:
            scroll5.set(LedSpriteProperty.X, 0)
        else:
            scroll5.change(LedSpriteProperty.X, 1)

def on_button_pressed_ab():
    Cursor.delete()
    control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global scrolling2
    if scrolling:
        stop_scrolling()
        scrolling2 = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global scrolling2
    start_scrolling()
    scrolling2 = 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def set_cursor_brightness(brightness: number):
    if Cursor != None:
        Cursor.set(LedSpriteProperty.BRIGHTNESS, brightness)

def on_logo_pressed():
    global Note2
    if Cursor == None:
        return
    if Cursor.get(LedSpriteProperty.Y) == 4:
        music.play(music.create_sound_expression(WaveShape.SQUARE,
                200,
                1,
                255,
                0,
                100,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            music.PlaybackMode.UNTIL_DONE)
    else:
        music.play(music.tone_playable(WhatNote, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    Note2 = game.create_sprite(Cursor.get(LedSpriteProperty.X),
        Cursor.get(LedSpriteProperty.Y))
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

Note2: game.LedSprite = None
WhatNote = 0
scrolling2 = 0
scroll5: game.LedSprite = None
scroll4: game.LedSprite = None
scroll3: game.LedSprite = None
scroll2: game.LedSprite = None
scroll1: game.LedSprite = None
scrolling = False
cursor_flash_on = False
Cursor: game.LedSprite = None
cursor_flash_on = True
Cursor = game.create_sprite(4, 0)
set_cursor_brightness(255)

def on_forever():
    global cursor_flash_on
    if Cursor != None and not (scrolling):
        basic.pause(300)
        cursor_flash_on = not (cursor_flash_on)
        if cursor_flash_on:
            set_cursor_brightness(255)
        else:
            set_cursor_brightness(0)
    if Cursor != None:
        basic.pause(150)
        if Cursor.get(LedSpriteProperty.Y) == 4 and input.button_is_pressed(Button.A):
            basic.pause(150)
            Cursor.set(LedSpriteProperty.Y, 0)
        elif input.button_is_pressed(Button.A):
            basic.pause(150)
            Cursor.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever)

def on_forever2():
    if scrolling:
        basic.pause(250)
        scroll()
        if input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
            stop_scrolling()
basic.forever(on_forever2)

def on_forever3():
    if Cursor != None:
        if Cursor.get(LedSpriteProperty.X) == 4 and input.button_is_pressed(Button.B):
            basic.pause(150)
            Cursor.set(LedSpriteProperty.X, 0)
        elif input.button_is_pressed(Button.B):
            basic.pause(150)
            Cursor.change(LedSpriteProperty.X, 1)
basic.forever(on_forever3)

def on_forever4():
    if scrolling2 == 1:
        if scroll1.is_touching(Note2):
            music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
        if scroll2.is_touching(Note2):
            music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
        if scroll3.is_touching(Note2):
            pass
        if scroll4.is_touching(Note2):
            pass
        if scroll5.is_touching(Note2):
            pass
basic.forever(on_forever4)

def on_forever5():
    global WhatNote
    if Cursor != None:
        if Cursor.get(LedSpriteProperty.Y) == 0:
            WhatNote = 262
        if Cursor.get(LedSpriteProperty.Y) == 1:
            WhatNote = 311
        if Cursor.get(LedSpriteProperty.Y) == 2:
            WhatNote = 349
        if Cursor.get(LedSpriteProperty.Y) == 3:
            WhatNote = 392
        if Cursor.get(LedSpriteProperty.Y) == 4:
            WhatNote = 0
basic.forever(on_forever5)
