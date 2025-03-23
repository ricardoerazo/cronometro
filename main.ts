let Puntos = 0
let Iniciar = 0
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    music.play(music.tonePlayable(349, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    basic.showIcon(IconNames.Yes)
    basic.pause(100)
    if (Puntos < 5) {
        Puntos += 0 + 1
        basic.showString("" + Puntos)
        basic.pause(2000)
        basic.clearScreen()
    }
    if (Puntos == 5) {
        basic.showString("¡Ganador!")
        basic.pause(5000)
        music.play(music.stringPlayable("C5 B A G F E D C ", 120), music.PlaybackMode.UntilDone)
        Puntos = 0
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.AB, function () {
    Iniciar = 1
    for (let index = 0; index < 10; index++) {
        basic.showString("" + Iniciar)
        Iniciar += 1
        basic.pause(1000)
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    }
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    music.play(music.tonePlayable(349, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    basic.showIcon(IconNames.No)
    basic.pause(100)
    if (Puntos < 1) {
        Puntos += 0 + 1
        basic.showString("" + Puntos)
        basic.pause(2000)
        basic.clearScreen()
    }
    if (Puntos == 0) {
        basic.showString("Fin")
        basic.pause(5000)
        music.play(music.stringPlayable("C5 B A G F E D C ", 120), music.PlaybackMode.UntilDone)
        Puntos = 0
        basic.clearScreen()
    }
})
