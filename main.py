import pygame
from time import sleep

from grid import Grid
from a_star import AStar
from is_bomb_matcher import IsBombMatcher
import settings


def parse_data(file_name):
    # funkcja do parsowania danych z pliku
    to_return = []
    file = open(file_name, "r")
    for line in file:
        to_return.insert(len(to_return), line.rstrip().split(','))
    return to_return


pygame.init()

gameDisplay = pygame.display.set_mode((settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT))
pygame.display.set_caption(settings.GAME_NAME)
clock = pygame.time.Clock()

robot_img = pygame.image.load(settings.ROBOT_IMG_PATH)
robot_img = pygame.transform.scale(robot_img, (settings.ROBOT_SIZE, settings.ROBOT_SIZE))

bomba_img = pygame.image.load(settings.BOMB_IMG_PATH)
bomba_img = pygame.transform.scale(bomba_img, (settings.ROBOT_SIZE, settings.ROBOT_SIZE))

field_params = parse_data(settings.DATA_PATH)

map_obj = Grid(settings.HOW_MANY_FIELDS, settings.FIELD_SIZE, field_params)
game_map = map_obj.grid


def read_photo(field, model_file, label_file):
    # wczytanie obrazka
    is_b = IsBombMatcher()  # wykorzystanie tensorflow
    results = is_b.get_result(field.photo, model_file, label_file)
    return results


def move_robot(field):
    gameDisplay.blit(robot_img, (field.map_x, field.map_y))


[first_field, last_field] = map_obj.first_and_last()


def scan_for_bombs():
    # ustalanie pozycji bomb
    bomb_fields = []
    for y in game_map:
        for x in y:
            if is_bomb_here(x):
                print('Bomb position {}'.format(x.get_position()))
                bomb_fields.insert(len(bomb_fields), x)
    print('Ilość bomb: {}'.format(len(bomb_fields)))
    return bomb_fields


def is_bomb_here(field):
    # sprawdzenie czy tu jest bomba
    results = read_photo(field, settings.MODEL_FILE, settings.LABEL_FILE)
    first_result = results[1]
    return first_result.result_name == "bomb" and first_result.result_percent*100 > 75


fields_with_bombs = scan_for_bombs()


def game_loop(start_point, fields_with_bombs):
    # główna pętla
    a = AStar()
    current_field = start_point
    field_to_move = fields_with_bombs[0]
    fields_with_bombs.remove(field_to_move)
    path = a.find_path(current_field, field_to_move, map_obj)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        for y in game_map:
            for x in y:
                gameDisplay.fill(x.color, (x.map_x, x.map_y, settings.FIELD_SIZE, settings.FIELD_SIZE))
                if x.has_bomb:
                    gameDisplay.blit(bomba_img, (x.map_x, x.map_y))

        if len(path) > 0:
            current_field = path[0]
            move_robot(current_field)
            path.remove(current_field)

        elif len(fields_with_bombs) > 0:
            field_to_move = fields_with_bombs[0]
            fields_with_bombs.remove(field_to_move)
            path = a.find_path(current_field, field_to_move, map_obj)
            move_robot(current_field)

        if current_field == field_to_move:
            make_action_with_bomb(current_field, settings.LABEL_FILE_1, settings.MODEL_FILE_1)
            current_field.has_bomb = False
            sleep(1)
            if len(fields_with_bombs) == 0:
                quit()

        pygame.display.update()
        clock.tick(3)


def make_action_with_bomb(current_field, label_file, model_file):
    # wykonanie akcji
    what_bomb = read_photo(current_field, model_file, label_file)[1]
    action = settings.ACTIONS.get(what_bomb.result_name, 'To nie bomba.')
    found = 'Znaleziono: {} na {:.2f}%'.format(what_bomb.result_name, what_bomb.result_percent * 100)
    print('{}! {}'.format(action, found))
    pygame.display.update()

game_loop(first_field, fields_with_bombs)
