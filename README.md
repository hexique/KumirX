# KumirX
**KumirX** - an analog of a russian programming system "Кумир" (Kumir). Its like a Turtle pseudo-programming language for russian schools.

<p align="left">
<img src="https://docs.altlinux.org/ru-RU/alt-education/10.1/html/alt-education/images/kumir.png" title="Kumir" height="300" >
<img src="preview.png" title="KumirX" height="300">
</p>

## Code examples:

All Of these code will display minimalistic Linux Mint logo:\
```s:4 d:6 w:4 a:2 s:2 a ww:2 a s:3 aw ww:4```\
```down:4 right:6 up:4 left:2 down:2 left upw:2 left down:3 leftw upw:4```\
```down:4 right:6 up:4 left:2 down:2 left upwithout:2 left down:3 leftwithout upw:4```\
```↓:4 →:6 ↑:4 ←:2 ↓:2 ← ↑w:2 ← ↓:3 ←w ↑w:4```

## Settings

`Hide buttons` - Hide all buttons on the bottom (cuz they are so laggy)

## Shortcuts

`F5` - Run code\
`Ctrl+S` - Save\
`Ctrl+Alt+S` - Save as\
`Ctrl+O` - Open file\
`Ctrl+P` - Settings

## Commands
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
`color`, `col`, `c` - Changes a color of trail\
Example: `col:green` - Changes a turtle trail color to green\
Example №2: `col:#0000ff` - Changes a trail color to #0000ff, or blue

`cooldown`, `cd` - Adds cooldown between tile paint (broken)\
Example: `cooldown:1000` - cooldown between steps will be 1000ms or 1sec

`setpos`, `set`, `pos`, `sp` - Changes a position of turtle\
Example: `pos:5:7` - Turtle position will be x: 5, y: 7\
Example №2: `pos:0.5:17` - Turtle position will be x: 0.5 (a half of tile), y: 17\
Example №3: `pos:1:math.sin(1)` - Turtle position will be x: 1 y: sinus of number 1 (its 0.84)\

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

`func`, `fun`, `f` - Declarates or induces a function.\
Example: `func:go-right:d` - Creates a function, that goes right\
Example 1.1: `func:go-right` - Induces a function that we created in example 1

Exmaple №2: `func:square:d:5_s:5_a:5_w:5` - Creates a function, that draws a square 5x5.\
Exmaple №2.1: `func:square` - Induces a function that draws a square.

# KumirEditor
**KumirEditor** - a code generator on Kumir that uses only a few keys on your keyboard, instead of writing code

## Shortcuts in KumirEditor (gen.py)

