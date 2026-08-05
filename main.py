def on_button_pressed_a():
    if scrolling:
        stopscrolling()
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def scroll():
    global current_pause
    while scrolling:
        current_pause = 200
        for index in range(5):
            record.play_audio(record.BlockingState.NONBLOCKING)
            if not (scrolling):
                break
            if scroll1 != None:
                radar_x = scroll1.get(LedSpriteProperty.X)
                note_count = 0
                for n1 in notes_list:
                    if n1.get(LedSpriteProperty.X) == radar_x:
                        note_count += 1
                if note_count == 1:
                    for n2 in notes_list:
                        if n2.get(LedSpriteProperty.X) == radar_x:
                            ny = n2.get(LedSpriteProperty.Y)
                            if ny == 0:
                                if midimode == True:
                                    serial.write_string("" + String.from_char_code(144) + String.from_char_code(58) + String.from_char_code(127))
                                else:
                                    music.play(music.tone_playable(233, music.beat(BeatFraction.QUARTER)),
                                        music.PlaybackMode.IN_BACKGROUND)
                            elif ny == 1:
                                if midimode == True:
                                    serial.write_string("" + String.from_char_code(144) + String.from_char_code(60) + String.from_char_code(127))
                                else:
                                    music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)),
                                        music.PlaybackMode.IN_BACKGROUND)
                            elif ny == 2:
                                if midimode == True:
                                    serial.write_string("" + String.from_char_code(144) + String.from_char_code(63) + String.from_char_code(127))
                                else:
                                    music.play(music.tone_playable(311, music.beat(BeatFraction.QUARTER)),
                                        music.PlaybackMode.IN_BACKGROUND)
                            elif ny == 3:
                                if midimode == True:
                                    serial.write_string("" + String.from_char_code(144) + String.from_char_code(65) + String.from_char_code(127))
                                else:
                                    music.play(music.tone_playable(349, music.beat(BeatFraction.QUARTER)),
                                        music.PlaybackMode.IN_BACKGROUND)
                            elif ny == 4:
                                if midimode == True:
                                    serial.write_string("" + String.from_char_code(144) + String.from_char_code(67) + String.from_char_code(127))
                                else:
                                    music.play(music.tone_playable(392, music.beat(BeatFraction.QUARTER)),
                                        music.PlaybackMode.IN_BACKGROUND)
                elif note_count > 1:
                    for index2 in range(2):
                        if not (scrolling):
                            break
                        for n3 in notes_list:
                            if n3.get(LedSpriteProperty.X) == radar_x:
                                ny = n3.get(LedSpriteProperty.Y)
                                if ny == 0:
                                    if midimode == True:
                                        serial.write_string("" + String.from_char_code(144) + String.from_char_code(58) + String.from_char_code(127))
                                    else:
                                        music.play(music.tone_playable(233, music.beat(BeatFraction.QUARTER)),
                                            music.PlaybackMode.IN_BACKGROUND)
                                elif ny == 1:
                                    if midimode == True:
                                        serial.write_string("" + String.from_char_code(144) + String.from_char_code(60) + String.from_char_code(127))
                                    else:
                                        music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)),
                                            music.PlaybackMode.IN_BACKGROUND)
                                elif ny == 2:
                                    if midimode == True:
                                        serial.write_string("" + String.from_char_code(144) + String.from_char_code(63) + String.from_char_code(127))
                                    else:
                                        music.play(music.tone_playable(311, music.beat(BeatFraction.QUARTER)),
                                            music.PlaybackMode.IN_BACKGROUND)
                                elif ny == 3:
                                    if midimode == True:
                                        serial.write_string("" + String.from_char_code(144) + String.from_char_code(65) + String.from_char_code(127))
                                    else:
                                        music.play(music.tone_playable(349, music.beat(BeatFraction.QUARTER)),
                                            music.PlaybackMode.IN_BACKGROUND)
                                elif ny == 4:
                                    if midimode == True:
                                        serial.write_string("" + String.from_char_code(144) + String.from_char_code(67) + String.from_char_code(127))
                                    else:
                                        music.play(music.tone_playable(392, music.beat(BeatFraction.QUARTER)),
                                            music.PlaybackMode.IN_BACKGROUND)
            basic.pause(current_pause)
            if not (scrolling):
                break
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

