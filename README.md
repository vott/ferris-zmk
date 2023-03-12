# ZMK config for a custom Ferris Sweep keyboard

This is the configuration for a custom-built Ferris Sweep kit 
sold by [Mechboards UK](https://mechboards.co.uk/products/ferris-sweep-kit?variant=41437490544845)
using nice!nano v2 controllers.

The PCB uses a different pin layout than other Ferris Sweep boards so
a custom shield is needed (see `config/boards/shields/`).

## Layout

### Base layer:

    "       ,       .       p       y           f       g       c       r       l
    a       o ALT   e CTRL  u GUI   i           d       h GUI   t CTRL  n ALT   s
    :       q       j       k       x           b       m       w       v       z

            ESC MEH         SPACE               SHIFT           NUM_LAYER

### Num layer:

    '       _       &       {       }           ?       7       8       9       BACKSPACE
    TAB     -       =       (       )           !       4       5       6     
    ;       @       |       [       ]           0       1       2       3

            ARROW_LAYER     ENTER               CAPS_WORD     

### Arrow layer:

    `       %       #       <       >                                           DEL 
    S+TAB   +       =       $       ^           LEFT    DOWN    UP      RIGHT
                    \       /       ~

                                                                F_KEY_LAYER

### F-key layer:

            VOL+    >>|                         F12     F7      F8      F9    
            VOL-    |<<                         F11     F4      F5      F6
            MUTE    PLAY                        F10     F1      F2      F3

                            SYSTEM_LAYER

### System layer:

    RESET                           BT_SEL_0                                    RESET
    BOOTLOADER                      BT_SEL_1                                    BOOTLOADER
                            BT_CLR  BT_SEL_2


### TODOs

- The left thumb feels a bit overused because of layer switching.

## The ideas behind the layout

This is a general-purpose Dvorak layout featuring:

### No shifted keys besides alpha keys

We have to use layers to support all keys on a 34-key layout. 
I always struggled with shifted keys (like `:` and `;`) and keys on a
separate layer. You constantly use different modifier+key combinations, 
which messes up the flow.

That's why this layout only uses SHIFT for alpha keys. (Technically, you can 
use SHIFT on any key, and it will work, but you don't have to and should not.)


### Consistent layer switching

There is only one way to switch to a layer: using a 
[sticky layer key](https://zmk.dev/docs/behaviors/sticky-layer) on the right
thumb key on the base layer. 
From there, you can switch to the third layer using the *left* thumb key. 
Then, you go to the fourth layer with the *right* thumb key. 

To press the arrow-up key, for example, you press: `right thumb  left thumb  t` 

Hold the last layer-switch key to type multiple keys on that layer.

The reasoning for this is the same as for the shifted keys: reducing the 
amount of confusion. 


### Home row mods (ALT, CONTROL, GUI)

Coming from QMK (Moonlander), I was amazed at how uncomplicated and stable
the hold-tap behavior is in ZMK. No more accidental modifier+key presses when
rolling over the home row. And no delays either.


### A dedicated SHIFT (thumb) key

I got this from [Ben Vallack](https://www.youtube.com/watch?v=8wZ8FRwOzhU&t=444s).
His initial reason for having a separated SHIFT key was problems with
rolling when having SHIFT as a home row mod. Newer versions of ZMK eliminate this
problem.

But a dedicated SHIFT thumb key solves another problem:
Having to alternate between the left and right hand when typing capital letters!

It is much easier to know that SHIFT is always the same key regardless of whether
a letter is on the left or right side. And you don't have to hold SHIFT, you can
simply roll over it. 


### No double tapping

As with everything, this comes down to taste. I like alternating keys and dislike
double tapping. 


### All key combinations are available 

It's easy to produce a layout that only supports some combinations
of modifiers and keys. I've been there. :-)
