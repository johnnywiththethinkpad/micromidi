def on_button_pressed_ab():
    Cursor.delete()
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
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

WhatNote = 0
Cursor: game.LedSprite = None
Cursor = game.create_sprite(4, 0)

def on_forever():
    if Cursor.get(LedSpriteProperty.X) == 4 and input.button_is_pressed(Button.B):
        basic.pause(150)
        Cursor.set(LedSpriteProperty.X, 0)
    else:
        if input.button_is_pressed(Button.B):
            basic.pause(150)
            Cursor.change(LedSpriteProperty.X, 1)
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
    if Cursor.get(LedSpriteProperty.Y) == 4 and input.button_is_pressed(Button.A):
        basic.pause(150)
        Cursor.set(LedSpriteProperty.Y, 0)
    else:
        if input.button_is_pressed(Button.A):
            basic.pause(150)
            Cursor.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever3)
