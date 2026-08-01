input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    stop_scan()
    basic.showLeds(`
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        # # # # #
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    control.reset()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    if (!scan_active) {
        note_grid[cursor_x][cursor_y] = !note_grid[cursor_x][cursor_y]
        render_scene()
        if (cursor_y == 4) {
            music.play(music.createSoundExpression(WaveShape.Square, 220, 1, 180, 0, 40, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
        } else {
            music.play(music.tonePlayable(WhatNote, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        }
        
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    stop_scan()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    stop_scan()
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    scan_active = true
    scan_column = 0
    render_scene()
})
let WhatNote = 0
let cursor_x = 4
let cursor_y = 0
let scan_active = false
let scan_column = 0
let note_grid =  {TODO: ListComp} 
let blink_state = false
let blink_timer = 0
function render_scene() {
    let y: number;
    let is_cursor_cell: any;
    let cursor_on_note: any;
    let should_hide_cursor: any;
    basic.clearScreen()
    for (let x = 0; x < 5; x++) {
        for (y = 0; y < 5; y++) {
            is_cursor_cell = x == cursor_x && y == cursor_y
            cursor_on_note = note_grid[cursor_x][cursor_y]
            should_hide_cursor = is_cursor_cell && cursor_on_note && !blink_state
            if (note_grid[x][y] && !should_hide_cursor) {
                led.plot(x, y)
            }
            
        }
    }
    if (scan_active) {
        for (y = 0; y < 5; y++) {
            if (!(scan_column == cursor_x && y == cursor_y && !blink_state)) {
                led.plot(scan_column, y)
            }
            
        }
    }
    
    if (!scan_active) {
        if (note_grid[cursor_x][cursor_y]) {
            if (blink_state) {
                led.plot(cursor_x, cursor_y)
            }
            
        } else {
            led.plot(cursor_x, cursor_y)
        }
        
    }
    
}

function stop_scan() {
    
    scan_active = false
    render_scene()
}

function set_what_note() {
    
    if (cursor_y == 0) {
        WhatNote = 262
    } else if (cursor_y == 1) {
        WhatNote = 311
    } else if (cursor_y == 2) {
        WhatNote = 349
    } else if (cursor_y == 3) {
        WhatNote = 392
    } else {
        WhatNote = 0
    }
    
}

set_what_note()
render_scene()
basic.forever(function on_forever() {
    
    if (!scan_active && input.buttonIsPressed(Button.B)) {
        basic.pause(150)
        cursor_x = (cursor_x + 1) % 5
        set_what_note()
        render_scene()
    }
    
})
basic.forever(function on_forever2() {
    
    if (!scan_active && input.buttonIsPressed(Button.A)) {
        basic.pause(150)
        cursor_y = (cursor_y + 1) % 5
        set_what_note()
        render_scene()
    }
    
})
basic.forever(function on_forever3() {
    
    if (scan_active) {
        render_scene()
        basic.pause(50)
        scan_column = (scan_column + 1) % 5
        if (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
            stop_scan()
        }
        
    }
    
})
basic.forever(function on_forever4() {
    
    blink_timer += 1
    if (blink_timer >= 0) {
        blink_timer = 0
        blink_state = !blink_state
        render_scene()
    }
    
    basic.pause(1)
})
