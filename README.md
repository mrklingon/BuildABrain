# BuildABrain
Simple expert system for NeoTrinkey - yes/no questions, inspired by https://en.wikipedia.org/wiki/20Q

This project lets you put a simple expert system into your neotrinkey! The "brain" will ask yes/no question - touch pad #1 for "Yes" and pad #2 for "No"

Uncomment the dataset you want - this is shipped with a Star Wars set and Star Trek.
```
#from SWBrain import * #for Star Wars dataset
from STBrain import *  #for Star Trek dataset
```
Here's how the Star Trek set was designed:

<img width="796" height="745" alt="image" src="https://github.com/user-attachments/assets/717aed4b-6abd-48df-ac87-3dcc94f273b1" />

Basically, sketch out the decision tree, then number each node. Create a "yes" and "no" array that links each node to the next node (if any).

```
#Data in nodes for Star Trek info

Words = ["Think of someone from Kirk's Enterprise.","Gold uniform", "Captain", "Blue Uniform", "Kirk", "Russian", "Vulcan", "Male", "Chekov", "Sulu", "Spock", "Scotty", "Uhura", "Male", "Are they dead","McCoy", "Chapel"]

Yes = [0, 2, 4, 6, 0, 8, 10, 11, 0, 0, 0, 0, 0, 15, 0, 0, 0 ] #node for yes answers
No = [0, 3, 5, 7, 0, 9, 13, 12, 0, 0, 0, 14, 0, 16, 0, 0, 0 ] #node for no answers
```

note: the zeroth node should be the introduction, for Star Trek it's "Think of someone from Kirk's Enterprise."

Files:

* BuildABrain.py  - copy to code.py on NeoTrinkey
* STBrain.py - Star Trek data
* SWBrain.py - Star Wars data 
* prt.py - lets you redirect output via HID output, just set REPL=False

  Note:  if REPL=False the program will blink Neopixels until you touch one of the pads.


Here's how it looks in action:

```
Think of someone from Kirk's Enterprise.
Gold uniform?
No
Blue Uniform?
Yes
Vulcan?
Yes
Spock?
Yes
I was right!
let's try again
Think of someone from Kirk's Enterprise.
Gold uniform?
No
Blue Uniform?
No
Male?
Yes
Scotty?
No
Are they dead?
No
Maybe you should talk to my programmer!
```

Give it a try - see if you can build a brain for you NeoTrinkey!
