# ZMK config for a custom Ferris Sweep keyboard

This is the configuration for a custom-built Ferris Sweep kit 
sold by [Mechboards UK](https://mechboards.co.uk/products/ferris-sweep-kit?variant=41437490544845)
using nice!nano v2 controllers.

The PCB uses a different pin layout than other Ferris Sweep boards so
a custom shield is needed (see `config/boards/shields/`).

## Layout

### Base layer:

    "       ,       .       p       y           f       g       c       r       l
    a ALT   o GUI   e SHIFT u CTRL  i           d       h CTRL  t SHIFT n GUI   s ALT
    :       q       j       k       x           b       m       w       v       z

            ARROW_LAYER   SPACE / MEH           ARROW_LAYER     NUM_LAYER

### Num layer:

    '       _       &       {       }                   7       8       9       BACKSPACE
    +       -       =       (       )           0       4       5       6       ENTER     
    ;       @       |       [       ]                   1       2       3

                                  TAB           CAPS_WORD       

### Arrow layer:

    ESC     %       #       <       >                           PG_DN   PG_UP   DEL 
    !       /       *       $       ^                   LEFT    DOWN    UP      RIGHT
            \       ~       `       ?                   A+LEFT                  A+RIGHT 

            NUM_LAYER                                           F_KEY_LAYER

### F-key layer:

     >>|    |<<     PLAY                        F12     F7      F8      F9    
     VOL+   VOL-    MUTE                        F11     F4      F5      F6
                                                F10     F1      F2      F3

                         SYSTEM_LAYER

### System layer:

    RESET                           BT_SEL_0                                    RESET
    BOOTLOADER                      BT_SEL_1                                    BOOTLOADER
                            BT_CLR  BT_SEL_2

## The ideas behind the layout

This is a general-purpose Dvorak layout featuring:

### No shifted keys besides alpha keys

We have to use layers to support all keys on a 34-key layout. 
I always struggled with shifted keys (like `:` and `;`) and keys on a
separate layer. You constantly use different modifier+key combinations, 
which messes up the flow.

That's why this layout only uses SHIFT for alpha keys. (Technically, you can 
use SHIFT on any key, and it will work, but you don't have to and should not.)


### Home row mods (ALT, CONTROL, GUI, SHIFT)

Coming from QMK (Moonlander), I was amazed at how uncomplicated and stable
the hold-tap behavior is in ZMK. No more accidental modifier+key presses when
rolling over the home row. And no delays either.


### No double tapping

As with everything, this comes down to taste. I like alternating keys and dislike
double tapping. 


### All key combinations are available 

It's easy to produce a layout that only supports some combinations
of modifiers and keys. I've been there. :-)

### Deviation from standard Dvorak

Because I type double quotes much more often then single quotes and colon much more often than
semicolon (VIM user here :-) ), I switched those keys.

## How to type certain symbols

- € `ALT+SHIFT+2`
- £ `ALT+3`
- § `ALT+6`

