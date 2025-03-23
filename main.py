Puntos = 0
Iniciar = 0

def on_button_pressed_a():
    global Puntos
    basic.clear_screen()
    music.play(music.tone_playable(349, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_icon(IconNames.YES)
    basic.pause(100)
    if Puntos < 5:
        Puntos += 0 + 1
        basic.show_string("" + str((Puntos)))
        basic.pause(2000)
        basic.clear_screen()
    if Puntos == 5:
        basic.show_string("¡Ganador!")
        basic.pause(5000)
        music.play(music.string_playable("C5 B A G F E D C ", 120),
            music.PlaybackMode.UNTIL_DONE)
        Puntos = 0
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Iniciar
    Iniciar = 1
    for index in range(10):
        basic.show_string("" + str((Iniciar)))
        Iniciar += 1
        basic.pause(1000)
        music.play(music.tone_playable(988, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Puntos
    basic.clear_screen()
    music.play(music.tone_playable(349, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_icon(IconNames.NO)
    basic.pause(100)
    if Puntos < 1:
        Puntos += 0 + 1
        basic.show_string("" + str((Puntos)))
        basic.pause(2000)
        basic.clear_screen()
    if Puntos == 0:
        basic.show_string("Fin")
        basic.pause(5000)
        music.play(music.string_playable("C5 B A G F E D C ", 120),
            music.PlaybackMode.UNTIL_DONE)
        Puntos = 0
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
