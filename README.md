# KumirX
**KumirX** - is an analog of a russian programming system "Кумир" (Kumir). Its like a Turtle pseudo-programming language for russian schools.

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
`scale`, `sc` - Changes scale of one tile (in pixels, default is 20)
`cooldows`, `cd` - Adds cooldown between tile paint (broken)

## Operators:
`:` - Multiplies a command or assign a value to variable. Example:\
`s:10` - Moves 10 tiles down\
`scale:10` - Assign a tile size to 10 pixels
