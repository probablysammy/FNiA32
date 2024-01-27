win_width = 640 #game window width
win_height = 480 #game window height
tilesize = 32 #define size of tiles
fps = 60 #define frames per second

#define colours using rgb
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128,128,128)
brown = (159, 129, 97)
keygrey = (195,195,195)

#define speeds
player_speed = 3
enemy_speed = 2

#define layers
menu_layer = 6
dialogue_layer = 5
player_layer = 4
item_layer = 3
friend_layer = 3
enemy_layer = 2
block_layer = 2
ground_layer = 1
hell_layer = 0

levelmap = [
    [
    'BBBBBBBBBBBBBBBBBBBB',
    'B........D.........B',
    'B..................B',
    'B........E.........B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B........P.........B',
    'B..................B',
    'B..................B',
    'B...............N..B',
    'B........I.........B',
    'B..................B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB'
    ],
    [
    'BBBBBBBBBBBBBBBBBBBB',
    'B..N.....D.........B',
    'B........P.........B',
    'B..................B',
    'BBBBBBBB...BBBBBBBBB',
    'B......B...........B',
    'B......B...........B',
    'B..B..........BBBBBB',
    'BBBB..........B....B',
    'B..B..BBBBBB..B....B',
    'B..B..B.......BBB..B',
    'B..B..BBBBBB....B..B',
    'B..B.......B....B..B',
    'B......B.I.B.......B',
    'BBBBBBBBBBBBBBBBBBBB'
    ],
    [
    'BBBBBBBBBBBBBBBBBBBB',
    'B........D.........B',
    'B........P.........B',
    'B...........N......B',
    'BBBBBB........BBBBBB',
    'B......E...........B',
    'B...E..............B',
    'B...........E......B',
    'B..................B',
    'B......E...........B',
    'B.............E....B',
    'B.......E..........B',
    'B..................B',
    'B........I.........B',
    'BBBBBBBBBBBBBBBBBBBB'
    ],
    [
    'BBBBBBBBBBBBBBBBBBBB',
    'B........D.........B',
    'B........P.........B',
    'B...........N......B',
    'B..................B',
    'B..N...............B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B............N.....B',
    'B..................B',
    'B........I.........B',
    'BBBBBBBBBBBBBBBBBBBB'
    ],
    [
    'BBBBBBBBBBBBBBBBBBBB',
    'B........S.........B',
    'B........P.........B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B...D..........D...B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B........D.........B',
    'B..................B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB'
    ]
]

itemlist = "item","flashlight","key","cake"

tutorialdialogue = [
    ["box 1 line 1", "box 1 line 2"],
    ["box 2 line 1", "box 2 line 2"],
    ["box 3 line 1", "box 3 line 2"]
]

fd_1 = [
    ["Press x on the yellow star","to pick up an item!"],
["Go on, do it!","You won't regret it!"],
    ["It's easy! Just","press x."]
]
fd_2 = [
    ["Can you get the item at","the end of the maze?"],
    ["I'd do it myself, but","I'm scared."],
    ["What if I get lost?","Please help me!"]
]
fd_3 = [
    ["Can you get the item that's","past all the enemies?"],
    ["Just dodge them.","It shouldn't be difficult."],
    ["Thanks a bunch!",""]
]
fd_4 =[
    ["Great job!","You did so good!"],
    ["Seriously!",""]
]
fd_5 = [
    ["Everyone is so proud of you!",""],
    ["Major W!",""]
]
fd_6 = [
    ["Yippee!",""]
]

friend_dialogue = [
    fd_1,fd_2,fd_3,fd_4,fd_5,fd_6
    ]


tut_item = [
    ["You got: TUTORIAL ITEM","Press escape to equip in the menu"]
]
flashlight = [
    ["You got: FLASHLIGHT","Press escape to equip in the menu"]
]
key = [
    ["You got: KEY","Press escape to equip in the menu"]
]
cake = [
    ["You got: CAKE", "Press escape to equip in the menu"]
]
item_dialogue = [
    tut_item,flashlight,key,cake
]

