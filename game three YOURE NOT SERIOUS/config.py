#define size of game window
win_width = 640
win_height = 480
tilesize = 32 #define size of tiles
fps = 60 #define frames per second

#define layers
player_layer = 4
enemy_layer = 3
block_layer = 2
ground_layer = 1

#define speeds
player_speed = 3
enemy_speed = 2

#define colours using rgb
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

#define current level
level = 0


level3map = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B.......BBB........B',
    'B......B...........B',
    'B.......B..........B',
    'B.........B........B',
    'B.......B.P........B',
    'B.....B............B',
    'B.......BBB........B',
    'B..................B',
    'B..................B',
    'B........E.........B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB',
]

level2map = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B............E.....B',
    'B..................B',
    'B........BBBB......B',
    'B.......B.....B....B',
    'B.............B....B',
    'B.........P...B....B',
    'B...........B......B',
    'B.........B........B',
    'B........BBBBB.....B',
    'B..................B',
    'B........E.........B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB',
]

level1map = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B............E.....B',
    'B....BB............B',
    'B...B..B...........B',
    'B.......B.....B....B',
    'B.............B....B',
    'B....B....P..B.....B',
    'B.....B.....B......B',
    'B.......B..........B',
    'B.........B........B',
    'B..................B',
    'B........E.........B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB',
]

tilemaps = [['BBBBBBBBBBBBBBBBBBBB','B.....BBB..........B','B..................B','B.........E........B','B..................B','B........I.........B','B..................B','B.........P........B','B..................B','B..................B','B..................B','B..................B','B..................B','B..................B','BBBBBBBBBBBBBBBBBBBB'],
    ['BBBBBBBBBBBBBBBBBBBB','B..................B','B............E.....B','B....BB............B','B...B..B...........B','B.......B.....B....B','B.............B....B','B....B....P..B.....B','B.....B.....B......B','B.......B..........B','B.........B........B','B..................B','B........E.........B','B..................B','BBBBBBBBBBBBBBBBBBBB'],
    [#level 2 map
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B............E.....B',
    'B..................B',
    'B........BBBB......B',
    'B.......B.....B....B',
    'B.............B....B',
    'B.........P...B....B',
    'B...........B......B',
    'B.........B........B',
    'B........BBBBB.....B',
    'B..................B',
    'B........E.........B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB'
    ],
    [#level 3 map
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B.......BBB........B',
    'B......B...........B',
    'B.......B..........B',
    'B.........B........B',
    'B.......B.P........B',
    'B.....B............B',
    'B.......BBB........B',
    'B..................B',
    'B..................B',
    'B........E.........B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB'
    ]
    ]
