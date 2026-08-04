input.onButtonPressed(Button.A, function () {
    if (scrolling) {
        stopscrolling()
    } else {
    	
    }
})
function scroll () {
    while (scrolling) {
        for (let index = 0; index < 5; index++) {
            basic.pause(700)
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
input.onButtonPressed(Button.B, function () {
    if (scrolling) {
        stopscrolling()
    } else {
    	
    }
})
input.onGesture(Gesture.Shake, function () {
    if (scrolling) {
    	
    } else {
        scrolling = true
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
            music.play(music.createSoundExpression(WaveShape.Square, 200, 1, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
        } else {
            music.play(music.tonePlayable(WhatNote, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
        }
        new_note = game.createSprite(Cursor.get(LedSpriteProperty.X), Cursor.get(LedSpriteProperty.Y))
        notes_list.push(new_note)
    }
})
function stopscrolling () {
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
    scrolling = false
}
let CY = 0
let CX = 0
let new_note: game.LedSprite = null
let WhatNote = 0
let ifplaced = false
let scroll5: game.LedSprite = null
let scroll4: game.LedSprite = null
let scroll3: game.LedSprite = null
let scroll2: game.LedSprite = null
let scroll1: game.LedSprite = null
let scrolling = false
let Cursor: game.LedSprite = null
music._playDefaultBackground(music.builtInPlayableMelody(Melodies.BaDing), music.PlaybackMode.InBackground)
let notes_list : game.LedSprite[] = []
Cursor = game.createSprite(4, 0)
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
    if (Cursor == null) {
        basic.pause(50)
        return
    }
    if (Cursor.get(LedSpriteProperty.Y) == 0) {
        WhatNote = 262
    }
    if (Cursor.get(LedSpriteProperty.Y) == 1) {
        WhatNote = 311
    }
    if (Cursor.get(LedSpriteProperty.Y) == 2) {
        WhatNote = 349
    }
    if (Cursor.get(LedSpriteProperty.Y) == 3) {
        WhatNote = 392
    }
    if (Cursor.get(LedSpriteProperty.Y) == 4) {
        WhatNote = 0
    }
    basic.pause(50)
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
    let radar_x: number;
let note_y: number;
if (scrolling && scroll1 != null) {
        radar_x = scroll1.get(LedSpriteProperty.X)
        for (let note3 of notes_list) {
            if (note3.get(LedSpriteProperty.X) == radar_x) {
                note_y = note3.get(LedSpriteProperty.Y)
                if (note_y == 0) {
                    music.play(music.tonePlayable(262, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
                } else if (note_y == 1) {
                    music.play(music.tonePlayable(311, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
                } else if (note_y == 2) {
                    music.play(music.tonePlayable(349, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
                } else if (note_y == 3) {
                    music.play(music.tonePlayable(392, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
                } else if (note_y == 4) {
                    music.play(music.createSoundExpression(WaveShape.Square, 200, 1, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.InBackground)
                }
            }
        }
        basic.pause(700)
    } else {
        basic.pause(100)
    }
})
