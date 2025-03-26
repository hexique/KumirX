# KumirX
**KumirX** - is an analog of a russian programming system "Кумир" (Kumir). Its like a Turtle pseudo-programming language for russian schools.

Kumir

<img src="https://docs.altlinux.org/ru-RU/alt-education/10.1/html/alt-education/images/kumir.png" title="Kumir" height="300">
<img src="preview.png" title="KumirX" height="300">

## Code examples:

All Of these code will display minimalistic Linux Mint logo:\
```s:4 d:6 w:4 a:2 s:2 a ww:2 a s:3 aw ww:4```\
```down:4 right:6 up:4 left:2 down:2 left upw:2 left down:3 leftw upw:4```\
```down:4 right:6 up:4 left:2 down:2 left upwithout:2 left down:3 leftwithout upw:4```\
```↓:4 →:6 ↑:4 ←:2 ↓:2 ← ↑w:2 ← ↓:3 ←w ↑w:4```

## Shortcuts in `gen.py`

`WASD` - Move turtle to up, left, down, right\
`Ctrl+WASD` - Move turle without paint\
`Alt+WASD` - Erase (Don't work in Kumir)

## Shortcuts in `main.py`

`F5` - Run code
`Ctrl+S` - Save
`Ctrl+Alt+S` - Save as
`Ctrl+O` - Open file
`Ctrl+P` - Settings

## Settings
### Programm system
Translates your code to selected programm system.

`Kumir` - original KumirX reference. Code example: `вниз закрасить вправо закрасить верх влево`\
`KumirX letters` - KumirX code with commands as letters WASD. Code example: `s d ww aw`\
`KumirX fullwords` - KumirX code with commands as words and full arguments. Code example: `down right upwithout leftwithout`\
`KumirX words` - KumirX code with commands as words and abbreviated arguments. Code example: `down right upw leftw`\
`KumirX arrows` - KumirX code with commands as arrow symbols (↑←↓→). Code example: `↓ → ↑w ←w`

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
#### `color`, `col`, `c` - Changes a color of trail\
Example: `col:green` - Changes a turtle trail color to green\
Example №2: `col:#0000ff` - Changes a trail color to #0000ff, or blue

`cooldown`, `cd` - Adds cooldown between tile paint (broken)\
Example: `cooldown:1000` - cooldown between steps will be 1000ms or 1sec

`setpos`, `set`, `pos`, `sp` - Changes a position of turtle\
Example: `pos:5:7` - Turtle position will be x: 5, y: 7\
Example №2: `pos:0.5:17` - Turtle position will be x: 0.5 (a half of tile), y: 17\
Example №3: `pos:1:math.sin(1)` - Turtle position will be x: 1 y: sinus of number 1, and its equals or 0.84\

`pointercolor`, `pointercol`, `pcol`, `pc` - Changes a color of turtle\
Example: `pointercol:cyan` - Changes a color of turtle to cyan (default is 'red')\
Example №2: `pointercol:#1b1b1b` - Changes a color of turtle to `#1b1b1b` (color of background and this command makes turtle invisible)

`scale`, `sc` - Changes scale of one tile\
Example: `sc:10` - Tile size changed to 10 pixels (default is 20)\
Example №2: `sc:1.5` - Tile size changes to 1.5 pixels

`word`, `wo` - Displays a word\
Example: `word:hello` - Displays a pixel text 'hello'\
Example №2: `word:hello-world` - Displays a pixel text 'hello world' (hyphen is treated as a space)

`loop`, `for`, `l` - Executes a sequence of commands several times.\
Example: `for:5:d_sw` - 5 times move diagonaly (use underscore instead of space).\
Example №2: `for:6:right:5` - Go right 5 times by 6 times (5*6=30).\
Example №3: `for:7:pos:item:5_p` - Paint an every tile by y from 0 to 7.\
Example №4: `sc:5for:100:pos%item%(math.sin(item)+5)*5_p` - Draws a sinusoid.

`func`, `fun`, `f` - Declarates or induces a function.\.
Example: `func:go-right:d` - Creates a function, that goes right
Example 1.1: `func:go-right` - Induces a function that we created in example 1

Exmaple №2: `func:square:d:5_s:5_a:5_w:5` - Creates a function, that draws a square 5x5.
Exmaple №2.1: `func:square` - Induces a function that draws a square.