`WASD` - Move turtle to up, left, down, right\
`Ctrl+WASD` - Move turle without paint\
`Alt+WASD` - Erase (Don't work in Kumir)

## Settings in KumirEditor
### Programm system
Translates your code to selected programm system.

`Kumir` - original KumirX reference. Code example: `вниз закрасить вправо закрасить верх влево`\
`KumirX letters` - KumirX code with commands as letters WASD. Code example: `s d ww aw`\
`KumirX fullwords` - KumirX code with commands as words and full arguments. Code example: `down right upwithout leftwithout`\
`KumirX words` - KumirX code with commands as words and abbreviated arguments. Code example: `down right upw leftw`\
`KumirX arrows` - KumirX code with commands as arrow symbols (↑←↓→). Code example: `↓ → ↑w ←w`

# KxGraph
KxGraph - a simple graphing calculator that can graph functions using Python.

## Graph examples:
`0` - straight line at 0.\
`x` - diagonal.\
`x**2` - square graph.\
`math.sin(x)` - sinusoid.\
`math.sin(x/10)*10` - more detailed sinusoid.\
`math.tan(x)` - tangent graph.\
`math.exp(x)` - exponent graph.

There is used built-in module named 'math'. Documentation and all functions: <a href="https://docs.python.org/3/library/math.html" target="_blank">https://docs.python.org/3/library/math.html</a>

## Operators and built-in functions:
`|` - splits your graph and allows you to create several graphs in one line\
Example: `x | x+2 | x*2` - Will create a 3 graphs\
Example №2: `sin(x) | math.cos(x)` - Sine wave and cosine wave

`loop(function, **kwargs (start*, end))` - Works like a loop and saves iteration in variable 'item'\
Example: `loop('x*item', start=0, end=5)` - Makes a five graphs with functions x*0, x\*1, x\*2, etc.\
Example №2: `loop('sin(x/item)*item', end=10)` - Makes a ten sine waves, that are getting bigger and bigger (math.sin(x/0)\*0, math.sin(x/1)\*1, math.sin(x/2)\*2...)

`isprime(num)` - Checks for a prime number, if it prime - returns True (1), else returns False (0)\
Example: `isprime(7)` - Returns 1 because 7 is prime number\
Exmaple №2: `isprime(9)` - Returns 0 because 9 is not prime number (divisior is 7)

`get_prime(num)` - Returns a *num*th prime number\
Example: `get_prime(3)` - Returns 5, because this is a 3rd prime number (2, 3, **5**)\
Example №2: `get_prime(4)` - Returns 7, 4th prime number. (2, 3, 5, **7**)\
Example №3: `get_prime(10)` - Returns 27, (2, 3, 5, 7, 11, 13, 17, 19, 23, **27**)

`fibonacci(num)` - Returns a *num*th number in fibonacci sequence\
Example: `fibonacci(5)` - Returns 13, because 13 is a 5th number in fibonacci sequence\
Exmaple №2: `fibonacci(3)` - Returns 5 (5th fibonacci number)\
Example №3: `fibonacci(16)` - Returns 2584 (16th fibonacci number)

`fibonacci(num)` - Returns a *num*th number in fibonacci sequence\
Example: `fibonacci(5)` - Returns 13, because 13 is a 5th number in fibonacci sequence\
Exmaple №2: `fibonacci(3)` - Returns 5 (5th fibonacci number)\
Example №3: `fibonacci(16)` - Returns 2584 (16th fibonacci number)

`collatz(num)` - Returns a sequence of [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) of num.\
Example: `collatz(3)` - Returns [3, 10, 5, 16, 8, 4, 2, 1].\
Example №2: `len(collatz(27))` - Returns 112 (the length of sequence of number 27)\
Exmaple №3 `sorted(collatz(123))[-1]` - Returns the biggest number in sequence of number 123 (628)

`divisiors(num)` - Returns a list of divisiors of num.\
Example: `divisiors(10)` - Returns [1, 2, 5, 10] (all divisiors of number 10)\
Example №2: `len(divisiors(10))` - Returns 4 (total divisiors)

## Shortcuts in KxGraph (graph.py)

`Enter`, `F5` - Create graph\
`Enter` (in settings) - Apply\
`Ctrl+P`, `Tab` - Settings\
`Ctrl+G` - Color table\
`Delete` - Clear\
`Esc` - Delete graph by index in settings\
`Ctrl+Esc` - Delete last graph\
`Shift+Esc` - Delete first graph\
`Ctrl+S` - Save graph as file

## Settings in KxGraph
### Main settings
`Step` - The smaller the number, the more accurate. Is a number that is added to x (default value is 1)\
`Scale` - Scale of one tile (default value is step*10)
`Offset` - Places the graph down by a certain amount of units (default value is 0)\
`Index` - Moves x units graph down (default value is -1)

`Different color for every graph` - All new graphs will be a different colors\
`Delete graph after error` - If while drawing graph will be error occured program will delete this graph\
`Graph switch` - Deletes all graphs before creating new

### Customization
`Background color` - Background color in program (default valuue is #1b1b1b)\
`Offset color` - Color of line at 0 (default value is #2d2d2d)\
`Graph color` - Background color in program, that applys when change graph color is turned off (default value is #ffffff)

`Colors` - Massive of colors with turned on option change graph color, if it ends it will generate random colors (default value is [#ff0000, #00ff00, #0000ff, #ffff00, #00ffff, #ff00ff])\
`Add` - Add color in massive at the end\
`Delete` - Delete an element in massive by index option\
`Clear` - Deletes all elements from massive


