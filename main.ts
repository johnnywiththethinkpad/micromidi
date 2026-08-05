input.onButtonPressed(Button.A, function () {
    if (scrolling) {
        stopscrolling()
    } else {
    	
    }
})
function scroll () {
    let radar_x: number;
let note_count: number;
let ny: number;
while (scrolling) {
        current_pause = 200
        for (let index = 0; index < 5; index++) {
            record.playAudio(record.BlockingState.Nonblocking)
            if (!(scrolling)) {
                break;
            }
            if (scroll1 != null) {
                radar_x = scroll1.get(LedSpriteProperty.X)
                note_count = 0
                for (let n1 of notes_list) {
                    if (n1.get(LedSpriteProperty.X) == radar_x) {
                        note_count += 1
                    }
                }
                if (note_count == 1) {
                    for (let n2 of notes_list) {
                        if (n2.get(LedSpriteProperty.X) == radar_x) {
                            ny = n2.get(LedSpriteProperty.Y)
                            if (ny == 0) {
                                if (midimode == true) {
                                    serial.writeString("" + String.fromCharCode(144) + String.fromCharCode(58) + String.fromCharCode(127))
                                } else {
                                    music.play(music.tonePlayable(233, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
                                }
                            } else if (ny == 1) {
                                if (midimode == true) {
                                    serial.writeString("" + String.fromCharCode(144) + String.fromCharCode(60) + String.fromCharCode(127))
                                } else {
                                    music.play(music.tonePlayable(262, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
                                }
                            } else if (ny == 2) {
                                if (midimode == true) {
                                    serial.writeString("" + String.fromCharCode(144) + String.fromCharCode(63) + String.fromCharCode(127))
                                } else {
                                    music.play(music.tonePlayable(311, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
                                }
                            } else if (ny == 3) {
                                if (midimode == true) {
                                    serial.writeString("" + String.fromCharCode(144) + String.fromCharCode(65) + String.fromCharCode(127))
                                } else {
                                    music.play(music.tonePlayable(349, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
                                }
                            } else if (ny == 4) {
                                if (midimode == true) {
                                    serial.writeString("" + String.fromCharCode(144) + String.fromCharCode(67) + String.fromCharCode(127))
                                } else {
                                    music.play(music.tonePlayable(392, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
                                }
                            }
                        }
                    }
                } else if (note_count > 1) {
                    for (let index = 0; index < 2; index++) {
                        if (!(scrolling)) {
                            break;
                        }
                        for (let n3 of notes_list) {
                            if (n3.get(LedSpriteProperty.X) == radar_x) {
                                ny = n3.get(LedSpriteProperty.Y)
                                if (ny == 0) {
                                    if (midimode == true) {
                                        serial.writeString("" + String.fromCharCode(144) + String.fromCharCode(58) + String.fromCharCode(127))
                                    } else {
                                        music.play(music.tonePlayable(233, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
                                    }
                                } else if (ny == 1) {
                                    if (midimode == true) {
                                        serial.writeString("" + String.fromCharCode(144) + String.fromCharCode(60) + String.fromCharCode(127))
                                    } else {
                                        music.play(music.tonePlayable(262, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
                                    }
                                } else if (ny == 2) {
                                    if (midimode == true) {
                                        serial.writeString("" + String.fromCharCode(144) + String.fromCharCode(63) + String.fromCharCode(127))
                                    } else {
                                        music.play(music.tonePlayable(311, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
                                    }
                                } else if (ny == 3) {
                                    if (midimode == true) {
                                        serial.writeString("" + String.fromCharCode(144) + String.fromCharCode(65) + String.fromCharCode(127))
                                    } else {
                                        music.play(music.tonePlayable(349, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
                                    }
                                } else if (ny == 4) {
                                    if (midimode == true) {
                                        serial.writeString("" + String.fromCharCode(144) + String.fromCharCode(67) + String.fromCharCode(127))
                                    } else {
                                        music.play(music.tonePlayable(392, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
                                    }
                                }
                            }
                        }
                    }
                }
            }
            basic.pause(current_pause)
            if (!(scrolling)) {
                break;
            }
            if (scroll1 != null) {
                scroll1.change(LedSpriteProperty.X, 1)
            }
            if (scroll2 != null) {
                scroll2.change(LedSpriteProperty.X, 1)
            }
            if (scroll3 != null) {
                scroll3.change(LedSpriteProperty.X, 1)
            }
            if (scroll4 != null) {
                scroll4.change(LedSpriteProperty.X, 1)
            }
            if (scroll5 != null) {
                scroll5.change(LedSpriteProperty.X, 1)
            }
        }
        if (scroll1 != null) {
            scroll1.set(LedSpriteProperty.X, 0)
        }
        if (scroll2 != null) {
            scroll2.set(LedSpriteProperty.X, 0)
        }
        if (scroll3 != null) {
            scroll3.set(LedSpriteProperty.X, 0)
        }
        if (scroll4 != null) {
            scroll4.set(LedSpriteProperty.X, 0)
        }
        if (scroll5 != null) {
            scroll5.set(LedSpriteProperty.X, 0)
        }
    }
}
input.onButtonPressed(Button.AB, function () {
    if (midimode == true) {
        music.play(music.createSoundExpression(WaveShape.Sine, 1, 5000, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
        midimode = false
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    } else {
        midimode = true
        music.play(music.createSoundExpression(WaveShape.Sine, 5000, 1, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # . # . #
            `)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
input.onButtonPressed(Button.B, function () {
    if (scrolling) {
        stopscrolling()
    } else {
    	
    }
})
input.onGesture(Gesture.Shake, function () {
    let shift_pitch: number;
if (scrolling) {
        if (speed_level >= 4) {
            speed_level = 1
        } else {
            speed_level += 1
        }
        shift_pitch = 392
        if (speed_level == 2) {
            shift_pitch = 523
        } else if (speed_level == 3) {
        	
        } else if (speed_level == 4) {
        	
        }
        music.play(music.tonePlayable(shift_pitch, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.InBackground)
    } else {
        scrolling = true
        speed_level = 1
        music.play(music.tonePlayable(392, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
        if (Cursor != null) {
            Cursor.delete()
        }
        scroll1 = game.createSprite(0, 0)
        scroll2 = game.createSprite(0, 1)
        scroll3 = game.createSprite(0, 2)
        scroll4 = game.createSprite(0, 3)
        scroll5 = game.createSprite(0, 4)
        scroll()
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    ifplaced = true
    for (let note of notes_list) {
        if (Cursor != null && Cursor.isTouching(note)) {
            music.play(music.createSoundExpression(WaveShape.Noise, 54, 54, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
            note.delete()
            notes_list.removeElement(note)
return
        }
    }
    if (Cursor != null) {
        if (Cursor.get(LedSpriteProperty.Y) == 4) {
            if (midimode == true) {
                serial.writeString(midinote)
            } else {
                music.play(music.tonePlayable(WhatNote, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            }
        } else {
            if (midimode == true) {
                serial.writeString(midinote)
            } else {
                music.play(music.tonePlayable(WhatNote, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            }
        }
        new_note = game.createSprite(Cursor.get(LedSpriteProperty.X), Cursor.get(LedSpriteProperty.Y))
        notes_list.push(new_note)
    }
})
function stopscrolling () {
    scrolling = false
    if (scroll1 != null) {
        scroll1.delete()
    }
    if (scroll2 != null) {
        scroll2.delete()
    }
    if (scroll3 != null) {
        scroll3.delete()
    }
    if (scroll4 != null) {
        scroll4.delete()
    }
    if (scroll5 != null) {
        scroll5.delete()
    }
    Cursor = game.createSprite(4, 0)
    speed_level = 1
}
let CY = 0
let CX = 0
let new_note: game.LedSprite = null
let WhatNote = 0
let midinote = ""
let ifplaced = false
let scroll5: game.LedSprite = null
let scroll4: game.LedSprite = null
let scroll3: game.LedSprite = null
let scroll2: game.LedSprite = null
let midimode = false
let scroll1: game.LedSprite = null
let scrolling = false
let current_pause = 0
let speed_level = 0
let Cursor: game.LedSprite = null
let notes_list : game.LedSprite[] = []
serial.redirectToUSB()
record.setSampleRate(44100)
Cursor = game.createSprite(4, 0)
speed_level = 1
current_pause = 700
basic.forever(function () {
    if (scrolling) {
    	
    } else {
        basic.pause(80)
        if (Cursor != null && Cursor.get(LedSpriteProperty.Y) == 4 && input.buttonIsPressed(Button.A)) {
            basic.pause(80)
            if (Cursor != null) {
                Cursor.set(LedSpriteProperty.Y, 0)
            }
        } else if (input.buttonIsPressed(Button.A)) {
            basic.pause(80)
            if (Cursor != null) {
                Cursor.change(LedSpriteProperty.Y, 1)
            }
        }
    }
})
basic.forever(function () {
    if (Cursor != null) {
        CX = Cursor.get(LedSpriteProperty.X)
        CY = Cursor.get(LedSpriteProperty.Y)
    }
    basic.pause(50)
})
basic.forever(function () {
    if (scrolling) {
    	
    } else {
        basic.pause(80)
        if (Cursor != null && Cursor.get(LedSpriteProperty.X) == 4 && input.buttonIsPressed(Button.B)) {
            basic.pause(80)
            if (Cursor != null) {
                Cursor.set(LedSpriteProperty.X, 0)
            }
        } else if (input.buttonIsPressed(Button.B)) {
            basic.pause(80)
            if (Cursor != null) {
                Cursor.change(LedSpriteProperty.X, 1)
            }
        }
    }
})
basic.forever(function () {
    let overlapping: boolean;
if (!(scrolling) && Cursor != null) {
        overlapping = false
        for (let note2 of notes_list) {
            if (Cursor.isTouching(note2)) {
                overlapping = true
                break;
            }
        }
        if (overlapping) {
            led.unplot(CX, CY)
            basic.pause(150)
            led.plot(CX, CY)
            basic.pause(150)
        } else {
            basic.pause(100)
        }
    } else {
        basic.pause(200)
    }
})
basic.forever(function () {
    if (Cursor == null) {
        basic.pause(50)
        return
    }
    if (Cursor.get(LedSpriteProperty.Y) == 0) {
        if (midimode == true) {
            midinote = "" + String.fromCharCode(144) + String.fromCharCode(58) + String.fromCharCode(127)
        } else {
            WhatNote = 233
        }
    }
    if (Cursor.get(LedSpriteProperty.Y) == 1) {
        if (midimode == true) {
            midinote = "" + String.fromCharCode(144) + String.fromCharCode(60) + String.fromCharCode(127)
        } else {
            WhatNote = 262
        }
    }
    if (Cursor.get(LedSpriteProperty.Y) == 2) {
        if (midimode == true) {
            midinote = "" + String.fromCharCode(144) + String.fromCharCode(63) + String.fromCharCode(127)
        } else {
            WhatNote = 311
        }
    }
    if (Cursor.get(LedSpriteProperty.Y) == 3) {
        if (midimode == true) {
            midinote = "" + String.fromCharCode(144) + String.fromCharCode(65) + String.fromCharCode(127)
        } else {
            WhatNote = 349
        }
    }
    if (Cursor.get(LedSpriteProperty.Y) == 4) {
        if (midimode == true) {
            midinote = "" + String.fromCharCode(144) + String.fromCharCode(67) + String.fromCharCode(127)
        } else {
            WhatNote = 392
        }
    }
    basic.pause(50)
})