def on_button_pressed_ab():
    global midimode
    if midimode == True:
        music.play(music.create_sound_expression(WaveShape.SINE,
                1,
                5000,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.IN_BACKGROUND)
        midimode = False
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
        basic.pause(100)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    else:
        midimode = True
        music.play(music.create_sound_expression(WaveShape.SINE,
                5000,
                1,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # . # . #
            """)
        basic.pause(100)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if scrolling:
        stopscrolling()
    else:
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global speed_level, scrolling, scroll1, scroll2, scroll3, scroll4, scroll5
    if scrolling:
        if speed_level >= 4:
            speed_level = 1
        else:
            speed_level += 1
        shift_pitch = 392
        if speed_level == 2:
            shift_pitch = 523
        elif speed_level == 3:
            pass
        elif speed_level == 4:
            pass
        music.play(music.tone_playable(shift_pitch, music.beat(BeatFraction.SIXTEENTH)),
            music.PlaybackMode.IN_BACKGROUND)
    else:
        scrolling = True
        speed_level = 1
        music.play(music.tone_playable(392, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.IN_BACKGROUND)
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
            music.play(music.tone_playable(WhatNote, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            serial.write_string(midinote)
        else:
            music.play(music.tone_playable(WhatNote, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            serial.write_string(midinote)
        new_note = game.create_sprite(Cursor.get(LedSpriteProperty.X),
            Cursor.get(LedSpriteProperty.Y))
        notes_list.append(new_note)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def stopscrolling():
    global scrolling, Cursor, speed_level
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
    speed_level = 1
CY = 0
CX = 0
new_note: game.LedSprite = None
midinote = ""
WhatNote = 0
ifplaced = False
scroll5: game.LedSprite = None
scroll4: game.LedSprite = None
scroll3: game.LedSprite = None
scroll2: game.LedSprite = None
midimode = False
scroll1: game.LedSprite = None
scrolling = False
current_pause = 0
speed_level = 0
Cursor: game.LedSprite = None
notes_list: List[game.LedSprite] = []
serial.redirect_to_usb()
record.set_sample_rate(44100)
Cursor = game.create_sprite(4, 0)
speed_level = 1
current_pause = 700

def on_forever():
    global midinote, WhatNote
    if Cursor == None:
        basic.pause(50)
        return
    if Cursor.get(LedSpriteProperty.Y) == 0:
        if midimode == True:
            midinote = "" + String.from_char_code(144) + String.from_char_code(58) + String.from_char_code(127)
        else:
            WhatNote = 233
    if Cursor.get(LedSpriteProperty.Y) == 1:
        if midimode == True:
            midinote = "" + String.from_char_code(144) + String.from_char_code(60) + String.from_char_code(127)
        else:
            WhatNote = 262
    if Cursor.get(LedSpriteProperty.Y) == 2:
        if midimode == True:
            midinote = "" + String.from_char_code(144) + String.from_char_code(63) + String.from_char_code(127)
        else:
            WhatNote = 311
    if Cursor.get(LedSpriteProperty.Y) == 3:
        if midimode == True:
            midinote = "" + String.from_char_code(144) + String.from_char_code(65) + String.from_char_code(127)
        else:
            WhatNote = 349
    if Cursor.get(LedSpriteProperty.Y) == 4:
        if midimode == True:
            midinote = "" + String.from_char_code(144) + String.from_char_code(67) + String.from_char_code(127)
        else:
            WhatNote = 392
    basic.pause(50)
basic.forever(on_forever)

def on_forever2():
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
