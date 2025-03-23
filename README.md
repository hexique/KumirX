# KumirX
**KumirX** - is an analog of a russian programming system "Кумир" (Kumir). Its like a Turtle pseudo-programming language for russian schools.

Kumir

<img src="https://docs.altlinux.org/ru-RU/alt-education/10.1/html/alt-education/images/kumir.png" height="300">

## Shortcuts
Works in `gen.py`

`WASD` - Move turtle to up, left, down, right\
`Ctrl+WASD` - Move turle without paint\
`Alt+WASD` - Erase (Don't work in Kumir)

## Commands:
### Moves with paint:
`w`, `up`, `↑` - move turtle up\
`a`, `left`, `←` - move turtle left\
`s`, `down`, `↓` - move turtle down\
`d`, `right`, `→` - move turtle right

### Moves without paint:
`ww`, `upw`, `wwithout`, `upwithout`, `↑w` - move turtle up without paint\
`aw`, `leftw`, `awithout`, `leftwithout`, `←w` - move turtle left without paint\
`sw`, `downw`, `swithout`, `downwithout`, `↓w` - move turtle down without paint\
`dw`, `rightw`, `dwithout`, `rightwithout` `→w` - move turtle right without paint

### Moves with erase
`wd`, `upd`, `wdelete`, `updelete`, `↑d` - move turtle up and erase this tile\
`ad`, `leftd`, `adelete`, `leftdelete`, `←d` - move turtle left and erase this tile\
`sd`, `downd`, `sdelete`, `downdelete`, `↓d` - move turtle down and erase this tile\
`dd`, `rightd`, `ddelete`, `rightdelete` `→d` - move turtle right and erase this tile

### Other
`scale`, `sc` - Changes scale of one tile (in pixels, default is 20)\
`cooldows`, `cd` - Adds cooldown between tile paint (broken)

## Operators:
`:` - Multiplies a command or assign a value to variable. Example:\
`s:{value}` - Moves {value} tiles down\
`scale:value` - Assign a tile size to {value} pixels
