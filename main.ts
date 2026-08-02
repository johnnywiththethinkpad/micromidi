input.onPinPressed(TouchPin.P0, function () {
	
})
function stop_scrolling () {
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
    cursor_flash_on = true
    set_cursor_brightness(255)
}
input.onButtonPressed(Button.A, function () {
    if (scrolling) {
        scrolling2 = 0
        stop_scrolling()
    }
})
function start_scrolling () {
    scrolling = true
    scroll1 = game.createSprite(0, 0)
    scroll2 = game.createSprite(0, 1)
    scroll3 = game.createSprite(0, 2)
    scroll4 = game.createSprite(0, 3)
    scroll5 = game.createSprite(0, 4)
    if (Cursor != null) {
        Cursor.delete()
    }
    Cursor = null
}
function scroll () {
    if (scroll1 != null) {
        if (scroll1.get(LedSpriteProperty.X) == 4) {
            scroll1.set(LedSpriteProperty.X, 0)
        } else {
            scroll1.change(LedSpriteProperty.X, 1)
        }
    }
    if (scroll2 != null) {
        if (scroll2.get(LedSpriteProperty.X) == 4) {
            scroll2.set(LedSpriteProperty.X, 0)
        } else {
            scroll2.change(LedSpriteProperty.X, 1)
        }
    }
    if (scroll3 != null) {
        if (scroll3.get(LedSpriteProperty.X) == 4) {
            scroll3.set(LedSpriteProperty.X, 0)
        } else {
            scroll3.change(LedSpriteProperty.X, 1)
        }
    }
    if (scroll4 != null) {
        if (scroll4.get(LedSpriteProperty.X) == 4) {
            scroll4.set(LedSpriteProperty.X, 0)
        } else {
            scroll4.change(LedSpriteProperty.X, 1)
        }
    }
    if (scroll5 != null) {
        if (scroll5.get(LedSpriteProperty.X) == 4) {
            scroll5.set(LedSpriteProperty.X, 0)
        } else {
            scroll5.change(LedSpriteProperty.X, 1)
        }
    }
}
input.onButtonPressed(Button.AB, function () {
    Cursor.delete()
    control.reset()
})
input.onButtonPressed(Button.B, function () {
    if (scrolling) {
        scrolling2 = 0
        stop_scrolling()
    }
})
input.onGesture(Gesture.Shake, function () {
    start_scrolling()
})
function set_cursor_brightness (brightness: number) {
    if (Cursor != null) {
        Cursor.set(LedSpriteProperty.Brightness, brightness)
    }
}
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (Cursor == null) {
        return
    }
    if (Cursor.get(LedSpriteProperty.Y) == 4) {
        music.play(music.createSoundExpression(WaveShape.Square, 200, 1, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
    } else {
        music.play(music.tonePlayable(WhatNote, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    }
    Note2 = game.createSprite(Cursor.get(LedSpriteProperty.X), Cursor.get(LedSpriteProperty.Y))
})
let Note2: game.LedSprite = null
let WhatNote = 0
let scrolling2 = 0
let scroll5: game.LedSprite = null
let scroll4: game.LedSprite = null
let scroll3: game.LedSprite = null
let scroll2: game.LedSprite = null
let scroll1: game.LedSprite = null
let scrolling = false
let cursor_flash_on = false
let Cursor : game.LedSprite = null
cursor_flash_on = true
Cursor = game.createSprite(4, 0)
set_cursor_brightness(255)
basic.forever(function () {
    if (Cursor != null && !(scrolling)) {
        basic.pause(300)
        cursor_flash_on = !(cursor_flash_on)
        if (cursor_flash_on) {
            set_cursor_brightness(255)
        } else {
            set_cursor_brightness(0)
        }
    }
    if (Cursor != null) {
        basic.pause(150)
        if (Cursor.get(LedSpriteProperty.Y) == 4 && input.buttonIsPressed(Button.A)) {
            basic.pause(150)
            Cursor.set(LedSpriteProperty.Y, 0)
        } else if (input.buttonIsPressed(Button.A)) {
            basic.pause(150)
            Cursor.change(LedSpriteProperty.Y, 1)
        }
    }
})
basic.forever(function () {
    if (scrolling) {
        basic.pause(250)
        scroll()
        if (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
            stop_scrolling()
        }
    }
})
basic.forever(function () {
    if (Cursor != null) {
        if (Cursor.get(LedSpriteProperty.X) == 4 && input.buttonIsPressed(Button.B)) {
            basic.pause(150)
            Cursor.set(LedSpriteProperty.X, 0)
        } else if (input.buttonIsPressed(Button.B)) {
            basic.pause(150)
            Cursor.change(LedSpriteProperty.X, 1)
        }
    }
})
basic.forever(function () {
    if (Cursor != null) {
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
    }
})
