class Field:
    def __init__(self, x, y, params, size, walkable=True, has_bomb=False, is_mud=False, is_water=False, photo="", has_tree = False, has_rock = False):
        self.x = x
        self.y = y
        self.map_x = x * size
        self.map_y = y * size
        self.params = params
        self.walkable = walkable
        self.has_bomb = has_bomb
        self.is_mud = is_mud
        self.is_water = is_water
        self.photo = photo
        self.has_tree = has_tree
        self.has_rock = has_rock

        if is_mud:
            self.color = (80, 0, 0)
        elif is_water:
            self.color = (80, 0, 255)
        elif walkable:
            self.color = (2, 66, 0)
        else:
            self.color = (255, 0, 0)

        self.g_cost = 0
        self.h_cost = 0

    def get_position(self):
        return self.x, self.y

    def f_cost(self):
        return self.g_cost + self.h_cost

    def set_parent(self, parent):
        self.parent = parent
