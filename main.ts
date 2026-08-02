function scroll () {
    for (let index = 0; index < 4; index++) {
        basic.pause(500)
        scroll1.change(LedSpriteProperty.X, 1)
        scroll2.change(LedSpriteProperty.X, 1)
        scroll3.change(LedSpriteProperty.X, 1)
        scroll4.change(LedSpriteProperty.X, 1)
        scroll5.change(LedSpriteProperty.X, 1)
    }
}
input.onButtonPressed(Button.AB, function () {
    Cursor.delete()
    control.reset()
})
input.onGesture(Gesture.Shake, function () {
    scroll1 = game.createSprite(0, 0)
    scroll2 = game.createSprite(0, 1)
    scroll3 = game.createSprite(0, 2)
    scroll4 = game.createSprite(0, 3)
    scroll5 = game.createSprite(0, 4)
    scroll()
    Cursor.delete()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (Cursor.get(LedSpriteProperty.Y) == 4) {
        music.play(music.createSoundExpression(WaveShape.Square, 200, 1, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
    } else {
        music.play(music.tonePlayable(WhatNote, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    }
    Note2 = game.createSprite(Cursor.get(LedSpriteProperty.X), Cursor.get(LedSpriteProperty.Y))
})
let Note2: game.LedSprite = null
let WhatNote = 0
let scroll5: game.LedSprite = null
let scroll4: game.LedSprite = null
let scroll3: game.LedSprite = null
let scroll2: game.LedSprite = null
let scroll1: game.LedSprite = null
let Cursor: game.LedSprite = null
Cursor = game.createSprite(4, 0)
basic.forever(function () {
    basic.pause(150)
    if (Cursor.get(LedSpriteProperty.Y) == 4 && input.buttonIsPressed(Button.A)) {
        basic.pause(150)
        Cursor.set(LedSpriteProperty.Y, 0)
    } else if (input.buttonIsPressed(Button.A)) {
        basic.pause(150)
        Cursor.change(LedSpriteProperty.Y, 1)
    }
})
basic.forever(function () {
    if (Cursor.get(LedSpriteProperty.X) == 4 && input.buttonIsPressed(Button.B)) {
        basic.pause(150)
        Cursor.set(LedSpriteProperty.X, 0)
    } else if (input.buttonIsPressed(Button.B)) {
        basic.pause(150)
        Cursor.change(LedSpriteProperty.X, 1)
    }
})
basic.forever(function () {
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
})
