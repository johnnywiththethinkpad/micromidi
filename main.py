def on_button_pressed_a():
    if scrolling:
        stopscrolling()
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def scroll():
    while scrolling:
        for index in range(5):
            basic.pause(700)
            scroll1.change(LedSpriteProperty.X, 1)
            scroll2.change(LedSpriteProperty.X, 1)
            scroll3.change(LedSpriteProperty.X, 1)
            scroll4.change(LedSpriteProperty.X, 1)
            scroll5.change(LedSpriteProperty.X, 1)
        scroll1.set(LedSpriteProperty.X, 0)
        scroll2.set(LedSpriteProperty.X, 0)
        scroll3.set(LedSpriteProperty.X, 0)
        scroll4.set(LedSpriteProperty.X, 0)
        scroll5.set(LedSpriteProperty.X, 0)

def on_button_pressed_b():
    if scrolling:
        stopscrolling()
    else:
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global scrolling, scroll1, scroll2, scroll3, scroll4, scroll5
    if scrolling:
        pass
    else:
        scrolling = True
        Cursor.delete()
        scroll1 = game.create_sprite(0, 0)
        scroll2 = game.create_sprite(0, 1)
        scroll3 = game.create_sprite(0, 2)
        scroll4 = game.create_sprite(0, 3)
        scroll5 = game.create_sprite(0, 4)
        scroll()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global ifplaced, new_note
    ifplaced = True
    for note in notes_list:
        if Cursor.is_touching(note):
            music.play(music.create_sound_expression(WaveShape.NOISE,
                    54,
                    54,
                    255,
                    0,
                    500,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.LINEAR),
                music.PlaybackMode.IN_BACKGROUND)
            note.delete()
            notes_list.remove_element(note)
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
            music.PlaybackMode.IN_BACKGROUND)
    new_note = game.create_sprite(Cursor.get(LedSpriteProperty.X),
        Cursor.get(LedSpriteProperty.Y))
    notes_list.append(new_note)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def stopscrolling():
    global Cursor, scrolling
    scroll1.delete()
    scroll2.delete()
    scroll3.delete()
    scroll4.delete()
    scroll5.delete()
    Cursor = game.create_sprite(4, 0)
    scrolling = False
CY = 0
CX = 0
new_note: game.LedSprite = None
WhatNote = 0
ifplaced = False
scroll5: game.LedSprite = None
scroll4: game.LedSprite = None
scroll3: game.LedSprite = None
scroll2: game.LedSprite = None
scroll1: game.LedSprite = None
scrolling = False
Cursor: game.LedSprite = None
# FIX: Changed single Note2 variable into an empty list to track multiple sprites
notes_list: List[game.LedSprite] = []
Cursor = game.create_sprite(4, 0)

def on_forever():
    if scrolling:
        pass
    else:
        basic.pause(80)
        if Cursor.get(LedSpriteProperty.Y) == 4 and input.button_is_pressed(Button.A):
            basic.pause(80)
            Cursor.set(LedSpriteProperty.Y, 0)
        elif input.button_is_pressed(Button.A):
            basic.pause(80)
            Cursor.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever)

def on_forever2():
    global WhatNote
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
basic.forever(on_forever2)

def on_forever3():
    global CX, CY
    CX = Cursor.get(LedSpriteProperty.X)
    CY = Cursor.get(LedSpriteProperty.Y)
basic.forever(on_forever3)

def on_forever4():
    if scrolling:
        pass
    else:
        basic.pause(80)
        if Cursor.get(LedSpriteProperty.X) == 4 and input.button_is_pressed(Button.B):
            basic.pause(80)
            Cursor.set(LedSpriteProperty.X, 0)
        elif input.button_is_pressed(Button.B):
            basic.pause(80)
            Cursor.change(LedSpriteProperty.X, 1)
basic.forever(on_forever4)
