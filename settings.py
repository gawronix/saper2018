"""
Settings for setup conts for run a game
"""

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800

BLACK = (0, 0, 0)

HOW_MANY_FIELDS = 10

FIELD_SIZE = DISPLAY_HEIGHT / HOW_MANY_FIELDS
ROBOT_SIZE = int(FIELD_SIZE * 0.8)

MODEL_FILE = 'tf/tf_files_1/retrained_graph.pb'
LABEL_FILE = 'tf/tf_files_1/retrained_labels.txt'
MODEL_FILE_1 = 'tf/tf_files_2/retrained_graph.pb'
LABEL_FILE_1 = 'tf/tf_files_2/retrained_labels.txt'

ROBOT_IMG_PATH = 'images/robot.png'
BOMB_IMG_PATH = 'images/bomba.png'
TREE_IMG_PATH = 'images/tree.png'
ROCK_IMG_PATH = 'images/rock.png'


DATA_PATH = 'data/data.txt'
FONT_NAME = 'freesansbold.ttf'
GAME_NAME = 'Saper'

ACTIONS = {
    'bomba': 'Detonuje',
    'c4': 'Rozbrajam',
    'dynamit': 'Zabieram',
    'mina': 'Detonuje'
}
