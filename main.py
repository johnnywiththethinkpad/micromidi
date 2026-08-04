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
            if scroll1 != None:
                scroll1.change(LedSpriteProperty.X, 1)
            if scroll2 != None:
                scroll2.change(LedSpriteProperty.X, 1)
            if scroll3 != None:
                scroll3.change(LedSpriteProperty.X, 1)
            if scroll4 != None:
                scroll4.change(LedSpriteProperty.X, 1)
            if scroll5 != None:
                scroll5.change(LedSpriteProperty.X, 1)
        if scroll1 != None:
            scroll1.set(LedSpriteProperty.X, 0)
        if scroll2 != None:
            scroll2.set(LedSpriteProperty.X, 0)
        if scroll3 != None:
            scroll3.set(LedSpriteProperty.X, 0)
        if scroll4 != None:
            scroll4.set(LedSpriteProperty.X, 0)
        if scroll5 != None:
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
        if Cursor != None:
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
        if Cursor != None and Cursor.is_touching(note):
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
    if Cursor != None:
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
notes_list: List[game.LedSprite] = []
Cursor = game.create_sprite(4, 0)

def on_forever():
    if scrolling:
        pass
    else:
        basic.pause(80)
        if Cursor != None and Cursor.get(LedSpriteProperty.Y) == 4 and input.button_is_pressed(Button.A):
            basic.pause(80)
            if Cursor != None:
                Cursor.set(LedSpriteProperty.Y, 0)
        elif input.button_is_pressed(Button.A):
            basic.pause(80)
            if Cursor != None:
                Cursor.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever)

def on_forever2():
    global WhatNote
    if Cursor == None:
        basic.pause(50)
        return
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
    basic.pause(50)
basic.forever(on_forever2)

def on_forever3():
    global CX, CY
    if Cursor != None:
        CX = Cursor.get(LedSpriteProperty.X)
        CY = Cursor.get(LedSpriteProperty.Y)
    basic.pause(50)
basic.forever(on_forever3)

def on_forever4():
    if scrolling:
        pass
    else:
        basic.pause(80)
        if Cursor != None and Cursor.get(LedSpriteProperty.X) == 4 and input.button_is_pressed(Button.B):
            basic.pause(80)
            if Cursor != None:
                Cursor.set(LedSpriteProperty.X, 0)
        elif input.button_is_pressed(Button.B):
            basic.pause(80)
            if Cursor != None:
                Cursor.change(LedSpriteProperty.X, 1)
basic.forever(on_forever4)

def on_forever5():
    if not (scrolling) and Cursor != None:
        overlapping = False
        for note2 in notes_list:
            if Cursor.is_touching(note2):
                overlapping = True
                break
        if overlapping:
            led.unplot(CX, CY)
            basic.pause(150)
            led.plot(CX, CY)
            basic.pause(150)
        else:
            basic.pause(100)
    else:
        basic.pause(200)
basic.forever(on_forever5)

def on_forever6():
    if scrolling and scroll1 != None:
        radar_x = scroll1.get(LedSpriteProperty.X)
        for note3 in notes_list:
            if note3.get(LedSpriteProperty.X) == radar_x:
                note_y = note3.get(LedSpriteProperty.Y)
                if note_y == 0:
                    music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)),
                        music.PlaybackMode.IN_BACKGROUND)
                elif note_y == 1:
                    music.play(music.tone_playable(311, music.beat(BeatFraction.QUARTER)),
                        music.PlaybackMode.IN_BACKGROUND)
                elif note_y == 2:
                    music.play(music.tone_playable(349, music.beat(BeatFraction.QUARTER)),
                        music.PlaybackMode.IN_BACKGROUND)
                elif note_y == 3:
                    music.play(music.tone_playable(392, music.beat(BeatFraction.QUARTER)),
                        music.PlaybackMode.IN_BACKGROUND)
                elif note_y == 4:
                    music.play(music.create_sound_expression(WaveShape.SQUARE,
                            200,
                            1,
                            255,
                            0,
                            100,
                            SoundExpressionEffect.NONE,
                            InterpolationCurve.CURVE),
                        music.PlaybackMode.IN_BACKGROUND)
        basic.pause(700)
    else:
        basic.pause(100)
basic.forever(on_forever6)
