from tkinter import *
from tkinter.ttk import Combobox
from creatures.Plant import Plant
from creatures.Animal import Animal
from World import World
from Point import Point
from Arrows import Arrows


class Window(object):
    TITLE = "World Simulator Stanislaw Gora 165696"
    NEXT_ROUND_TEXT = "Next Round"
    SAVE_WORLD_TEXT = "Save World"
    LOAD_WORLD_TEXT = "Load World"
    CREATE_WORLD_TEXT = "Create World"
    HUMAN_ABILITY_TEXT = "Use human ability"

    DEF_X_SIZE = 1200
    DEF_Y_SIZE = 600
    WORLD_SIZE = 20
    TILE_SIZE = 20
    CANVAS_OFFSET = TILE_SIZE
    EMPTY_TILE_COLOR = "#ddd"
    EMPTY_TILE_SIZE = 0.15
    ACCENT_COLOR = "#6abff7"

    PADDING = 12
    CANVAS_PERCENT = 0.6

    def __init__(self, master):
        master.title(Window.TITLE)
        self.world = World()

        self.button_frame = Frame(master)
        self.next_round_button = Button(self.button_frame, text=str(Window.NEXT_ROUND_TEXT),
                                        command=self.next_round, bg=Window.ACCENT_COLOR)
        self.next_round_button.pack(side=LEFT, anchor=W, padx=Window.PADDING, pady=Window.PADDING)
        self.human_ability_button = Button(self.button_frame, text=str(Window.HUMAN_ABILITY_TEXT),
                                           command=self.world.use_human_ability, bg=Window.ACCENT_COLOR)
        self.human_ability_button.pack(side=LEFT, anchor=W, padx=Window.PADDING, pady=Window.PADDING)
        self.creature_choice_var = StringVar()
        self.creature_choice = Combobox(self.button_frame, textvariable=self.creature_choice_var,
                                        values=Animal.get_names() + Plant.get_names(), state='readonly')
        self.creature_choice.pack(side=LEFT, anchor=W, padx=Window.PADDING, pady=Window.PADDING)
        self.creature_choice.current(0)

        self.save_frame = Frame(self.button_frame)
        self.save_world_button = Button(self.save_frame, text=str(Window.SAVE_WORLD_TEXT),
                                        bg=Window.ACCENT_COLOR, command=self.world.save_world_state)
        self.save_world_button.pack(side=LEFT, anchor=W, padx=Window.PADDING, pady=Window.PADDING)
        self.load_world_button = Button(self.save_frame, text=str(Window.LOAD_WORLD_TEXT),
                                        bg=Window.ACCENT_COLOR, command=self.load_world)
        self.load_world_button.pack(side=LEFT, anchor=W, padx=Window.PADDING, pady=Window.PADDING)
        self.save_frame.pack(side=LEFT, anchor=W)

        self.create_world_button = Button(self.button_frame, text=str(Window.CREATE_WORLD_TEXT),
                                          command=self.create_new_world, bg=Window.ACCENT_COLOR)
        self.create_world_button.pack(side=LEFT, anchor=W, padx=Window.PADDING, pady=Window.PADDING)
        self.button_frame.pack(fill=X)
        self.main_frame = Frame(master)
        self.canvas = Canvas(self.main_frame)
        self.canvas.bind("<Button-1>", self.add_creature)
        self.canvas.place(relheight=1, relwidth=Window.CANVAS_PERCENT)

        self.log_area = Text(self.main_frame)
        self.log_area.configure(state='disabled')
        self.log_area.place(relx=Window.CANVAS_PERCENT, relheight=1, relwidth=1 - Window.CANVAS_PERCENT)
        self.world.log_area = self.log_area

        self.main_frame.bind_all('<Key>', self.move_human)
        self.main_frame.pack(fill=BOTH, expand=1)

        self.create_new_world()

    def create_new_world(self):
        self.world.reset(Point(Window.WORLD_SIZE, Window.WORLD_SIZE))
        self.draw_world()

    def next_round(self):
        self.log_area.configure(state='normal')
        self.log_area.delete('1.0', END)
        self.log_area.configure(state='disabled')

        self.world.update()
        self.draw_world()

    def move_human(self, event):
        if self.world.get_human() is None:
            return
        if event.keysym == 'Right':
            self.world.get_human().set_next_move(Arrows.RIGHT)
        elif event.keysym == 'Left':
            self.world.get_human().set_next_move(Arrows.LEFT)
        elif event.keysym == 'Up':
            self.world.get_human().set_next_move(Arrows.UP)
        elif event.keysym == 'Down':
            self.world.get_human().set_next_move(Arrows.DOWN)
        self.next_round()

    def load_world(self):
        self.world.load_world_state()
        self.draw_world()

    def add_creature(self, event):
        point = Point(event.x, event.y).subtract_n(Window.CANVAS_OFFSET).divide_n(Window.TILE_SIZE)
        if self.world.get_map().position_fits(point):
            self.world.give_birth(self.creature_choice_var.get(), point, True)
        self.draw_world()

    def draw_world(self):
        self.canvas.delete("all")
        for x in range(0, self.world.get_map().get_size().x):
            for y in range(0, self.world.get_map().get_size().y):
                self.canvas.create_rectangle(Window.CANVAS_OFFSET + (x + Window.EMPTY_TILE_SIZE) * Window.TILE_SIZE,
                                             Window.CANVAS_OFFSET + (y + Window.EMPTY_TILE_SIZE) * Window.TILE_SIZE,
                                             Window.CANVAS_OFFSET + (x + 1 - Window.EMPTY_TILE_SIZE) * Window.TILE_SIZE,
                                             Window.CANVAS_OFFSET + (y + 1 - Window.EMPTY_TILE_SIZE) * Window.TILE_SIZE,
                                             fill=Window.EMPTY_TILE_COLOR, outline="")
        for creature in self.world.get_list():
            pos = creature.get_position()
            self.canvas.create_rectangle(Window.CANVAS_OFFSET + pos.x * Window.TILE_SIZE,
                                         Window.CANVAS_OFFSET + pos.y * Window.TILE_SIZE,
                                         Window.CANVAS_OFFSET + (pos.x + 1) * Window.TILE_SIZE,
                                         Window.CANVAS_OFFSET + (pos.y + 1) * Window.TILE_SIZE,
                                         fill=creature.get_color(), outline="")

root = Tk()
root.geometry(str(Window.DEF_X_SIZE) + "x" + str(Window.DEF_Y_SIZE))
app = Window(root)
root.mainloop()
